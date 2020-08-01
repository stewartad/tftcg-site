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
        return self.card.image

class CharCard():
    def __init__(self, faction, size='large'):
        super().__init__()
        if faction == 'autobot':
            template = os.path.join(resource_dir, "autobot_alt.png")
        else:
            template = os.path.join(resource_dir, "autobot_alt.png")
        self.image = Image.open(template)
        self.drawer = ImageDraw.Draw(self.image)

        name_path = os.path.join(resource_dir, "SmartSansStd-Bold.otf")
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

    # def generate(self):
    #     filename = str(uuid.uuid4()) + ".png"
    #
    #     out_path = os.path.join("media", "characters", filename)
    #     self.image.save(out_path, format='png')
    #     return os.path.join(settings.MEDIA_URL, "characters", filename)