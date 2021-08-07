from django.urls import path

from fitness.accounts.views import logout_user, RegisterView, ProfileDetailsView, LoginUserView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='log in'),
    path('logout/', logout_user, name='log out'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileDetailsView.as_view(), name='profile details'),


]