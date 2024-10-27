import os

import ss
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import *
from PIL import Image, ImageFilter
import os

class PhotoManager:
    def __init__(self):
        self.photo = None
        self.folder = None
        self.filename = None
        self.image_lbl= None

    def loed(self):
        imahe_path = os.path.join(self,folder, self.filename)
        self.photo = Image.open(imahe_path)


    def bw(self):
        self.photo = self.photo("L")
        self.show_image(self.image_lbl)


    def leften(self):
        self.photo = self.photo.transpose(Image.ROTATE_90)
        self.show_image(self.image_lbl)

    def mirron (self):
        self.photo = self.photo.transpose(Image.FLIP_LEFT_RIGHT)
        self.show_image(self.image_lbl)

    def risk(self):
        self.photo = self.photo.filter(ImageFilter.SHARPEN)
        self.show_image(self.image_lbl)


    def rr(self):
       self.photo = self.photo.filter(ImageFilter.CONTOUR)
       self.show_image(self.image_lbl)


    def ss(self):
       self.photo = self.photo.filter(ImageFilter.DETAIL)

       def aa(self):
           self.photo = self.photo.filter(ImageFilter.BLUR)

       def hh(self):
           self.photo = self.photo.filterImageEnhance.Color(self.photo).enhance(1.5)


def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap

def show_images(self):
   pixels = pil2pixmap(self.photo)
   pixels = pixels.scaledToWidth(500)
   image_lbl.setPixmap(pixels)



app = QApplication([])

window = QWidget()
folder = QPushButton("Папка")
image_lbl = QLabel("Картинка")
list = QListWidget()
photo = QLabel("фото")
left = QPushButton("Вліво")
rr = QPushButton("Накладання конрурів")
mirror = QPushButton("Дзеркало")
sharpness = QPushButton("Різкість")
chb = QPushButton("Ч/Б")


hh = QPushButton("Збільшення насиченості")
aa = QPushButton("Розмивання")
sss =  QPushButton("Збшльшення детфлізації")




mainline = QHBoxLayout()
line = QVBoxLayout()
line2 = QVBoxLayout()
line3 = QHBoxLayout()

mainline.addLayout(line)
mainline.addLayout(line2)

line.addWidget(folder)
line.addWidget(list)
line2.addWidget(photo)
line2.addLayout(line3)

line3.addWidget(left)
line3.addWidget(rr)
line3.addWidget(mirror)
line3.addWidget(sharpness)
line3.addWidget(chb)


app.setStyleSheet("""
         QWidget {
             background:  #OOff66;
         }


        QPushButton
        {
        backgroud-color: #66ff00;
        border-style: outset;
        font-family; Roboro;
        main-width: 6em:
""")

photo_manager = PhotoManager()
photo_manager.image_lbl = image_lbl
def open_folder():
    photo_manager.folder = QFileDialog.getExistingDirectoryUrl()
    files = os.listdir(photo_manager.folder)
    list.clear()
    list.addItems(files)


def show_chesen_image():
    photo_manager.fiename = list.currentItem().text()
    photo_manager.show_images(photo)

list.currentRowChanged.connect(show_chesen_image)
chb.clicked.connect(photo_manager.bw)
left.clicked.connect(photo_manager.leften)
mirror.clicked.connect(photo_manager.mirron)
rr.clicked.connect(photo_manager.rr)
sss.clicked.connect(photo_manager.ss)
aa.clicked.connect(photo_manager.aa)
hh.clicked.connect(photo_manager.hh)
sharpness.clicked.connect(photo_manager.risk())
folder.clicked.connect(open_folder)
window.setLayout(mainline)
window.show()
app.exec()

