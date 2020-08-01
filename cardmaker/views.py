from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse

from .models import CharacterCard

# Create your views here.
def index(request):
    card_list = CharacterCard.objects.all()
    template = loader.get_template('cardmaker/index.html')
    context = {
        'card_list': card_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, card_id):
    card = get_object_or_404(CharacterCard, pk=card_id)
    sides = list(card.characterside_set.all())
    for s in sides:
        s.generateImage()

    return render(request, 'cardmaker/detail.html', { 'side_list': sides })