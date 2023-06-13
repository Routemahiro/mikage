# timer_controller.py
from PySide6.QtCore import QTimer, Slot
from models.timer_model import TimerModel
from views.countdowntimer_view import TimerView
from PySide6.QtCore import QTime
from controllers.ActiveWindowTracker import ActiveWindowTracker
from controllers.pomodoro_db_controller import PomodoroDBController
from datetime import datetime
from database.db_handler import DB_PATH

class TimerController:
    def __init__(self):
        self.view = TimerView()
        self.model = TimerModel()
        
        self.view.btn.clicked.connect(self.toggle_timer)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.update_label()
        self.db_controller = PomodoroDBController(DB_PATH)
        self.tracker = None
        self.session_id = None

    def update_label(self):
        self.view.timer_label.setText(self.model.remaining_time.toString())

    @Slot()
    def toggle_timer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.view.btn.setText('Start')
            
            # Stop tracking when timer is stopped
            if self.tracker:
                self.tracker.stop_tracking()
        else:
            # Add session to db and start tracking when timer is started
            self.session_id = self.db_controller.add_pomodoro_session(start_time, end_time, ai_comment)
            self.tracker = ActiveWindowTracker(self.db_controller, self.session_id)
            self.tracker.start_tracking()

            self.timer.start(1000)
            self.view.btn.setText('Stop')

    @Slot()
    def update_timer(self):
        self.model.remaining_time = self.model.remaining_time.addSecs(-1)
        self.update_label()

        if self.model.remaining_time == QTime(0, 0):
            self.model.reset()


    def end_session(self):
        end_time = datetime.now()
        ai_comment = "AI comment"  # Replace this with actual AI comment
        self.db_controller.update_session_end_time_and_comment(self.session_id, end_time, ai_comment)

        # Show AI comment in a textbox
        create_textbox(ai_comment)