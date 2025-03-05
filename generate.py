from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QComboBox, QPushButton, QSlider
from PySide6.QtCore import Qt

class GenerateWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generate Data")
        self.setGeometry(550, 550, 400, 300)

        # Layout
        layout = QVBoxLayout()

        self.label = QLabel("Select options for data generation:", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 14px; font-weight: bold; color: black; margin: 10px")
        layout.addWidget(self.label)

        # Dropdowns
        self.label1 = QLabel("Select Scaling Factor", self)
        self.label1.setAlignment(Qt.AlignLeft)
        self.label1.setStyleSheet("font-size: 12px; font-weight: bold; color:black; margin-top: 10px; margin-left: 5px;")
        layout.addWidget(self.label1)

        self.dropdown1 = QComboBox(self)
        self.dropdown1.addItems(["Option 1A", "Option 1B", "Option 1C"])
        self.dropdown1.setStyleSheet("color: black;")  # Modify with actual options
        layout.addWidget(self.dropdown1)

        self.label2 = QLabel("Select Ground Truth Size:", self)
        self.label2.setAlignment(Qt.AlignLeft)
        self.label2.setStyleSheet("font-size: 12px; font-weight: bold; color:black; margin-top: 10px; margin-left: 5px;")
        layout.addWidget(self.label2)

        self.dropdown2 = QComboBox(self)
        self.dropdown2.addItems(["Option 2A", "Option 2B", "Option 2C"])
        self.dropdown2.setStyleSheet("color: black;")  # Modify with actual options
        layout.addWidget(self.dropdown2)

        self.label3 = QLabel("Select Ground Truth Distance:", self)
        self.label3.setAlignment(Qt.AlignLeft)
        self.label3.setStyleSheet("font-size: 12px; font-weight: bold; color:black; margin-top: 10px; margin-left: 5px;")
        layout.addWidget(self.label3)

        self.slider1 = QSlider(Qt.Horizontal, self)
        self.slider1.setRange(-12.5, 12.5)
        self.slider1.setTickInterval(.5)
        self.slider1.setTickPosition(QSlider.TicksBelow)
        layout.addWidget(self.slider1)
        
        self.slider2 = QSlider(Qt.Horizontal, self)
        self.slider2.setRange(-12.5, 12.5)
        self.slider2.setTickInterval(.5)
        self.slider2.setTickPosition(QSlider.TicksBelow)
        layout.addWidget(self.slider2)
        self.slider_label1 = QLabel("Vertical Value: 0", self)
        self.slider_label1.setStyleSheet("font-size: 12px; font-weight: bold; color:black; margin: 5px")
        layout.addWidget(self.slider_label1)
        
        self.slider_label2 = QLabel("Horizontal Value: 0", self)
        self.slider_label2.setStyleSheet("font-size: 12px; font-weight: bold; color:black; margin: 5px")
        layout.addWidget(self.slider_label2)
        
        self.slider1.valueChanged.connect(lambda value: self.slider_label1.setText(f"Slider 1 Value: {value}"))
        self.slider2.valueChanged.connect(lambda value: self.slider_label2.setText(f"Slider 2 Value: {value}"))  # Modify with actual options

        # Save Button
        self.save_button = QPushButton("Save Selections", self)
        self.save_button.setStyleSheet("background-color: #B7BFC7; font-size: 14px; font-weight: bold; padding: 10px")
        self.save_button.clicked.connect(self.save_selections)
        layout.addWidget(self.save_button)

        # Container
        container = QWidget()
        container.setLayout(layout)
        container.setStyleSheet("background-color: #E2E5E8;")
        self.setCentralWidget(container)

    def save_selections(self):
        self.selection1 = self.dropdown1.currentText()
        self.selection2 = self.dropdown2.currentText()
        self.selection3_slider1 = self.slider1.value()
        self.selection3_slider2 = self.slider2.value()
        print(f"Selections saved: {self.selection1}, {self.selection2}, Slider 1: {self.selection3_slider1}, Slider 2: {self.selection3_slider2}")  # Replace with actual saving logic
