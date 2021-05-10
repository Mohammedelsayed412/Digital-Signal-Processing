from __future__ import print_function
from PyQt5 import QtWidgets
from home import Ui_MainWindow
from Song import Ui_Song
from party import Ui_party
from ECG import Ui_ECG
import sys
from scipy.io import wavfile
from FastICA import FastICA as FA
import utilities as utl
import numpy as np
from sklearn.datasets import load_digits
from sklearn.decomposition import FastICA
import scipy.io.wavfile
from matplotlib import pyplot as plt
import pandas as pd 
import librosa.display
import librosa
import skimage
from skimage import io
from skimage.transform import resize
import matplotlib.image as mpimg
from pyqtgraph import PlotWidget
import pyqtgraph as pg
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout,QTableWidgetItem
from PyQt5 import QtCore, QtWidgets, QtMultimedia


class pop_window1(QtWidgets.QMainWindow,Ui_Song):
    path = ""
    
    def __init__(self):
        super(pop_window1, self).__init__()
        self.ui1 = Ui_Song()
        self.ui1.setupUi(self)
        self.ui1.songOpen.clicked.connect(self.loaddata)
        self.ui1.song_result.clicked.connect(self.control)

    def loaddata(self):
        filename = QFileDialog.getOpenFileName(self)
        if filename[0]:
            self.path = filename[0]
        if  not (self.path.endswith(".wav")):
            self.alarm("Please Chose .wav File")

    def song(self,path):
        y, sr = librosa.load(self.path, duration=120)
        S_full, phase = librosa.magphase(librosa.stft(y))

        S_filter = librosa.decompose.nn_filter(S_full,aggregate=np.median,metric='cosine',
                    width=int(librosa.time_to_frames(2, sr=sr)))                                     
        S_filter = np.minimum(S_full, S_filter)
        margin_i, margin_v = 2, 10
        power = 2

        mask_i = librosa.util.softmask(S_filter,margin_i * (S_full - S_filter),power=power)
        mask_v = librosa.util.softmask(S_full - S_filter,margin_v * S_filter,power=power)

        S_foreground = mask_v * S_full
        S_background = mask_i * S_full

        music =librosa.griffinlim(S_background)
        vocal =librosa.griffinlim(S_foreground)
        scipy.io.wavfile.write('sound_results/song/music.wav',sr,music) 
        scipy.io.wavfile.write('sound_results/song/vocal.wav',sr,vocal) 
        utl.plotSounds([music, vocal], ["music", "vocal"], sr, "plot_results/song/song_separation_plot.png")
        img = pg.QtGui.QGraphicsPixmapItem(pg.QtGui.QPixmap('plot_results/song/song_separation_plot.png'))
        self.ui1.widget_song.addItem(img)
        self.ui1.widget_song.invertY(True)
        self.alarm("Check Plot & Sound Results Files")

    def alarm(self,value):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText(value)  
        msg.setIcon(QMessageBox.Warning)
        x=msg.exec_() 

    
    def control(self):
        if(self.path==""):
            self.alarm("Please Select Song First")
        else:
            self.song(self.path)

class pop_window2(QtWidgets.QMainWindow,Ui_party):
    path1 =""
    path2 =""
    def __init__(self):
        super(pop_window2, self).__init__()
        self.ui2=Ui_party()
        self.ui2.setupUi(self)
        self.ui2.party1.clicked.connect(self.loaddata1)
        self.ui2.party2.clicked.connect(self.loaddata2)
        self.ui2.result_party.clicked.connect(self.control)
        

    
    def loaddata1(self):
        filename = QFileDialog.getOpenFileName(self)
        if filename[0]:
            self.path1 = filename[0]
        if  not (self.path1.endswith(".wav")):
            self.alarm("Please Chose .wav File")
        

    def loaddata2(self):
        filename = QFileDialog.getOpenFileName(self)
        if filename[0]:
            self.path2 = filename[0]
        if  not (self.path2.endswith(".wav")):
            self.alarm("Please Chose .wav File")
            
            
    def cocktail(self):
        eps = 0.00000001
        rate1, data1 = wavfile.read(self.path1)
        rate2, data2 = wavfile.read(self.path2)
        if(data1.ndim != 1 or data2.ndim != 1):
            self.alarm("Please Chose another file with 1D data")
        else:
            data1 = data1 - np.mean(data1)
            data1 = data1/max(data1)
            data2 = data2 - np.mean(data2)
            data2 = data2/max(data2)
            signals = [data1, data2]
            matrix = np.vstack(signals)
            whiteMatrix = utl.whitenMatrix(matrix)
            X = whiteMatrix
            vectors = []
            for i in range(0, X.shape[0]):
                vector = FA(X, vectors, eps)
                vectors.append(vector)
                
            
            W = np.vstack(vectors)
            

            S = np.dot(W, whiteMatrix)

            utl.plotSounds([S[0], S[1]], ["source_1", "source_2"], rate1, "plot_results/cocktail_party/song_separation_plot.png")
            wavfile.write("sound_results/cocktail_party/source1.wav" ,rate1, 5000*S[0].astype(np.int16))
            wavfile.write("sound_results/cocktail_party/source2.wav" , rate1, 5000*S[1].astype(np.int16))
            img = pg.QtGui.QGraphicsPixmapItem(pg.QtGui.QPixmap('plot_results/cocktail_party/song_separation_plot.png'))
            self.ui2.widget_party.addItem(img)
            self.ui2.widget_party.invertY(True)
            self.alarm("Check Plot & Sound Results Files")
        

    def control(self):
        if(self.path1=="" or self.path2==""):
            self.alarm("Please Make Sure Of Choose 2 Files")
        else:
            self.cocktail()

    def alarm(self,value):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText(value)  
        msg.setIcon(QMessageBox.Warning)
        x=msg.exec_() 

class pop_window3(QtWidgets.QMainWindow,Ui_ECG):
    path=""
    
    def __init__(self):
        super(pop_window3, self).__init__()
        self.ui3=Ui_ECG()
        self.ui3.setupUi(self)
        self.ui3.ecgopen.clicked.connect(self.loaddata)
        self.ui3.ecg_result.clicked.connect(self.control)
    
    def loaddata(self):
        filename = QFileDialog.getOpenFileName(self)
        if filename[0]:
            self.path = filename[0]
        if  not (self.path.endswith(".csv")):
            self.alarm("Please Chose .csv Format")
        

    def ecg(self,path):
        y= pd.read_csv(path)
        if(y.ndim != 2):
            self.alarm("Please Chose 2D data ")
        else:
            data1 = np.array(y.iloc[:3500,0])
            data2= np.array(y.iloc[:3500,1])
            data= np.c_[data1,data2] 
            m = data1+data2
            transformer = FastICA(n_components=2
                    ,random_state=0)
            data_transformed = transformer.fit_transform(data)
            data_transformed = data_transformed.transpose()
            self.plot(m,data_transformed[0]*-1,data_transformed[1]*-1,"plot_results/ecg/ecg_plot.png")
            img = pg.QtGui.QGraphicsPixmapItem(pg.QtGui.QPixmap('plot_results/ecg/ecg_plot.png'))
            self.ui3.widget_ecg.addItem(img)
            self.ui3.widget_ecg.invertY(True)
            self.alarm("Check Plot files")
        
    def plot(self,sig1,sig2,sig3,path):
        fig = plt.figure()
        plt.subplot(3, 1,1)        
        plt.plot(sig1,color = 'red')
        plt.subplot(3, 1,2) 
        plt.plot((sig2),color = 'orange')
        plt.subplot(3, 1,3) 
        plt.plot((sig3),color = 'blue')
        fig.tight_layout()     
        fig.savefig(path)

    def control(self):
        if(self.path==""):
            self.alarm("Please Make Sure Of Choose 2 Files")
        else:
            self.ecg(self.path)

    def alarm(self,value):
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText(value)  
        msg.setIcon(QMessageBox.Warning)
        x=msg.exec_()



class ApplicationWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Button_song.clicked.connect(self.popWin1)
        self.ui.Button_party.clicked.connect(self.popWin2)
        self.ui.Button_ECG.clicked.connect(self.popWin3)

    def popWin1(self):
        
        global application1
        application1=pop_window1()
        application1.show()

    
    
    def popWin2(self):

        global application2
        application2=pop_window2()
        application2.show()


    def popWin3(self):   

        global application3
        application3=pop_window3()
        application3.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()