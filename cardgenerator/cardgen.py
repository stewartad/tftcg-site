import os

from cardgenerator.char_card import CharCard
from cardgenerator.strat_card import StratCard

resource_dir = os.path.join("cardgenerator/card_resources")
out_dir = os.path.join(os.pardir, "media", "characters")

name_path = os.path.join(resource_dir, "SmartSansStd-Bold.otf")

class CardImage:
    def __init__(self, card_type, card_info):
        self.card = None
        self.card_type = card_type
        self.card_info = card_info

    def draw_image(self):
        if self.card_type == 'character':
            self.card = CharCard(self.card_info['faction'], self.card_info['size'])
            self.card.draw_name(self.card_info['name'])
            self.card.draw_subtitle(self.card_info['subtitle'])
            self.card.draw_stats(self.card_info['atk'], self.card_info['def'], self.card_info['hp'])
            self.card.draw_card_text(self.card_info['card_text'])
        elif self.card_type == 'stratagem':
            self.card = StratCard(self.card_info['name'], self.card_info['target'],
                                  self.card_info['card_text'], self.card_info['stars'], art=self.card_info['art'])
            self.card.draw()
        return self.card.image


