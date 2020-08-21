from django.forms import BaseModelFormSet, ModelForm, modelformset_factory, inlineformset_factory
from cardmaker.models import StratagemCard

# class CharacterSideForm(ModelForm):
#
#     class Meta:
#         model = CharacterSide
#         exclude = ()
#
# CharacterSideFormSet = inlineformset_factory(CharacterCard, CharacterSide,
#                                              fields='__all__', can_delete=True, max_num=2, extra=2)

class StratagemForm(ModelForm):

    class Meta:
        model = StratagemCard
        fields = ['name', 'target', 'stars', 'card_text', 'art']
