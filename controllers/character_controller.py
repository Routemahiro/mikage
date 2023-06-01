from models.timer import Timer
# from models.task_list import TaskList
from views.timer_view import TimerView

class CharacterController:
    def __init__(self):

        self.view = TimerView()



if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)


    sys.exit(app.exec())
