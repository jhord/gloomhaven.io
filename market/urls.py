from django.urls import path

from . import views

urlpatterns = [
    path('', views.MarketPageView.as_view(), name='market'),
]