# timer_controller.py
from PySide6.QtCore import QTimer, Slot
from models.timer_model import TimerModel
from views.countdowntimer_view import TimerView
from PySide6.QtCore import QTime

class TimerController:
    def __init__(self):
        self.view = TimerView()
        self.model = TimerModel()
        
        self.view.btn.clicked.connect(self.toggle_timer)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.update_label()

    def update_label(self):
        self.view.timer_label.setText(self.model.remaining_time.toString())

    @Slot()
    def toggle_timer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.view.btn.setText('Start')
        else:
            self.timer.start(1000)
            self.view.btn.setText('Stop')

    @Slot()
    def update_timer(self):
        self.model.remaining_time = self.model.remaining_time.addSecs(-1)
        self.update_label()

        if self.model.remaining_time == QTime(0, 0):
            self.model.reset()
