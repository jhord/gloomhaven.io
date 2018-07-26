from django.urls import path, include
from . import views



urlpatterns = [
	path('', views.ItemsView.as_view(), name='items'),
]