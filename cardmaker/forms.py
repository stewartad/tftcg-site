from django.forms import ModelForm, inlineformset_factory
from cardmaker.models import StratagemCard, Character, CharacterMode


class CharacterModeForm(ModelForm):

    class Meta:
        model = CharacterMode
        exclude = ()


CharacterModeFormSet = inlineformset_factory(Character, CharacterMode,
                fields='__all__', can_delete=True, max_num=3, extra=1)

class StratagemForm(ModelForm):

    class Meta:
        model = StratagemCard
        fields = ['name', 'target', 'stars', 'card_text', 'art']
