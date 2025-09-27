# ჯანგოში ჩაშენებული User მოდელის იმპორტი, რომელსაც to='User'-ით ვერ გამოვიყენებ კავშირებში
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, verbose_name='User')
    bio = models.TextField(blank=True, verbose_name='Bio')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Phone')
    birth_date = models.DateField(blank=True, null=True, verbose_name='Birth Date')
    gender = models.CharField(max_length=10, blank=True, verbose_name='Gender')
    profession = models.CharField(max_length=60, blank=True, verbose_name='Profession')
    avatar = models.ImageField(upload_to='avatars/', blank=True, verbose_name='Avatar')
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, verbose_name='Profile Picture')
    profile_cover = models.ImageField(upload_to='profiles/cover/', blank=True, verbose_name='Profile Cover')

    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f"{self.user.username} Profile"


class Post(models.Model):
    profile = models.ForeignKey(to='Profile', related_name='posts', on_delete=models.CASCADE, null=True, blank=True,
                                verbose_name='Profile', )
    image = models.ImageField(upload_to='posts/', blank=True, verbose_name='Post Image')
    caption = models.TextField(blank=True, verbose_name='Caption')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    likes = models.PositiveIntegerField(default=0, verbose_name='Likes Count')
    comments = models.PositiveIntegerField(default=0, verbose_name='Comments Count')

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"{self.profile.user.username} - {self.caption[:30] or 'No caption'}"
