from django.contrib import admin

from profiles.models import Profile, Post


# Post მინდა რომ იყოს Profile-ის შიგნით და არა ცალკე განყოფილებაში
class PostInline(admin.TabularInline):
    model = Post
    extra = 1
    fields = ('image', 'caption', 'created_at', 'likes', 'comments')
    readonly_fields = ('created_at', 'likes', 'comments')

    # get_queryset მეთოდით უნდა გავფილტრო პოსტები კონკრეტული იუზერის მიხედვით, რომ ადმინში
    # კონკრეტულ იუზერზე მხოლოდ მისი პოსტები გამოჩნდეს და არა ყველა იუზერის პოსტი
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # აქ უნდა გაფილტრო პოსტები, რომლებიც დაკავშირებულია ამ Profile-ის იუზერთან
        if hasattr(self, 'parent_object') and self.parent_object:
            return qs.filter(profile=self.parent_object)
        return qs

    # get_formset იღებს obj - ს(Profile - ის ობიექტს), ინახავს მას self.parent_object - ში,
    # შემდეგ, როცა get_queryset - ში დამჭირდება კონკრეტული პოსტებს ჩვენება შემიძლია მივწვდე
    # ამ parent ობიექტს და შესაბამისად გავფილტრო
    def get_formset(self, request, obj=None, **kwargs):
        self.parent_object = obj
        return super().get_formset(request, obj, **kwargs)


class ProfileAdmin(admin.ModelAdmin):
    inlines = [PostInline]
    list_display = ('user', 'phone', 'birth_date', 'gender', 'profession')
    list_filter = ('gender', 'profession')
    search_fields = ('user__username', 'phone', 'profession')
    ordering = ('user__username',)

    # თუ obj(კონკრეტული Profile ობიექტი) არ არსებობს(ანუ როდესაც ვქმნი ახალ Profile-ს და ჯერ შენახული არ არის),
    # ამ დროს არ მინდა, რომ Inline-ები გამოჩნდეს რადგან პოსტებს ვერ დავუკავშირებ ახალ ობიექტს, რომელიც ჯერ ბაზაში არ არის
    def get_inline_instances(self, request, obj=None):
        # თუ ობიექტი არ არის(შექმნის ეტაპზეა), ვუბრუნდები ცარიელ სიას — ანუ
        # Inline-ები არ გამოისახება.
        if not obj:
            return []
        return super().get_inline_instances(request, obj)


admin.site.register(Profile, ProfileAdmin)
