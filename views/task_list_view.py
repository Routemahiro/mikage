# from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem
# from PySide6.QtCore import Qt,QTimer

# class TaskListView(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.layout = QVBoxLayout()

#         self.new_task_input = QLineEdit()
#         self.layout.addWidget(self.new_task_input)

#         self.add_task_button = QPushButton("Add Task")
#         self.layout.addWidget(self.add_task_button)

#         self.remove_task_button = QPushButton("Remove Task")  # ここでremove_task_buttonを定義
#         self.layout.addWidget(self.remove_task_button)

#         self.task_list_widget = QListWidget()
#         self.layout.addWidget(self.task_list_widget)

#         self.setLayout(self.layout)

#     def add_task_to_list(self, task_name):
#         self.task_list_widget.addItem(task_name)
#         self.new_task_input.clear()  # 入力欄の文字を削除


#     def get_new_task_name(self):
#         return self.new_task_input.text()

#     def get_selected_task_name(self):
#         selected_item = self.task_list_widget.currentItem()
#         if selected_item:
#             return selected_item.text()
#         return None
    
#     def remove_selected_task_from_list(self):
#         selected_items = self.task_list_widget.selectedItems()
#         for item in selected_items:
#             self.task_list_widget.takeItem(self.task_list_widget.row(item))

#     def flash_task_input(self):
#         original_color = self.new_task_input.palette().color(self.new_task_input.backgroundRole())
#         self.new_task_input.setStyleSheet("background-color: pink;")
#         QTimer.singleShot(100, lambda: self.new_task_input.setStyleSheet("background-color: {};".format(original_color.name())))

# if __name__ == '__main__':
#     import sys

#     app = QApplication(sys.argv)

#     main_window = TaskListView()
#     main_window.show()

#     sys.exit(app.exec())
