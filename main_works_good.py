import sys  
import os  
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from PyQt5 import QtWidgets
import pickle
import pds as projectDesign 
from sklearn.externals import joblib
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import csv
def make_str(array):
	answer_str=''
	for i in range(len(array)):
		diagnoz=''
		if(array[i]==0):
			diagnoz = 'Здоров'
		if(array[i]==1):
			diagnoz='Слабые подозрение на заболевание сердца'
		if(array[i]==2):
			diagnoz='Возможна болезнь сердца'
		if(array[i]==3):
			diagnoz='Обнаружена болезнь сердца'
		if(array[i]==4):
			diagnoz='Серьезное заболевание сердца'
		
		answer_str+=('У '+str(i+1)+'ого пациента диагноз - '+str(diagnoz)+'\n')
	return answer_str
class ExampleApp(QtWidgets.QMainWindow, projectDesign.Ui_MainWindow):
    def __init__(self):
          super().__init__()
          self.setupUi(self)
          self.pushButton.clicked.connect(self.browse_folder)  


    def browse_folder(self):
        #self.listWidget.clear() 
        directory = QtWidgets.QFileDialog.getOpenFileName(self, "Select a folder")
        data=pd.read_csv(directory[0].split('/')[-1])
        

        if directory: 
            rfc = joblib.load('rf_classifier.pkl')
            ic=0
            self.tableWidget.setColumnCount(13)
            with open(directory[0].split('/')[-1], newline='') as csvfile:
                reader=csv.reader(csvfile,delimiter=',')
                for row in reader:
                    ic+=1
            self.tableWidget.setRowCount(ic)
            ic=0
            with open('test.csv', newline='') as csvfile:
                reader=csv.reader(csvfile,delimiter=',')
            #print(reader)
			
                for row in reader:
                    
                    for j in range(len(row)):
                    
                        self.tableWidget.setItem(ic,j, QTableWidgetItem(row[j]))
                    ic+=1
                    
            mb=QMessageBox();predictions=rfc.predict(data)
            mb.information(self, "Prediction", make_str(rfc.predict(data))); self.tableWidget.show()

			
  
def main():
	
    app = QtWidgets.QApplication(sys.argv)  
    window = ExampleApp()  
    window.show() 
    app.exec_()  
if __name__ == '__main__':  
    main()  