#!/usr/bin/python3

from PIL import Image
from PIL import PSDraw

img = Image.open("../../img/tomatoes.jpg")
title = "Tomatoes"

# box in points
box = (1*72, 2*72, 7*72, 10*72)

# default is sys.stdout
ps = PSDraw.PSDraw()
ps.begin_document(title)

# draw the image (75 dpi)
ps.image(box, img, 75)
ps.rectangle(box)

# draw title
ps.setfont("HelveticaNarrow-Bold", 36)
ps.text((3*72, 4*72), title)

ps.end_document()
