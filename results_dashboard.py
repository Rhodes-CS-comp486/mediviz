from PySide6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, QLabel, QTableWidget, QTableWidgetItem,
    QHeaderView, QPushButton, QFileDialog, QMessageBox
)
from PySide6.QtCore import Qt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import numpy as np
import matplotlib.pyplot as plt

class ResultsWindow(QMainWindow):
    def __init__(self, report_text, y_true=None, y_pred=None):
        super().__init__()
        self.setWindowTitle("SVM Results Dashboard")
        self.setGeometry(500, 500, 700, 500)
        self.y_true = y_true
        self.y_pred = y_pred
        self.report_text = report_text

        layout = QVBoxLayout()

        label = QLabel("SVM Classification Report")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 18px; font-weight: bold; color: white; margin: 10px;")
        layout.addWidget(label)

        self.table = QTableWidget()
        self.populate_table(report_text)
        layout.addWidget(self.table)

        # Export Button
        export_button = QPushButton("Export Report to CSV")
        export_button.clicked.connect(self.export_to_csv)
        layout.addWidget(export_button)

        # Confusion Matrix Button (only if data available)
        if y_true is not None and y_pred is not None:
            cm_button = QPushButton("Show Confusion Matrix")
            cm_button.clicked.connect(self.show_confusion_matrix)
            layout.addWidget(cm_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def populate_table(self, report):
        lines = [line.strip() for line in report.strip().split('\n') if line.strip()]
        header = lines[0].split()
        data_lines = lines[1:]

        self.table.setColumnCount(len(header) + 1)
        self.table.setRowCount(len(data_lines))
        self.table.setHorizontalHeaderLabels([""] + header)

        for row_idx, line in enumerate(data_lines):
            parts = line.split()
            row_label = parts[0]
            values = parts[1:]

            self.table.setItem(row_idx, 0, QTableWidgetItem(row_label))

            for col_idx, value in enumerate(values):
                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignCenter)

                # Color coding based on value
                try:
                    float_val = float(value)
                    if float_val >= 0.9:
                        item.setBackground(Qt.green)
                    elif float_val < 0.6:
                        item.setBackground(Qt.red)
                except:
                    pass  # For labels like "accuracy", etc.

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

    def show_confusion_matrix(self):
        if self.y_true is None or self.y_pred is None:
            QMessageBox.warning(self, "Error", "Missing labels for confusion matrix.")
            return

        cm = confusion_matrix(self.y_true, self.y_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm)
        disp.plot(cmap=plt.cm.Blues)
        plt.title("Confusion Matrix")
        plt.show()
