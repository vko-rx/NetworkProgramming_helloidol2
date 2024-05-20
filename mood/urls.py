from django.urls import path

from mood import views

app_name = 'mood'

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character_list'),
]