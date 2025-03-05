from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QComboBox, QPushButton, QSlider, QFrame
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

        # self.label3 = QLabel("Select Ground Truth Distance:", self)
        # self.label3.setAlignment(Qt.AlignLeft)
        # self.label3.setStyleSheet("font-size: 12px; font-weight: bold; color:black; margin-top: 10px; margin-left: 5px;")
        # layout.addWidget(self.label3)

        # self.slider1 = QSlider(Qt.Horizontal, self)
        # self.slider1.setRange(-12.5, 12.5)
        # self.slider1.setTickInterval(.5)
        # self.slider1.setTickPosition(QSlider.TicksBelow)
        # layout.addWidget(self.slider1)
        
        # self.slider2 = QSlider(Qt.Horizontal, self)
        # self.slider2.setRange(-12.5, 12.5)
        # self.slider2.setTickInterval(.5)
        # self.slider2.setTickPosition(QSlider.TicksBelow)
        # layout.addWidget(self.slider2)
        # self.slider_label1 = QLabel("Vertical Value: 0", self)
        # self.slider_label1.setStyleSheet("font-size: 12px; font-weight: bold; color:black; margin: 5px")
        # layout.addWidget(self.slider_label1)
        
        # self.slider_label2 = QLabel("Horizontal Value: 0", self)
        # self.slider_label2.setStyleSheet("font-size: 12px; font-weight: bold; color:black; margin: 5px")
        # layout.addWidget(self.slider_label2)
        
        # self.slider1.valueChanged.connect(lambda value: self.slider_label1.setText(f"Slider 1 Value: {value}"))
        # self.slider2.valueChanged.connect(lambda value: self.slider_label2.setText(f"Slider 2 Value: {value}"))  # Modify with actual options

        self.grid = QFrame(self)
        self.grid.setFixedSize(250, 250)
        self.grid.setStyleSheet("background-color: black; margin: 10px")
        layout.addWidget(self.grid)
# **4x4 Box (Movable)**
        self.box = QLabel(self.grid)
        self.box.setFixedSize(40, 40)  # 4x4 box in a 25x25 grid
        self.box.setStyleSheet("background-color: red; border: 1px solid black; opacity: 0.7;")
        self.box.move(0, 0)  # Start at top-left (0,0)

        # **Sliders**
        self.label_x = QLabel("X Position: 0", self)
        self.label_x.setStyleSheet("font-size: 12px; font-weight: bold; color:black; margin: 5px")
        layout.addWidget(self.label_x)

        self.slider_x = QSlider(Qt.Horizontal, self)
        self.slider_x.setRange(0, 21)  # Max 21 to prevent moving out of 25x25 grid
        self.slider_x.setTickInterval(1)
        self.slider_x.setTickPosition(QSlider.TicksBelow)
        layout.addWidget(self.slider_x)

        self.label_y = QLabel("Y Position: 0", self)
        self.label_y.setStyleSheet("font-size: 12px; font-weight: bold; color:black; margin: 5px")
        layout.addWidget(self.label_y)

        self.slider_y = QSlider(Qt.Horizontal, self)
        self.slider_y.setRange(0, 21)
        self.slider_y.setTickInterval(1)
        self.slider_y.setTickPosition(QSlider.TicksBelow)
        layout.addWidget(self.slider_y)

        # **Slider event connections**
        self.slider_x.valueChanged.connect(self.update_box_position)
        self.slider_y.valueChanged.connect(self.update_box_position)


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
        self.slider_x = self.slider_x.value()
        self.slider_y = self.slider_y.value()
        print(f"Selections saved: {self.selection1}, {self.selection2}, Slider 1: {self.selection3_slider1}, Slider 2: {self.selection3_slider2}")  # Replace with actual saving logic



    def update_box_position(self):
        """Updates the 4x4 box position based on slider values."""
        x_pos = self.slider_x.value() * 10  # Scale to pixel space
        y_pos = self.slider_y.value() * 10  # Scale to pixel space

        # **Update Labels**
        self.label_x.setText(f"X Position: {self.slider_x.value()}")
        self.label_y.setText(f"Y Position: {self.slider_y.value()}")

        # **Move the box**
        self.box.move(x_pos, y_pos)

    def save_selection(self):
        """Saves the selection and converts to a CSV format."""
        x_grid = self.slider_x.value()
        y_grid = self.slider_y.value()

        # **Generate 25x25 matrix with 0s**
        grid_data = [[0 for _ in range(25)] for _ in range(25)]

        # **Mark the selected 4x4 area with 1s**
        for i in range(4):
            for j in range(4):
                grid_data[y_grid + i][x_grid + j] = 1  # y first, then x (row-major order)

        # **Save to CSV**
        with open("ground_truth.csv", "w") as file:
            for row in grid_data:
                file.write(",".join(map(str, row)) + "\n")

        print(f"Saved ground truth box at ({x_grid}, {y_grid}) to 'ground_truth.csv'.")
