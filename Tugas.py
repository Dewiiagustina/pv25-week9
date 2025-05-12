from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox,QPushButton,
    QLineEdit, QTabWidget, QFormLayout, QVBoxLayout, QWidget, QLabel, QFontDialog,QInputDialog
)
import sys

class MenuBarDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week-9, QDialog, QTabWidget & Menu Bar ")
        self.setGeometry(100, 100, 600, 400)

        # Menu Bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        file_fitur = menu_bar.addMenu("Fitur")

        # Exit
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Feature actions
        inName_action = QAction("Input Name", self)
        inName_action.triggered.connect(self.show_input_name_tab)
        file_fitur.addAction(inName_action)

        chosFont_action = QAction("Pilih Font", self)
        chosFont_action.triggered.connect(self.choose_font)
        file_fitur.addAction(chosFont_action)

        opFile_action = QAction("Buka file", self)
        opFile_action.triggered.connect(self.open_file)
        file_fitur.addAction(opFile_action)

        # Tabs
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tabs.addTab(self.tab1, "Input Nama")
        self.tabs.addTab(self.tab2, "Pilih Font")
        self.tabs.addTab(self.tab3, "Buka File")

        self.init_tab1()
        self.init_tab2()
        self.init_tab3()

    def init_tab1(self):
        layout = QVBoxLayout()
        self.name_input = QPushButton("Input nama")
        self.name_input.clicked.connect(self.getName)
        self.label_name=QLabel("Nama : ")
        layout.addWidget(self.name_input)
        layout.addWidget(self.label_name)
        self.tab1.setLayout(layout)
    
    def init_tab2(self):
        layout = QVBoxLayout()
        self.font_input=QPushButton("Pilih Font")
        self.font_input.clicked.connect(self.choose_font)
        self.font_label = QLabel("Nama: ")
        layout.addWidget(self.font_input)
        layout.addWidget(self.font_label)
        self.tab2.setLayout(layout)
        
    def getName(self):
        text,ok=QInputDialog.getText(self,"Text input Dialog", "Enter your name")
        if ok and text:
            self.label_name.setText(f"Name: {text}")
            self.font_label.setText(f"Name: {text}")

    def init_tab3(self):
        layout = QVBoxLayout()
        self.file_input=QPushButton("BUka File .txt")
        self.file_input.clicked.connect(self.open_file)
        self.text_area = QTextEdit()
        layout.addWidget(self.file_input)
        layout.addWidget(self.text_area)
        self.tab3.setLayout(layout)

    def show_input_name_tab(self):
        self.tabs.setCurrentIndex(0)

    def choose_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.font_label.setFont(font)
            self.tabs.setCurrentIndex(1)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Text File","","Text Files(*.txt)")
        if file_name:
            try:
                with open(file_name, 'r',encoding='utf-8',errors='ignore') as f:
                    content = f.read()
                self.text_area.setText(content)
                self.tabs.setCurrentIndex(2)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal membuka file: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MenuBarDemo()
    window.show()
    sys.exit(app.exec_())
