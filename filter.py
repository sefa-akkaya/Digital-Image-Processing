from PIL import Image, ImageFilter, ImageOps, ImageTk
def resim_al():
    resim = input()
    return resim  
def negative(resim):
    img = Image.open(resim)     
    for i in range(0, img.size[0]-1): 
        for j in range(0, img.size[1]-1):
            pixelColorVals = img.getpixel((i,j));
            redPixel    = 255 - pixelColorVals[0]; # Negate red pixel
            greenPixel  = 255 - pixelColorVals[1]; # Negate green pixel
            bluePixel   = 255 - pixelColorVals[2];
            img.putpixel((i,j),(redPixel, greenPixel, bluePixel))
    imgGray = img.convert('L')
    imgGray.save('C:/Users/SEFA/Desktop/PYTHON/negative.png')
    return 'C:/Users/SEFA/Desktop/PYTHON/negative.png'

def blur(resim):
    image = Image.open(resim)
    image_blur = image.filter(ImageFilter.BLUR) 
    temp = image_blur.resize((300,400),Image.ANTIALIAS)
    temp.save("C:/Users/SEFA/Desktop/PYTHON/blur.png")
    return 'C:/Users/SEFA/Desktop/PYTHON/blur.png'
def contour(resim):
    image = Image.open(resim)
    image_contour = image.filter(ImageFilter.CONTOUR)
    temp = image_contour.resize((300,400),Image.ANTIALIAS)
    temp.save("C:/Users/SEFA/Desktop/PYTHON/contour.png")
    return 'C:/Users/SEFA/Desktop/PYTHON/contour.png'
def detail(resim):
    image = Image.open(resim)
    image_detail = image.filter(ImageFilter.DETAIL)
    temp = image_detail.resize((300,400),Image.ANTIALIAS)
    temp.save("C:/Users/SEFA/Desktop/PYTHON/detail.png")
    return 'C:/Users/SEFA/Desktop/PYTHON/detail.png'
def image_edge(resim):
    image = Image.open(resim)
    image_edge = image.filter(ImageFilter.EDGE_ENHANCE)
    temp = image_edge.resize((300,400),Image.ANTIALIAS)
    temp.save("C:/Users/SEFA/Desktop/PYTHON/edge.png")
    return 'C:/Users/SEFA/Desktop/PYTHON/edge.png'
def find_edge(resim):
    image = Image.open(resim)
    image_find_edges = image.filter(ImageFilter.FIND_EDGES)
    temp = image_find_edges.resize((300,400),Image.ANTIALIAS)
    temp.save("C:/Users/SEFA/Desktop/PYTHON/findedge.png")
    return 'C:/Users/SEFA/Desktop/PYTHON/findedge.png'
def emboss(resim):
    image = Image.open(resim)
    image_emboss = image.filter(ImageFilter.EMBOSS)
    temp = image_emboss.resize((300,400),Image.ANTIALIAS)
    temp.save("C:/Users/SEFA/Desktop/PYTHON/emboss.png")
    return 'C:/Users/SEFA/Desktop/PYTHON/emboss.png'
def sharp(resim):
    image = Image.open(resim)
    image_sharp = image.filter(ImageFilter.SHARPEN)
    temp = image_sharp.resize((300,400),Image.ANTIALIAS)
    temp.save("C:/Users/SEFA/Desktop/PYTHON/sharp.png")
    return 'C:/Users/SEFA/Desktop/PYTHON/sharp.png'
def smooth(resim):
    image = Image.open(resim)
    image_smooth = image.filter(ImageFilter.SMOOTH)
    temp = image_smooth.resize((300,400),Image.ANTIALIAS)
    temp.save("C:/Users/SEFA/Desktop/PYTHON/smooth.png")
    return 'C:/Users/SEFA/Desktop/PYTHON/smooth.png'
def min(resim):
    image = Image.open(resim)
    image_filtered_min = image.filter(ImageFilter.MinFilter(size = 5))
    temp = image_filtered_min.resize((300,400),Image.ANTIALIAS)
    temp.save("C:/Users/SEFA/Desktop/PYTHON/min.png")
    return 'C:/Users/SEFA/Desktop/PYTHON/min.png'
def median(resim):
    image = Image.open(resim)
    image_filtered_median = image.filter(ImageFilter.MedianFilter(size = 5))
    temp = image_filtered_median.resize((300,400),Image.ANTIALIAS)
    temp.save("C:/Users/SEFA/Desktop/PYTHON/median.png")
    return 'C:/Users/SEFA/Desktop/PYTHON/median.png'
def max(resim):
    image = Image.open(resim)
    image_filtered_max = image.filter(ImageFilter.MaxFilter(size = 5))
    temp = image_filtered_max.resize((300,400),Image.ANTIALIAS)
    temp.save("C:/Users/SEFA/Desktop/PYTHON/max.png")
    return 'C:/Users/SEFA/Desktop/PYTHON/max.png'
def gauss(resim):
    image = Image.open(resim)
    image_gaussblur = image.filter(ImageFilter.GaussianBlur(radius = 10))
    temp = image_gaussblur.resize((300,400),Image.ANTIALIAS)
    temp.save("C:/Users/SEFA/Desktop/PYTHON/gauss.png")
    return 'C:/Users/SEFA/Desktop/PYTHON/gauss.png'
