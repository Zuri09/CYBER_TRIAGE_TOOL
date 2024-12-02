import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QFileDialog, QWidget
)
from ai_model import train_ai_model
from forensic_analysis import analyze_raw_file
from report_generator import generate_report

class ForensicToolApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digital Forensics and Incident Response Tool")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.status_label = QLabel("Welcome to the Forensic Tool!")
        self.train_btn = QPushButton("Train AI Model")
        self.analyze_btn = QPushButton("Analyze RAW File")
        self.generate_btn = QPushButton("Generate Report")

        self.train_btn.clicked.connect(self.train_model)
        self.analyze_btn.clicked.connect(self.analyze_file)
        self.generate_btn.clicked.connect(self.generate_report)

        layout.addWidget(self.status_label)
        layout.addWidget(self.train_btn)
        layout.addWidget(self.analyze_btn)
        layout.addWidget(self.generate_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def train_model(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Training Data", "", "CSV Files (*.csv)")
        if file_name:
            self.model, self.label_encoder = train_ai_model(file_name)
            self.status_label.setText("AI Model trained successfully!")

    def analyze_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select RAW File", "", "RAW Files (*.raw *.e01)")
        if file_name:
            self.analysis_data = analyze_raw_file(file_name)
            self.status_label.setText(f"Analyzed file: {file_name}")

    def generate_report(self):
        if hasattr(self, "analysis_data"):
            generate_report(self.analysis_data)
            self.status_label.setText("Report generated successfully!")
        else:
            self.status_label.setText("No data to generate a report.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ForensicToolApp()
    window.show()
    sys.exit(app.exec_())
