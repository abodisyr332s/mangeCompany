from PyQt6.QtWidgets import QApplication , QWidget,QVBoxLayout,QPushButton,QCheckBox,QLineEdit,QLabel,QMessageBox, \
                                                        QTextEdit,QFrame,QTableWidget,QGridLayout,QTableWidgetItem,QTreeView,\
                                                        QRadioButton,QComboBox,QFileDialog,QMainWindow,QTextEdit,QMenu,QGridLayout,QScrollArea,QDateEdit
from PyQt6.QtGui import QIcon,QFont,QIntValidator,QScreen,QFont,QPixmap,QColor,QMovie,QCursor,QAction,QResizeEvent,QKeyEvent,QWheelEvent
from PyQt6 import uic
from PyQt6.QtCore import Qt,QCoreApplication,QSize,QTimer,QLocale,QDate
import sqlite3
import sys
from docx.shared import Mm
from docx.oxml.xmlchemy import OxmlElement
from docx.oxml.ns import qn as qn2
import shutil
from openpyxl import Workbook,load_workbook
import os
from datetime import date
from datetime import timedelta
from hijri_converter import Hijri, Gregorian
from dateutil.relativedelta import relativedelta
import docx
from contextlib import contextmanager
from docx2pdf import convert
import docx.shared
from docx.oxml.ns import qn
from docx.shared import Pt
from docx.oxml import OxmlElement



CURRENT_TIME_GEO = (str(date.today())).replace("-","/")
CURRENT_TIME_TEMP = (str(date.today())).split("-")  
CURRENT_TIME_HIJ = str(Gregorian(int(CURRENT_TIME_TEMP[0]),int(CURRENT_TIME_TEMP[1]),int(CURRENT_TIME_TEMP[2])).to_hijri()).replace("-","/")
title = "برنامج متابعة المخزون"
icon = "assests/icon.ico"
con = sqlite3.connect("app.db")
cr = con.cursor()

class CustomDateEdit(QDateEdit):
    def keyPressEvent(self, event: QKeyEvent):
        # Ignore key press events to prevent typing
        event.ignore()
    def wheelEvent(self, event: QWheelEvent):
        # Ignore wheel events to prevent changing date with mouse scroll
        event.ignore()

@contextmanager
def suppress_output():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = devnull
        sys.stderr = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr