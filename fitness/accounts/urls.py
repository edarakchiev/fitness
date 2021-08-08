from django.urls import path

from fitness.accounts.views import RegisterView, ProfileDetailsView, LoginUserView, EditProfile, LogoutUser

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='log in'),
    path('logout/', LogoutUser.as_view(), name='log out'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>', ProfileDetailsView.as_view(), name='profile details'),
    path('edit_profile/<int:pk>', EditProfile.as_view(), name='profile edit'),


]