import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QGuiApplication
from controllers.countdown_timer_controller import TimerController
from controllers.character_controller import CharacterController
# from controllers.task_list_controller import TaskListController

if __name__ == '__main__':
    app = QApplication(sys.argv)

    controller = TimerController()
    character = CharacterController()
    controller.view.show()
    # character.view.show()

    # ディスプレイサイズを取得します
    screen_geometry = QGuiApplication.primaryScreen().availableGeometry()
    screen_width = screen_geometry.width()
    screen_height = screen_geometry.height()



    sys.exit(app.exec())

