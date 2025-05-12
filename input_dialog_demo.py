from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QPushButton, QLabel, QVBoxLayout,QLineEdit, QFormLayout

import sys


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("input dialog demo")
        self.setGeometry(100,100,600,100)
        
        self.list_edit=QLineEdit()
        self.name_edit=QLineEdit()
        self.number_edit=QLineEdit()
        
        self.list_btn=QPushButton("Choose from list")
        self.list_btn.clicked.connect(self.getList)
        
        self.name_btn=QPushButton("Get Name")
        self.name_btn.clicked.connect(self.getName)
        
        self.number_btn=QPushButton("get Integer")
        self.number_btn.clicked.connect(self.getNumber)
        
        
        layout=QFormLayout()
        layout.addRow(self.list_btn, self.list_edit)
        layout.addRow(self.name_btn,self.name_edit)
        layut.addRow(self.number_btn,self.number_edit)
        
        self.setLayout(layout)
        self.show()
        
    def getList(self):
        items=["c","c++","java","python"]
        item,ok=QInputDialog.getItem(self,"select input dialog","list of languages",items,0,False)
        if ok and item:
            self.list_edit.setText(item)
            
    def getName(self):
        text,ok=QInputDialog.getText(self,"Text input dialog","Enter your name")
        if ok and text:
            self.name_edit.setText(text)
            
    def getNumber(self):
        num,ok=QInputDialgo.getInt(self,"integer input dualog", "enter a number")
        if ok:
            self.number_edit.setText(str(num))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
