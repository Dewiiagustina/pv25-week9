from PyQt5.QtWidgets import (
    QApplication, QWidget, QStackedWidget, QListWidget,
    QHBoxLayout, QVBoxLayout, QFormLayout, QLabel, QLineEdit,
    QRadioButton, QCheckBox
)
import sys

class StackedWidgetDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StackedWidget demo")
        self.setGeometry(100, 100, 600, 200)

        # List menu di kiri
        self.list_widget = QListWidget()
        self.list_widget.insertItem(0, "Contact")
        self.list_widget.insertItem(1, "Personal")
        self.list_widget.insertItem(2, "Educational")

        # Stacked widget
        self.stack = QStackedWidget()
        self.stack.addWidget(self.contactUI())
        self.stack.addWidget(self.personalUI())
        self.stack.addWidget(self.educationalUI())

        # Layout utama
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.list_widget)
        main_layout.addWidget(self.stack)

        self.setLayout(main_layout)

        # Event list selection
        self.list_widget.currentRowChanged.connect(self.stack.setCurrentIndex)

    def contactUI(self):
        widget = QWidget()
        layout = QFormLayout()
        layout.addRow("Name", QLineEdit())
        layout.addRow("Address", QLineEdit())
        widget.setLayout(layout)
        return widget

    def personalUI(self):
        widget = QWidget()
        layout = QFormLayout()

        male_radio = QRadioButton("Male")
        female_radio = QRadioButton("Female")
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(male_radio)
        gender_layout.addWidget(female_radio)

        layout.addRow("Sex", gender_layout)
        layout.addRow("Date of Birth", QLineEdit())
        widget.setLayout(layout)
        return widget

    def educationalUI(self):
        widget = QWidget()
        layout = QFormLayout()

        physics_cb = QCheckBox("Physics")
        maths_cb = QCheckBox("Maths")
        subject_layout = QHBoxLayout()
        subject_layout.addWidget(physics_cb)
        subject_layout.addWidget(maths_cb)

        layout.addRow("Subjects", subject_layout)
        widget.setLayout(layout)
        return widget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = StackedWidgetDemo()
    demo.show()
    sys.exit(app.exec_())
