from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from profiles.models import Profile


def profile_list(request):
    profiles = Profile.objects.select_related('user').all()

    paginator = Paginator(profiles, 8)  # აჩვენე 8 პროფილი თითო გვერდზე
    page_number = request.GET.get('page')  # URL-დან ამოიღებს ?page=2
    page_obj = paginator.get_page(page_number)

    return render(request, template_name='user_list.html', context={'page_obj': page_obj})


def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    posts = profile.posts.all()
    return render(request, template_name='profile_detail.html', context={'profile': profile, 'posts': posts})
