from ascii_image_art.ascii_images_and_text import ASCIIArt
from ascii_image_art.usingAI import usingAIClass

a=ASCIIArt(chars=' .ASD',path='',scale=0.05)
a.getPath()
a.convert()
a.convertWithAI(depth=1)
a.printASCII()

# a=usingAIClass(chars=' .ASD',path='asad.png',scale=0.1,K=20,filename="OutputAIfromMain")
# a.convert()
# a.printASCII()

# or print('main file',a.getASCII())
