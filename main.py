import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QGuiApplication
from controllers.timer_controller import TimerController
from controllers.task_list_controller import TaskListController

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # タイマーコントローラーとタスクリストコントローラーをインスタンス化します
    timer_controller = TimerController()
    task_list_controller = TaskListController()

    # ディスプレイサイズを取得します
    screen_geometry = QGuiApplication.primaryScreen().availableGeometry()
    screen_width = screen_geometry.width()
    screen_height = screen_geometry.height()

    # タスクリストビューの位置とサイズを調整します
    task_list_controller.view.setGeometry(screen_width - task_list_controller.view.width(), screen_height - task_list_controller.view.height(), task_list_controller.view.width(), task_list_controller.view.height())

    # タイマービューの位置を調整します
    timer_controller.view.move(task_list_controller.view.x() - timer_controller.view.width(), task_list_controller.view.y())

    # タイマービューとタスクリストビューを表示します
    timer_controller.view.show()
    task_list_controller.view.show()

    sys.exit(app.exec())

