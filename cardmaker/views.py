from django.db import transaction
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.forms import modelformset_factory, modelform_factory, inlineformset_factory

from .forms import CharacterModeFormSet, CharacterModeForm
from .models import Character, Card, StratagemCard, CharacterMode


# Create your views here.
def index(request):
    card_list = Character.objects.all()
    strat_list = StratagemCard.objects.all()
    template = loader.get_template('cardmaker/index.html')
    context = {
        'char_list': card_list,
        'strat_list': strat_list,
    }
    return HttpResponse(template.render(context, request))


class StratagemDetail(generic.DetailView):
    model = StratagemCard
    context_object_name = 'card'


class CharacterDetail(generic.DetailView):
    model = Character

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.card = get_object_or_404(Character, id=self.kwargs['pk'])
        context['card'] = self.card
        context['side_list'] = self.card.charactermode_set.all()
        return context


class CreateCharacter(generic.CreateView):
    model = Character
    fields = '__all__'
    form = CharacterModeForm

    def get_context_data(self, **kwargs):
        data = super(CreateCharacter, self).get_context_data(**kwargs)
        if self.request.POST:
            data['modes'] = CharacterModeFormSet(self.request.POST, self.request.FILES)
        else:
            data['modes'] = CharacterModeFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        modes = context['modes']
        with transaction.atomic():
            self.object = form.save()
            if modes.is_valid():
                modes.instance = self.object
                modes.save()
        return super(CreateCharacter, self).form_valid(form)

class EditCharacter(generic.UpdateView):
    model = Character
    fields = '__all__'
    form = CharacterModeForm

    def get_context_data(self, **kwargs):
        data = super(EditCharacter, self).get_context_data(**kwargs)
        if self.request.POST:
            data['modes'] = CharacterModeFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['modes'] = CharacterModeFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        modes = context['modes']
        with transaction.atomic():
            self.object = form.save()
            if modes.is_valid():
                modes.instance = self.object
                modes.save()
        return super(EditCharacter, self).form_valid(form)



class EditStratagem(generic.UpdateView):
    model = StratagemCard
    fields = '__all__'


class CreateStratagem(generic.CreateView):
    model = StratagemCard
    fields = '__all__'