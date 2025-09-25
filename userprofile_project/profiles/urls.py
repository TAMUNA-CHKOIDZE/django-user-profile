from django.urls import path
from profiles.views import profile_list, profile_detail, delete_post, edit_post

app_name = 'profiles'

urlpatterns = [
    path('', profile_list, name='user_list'),  # ყველა მომხმარებლის სია
    path('<int:pk>/', profile_detail, name='profile_detail'),  # კონკრეტული პროფილი
    path('<int:profile_pk>/delete-post/<int:post_pk>/', delete_post, name='delete_post'),
    path('<int:profile_pk>/edit-post/<int:post_pk>/', edit_post, name='edit_post'),
]
