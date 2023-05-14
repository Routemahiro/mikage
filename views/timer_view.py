from PySide6.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QWidget,QGridLayout
from PySide6.QtGui import QPixmap, QIcon, QPalette, QColor
from PySide6.QtCore import Qt, QPoint, QSize,QEvent


class CharacterWindow(QWidget):
    def __init__(self):
        super().__init__()

        # キャラクター画像
        self.character_label = QLabel(self)
        pixmap = QPixmap("img\character.png")

        # ディスプレイサイズの取得
        screen = QApplication.primaryScreen().availableGeometry()

        # 画像をディスプレイサイズの3分の1にリサイズ
        resize_bairitsu = 2.5
        pixmap = pixmap.scaled(screen.width() // resize_bairitsu, screen.height() // resize_bairitsu, Qt.KeepAspectRatio)

        self.character_label.setPixmap(pixmap)
        self.character_label.setGeometry(0, 0, pixmap.width(), pixmap.height())

        # 設定ボタン
        self.setting_button = QPushButton(self)
        self.setting_button.setIcon(QIcon('img\setting_icon.png'))  # アイコンを設定
        self.setting_button.setIconSize(QSize(40, 40))  # アイコンサイズを設定
        self.setting_button.setFixedSize(QSize(50, 50))  # ボタンのサイズを設定
        
        # ボタンの背景を透明にするためのスタイルシートを設定
        self.setting_button.setStyleSheet("background-image: url('img\transparent_background.png'); border: none;")

        self.setting_button.setAttribute(Qt.WA_TranslucentBackground)

        # ボタンの位置を移動
        button_pos_x = 240  # これは任意のx座標
        button_pos_y = self.character_label.height() // 15  
        self.setting_button.move(button_pos_x, button_pos_y)  # (x, y)座標を指定

        # テキストエディットエリア
        self.chat_text_area = QTextEdit()
        
        palette = self.chat_text_area.palette()
        palette.setColor(QPalette.Base, QColor(0, 0, 0, 127))  # 背景色を半透明の黒に
        palette.setColor(QPalette.Text, QColor(255, 255, 255))  # テキスト色を白に
        self.chat_text_area.setPalette(palette)

        self.chat_text_area.textChanged.connect(self.adjust_text_area_height)

        self.chat_text_area.setStyleSheet("""
            QTextEdit {
                background-color: rgba(0, 0, 0, 125);
                border-radius: 10px;
                padding: 1px;
                color: white;
            }
        """)




        # 初期は2行分の高さに設定
        self.chat_text_area.setMaximumHeight(self.chat_text_area.fontMetrics().lineSpacing() * 1)

        # ウィンドウ設定
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # ボタンの背景を透明に
        self.setting_button.setAttribute(Qt.WA_TranslucentBackground)

        # ドラッグでウィンドウを移動するための変数
        self.m_drag = False
        self.m_DragPosition = QPoint()

        # 送信ボタンの作成
        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.send_message)

        # レイアウトの設定
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.character_label, 0, 0, 1, 2)
        self.layout.addWidget(self.chat_text_area, 1, 0)
        self.layout.addWidget(self.send_button, 1, 1)  # 送信ボタンをレイアウトに追加

        self.setLayout(self.layout)
        # テキストエリアにフォーカスを設定
        self.chat_text_area.setFocus()    

        self.chat_text_area.installEventFilter(self)    


    def eventFilter(self, obj, event):
        if obj == self.chat_text_area and event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return and event.modifiers() & Qt.ShiftModifier:
                self.send_message()
                return True
        return super().eventFilter(obj, event)

    def show_finished_message(self):
        # キャラクターが終わったことを伝える吹き出しメッセージを表示
        dummy_message = "美影: 25分が経過しました！"
        response_label = QLabel(dummy_message)
        response_label.setStyleSheet("""
            QLabel {
                background-color: rgba(255, 255, 255, 255);
                border-radius: 10px;
                padding: 10px;
                color: black;
            }
        """)
        self.layout.addWidget(response_label, 2, 0, 1, 2)  # レイアウトに追加


    def send_message(self):
        user_message = self.chat_text_area.toPlainText()  # ユーザーが入力したテキストを取得
        self.chat_text_area.clear()  # テキストエディットエリアをクリア

        # ユーザーが何も入力していない場合は、何もしない
        if user_message.strip() == "":
            return
            
        # キャラクターとのチャット処理を実行（ここではダミーの応答を返す）
        character_response = f"美影: {user_message}"
        
        # 応答をテキストエディットエリアに表示
        response_label = QLabel(character_response)
        response_label.setStyleSheet("""
            QLabel {
                background-color: rgba(255, 255, 255, 255);
                border-radius: 10px;
                padding: 10px;
                color: black;
            }
        """)
        self.layout.addWidget(response_label)  # レイアウトに追加
                                                        

    def adjust_text_area_height(self):
        # テキストエリアの内容に基づいて高さを調整
        doc_height = self.chat_text_area.document().size().height()+10
        self.chat_text_area.setMaximumHeight(doc_height + 5)  # +5はパディング分
              

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    # マウスが移動した時のイベント
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.m_drag:
            self.move(event.globalPos() - self.m_DragPosition)
            event.accept()

    # マウスボタンが離された時のイベント
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = False
    

# class TimerView(QWidget):
#     def __init__(self):
#         super().__init__()

#         # UIコンポーネントの作成
#         self.layout = QVBoxLayout()


#         self.time_label = QLabel("25:00")
#         self.layout.addWidget(self.time_label)

#         self.start_button = QPushButton("Start")  # ここでstart_buttonを定義
#         self.layout.addWidget(self.start_button)

#         self.reset_button = QPushButton("Reset")  # ここでreset_buttonを定義
#         self.layout.addWidget(self.reset_button)

#         self.setLayout(self.layout)

#     def update_start_button_text(self, text):
#         self.start_button.setText(text)

#     def update_time_label(self, time_text):
#         self.time_label.setText(time_text)

