from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.CharacterView.as_view(), name='character'),
]