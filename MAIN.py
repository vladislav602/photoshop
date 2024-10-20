import os

from PyQt5.QtWidgets import *
from PIL import Image
import os

class PhotoManager:
    def __init__(self):
        self.photo = None
        self.folder = None
        self.filename = None


    def loed(self):
        imahe_path = os.path.join(self,folder, self,filename)
        self.photo = Image.open(imahe_path)

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
list = QListWidget()
photo = QLabel("фото")
left = QPushButton("Вліво")
right = QPushButton("Вправо")
mirror = QPushButton("Дзеркало")
sharpness = QPushButton("Різкість")
chb = QPushButton("Ч/Б")




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
line3.addWidget(right)
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

def open_folder():
    photo_manager.folder = QFileDialog.getExistingDirectoryUrl()
    files = os.listdir(photo_manager.folder)
    list.clear()
    list.addItems(files)


def show_chjsen_image():
    photo_manager.fiename = images_list.currentItem().text()
    photo_manager.show_images(photo)

images_list.connect(show_chosen_image)
folder.clicked.connect(open_folder()
window.setLayout(mainline)
window.show()
app.exec()

