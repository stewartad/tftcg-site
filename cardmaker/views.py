from django.db import transaction
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.forms import modelformset_factory, modelform_factory, inlineformset_factory

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
        context['side_list'] = self.card.characterside_set.all()
        return context


class CreateCharacter(generic.CreateView):
    model = Character
    fields = '__all__'

    # def get_context_data(self, **kwargs):
    #     data = super(CreateCharacter, self).get_context_data(**kwargs)
    #     if self.request.POST:
    #         data['sides'] = CharacterSideFormSet(self.request.POST)
    #     else:
    #         data['sides'] = CharacterSideFormSet()
    #     return data

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid:
    #         form.save()
    #     formset = CharacterSideFormSet(request.POST)
    #     if formset.is_valid():
    #         formset.save()
    #     return super(CreateCharacter, self).post(request, *args, **kwargs)




class EditCharacter(generic.UpdateView):
    model = Character
    fields = '__all__'


    # def get_context_data(self, **kwargs):
    #     data = super(EditCharacter, self).get_context_data(**kwargs)
    #     if self.request.POST:
    #         data['sides'] = CharacterSideFormSet(self.request.POST, instance=self.object)
    #     else:
    #         data['sides'] = CharacterSideFormSet(instance=self.object)
    #     return data

    # def post(self, request, *args, **kwargs):
    #     formset = CharacterSideFormSet(request.POST)
    #     if formset.is_valid():
    #         formset.save()
    #     return super(EditCharacter, self).post(request, *args, **kwargs)


class EditStratagem(generic.UpdateView):
    model = StratagemCard
    fields = '__all__'


class CreateStratagem(generic.CreateView):
    model = StratagemCard
    fields = '__all__'