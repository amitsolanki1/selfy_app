import sys
from time import sleep,strftime
import datetime
from turtle import width 
from face import Ui_MainWindow
import cv2
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage,QPixmap

# class main_(QThread):
#     def __init__(self):
#         super(main_,self).__init__()
#         self.ui=Ui_MainWindow()
#         self.ui.setupUi(self)
#     def run(self):
        
# startfirstclass=main_()

class Main(QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        cam=cv2.VideoCapture(0)
        self.ui.pushButton.clicked.connect(lambda x:self.fetchimg(cam))

    def fetchimg(self,img):
        count=0
        while True:
            _,image=img.read()
            if _ is not None:
                image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
                image=cv2.flip(image,1)
                height,width,channel=image.shape
                step=channel*width
                Qimage=QImage(image.data,width,height,step,QImage.Format_RGB888)
                self.ui.label.setPixmap(QPixmap.fromImage(Qimage))
                # self.ui.label.setText(str(frame))
                if cv2.waitKey(0) & 0xFF==ord('q'):
                    break
                a=1
                if a:
                    image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
                    self.ui.pushButton1.clicked.connect(lambda x:self.takeimg(image,count,a))
                # a=0
                count+=1
        img.release()
        cv2.destroyAllWindows()
    def takeimg(self,mg,status,check):
        # for i in range(2):
        if check:
            t=datetime.datetime.now();
            t=strftime("%m_%Y_%H_%M_%p")
            # print(t)
            mg=cv2.cvtColor(mg,cv2.COLOR_BGR2RGB)
            cv2.imwrite(f"{t}_{status}.png",mg)
                # break

app=QApplication(sys.argv)
s=Main()
s.show()
sys.exit(app.exec_())