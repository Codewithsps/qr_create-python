from tkinter.ttk import Scale
import qrcode
img = qrcode.make('https://codewithsps.github.io/sps/') #some data here
type(img)
img.save("qr.png") #file name