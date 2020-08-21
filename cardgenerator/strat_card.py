import os
import textwrap

from PIL import ImageFont, Image, ImageDraw


resource_dir = os.path.join("cardgenerator/card_resources")
name_path = os.path.join(resource_dir, "Coluna.otf")
target_path = os.path.join(resource_dir, "NivaSmallCaps-ExtraLight-Italic.ttf")
text_path = os.path.join(resource_dir, "Roboto-Regular.ttf")

positions = {
    'name': (40, 45),
    'target': (58, 100),
    'card_text': (36, 517),
    'star': (20, 712),
    'art': (20, 72, 526, 491),
}

dimensions = {
    'name': (461, 38),
    'target': (428, 17),
    'card_text': (475, 157),
    'star': (29, 27),
    'art': (506, 419)
}

class StratCard:
    def __init__(self, name, target, text, stars, art=None):
        self.name_font = ImageFont.truetype(font=name_path, size=42)
        self.target_font = ImageFont.truetype(font=target_path, size=19)
        self.text_font = ImageFont.truetype(font=text_path, size=19)
        self.name = name
        self.target = target
        self.text = text
        self.stars = stars
        self.art = Image.open(art)
        template = os.path.join(resource_dir, "strat_blank.png")
        starimg = os.path.join(resource_dir, "star.png")
        self.card_layer = Image.open(template)
        self.drawer = ImageDraw.Draw(self.card_layer)
        self.image = Image.new('RGBA', self.card_layer.size)
        self.star = Image.open(starimg)

    def _calc_target_pos(self, text):
        dims = self.drawer.textsize(text, font=self.text_font)
        left_x = (self.card_layer.width / 2 )- (dims[0] / 2)
        return (left_x, positions['target'][1])

    def _calc_cardtext_pos(self, text):
        dims = self.drawer.textsize(text, font=self.text_font)
        left_x = (self.card_layer.width / 2) - (dims[0] / 2)
        return (left_x, positions['card_text'][1])

    def _split_card_text(self, text):
        return textwrap.fill(text, width=50)

    def draw(self):
        name_str = str.upper(self.name)
        self.drawer.text(positions['name'], name_str, fill='white',  font=self.name_font)
        target_str = str.upper(self.target)
        target_pos = self._calc_target_pos(target_str)
        self.drawer.text(target_pos, target_str, fill='black', font=self.target_font)

        text_str = self._split_card_text(self.text)
        text_pos = self._calc_cardtext_pos(text_str)
        self.drawer.text(text_pos, text_str, align='center', fill='black', font=self.text_font)

        new_art = self.art.crop(positions['art'])
        self.image.paste(new_art, positions['art'])
        self.image.alpha_composite(self.card_layer)
        for i in range(self.stars):
            x_offset = positions['star'][0] + (i * dimensions['star'][0])
            self.image.alpha_composite(self.star, (x_offset, positions['star'][1]))