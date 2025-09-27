from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from profiles.forms import PostForm, CoverUpdateForm
from profiles.models import Profile, Post
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def profile_list(request):
    profiles = Profile.objects.select_related('user').all()

    paginator = Paginator(profiles, 8)  # აჩვენე 8 პროფილი თითო გვერდზე
    page_number = request.GET.get('page')  # URL-დან ამოიღებს ?page=2
    page_obj = paginator.get_page(page_number)

    return render(request, template_name='user_list.html', context={'page_obj': page_obj})


from django.contrib import messages  # თუ გინდა შეტყობინება messages-ითაც


def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    posts = profile.posts.all()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.profile = profile
            post.save()
            return redirect('profiles:profile_detail', pk=pk)
    else:
        form = PostForm()

    return render(request, 'profile_detail.html', {
        'profile': profile,
        'posts': posts,
        'form': form,
    })


# delete_post ფუნქცია
def delete_post(request, profile_pk, post_pk):
    profile = get_object_or_404(Profile, pk=profile_pk)
    post = get_object_or_404(Post, pk=post_pk, profile=profile)

    if request.method == 'POST':
        post.delete()
        return redirect('profiles:profile_detail', pk=profile_pk)

    return redirect('profiles:profile_detail', pk=profile_pk)


# edit_post ფუნქცია
def edit_post(request, profile_pk, post_pk):
    profile = get_object_or_404(Profile, pk=profile_pk)
    post = get_object_or_404(Post, pk=post_pk, profile=profile)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('profiles:profile_detail', pk=profile_pk)
    else:
        form = PostForm(instance=post)

    posts = profile.posts.all()
    return render(request, 'profile_detail.html', {
        'profile': profile,
        'posts': posts,
        'form': form,
        'edit_mode': True,
        'editing_post': post,
    })


@require_POST
def update_cover(request, pk):
    profile = get_object_or_404(Profile, pk=pk)

    form = CoverUpdateForm(request.POST, request.FILES, instance=profile)
    if form.is_valid():
        form.save()
        messages.success(request, "Cover photo updated!")
    else:
        messages.error(request, "Invalid file.")

    return redirect('profiles:profile_detail', pk=pk)
