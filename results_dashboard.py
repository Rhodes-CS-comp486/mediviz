from PySide6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, QLabel, QTableWidget, QTableWidgetItem,
    QHeaderView, QPushButton, QFileDialog, QMessageBox
)
from PySide6.QtCore import Qt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import re

class ResultsWindow(QMainWindow):
    def __init__(self, report_text, y_true=None, y_pred=None, train_true=None, train_pred=None, model=None):
        super().__init__()
        self.setWindowTitle("SVM Results Dashboard")
        self.setGeometry(500, 500, 700, 500)
        self.y_true = y_true
        self.y_pred = y_pred
        self.report_text = report_text
        self.model = model
        self.train_true = train_true
        self.train_pred = train_pred

        layout = QVBoxLayout()

        label = QLabel("SVM Classification Report")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 18px; font-weight: bold; color: black; margin: 10px;")
        layout.addWidget(label)

        self.table = QTableWidget()
        self.populate_table(report_text)
        layout.addWidget(self.table)

        # Export Button
        export_button = QPushButton("Export Report to CSV")
        export_button.clicked.connect(self.export_to_csv)
        layout.addWidget(export_button)

        # TRAINING Confusion Matrix Button (only if data available)
        if train_true is not None and train_pred is not None:
            cm_train_button = QPushButton("Show Training Confusion Matrix")
            cm_train_button.clicked.connect(self.show_training_confusion_matrix)
            layout.addWidget(cm_train_button)
        
        # TESTING Confusion Matrix Button (only if data available)
        if y_true is not None and y_pred is not None:
            cm_test_button = QPushButton("Show Testing Confusion Matrix")
            cm_test_button.clicked.connect(self.show_testing_confusion_matrix)
            layout.addWidget(cm_test_button)
        
        hm_button = QPushButton("Show Voxel Weight Heatmap")
        hm_button.clicked.connect(lambda: self.show_heatmap())
        layout.addWidget(hm_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def populate_table(self, report):
        

        lines = [line.strip() for line in report.strip().split('\n') if line.strip()]

        # Detect header row
        header_match = re.findall(r'\S+', lines[0])
        header = header_match
        data_lines = lines[1:]

        self.table.setColumnCount(len(header) + 1)
        self.table.setRowCount(len(data_lines))
        self.table.setHorizontalHeaderLabels([""] + header)

        for row_idx, line in enumerate(data_lines):
            # Use regex to split line into label and values
            match = re.match(r'(\D+?)\s+([\d\.]+\s+[\d\.]+\s+[\d\.]+\s+[\d\.]+)', line)
            if match:
                label = match.group(1).strip()
                values = match.group(2).split()
            else:
                parts = line.split()
                label = parts[0]
                values = parts[1:]

            self.table.setItem(row_idx, 0, QTableWidgetItem(label))

            for col_idx, value in enumerate(values):
                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignCenter)

                # Color coding
                try:
                    float_val = float(value)
                    if float_val >= 0.9:
                        item.setBackground(Qt.green)
                    elif float_val < 0.6:
                        item.setBackground(Qt.red)
                except:
                    pass

                self.table.setItem(row_idx, col_idx + 1, item)

                self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                self.table.verticalHeader().setVisible(False)
                self.table.setStyleSheet("""
                    QTableWidget {
                        border: 1px solid #ccc;
                        font-size: 14px;
                        background-color: #1e1e1e;
                        color: white;
                    }
                    QHeaderView::section {
                        background-color: #2b2b2b;
                        color: white;
                        font-weight: bold;
                        border: 1px solid #555;
                        padding: 4px;
                    }
                """)
                
    def export_to_csv(self):
        save_path, _ = QFileDialog.getSaveFileName(self, "Save Report", "svm_report.csv", "CSV Files (*.csv)")
        if not save_path:
            return

        with open(save_path, 'w') as f:
            header = []
            for i in range(self.table.columnCount()):
                header.append(self.table.horizontalHeaderItem(i).text())
            f.write(','.join(header) + '\n')

            for row in range(self.table.rowCount()):
                row_data = []
                for col in range(self.table.columnCount()):
                    item = self.table.item(row, col)
                    row_data.append(item.text() if item else '')
                f.write(','.join(row_data) + '\n')

        QMessageBox.information(self, "Success", f"Report saved to:\n{save_path}")

    def show_training_confusion_matrix(self):
        if self.train_true is None or self.train_pred is None:
            QMessageBox.warning(self, "Error", "Missing labels for confusion matrix.")
            return
        
        cm_train = confusion_matrix(self.train_true, self.train_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm_train)
        disp.plot(cmap=plt.cm.Blues)
        plt.title("Training Confusion Matrix", color="black")
        plt.show()

    def show_testing_confusion_matrix(self):
        if self.y_true is None or self.y_pred is None:
            QMessageBox.warning(self, "Error", "Missing labels for confusion matrix.")
            return

        cm_test = confusion_matrix(self.y_true, self.y_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm_test)
        disp.plot(cmap=plt.cm.Blues)
        plt.title("Testing Confusion Matrix", color="black")
        plt.show()
        
    def show_heatmap(self):
        if self.model is None:
            QMessageBox.warning(self, "Missing Model", "No Model Selected")
            return
        
        try: 
            if hasattr(self.model, 'coef_'):
                import os
                # Get the directory this script is in
                base_dir = os.path.dirname(os.path.abspath(__file__))

                # Point to ground_truth.csv in the project root
                gt_path = os.path.join(base_dir, "ground_truth.csv")
                ground_truth = pd.read_csv(gt_path, header = None).values 
                
                weights = self.model.coef_[0]
                heatmap = weights.reshape((50,50))
                
                plt.figure(figsize=(6,5))
                
                #switch between hot / seismic for heatmap?
                max_abs = np.max(np.abs(heatmap))  # Get the largest absolute weight
                heatmap_im = plt.imshow(
                    heatmap,
                    cmap='seismic',
                    interpolation='nearest',
                    vmin=-max_abs,
                    vmax=+max_abs
                )
                #Lay groundtruth onto heatmap 
                plt.contour(ground_truth, levels=[0.5], colors='blue', linewidths=1.5)
                
                plt.colorbar(heatmap_im)
                plt.title("SVM Weights Heatmap")
                plt.xlabel("X axis", fontsize=12)
                plt.ylabel("Y axis", fontsize=12)
                
                """
                #Add grid lines
                plt.grid(visible=True, color='gray', linewidth=0.2)
                plt.xticks(np.arange(0,50,5))
                plt.yticks(np.arange(0,50,5))
                plt.gca().set_xticks(np.arange(-.5, 50, 1), minor=True)
                plt.gca().set_yticks(np.arange(-.5, 50, 1), minor=True)
                plt.grid(which='minor', color='lightgray', linestyle='-', linewidth=0.3)
                        """
                
                plt.tight_layout()
                plt.show()
            else: 
                QMessageBox.warning(self, "Error", "Error Generating Heatmap")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to generate heatmap: {e}")