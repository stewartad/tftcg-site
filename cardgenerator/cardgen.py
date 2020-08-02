from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

resource_dir = os.path.join("cardgenerator/card_resources")
out_dir = os.path.join(os.pardir, "media", "characters")

name_pos = (16, 21)
name_height = 44
sub_pos = (18, 58)
sub_height = 14
stat_y = 500
trait_y = 91
trait_w = 150
trait_h = 30
trait_text_pos = (58, 7)
atk_pos = (45, stat_y)
hp_pos = (280, stat_y)
def_pos = (426, stat_y)
stat_height = 32
text_pos = (44, 563)

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
                                  self.card_info['card_text'], self.card_info['stars'])
            self.card.draw()
        return self.card.image

class StratCard:
    def __init__(self, name, target, text, stars):
        self.positions = {
            'name': (40, 43),
            'target': (58, 99),
            'card_text': (36, 517),
            'star': (20, 712)
        }
        self.dimensions = {
            'name': (461, 38),
            'target': (428, 17),
            'card_text': (475, 157),
            'star': (29, 27)
        }
        self.name_font = ImageFont.truetype(font=name_path, size=self.dimensions['name'][1])
        self.text_font = ImageFont.truetype(font='gadugi.ttf', size=12)
        self.name = name
        self.target = target
        self.text = text
        self.stars = stars
        template = os.path.join(resource_dir, "strat_blank.png")
        self.image = Image.open(template)
        self.drawer = ImageDraw.Draw(self.image)

    def draw(self):
        name_str = str.upper(self.name)
        self.drawer.text(self.positions['name'], name_str, fill='white',  font=self.name_font)
        target_str = str.upper(self.target)
        self.drawer.text(self.positions['target'], target_str, fill='black', font=self.text_font)
        self.drawer.text(self.positions['card_text'], self.text, fill='black', font=self.text_font)

class CharCard():
    def __init__(self, faction, size='large'):
        super().__init__()
        if faction == 'autobot':
            template = os.path.join(resource_dir, "autobot_alt.png")
        else:
            template = os.path.join(resource_dir, "autobot_alt.png")
        self.image = Image.open(template)
        self.drawer = ImageDraw.Draw(self.image)


        text_path = os.path.join(resource_dir, "Ultramagnetic.ttf")
        self.name_font = ImageFont.truetype(font=name_path, size=name_height)
        # self.text_font = ImageFont.truetype(font=text_path, size=sub_height)
        self.text_font = ImageFont.truetype(font='gadugi.ttf', size=sub_height)
        self.stat_font = ImageFont.truetype(font='impact.ttf', size=stat_height)

    def draw_name(self, text):
        new_text = str.upper(text)
        self.drawer.text(name_pos, new_text, fill="white", font=self.name_font)

    def draw_subtitle(self, text):
        new_text = str.upper(text)
        self.drawer.text(sub_pos, new_text, fill="white", font=self.text_font)

    def draw_stats(self, atk=0, shield=0, hp=0):
        self.drawer.text(atk_pos, str(atk), fill="white", font=self.stat_font)
        self.drawer.text(def_pos, str(shield), fill="white", font=self.stat_font)
        self.drawer.text(hp_pos, str(hp), fill="white", font=self.stat_font)

    def draw_card_text(self, text):
        new_text = textwrap.fill(text, width=65)
        self.drawer.text(text_pos, new_text, fill="black", font=self.text_font)