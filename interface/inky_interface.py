from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from datetime import datetime

class InkyInterface:

    def __init__(self):
        self.inky_display = InkyWHAT("red")
        self.inky_display.set_border(self.inky_display.WHITE)
        self.font_direction = ImageFont.truetype(FredokaOne, 18)
        self.font_time = ImageFont.truetype(FredokaOne, 22)
        self.padding = 10

        self.header_y = 100

    def render_departures(self, departures):
        img = Image.new("P", (self.inky_display.WIDTH, self.inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)

        self.render_header(img, draw)

        for i, departure in enumerate(departures):
            w, h = self.draw_time(draw, i, departure['time'])
            self.draw_direction(draw, i, departure['direction'], w, h)

        self.inky_display.set_image(img)
        self.inky_display.show()

    def draw_direction(self, draw, i, direction, w_time, h_time):        
        x = self.padding + w_time + self.padding
        y = self.padding * (i+1) + h_time*i + self.header_y

        draw.text((x, y), direction, self.inky_display.BLACK, self.font_direction)

    def draw_time(self, draw, i, time):
        w, h = self.font_time.getsize(time)   
        x = self.padding
        y = self.padding * (i+1) + h*i + self.header_y

        draw.text((x, y), time, self.inky_display.RED, self.font_direction)

        return w, h

    def render_header(self, img, draw):
        date = datetime.now()
        date_string = date.strftime("%d %b, %Y %H:%M") 

        x = self.padding
        y = self.padding

        draw.rectangle((0, 0, self.inky_display.WIDTH, self.header_y), fill=self.inky_display.RED)
        draw.text((x, y), date_string, self.inky_display.WHITE, self.font_time)
