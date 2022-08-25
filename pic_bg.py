from PIL import Image
me = Image.open('jafar.jpeg')
bg = Image.open('m1.jpeg')
bg.paste(me, (0, 0) ,me)
bg.show()