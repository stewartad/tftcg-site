from django.db import models
from cardgenerator.cardgen import CardImage
from django.conf import settings
from django.core.files import File
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

    class Meta:
        abstract = True

class CharacterCard(Card):
    subtitle = models.CharField(max_length=60)
    health = models.IntegerField()
    faction = models.CharField(max_length=2, choices=FACTIONS)

    def __str__(self):
        return '%s %s' % (self.name, self.subtitle)


class CharacterTrait(models.Model):
    trait = models.CharField(max_length=20)

    def __str__(self):
        return self.trait


class CharacterSide(models.Model):
    charactercard = models.ForeignKey(CharacterCard, on_delete=models.CASCADE)
    mode = models.CharField(max_length=3, choices=MODES)
    attack = models.IntegerField()
    defense = models.IntegerField()
    cardtext = models.CharField(max_length=360)
    traits = models.ManyToManyField(CharacterTrait)
    art = models.ImageField(upload_to='art', blank=True, null=True)
    image = models.ImageField(upload_to='cards', null=True, editable=False)

    def generateImage(self):
        card = {
            'faction': self.charactercard.faction,
            'size': 'large',
            'name': self.charactercard.name,
            'subtitle': self.charactercard.subtitle,
            'atk': self.attack,
            'def': self.defense,
            'hp': self.charactercard.health,
            'traits': self.traits,
            'card_text': self.cardtext,
        }
        card_img = CardImage('character', card).draw_image()
        filename = 'c%d.png' % self.id
        tmp_path = os.path.join(settings.MEDIA_ROOT, 'tmp', filename)
        with open(tmp_path, 'wb+') as f:
            card_img.save(f, format='png')
            self.image.save(filename, File(f), save=False)
        # os.remove(tmp_path)

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
        self.generateImage()
        super().save(*args, **kwargs)

    def __str__(self):
        return '%d %s %s' % (self.id, self.charactercard.subtitle, self.mode)

class StratagemCard(Card):
    target=models.CharField(max_length=60)
    card_text = models.CharField(max_length=360)
    art = models.ImageField(upload_to='art', blank=True, null=True)
    image = models.ImageField(upload_to='cards', null=True, editable=False)

    def generateImage(self):
        card = {
            'name': self.name,
            'target': self.target,
            'card_text': self.card_text,
            'stars': self.stars,
        }
        card_img = CardImage('stratagem', card).draw_image()
        filename = 's%d.png' % self.id
        tmp_path = os.path.join(settings.MEDIA_ROOT, 'tmp', filename)
        with open(tmp_path, 'wb+') as f:
            self.image.delete(save=False)
            card_img.save(f, format='png')
            self.image.save(filename, File(f), save=False)

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)
        self.generateImage()
        super().save(*args, **kwargs)