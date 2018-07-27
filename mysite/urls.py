"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from character import views
from items import views

urlpatterns = [
	# 127.0.0.1:8000/character/
	path('character/', include('character.urls')),
	# 127.0.0.1:8000/items
	path('items/', include('items.urls')),
	# 127.0.0.1:8000/admin
    path('admin/', admin.site.urls),
	# 127.0.0.1:8000
	path('', include('pages.urls')),
	# 127.0.0.1:8000/market
	path('market/', include('market.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
