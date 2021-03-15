from PIL import ImageDraw, ImageTk,Image,ImageFont

imageTest = Image.open(r"Untitled.png")
ImageDraw.Draw(imageTest).text((0,0),"r=",(0,0,0),font=ImageFont.truetype(r"./font.ttf",32))
imageTest.save("newImg.png")