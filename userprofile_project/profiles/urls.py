from django.urls import path
from profiles.views import profile_list, profile_detail, delete_post, edit_post, update_cover, update_profile_picture

app_name = 'profiles'

urlpatterns = [
    path('', profile_list, name='user_list'),  # ყველა მომხმარებლის სია
    path('<int:pk>/', profile_detail, name='profile_detail'),  # კონკრეტული პროფილი
    path('<int:profile_pk>/delete-post/<int:post_pk>/', delete_post, name='delete_post'),
    path('<int:profile_pk>/edit-post/<int:post_pk>/', edit_post, name='edit_post'),
    path('<int:pk>/update_cover/', update_cover, name='update_cover'),
    path('<int:pk>/update_profile_picture/', update_profile_picture, name='update_profile_picture'),
]
