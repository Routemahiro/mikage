import sys
from PySide6.QtWidgets import QApplication
from controllers.timer_controller import TimerController
from controllers.task_list_controller import TaskListController


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # タイマーコントローラーとタスクリストコントローラーをインスタンス化します
    timer_controller = TimerController()
    task_list_controller = TaskListController()

    # タイマービューとタスクリストビューを表示します
    timer_controller.view.show()
    task_list_controller.view.show()

    sys.exit(app.exec())
