from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.forms import modelformset_factory, modelform_factory, inlineformset_factory
from django.views.generic.edit import CreateView, UpdateView

from .models import CharacterCard, Card, StratagemCard, CharacterSide


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

class StratagemDetail(generic.DetailView):
    model = StratagemCard
    template_name='cardmaker/stratagem_detail.html'
    context_object_name = 'card'

class CharacterDetail(generic.DetailView):
    model = CharacterCard
    template_name = 'cardmaker/character_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.card = get_object_or_404(CharacterCard, id=self.kwargs['pk'])
        context['card'] = self.card
        context['side_list'] = self.card.characterside_set.all()
        return context

class CreateCharacter(CreateView):
    form_class = inlineformset_factory(CharacterCard, CharacterSide, fields='__all__')
    model = CharacterCard

class EditCharacter(UpdateView):
    form_class = inlineformset_factory(CharacterCard, CharacterSide, fields='__all__')
    model = CharacterCard

class EditStratagem(UpdateView):
    model = StratagemCard
    fields = '__all__'

class CreateStratagem(CreateView):
    model = StratagemCard
    fields = '__all__'