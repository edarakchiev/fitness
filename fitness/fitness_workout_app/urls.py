from django.urls import path

from fitness.fitness_workout_app.views import IndexView, WorkoutDetailsView, CreateWorkoutView, EditWorkoutView, \
    DeleteWorkoutView, SearchResultsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('details_workout/<int:pk>', WorkoutDetailsView.as_view(), name='workout details'),
    path('create_workout/', CreateWorkoutView.as_view(), name='create workout'),
    path('edit_workout/<int:pk>', EditWorkoutView.as_view(), name='edit workout'),
    path('delete_workout/<int:pk>', DeleteWorkoutView.as_view(), name='delete workout'),
    path('search/',  SearchResultsView.as_view(),  name='search results'),

]