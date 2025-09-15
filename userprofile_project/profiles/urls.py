from django.urls import path
from profiles.views import profile_list, profile_detail

app_name = 'profiles'

urlpatterns = [
    path('users/', profile_list, name='user_list'),  # ყველა მომხმარებლის სია
    path('users/<int:pk>/', profile_detail, name='profile_detail'),  # კონკრეტული პროფილი
]
