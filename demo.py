import png
f = open('ramp.png', 'wb')      # binary mode is important
w = png.Writer(255, 255, greyscale=True) # the image we want to write

row=[0]*255 # a row of zeros
pic=[row]*255 # 255 of those rows

w.write(f, pic)
f.close()
