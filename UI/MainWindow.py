from Level import Level
from UI.init import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow, QTableView
from PyQt5.QtGui import QIcon, QStandardItemModel, QPixmap, QStandardItem, QDrag, QCursor, QMouseEvent
from PyQt5.QtCore import QSize, Qt, QModelIndex


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.__level = Level(0)
        self.add_function()
        self.view_level()
        self.click_count = 0
        self.idx = QModelIndex()
        self.idx2 = QModelIndex()
        self.scope = 0

        def new_mouse_press_event(e) -> None:
            if e.button() == Qt.LeftButton:
                self.click_count += 1
                if self.click_count == 1:
                    self.idx = self.tableView.indexAt(e.pos())
                if self.click_count == 2:
                    self.idx2 = self.tableView.indexAt(e.pos())
                    self.on_item_clicked(self.idx, self.idx2)

        self.tableView.mousePressEvent = new_mouse_press_event

    def on_item_clicked(self, e: QModelIndex, e2: QModelIndex) -> None:
        index = (e.row(), e.column())
        index2 = (e2.row(), e2.column())

        delta_row = index2[0] - index[0]
        delta_col = index2[1] - index[1]
        if index[1] == index2[1]:
            self.scope += self.__level.move_col(index[1], delta_row)
            self.label_scope.setText(str(self.scope))
        if index[0] == index2[0]:
            self.scope += self.__level.move_row(index[0], delta_col)
            self.label_scope.setText(str(self.scope))
        self.click_count = 0
        self.view_level()

        if self.scope == 200:
            self.stackedWidget.setCurrentIndex(3)
            self.scope = 0

    def add_function(self):
        self.btn_play_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.btn_setings_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.btn_back_level.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(0))  # TODO спросить действительно ли хочет выйти из уровня
        self.btn_back_setings.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.btn_reset.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

    def view_level(self):
        size = self.__level.size
        self.model = QStandardItemModel()
        self.model.setRowCount(size[0])
        self.model.setColumnCount(size[1])
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().hide()
        self.tableView.verticalHeader().hide()

        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)

        self.size_col_row = 84
        self.tableView.setIconSize(QSize(self.size_col_row, self.size_col_row))

        for i in range(self.__level.size[1]):
            self.tableView.setColumnWidth(i, self.size_col_row)
        for i in range(self.__level.size[0]):
            self.tableView.setRowHeight(i, self.size_col_row)  # установка ширины столбца

        self.fill_table()

    def fill_table(self):
        for row in range(self.__level.size[0]):
            for col in range(self.__level.size[1]):
                self.model.setItem(row, col, self.__get_img(row, col))

    def __get_img(self, row, col):
        item = QStandardItem()
        index = int(self.__level.matrix[row][col])
        pixmap = QPixmap(f'images/img_{index}.png')
        icon = QIcon(pixmap)
        item.setIcon(icon)
        return item
