from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class TimerView(QWidget):
    def __init__(self):
        super().__init__()

        # UIコンポーネントの作成
        self.layout = QVBoxLayout()

        self.time_label = QLabel("25:00")
        self.layout.addWidget(self.time_label)

        self.start_button = QPushButton("Start")  # ここでstart_buttonを定義
        self.layout.addWidget(self.start_button)

        self.reset_button = QPushButton("Reset")  # ここでreset_buttonを定義
        self.layout.addWidget(self.reset_button)

        self.setLayout(self.layout)

    def update_start_button_text(self, text):
        self.start_button.setText(text)

    def update_time_label(self, time_text):
        self.time_label.setText(time_text)
