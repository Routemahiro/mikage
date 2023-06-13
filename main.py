import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QGuiApplication
from controllers.timer_controller import TimerController
from controllers.character_controller import CharacterController
from controllers.ai_controller import AIController
from controllers.ActiveWindowTracker import ActiveWindowTracker
from controllers.pomodoro_db_controller import PomodoroDBController
# from database.init_db import start_pomodoro_session, end_pomodoro_session
import time


if __name__ == '__main__':
    app = QApplication(sys.argv)

    timer_controller = TimerController()
    character_controller = CharacterController()
    ai_controller = AIController()
    db_controller = PomodoroDBController('database/data/mikage_timer.db')
    
    timer_controller.view.show()

    # ディスプレイサイズを取得します
    screen_geometry = QGuiApplication.primaryScreen().availableGeometry()
    screen_width = screen_geometry.width()
    screen_height = screen_geometry.height()
    
    # Start a new pomodoro session
    session_id = db_controller.start_pomodoro_session(time.ctime())
    
    # Start tracking window activity
    tracker = ActiveWindowTracker(db_controller, session_id)
    tracker.start_tracking()

    # Run the pomodoro timer
    timer_controller.start_timer()

    # After the timer ends, generate AI comment and stop tracking
    ai_comment = ai_controller.get_ai_comment(tracker.get_active_window_data())
    tracker.stop_tracking()
    
    # End the pomodoro session
    end_pomodoro_session(session_id, time.ctime(), ai_comment)

    sys.exit(app.exec())
