from django.views.generic.base import TemplateView
from character.models import MyCharacter
from character.models import MyItems

class CharacterView(TemplateView):

	template_name = "character/character.html"
	
	
class IndexView(TemplateView):

	template_name = "index.html"