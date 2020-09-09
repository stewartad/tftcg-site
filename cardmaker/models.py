from django.db import models

from cardgenerator.cardgen import CardImage
from django.conf import settings
from django.core.files import File
from django.urls import reverse
import os

FACTIONS = [
    ('AU', 'Autobot'),
    ('DE', 'Decepticon'),
    ('ME', 'Mercenary'),
]

PIP_COLORS = [
    ('O', 'Orange'),
    ('B', 'Blue'),
    ('L', 'Black'),
    ('G', 'Green'),
    ('W', 'White'),
]

RARITIES = [
    ('C', 'Common'),
    ('U', 'Uncommon'),
    ('R', 'Rare'),
    ('SR', 'Super Rare'),
]

BATTLECARD_TYPES = [
    ('A', 'Action'),
    ('U', 'Upgrade'),
]

BATTLECARD_SUBTYPES = [
    ('We', 'Weapon'),
    ('Ar', 'Armor'),
    ('Ut', 'Utility'),
]

MODES = [
    ('BOT', 'Bot Mode'),
    ('BOD', 'Body Mode'),
    ('COM', 'Combiner Mode'),
    ('ALT', 'Alt Mode'),
    ('CMB', 'Combiner Body Mode')
]


class Card(models.Model):
    name = models.CharField(max_length=60)
    stars = models.IntegerField()
    card_text = models.CharField(max_length=360)
    art = models.ImageField(upload_to='art', blank=True, null=True)
    image = models.ImageField(null=True, editable=False)

    def generate_image(self):
        pass

    class Meta:
        abstract = True


class Character(models.Model):
    name = models.CharField(max_length=60)
    stars = models.IntegerField()
    subtitle = models.CharField(max_length=60)
    health = models.IntegerField()
    faction = models.CharField(max_length=2, choices=FACTIONS)

    def get_absolute_url(self):
        return reverse('char_detail', args=[str(self.id)])

    def __str__(self):
        return '%s %s' % (self.name, self.subtitle)


class CharacterTrait(models.Model):
    trait = models.CharField(max_length=20)

    def __str__(self):
        return self.trait


class CharacterMode(Card):
    name = models.CharField(max_length=60, editable=False, blank=True, null=True)
    stars = models.IntegerField(editable=False, blank=True, null=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    mode = models.CharField(max_length=3, choices=MODES)
    attack = models.IntegerField()
    defense = models.IntegerField()

    traits = models.ManyToManyField(CharacterTrait)

    def generate_image(self):
        card = {
            'faction': self.character.faction,
            'size': 'large',
            'name': self.character.name,
            'subtitle': self.character.subtitle,
            'atk': self.attack,
            'def': self.defense,
            'hp': self.character.health,
            'traits': self.traits,
            'card_text': self.card_text,
            'art': self.art.path
        }
        card_img = CardImage('character', card).draw_image()
        filename = 'c%d.png' % self.id
        tmp_path = os.path.join(settings.MEDIA_ROOT, 'tmp', filename)
        with open(tmp_path, 'wb+') as f:
            card_img.save(f, format='png')
            self.image.save(filename, File(f), save=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.generate_image()
        super().save(*args, **kwargs)

    def __str__(self):
        return '%d %s %s' % (self.id, self.character.subtitle, self.mode)


class StratagemCard(Card):
    target = models.CharField(max_length=60)

    def generate_image(self):
        card = {
            'name': self.name,
            'target': self.target,
            'card_text': self.card_text,
            'stars': self.stars,
            'art': self.art.path
        }
        card_img = CardImage('stratagem', card).draw_image()
        filename = 's%d.png' % self.id
        tmp_path = os.path.join(settings.MEDIA_ROOT, 'tmp', filename)
        with open(tmp_path, 'wb+') as f:
            card_img.save(f, format='png')
            # return f
            self.image.save(filename, File(f), save=False)

    def get_absolute_url(self):
        return reverse('strat_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.generate_image()
        super().save(*args, **kwargs)

    def __str__(self):
        return '%s (%s)' % (self.name, self.target)
