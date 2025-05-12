from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QVBoxLayout, QFileDialog, QTextEdit
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

class FileDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Dialog Demo")
        self.setGeometry(100, 100, 600, 600)

        self.loaded_pixmap = None 


        self.btn_img = QPushButton("QFile Dialog Static Method Demo")
        self.btn_img.clicked.connect(self.openImage)

        
        self.image_label = QLabel("Image will appear here")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedHeight(250)
        self.image_label.setScaledContents(True)

        
        self.btn_text = QPushButton("QFileDialog Object")
        self.btn_text.clicked.connect(self.openText)

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        
        layout = QVBoxLayout()
        layout.addWidget(self.btn_img)
        layout.addWidget(self.image_label)
        layout.addWidget(self.btn_text)
        layout.addWidget(self.text_area)

        self.setLayout(layout)
        self.show()

    def openImage(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        if file_name:
            pixmap = QPixmap(file_name)
            if not pixmap.isNull():
                self.loaded_pixmap = pixmap
                self.updateImage()
            else:
                self.image_label.setText("Failed to load image.")

    def updateImage(self):
        if self.loaded_pixmap:
            scaled_pixmap = self.loaded_pixmap.scaled(
                self.image_label.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.image_label.setPixmap(scaled_pixmap)

    def resizeEvent(self, event):
        self.updateImage()
        super().resizeEvent(event)

    def openText(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Text File", "", "Text Files (*.txt *.log);;All Files (*)"
        )
        if file_name:
            try:
                with open(file_name, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                self.text_area.setPlainText(content)
            except Exception as e:
                self.text_area.setPlainText(f"Failed to load text file:\n{str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileDialogDemo()
    sys.exit(app.exec_())
