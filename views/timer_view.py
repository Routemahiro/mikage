from PySide6.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QWidget
from PySide6.QtGui import QPixmap, QIcon, QPalette, QColor
from PySide6.QtCore import Qt, QPoint, QSize


class CharacterWindow(QWidget):
    def __init__(self):
        super().__init__()

        # メインレイアウト
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)

        # キャラクターと設定ボタンのレイアウト
        self.character_layout = QHBoxLayout()

        # キャラクター画像
        self.character_label = QLabel(self)
        pixmap = QPixmap("img\character.png")
        
        # ディスプレイサイズの取得
        screen = QApplication.primaryScreen().availableGeometry()

        # 画像をディスプレイサイズの3分の1にリサイズ
        resize_bairitsu = 2.5
        pixmap = pixmap.scaled(screen.width() // resize_bairitsu, screen.height() // resize_bairitsu, Qt.KeepAspectRatio)

        self.character_label.setPixmap(pixmap)
        self.character_layout.addWidget(self.character_label)

        # 設定ボタン
        self.setting_button = QPushButton()
        self.setting_button.setIcon(QIcon('img\setting_icon.png'))  # アイコンを設定
        self.setting_button.setIconSize(QSize(24, 24))  # アイコンサイズを設定

        # CSSスタイルシートを設定
        self.setting_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 127);  # 半透明の白色
                border-radius: 15px;  # 半径15pxの丸形
            }
        """)

        self.character_layout.addWidget(self.setting_button)

        self.layout.addLayout(self.character_layout)

        # テキストエディットエリア
        self.chat_text_area = QTextEdit()

        palette = self.chat_text_area.palette()
        palette.setColor(QPalette.Base, QColor(0, 0, 0, 127))  # 背景色を半透明の黒に
        palette.setColor(QPalette.Text, QColor(255, 255, 255))  # テキスト色を白に
        self.chat_text_area.setPalette(palette)

        self.chat_text_area.textChanged.connect(self.adjust_text_area_height)

        # 初期は2行分の高さに設定
        self.chat_text_area.setMaximumHeight(self.chat_text_area.fontMetrics().lineSpacing() * 2)

        self.layout.addWidget(self.chat_text_area)

        self.setLayout(self.layout)

        # ウィンドウ設定
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # ドラッグでウィンドウを移動するための変数
        self.m_drag = False
        self.m_DragPosition = QPoint()

    def adjust_text_area_height(self):
        # 行の数を取得
        num_lines = self.chat_text_area.document().lineCount()

        # 行の高さを取得
        line_height = self.chat_text_area.fontMetrics().lineSpacing()

        # テキストエディットエリアの高さを調整
        self.chat_text_area.setMaximumHeight(line_height * num_lines)

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


class TimerView(QWidget):
    def __init__(self):
        super().__init__()

        # UIコンポーネントの作成
        self.layout = QVBoxLayout()

        # キャラクターウィンドウを作成し表示
        self.character_window = CharacterWindow()
        self.character_window.show()

        self.time_label = QLabel("25:00")
        self.layout.addWidget(self.time_label)

        self.start_button = QPushButton("Start")  # ここでstart_buttonを定義
        self.layout.addWidget(self.start_button)

        self.reset_button = QPushButton("Reset")  # ここでreset_buttonを定義
        self.layout.addWidget(self.reset_button)

        self.setLayout(self.layout)

    def update_start_button_text(self, text):
        self.start_button.setText(text)

    def update_time_label(self, time_text):
        self.time_label.setText(time_text)

