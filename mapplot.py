from PIL import Image
import matplotlib.pyplot as plt

im = Image.open("resources/heightmap01.png")
print(f"Image size {im.width} x {im.height}")

#find lowest color
lowest = 256
for x in range(im.width):
    for y in range(im.height):
        pix = im.getpixel((x,y))
        if pix[0] < lowest:
            lowest = pix[0]
        if lowest == 0:
            break


plotWidth = 800
plotHeight = 800

border = 10
dx = 1
dy = 10
maxheightsteps = 0.10

print("plot starting")

for y in range(0, plotHeight, dy):
    vx = []
    vy = []
    
    #fill with data
    for x in range(0, plotWidth, dx):
        imgx = int(float(x) / float(plotWidth) * im.width)
        imgy = int(float(y) / float(plotHeight) * im.height)
        pix = im.getpixel((imgx, imgy))

        vx.append(x)
        vy.append(y + (float(pix[0]) / 256.0 * plotHeight * maxheightsteps))

    #trim start and end
    for x in range(len(vx)):
        if vx != 0:
            break
        vx.pop(0)
        vy.pop(0)

    #print(f"{y}, {x}")
    plt.plot(vx, vy, 'k', linewidth=0.2)

print("all plot sent")

# function to show the plot 
#plt.show()
plt.savefig('output.png', dpi=300)
