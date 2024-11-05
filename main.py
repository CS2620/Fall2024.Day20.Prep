from PIL import Image
import math
from get_palette import get_palette
from print_palette import print_palette


for filename in ("cat.jpg", "abstract.jpg"):
  image = Image.open(filename)
  data = image.load()

  entries = get_palette(image, data)
  entries = [x for x in entries if x[1] > 1]

  print_palette(entries, 10, "palette_" + filename +".png")
