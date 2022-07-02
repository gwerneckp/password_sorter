from genericpath import exists
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import sys
from os import path, mkdir

def strToImage(str, output):
    WIDTH_PER_CHAR = 60
    PADDING = 5
    TEXT_COLOR = (0,0,0) #BLACK
    FONT_SIZE = 100

    width = (len(str) * WIDTH_PER_CHAR)
    img = Image.new('RGB', (width, 130), color=(255,255,255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Gidole-Regular.ttf', size=FONT_SIZE)
    draw.text((PADDING, PADDING), str, fill=TEXT_COLOR, font=font)
    img.save(output)

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        if(not path.exists('output')):
            mkdir('output')
        argument = sys.argv[1]
        if(argument.endswith('.txt') and path.exists(argument)):
            wordlist = open(argument, 'r')
            words = wordlist.read().splitlines() 
            for id, word in enumerate(words):
                strToImage(word, f'output/output{id}.png')
        else:
            strToImage(argument, 'output/output.png')
    else:
        print('Provide a word or wordlist as an argument. Ex: "python main.py wordlist.txt"')
    
    
