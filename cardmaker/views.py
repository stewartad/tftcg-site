from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.forms import modelformset_factory, modelform_factory

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

class EditStratagem(View):
    form_class = modelform_factory(StratagemCard, fields='__all__')
    initial = {'key': 'value'}
    template_name = 'cardmaker/stratagem_form.html'

    def get(self, request, *args, **kwargs):
        self.card = get_object_or_404(StratagemCard, id=self.kwargs['pk'])
        form = self.form_class(instance=self.card)
        return render(request, self.template_name, {'form': form, 'card': self.card})

    def post(self, request, *args, **kwargs):
        self.card = get_object_or_404(StratagemCard, id=self.kwargs['pk'])
        form = self.form_class(request.POST, instance=self.card)
        if form.is_valid():
            self.card = form.save()
            return HttpResponseRedirect('/cardmaker/stratagems/%d' % self.card.id)

        return render(request, self.template_name, {'form': form, 'card': self.card})

class CreateStratagem(View):
    form_class = modelform_factory(StratagemCard, fields='__all__')
    initial = {'key': 'value'}
    template_name = 'cardmaker/stratagem_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.card = form.save()
            return HttpResponseRedirect('/cardmaker/stratagems/%d' % self.card.id)

        return render(request, self.template_name, {'form': form})