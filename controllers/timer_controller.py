from models.timer import Timer
# from models.task_list import TaskList
from views.timer_view import TimerView

class TimerController:
    def __init__(self):
        self.timer = Timer()
        # self.task_list = TaskList()
        self.view = TimerView()

        # イベントハンドラの設定
        self.view.start_button.clicked.connect(self.start_timer)
        self.view.reset_button.clicked.connect(self.reset_timer)

    def start_timer(self):
        if self.timer.is_running:
            self.timer.pause()
            self.view.update_start_button_text("Start")
        else:
            self.timer.start()
            self.view.update_start_button_text("Pause")

    def reset_timer(self):
        self.timer.reset()

if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    controller = TimerController()
    controller.view.show()

    sys.exit(app.exec())
