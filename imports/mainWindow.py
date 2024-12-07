from .stuff import *
from .DriversWindow import *
from .TrucksWindow import *
from .WareHouseWindow import *
from .noficationsWindow import *
from .oilWindow import *
from .BigTrucksWindow import *
class MainWindow(DriversWindow, TrucksWindow, WareHouseWindow, QWidget, noficationsWindow, oilWindow, BigTrucksWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("assests/mainWindow.ui",self)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))
        self.driversButton.clicked.connect(self.showDrivers)
        self.trucksButton.clicked.connect(self.showTrucks)
        self.programmerButton.clicked.connect(self.showProgrammer)
        self.warehouseButton.clicked.connect(self.showWareHouse)
        self.noficationsButton.clicked.connect(self.showNofications)
        self.oilButton.clicked.connect(self.showOil)
        self.bigTrucksButton.clicked.connect(self.showBigTrucks)
        self.noficationsButton.setStyleSheet("QPushButton {text-align:center;qproperty-icon:url('assests/notification.png');qproperty-iconSize: 30px;border:1px solid black;font: 16pt 'Arial';}QPushButton:hover {background-color:#c8c8c8;}")
        if self.returnNoficationsMessagesToDisplayList()!=[]:
            self.noficationsButton.setStyleSheet("QPushButton {text-align:center;qproperty-icon:url('assests/notification.png');qproperty-iconSize: 30px;background-color:orange;border:1px solid black;font: 16pt 'Arial';}QPushButton:hover {background-color:#c8c8c8;}")
            self.showNofications()

        self.preWidth = 995
        self.preHeight = 680

        self.resizeEvent = self.resizeWindow
    def resizeWindow(self, resizeEvent):
        changedWidth = self.width() - 995
        changedHeight = self.height() - 680
        
        if self.width() >=995 and self.height() >=680:
            self.mainFrame.resize(self.width(), self.mainFrame.height() + self.height() - self.preHeight)
            self.buttonsFrame.resize(self.width(), 41)
            self.label.move((self.mainFrame.width() - self.label.width())//2, (self.mainFrame.height() - self.label.height())//2)

            
            self.preWidth = self.width()
            self.preHeight = self.height()

        try:
            self.exportAllItemsFrame.move((self.mainFrame.width()-160)//2,(self.mainFrame.height()-174)//2)
        except:
            pass
        try:
            self.putBigTrucksFrameAndStuff()
        except:
            pass

        try:
            self.addBigTruckFrame.move((self.mainFrame.width()-350)//2,(self.mainFrame.height()-506)//2)
        except:
            pass

        try:
            self.showBigTrucksNoteFrame.move((self.bigTrucksFrame.width()-450)//2,(self.bigTrucksFrame.height()-400)//2)
        except:
            pass

        try:
            self.editNoteFrame.move((self.bigTrucksFrame.width()-340)//2,(self.bigTrucksFrame.height()-360)//2)
        except:
            pass

        try:
            self.addNoteBigTruckFrame.move((self.bigTrucksFrame.width()-340)//2,(self.bigTrucksFrame.height()-360)//2)
        except:
            pass

        try:
            self.editBigTruckFrame.move((self.mainFrame.width()-350)//2,(self.mainFrame.height()-506)//2)
        except:
            pass

        try:
            self.addItemToTruckFrame.move((self.mainFrame.width()-360)//2,(self.mainFrame.height()-300)//2)
        except:
            pass

        try:
            self.placeDriversFrameAndStuff()
        except:
            pass

        try:
            self.addDriverFrame.move((self.mainFrame.width()-350)//2,(self.mainFrame.height()-506)//2)
        except:
            pass

        try:
            self.editDriverFrame.move((self.mainFrame.width()-350)//2,(self.mainFrame.height()-506)//2)
        except:
            pass

        try:
            self.exportDriverFrame.move((self.mainFrame.width()-160)//2,(self.mainFrame.height()-174)//2)
        except:
            pass

        try:
            self.showTripsFrame.move((self.width()-419)//2,(self.mainFrame.height()-319)//2)
        except:
            pass

        try:
            self.noficationsFrame.move((self.width()-410)//2,(self.mainFrame.height()-300)//2)
        except:
            pass

        try:
            self.putOilFrameAndStuff()
        except:
            pass

        try:
            self.showOilLifecycycleFrame.move((self.oilFrame.width()-500)//2,(self.oilFrame.height()-450)//2)
        except:
            pass
        
        try:
            self.addOilToTrukFrame.move((self.mainFrame.width()-360)//2,(self.mainFrame.height()-550)//2)
        except:
            pass

        try:
            self.addOilFrame.move((self.mainFrame.width()-350)//2,(self.mainFrame.height()-506)//2)
        except:
            pass

        try:
            self.putTrucksFrameAndStuff()
        except:
            pass

        try:
            self.addTruckFrame.move((self.mainFrame.width()-350)//2,(self.mainFrame.height()-506)//2)
        except:
            pass

        try:
            self.exportTrucksFrame.move((self.mainFrame.width()-160)//2,(self.mainFrame.height()-174)//2)
        except:
            pass

        try:
            self.showTrucksPartsFrame.move((self.trucksFrame.width()-450)//2,(self.trucksFrame.height()-450)//2)
        except:
            pass

        try:
            self.showNotesTrucksToItemsFrame.move((self.trucksFrame.width()-450)//2,(self.trucksFrame.height()-400)//2)
        except:
            pass

        try:
            self.showTrucksNoteFrame.move((self.trucksFrame.width()-450)//2,(self.trucksFrame.height()-400)//2)
        except:
            pass

        try:
            self.addNoteFrame.move((self.trucksFrame.width()-340)//2,(self.trucksFrame.height()-360)//2)
        except:
            pass

        try:
            self.editNoteFrame.move((self.trucksFrame.width()-340)//2,(self.trucksFrame.height()-360)//2)
        except:
            pass
        
        try:
            self.editTruckFrame.move((self.mainFrame.width()-350)//2,(self.mainFrame.height()-506)//2)
        except:
            pass

        try:
            self.putWareHouseFrameAndStuff()
        except:
            pass

        try:
            self.changeStatusFrame.move((self.wareHouseFrame.width()-340)//2,(self.wareHouseFrame.height()-160)//2)
        except:
            pass

        try:
            self.showStatsFrame.move((self.wareHouseFrame.width() - 400)//2,(self.wareHouseFrame.height() - 250)//2)
        except:
            pass

        try:
            self.addItemFrame.move((self.mainFrame.width()-350)//2,(self.mainFrame.height()-506)//2)
        except:
            pass

        try:
            self.showItemLifecycycleFrame.move((self.wareHouseFrame.width()-500)//2,(self.wareHouseFrame.height()-450)//2)
        except:
            pass

        try:
            self.showItemsNoteFrame.move((self.wareHouseFrame.width()-450)//2,(self.wareHouseFrame.height()-400)//2)
        except:
            pass

        try:
            self.editItemNoteFrame.move((self.wareHouseFrame.width()-340)//2,(self.wareHouseFrame.height()-360)//2)
        except:
            pass

        try:
            self.addItemsNoteFrame.move((self.wareHouseFrame.width()-340)//2,(self.wareHouseFrame.height()-360)//2)
        except:
            pass

        try:
            self.addItemToTruckFrame.move((self.mainFrame.width()-360)//2,(self.mainFrame.height()-550)//2)
        except:
            pass

        try:
            self.showProgrammerFrame.move((self.mainFrame.width()-273)//2,(self.mainFrame.height()-368)//2)
        except:
            pass
    def showProgrammer(self):
        try:
            self.destroyFrame(self.showProgrammerFrame)
        except:
            pass

        self.showProgrammerFrame = QFrame(parent=self.mainFrame)
        self.showProgrammerFrame.setGeometry((self.mainFrame.width()-273)//2,(self.mainFrame.height()-368)//2,273,368)
        self.showProgrammerFrame.setStyleSheet("background-color:white")


        
        logo = QLabel(parent=self.showProgrammerFrame,text="")

        closeButton = QPushButton(logo)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:8px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 18px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(360,0,31,31)
        closeButton.clicked.connect(lambda x, frame=self.showProgrammerFrame:self.destroyFrame(frame))

        logo.setGeometry(-139,10,571,281)
        logo.setPixmap(QPixmap("assests/MyLogo.png"))
        logo.setScaledContents(True)

        label = QLabel(parent=self.showProgrammerFrame,text="برمجة وتطوير: م.عبدالله ماهر الشامي")
        label.setStyleSheet('font: 12pt "Arial";color:rgb(255, 0, 0);')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setGeometry(30,250,201,20)

        label = QLabel(parent=self.showProgrammerFrame,text="للتواصل: 966558967920+")
        label.setStyleSheet('font: 12pt "Arial";color:rgb(255, 0, 0);')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setGeometry(50,280,181,20)

        label = QLabel(parent=self.showProgrammerFrame,text="جميع الحقوق محفوظة")
        label.setStyleSheet('font: 12pt "Arial";color:rgb(255, 0, 0);')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setGeometry(10,340,261,20)

        self.showProgrammerFrame.show()