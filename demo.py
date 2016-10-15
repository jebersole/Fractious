# creates a grayscale gradient box
import png
f = open('box.png', 'wb')
w = png.Writer(255, 255, greyscale=True)  # the image we want to write, 255 by 255 px
row = [0] * 255  # signpost the first one, black
pic = [row]
for color in range(254):
    row = [color] * 255  # one row
    pic += [row]  # 255 of those rows

w.write(f, pic)
f.close()
