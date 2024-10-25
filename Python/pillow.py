from PIL import Image, ImageDraw

width, height = 640, 480
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

draw.polygon([(320, 100), (100, 380), (540, 380)], outline='black')

point = (320,101) # draw a point

draw.point(point,fill='red')

def genpoint():
    x,y=0,0
    while True:
        yield (x,y)
        x+=1
        y+=1

genepoint = genpoint()

n=0

while(n<100):
        draw.point(tuple(next(genepoint)),fill='red')
        n+=1
        
image.save('output.png')
