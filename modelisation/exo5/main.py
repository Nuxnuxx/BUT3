from PIL import Image
img = Image.open("./I1.jpg")
img2 = Image.open("./I2.jpg")
img.show()
img2.show()

img3 = Image.new('RGB', (200, 444+101),  color="white")


offset1 = [0, 101]
offset2 = [0, 0]

img3.paste(img, offset1)
img3.paste(img2, offset2)
# img3.show()
