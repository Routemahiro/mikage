from models.task_list import TaskList
from views.task_list_view import TaskListView

class TaskListController:
    def __init__(self):
        self.task_list = TaskList()
        self.view = TaskListView()

        # イベントハンドラの設定
        self.view.add_task_button.clicked.connect(self.add_task)
        self.view.remove_task_button.clicked.connect(self.remove_selected_task)

    def add_task(self):
        task_name = self.view.get_new_task_name()
        self.task_list.add_task(task_name)
        self.view.add_task_to_list(task_name)

    def remove_selected_task(self):
        selected_task_name = self.view.get_selected_task_name()
        if selected_task_name:
            self.task_list.remove_task(selected_task_name)
            self.view.remove_selected_task_from_list()

    def add_task(self):
        task_name = self.view.get_new_task_name()
        if not task_name.strip():  # 入力が空白の場合
            self.view.flash_task_input()
            return
        self.task_list.add_task(task_name)
        self.view.add_task_to_list(task_name)

if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    controller = TaskListController()
    controller.view.show()

    sys.exit(app.exec())
