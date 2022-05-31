
from PIL import Image, ImageFont, ImageDraw
from datetime import datetime

class PilInterface:
    def __init__(self):
        font = ImageFont.load_default()
        self.font_direction = font
        self.font_time = ImageFont.truetype(font=font, size=22)
        self.padding = 10
        self.header_y = 100

    def render_departures(self, departures):
        img = Image.new("P", (600, 400),color="white" )
        draw = ImageDraw.Draw(img)

        self.render_header(img, draw)

        for i, departure in enumerate(departures):
            w, h = self.draw_time(draw, i, departure['time'])
            self.draw_direction(draw, i, departure['direction'], w, h)

        img.show()

    def draw_direction(self, draw, i, direction, w_time, h_time):        
        x = self.padding + w_time + self.padding
        y = self.padding * (i+1) + h_time*i + self.header_y

        draw.text((x, y), direction, "black", self.font_direction)

    def draw_time(self, draw, i, time):
        w, h = self.font_time.getsize(time)   
        x = self.padding
        y = self.padding * (i+1) + h*i + self.header_y

        draw.text((x, y), time, "red", self.font_direction)

        return w, h

    def render_header(self, img, draw):
        date = datetime.now()
        date_string = date.strftime("%d %b, %Y %H:%M") 

        x = self.padding
        y = self.padding

        draw.rectangle((0, 0, 600, self.header_y), fill="red")
        draw.text((x, y), date_string, "white", self.font_time)
