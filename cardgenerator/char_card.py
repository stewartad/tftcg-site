import os
import textwrap

from PIL import Image, ImageDraw, ImageFont


resource_dir = os.path.join("cardgenerator/card_resources")
name_path = os.path.join(resource_dir, "SmartSansStd-Bold.otf")

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