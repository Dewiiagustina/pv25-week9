from PyQt5.QtWidgets import (
    QApplication, QWidget, QTabWidget, QVBoxLayout,
    QLabel, QLineEdit, QRadioButton, QCheckBox,
    QHBoxLayout, QFormLayout
)
import sys

class TabDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab Demo")
        self.setGeometry(100, 100, 600, 200)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.tabs.addTab(self.tab1, "Contact Details")
        self.tabs.addTab(self.tab2, "Personal Details")
        self.tabs.addTab(self.tab3, "Education Details")

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)

    def tab1UI(self):
        layout = QFormLayout()
        self.name_input = QLineEdit()
        self.address_input = QLineEdit()
        layout.addRow("Name", self.name_input)
        layout.addRow("Address", self.address_input)
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QFormLayout()
        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")

        gender_layout = QHBoxLayout()
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)

        self.dob_input = QLineEdit()

        layout.addRow("Sex", gender_layout)
        layout.addRow("Date of Birth", self.dob_input)
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QFormLayout()
        self.physics_check = QCheckBox("Physics")
        self.maths_check = QCheckBox("Maths")

        subject_layout = QHBoxLayout()
        subject_layout.addWidget(self.physics_check)
        subject_layout.addWidget(self.maths_check)

        layout.addRow("Subjects", subject_layout)
        self.tab3.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = TabDemo()
    demo.show()
    sys.exit(app.exec_())
