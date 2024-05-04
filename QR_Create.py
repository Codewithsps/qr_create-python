from tkinter.ttk import Scale
import qrcode
qrcodegenrate = input("Enter some text:")#qr code vale
img = qrcode.make(qrcodegenrate) 
type(img)
img.save("qrgenrate.png") #file name
