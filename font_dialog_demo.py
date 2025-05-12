from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QVBoxLayout, QFontDialog
)
import sys
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class FontDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Font Dialog demo")
        self.setGeometry(100, 100, 600, 600)

        self.label = QLabel("Hello", self)
        self.label.setFont(QFont("Arial", 14))
        self.label.setAlignment(Qt.AlignCenter)

        self.btn = QPushButton("choose font", self)
        self.btn.clicked.connect(self.openFontDialog)

        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.show()

    def openFontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FontDialogDemo()
    sys.exit(app.exec_())
