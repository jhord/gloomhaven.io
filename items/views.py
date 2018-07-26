from django.views.generic.base import TemplateView
from character.models import MyItems


	
class ItemsView(TemplateView):

	template_name = "items/items.html"
	
class IndexView(TemplateView):

	template_name = "index.html"

