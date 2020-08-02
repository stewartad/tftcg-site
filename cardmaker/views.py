from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse

from .models import CharacterCard, Card, StratagemCard

# Create your views here.
def index(request):
    card_list = CharacterCard.objects.all()
    strat_list = StratagemCard.objects.all()
    template = loader.get_template('cardmaker/index.html')
    context = {
        'char_list': card_list,
        'strat_list': strat_list,
    }
    return HttpResponse(template.render(context, request))

def char_detail(request, card_id):
    card = get_object_or_404(CharacterCard, pk=card_id)
    context = {}
    sides = list(card.characterside_set.all())
    context['side_list']=sides

    return render(request, 'cardmaker/detail.html', context)

def strat_detail(request, card_id):
    card = get_object_or_404(StratagemCard, pk=card_id)
    context = {}
    context['card']=card

    return render(request, 'cardmaker/detail.html', context)