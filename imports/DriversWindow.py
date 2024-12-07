from .stuff import *

class DriversWindow():
    def set_arabic_format(self,cell):
        for paragraph in cell.paragraphs:
            pPr = paragraph._element.get_or_add_pPr()
            bidi = OxmlElement('w:bidi')
            bidi.set(qn('w:val'), '1')
            pPr.append(bidi)
            for run in paragraph.runs:
                run.font.name = 'Arial'
            lang = OxmlElement('w:lang')
            lang.set(qn('w:val'), 'ar-SA')
            pPr.append(lang)
    def showDrivers(self):
        try:
            self.destroyFrame(self.mainMenuDriversFrame)
            self.destroyFrame(self.driversFrame)
        except:
            pass
        self.driversFrame = QFrame(self.mainFrame)
        
        self.closeButtonDriversFrame = QPushButton(self.driversFrame)
        self.closeButtonDriversFrame.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        self.closeButtonDriversFrame.clicked.connect(lambda x, frame=self.driversFrame:self.destroyFrame(frame))

        self.comboSearchDriversBox = QComboBox(self.driversFrame)
        self.comboSearchDriversBox.setGeometry(500,30,150,20)
        self.comboSearchDriversBox.addItems(["الكل", "رقم الاقامة", "رقم الجوال", "الاسم"])
        self.comboSearchDriversBox.activated.connect(self.addSearchDriverEntries)



        self.driversFrame.setStyleSheet("background-color:white")

        self.driversTable = QTableWidget(self.driversFrame)

        self.driversTable.setColumnCount(7)
        self.driversTable.setHorizontalHeaderLabels(["اسم السائق","رقم الاقامة","رفم الجوال","الجنسية","انتهاء الاقامة","انتهاء التأمين","بطاقة السائق"])

        self.contextMenuDriversTable = QMenu(self.driversTable)
        self.contextMenuDriversTable.setStyleSheet("background-color:grey")
        self.createButtonDriversTable()

        self.driversTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.driversTable.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.driversTable.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.driversTable.customContextMenuRequested.connect(self.showMenuDriversTable)

        #Start minMenu Buttons style
        self.mainMenuDriversFrame = QFrame(self.driversFrame)
        self.mainMenuDriversFrame.setStyleSheet("background-color:white;border:2px solid black")
        
        label = QLabel(self.mainMenuDriversFrame,text="القائمة الرئيسيه")
        label.setStyleSheet("background-color:white;border-bottom:none;font: 14pt 'Arial';")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setGeometry(0,0,181,31)

        addDriverButton = QPushButton(self.mainMenuDriversFrame,text="اضافة سائق")
        addDriverButton.setGeometry(0,50,181,31)
        addDriverButton.setStyleSheet("QPushButton {background-color:white;border:2px solid black;font: 14pt 'Arial';} QPushButton:hover {background-color:#c8c8c8;}")
        addDriverButton.clicked.connect(self.addDriver)

        exportDriversReport = QPushButton(self.mainMenuDriversFrame,text="تصدير تقرير للسائقين")
        exportDriversReport.setGeometry(0,90,181,31)
        exportDriversReport.setStyleSheet("QPushButton {background-color:white;border:2px solid black;font: 14pt 'Arial';} QPushButton:hover {background-color:#c8c8c8;}")
        exportDriversReport.clicked.connect(self.exportDriversReport)

        exportDrivers = QPushButton(self.mainMenuDriversFrame,text="تصدير معلومات السائقين")
        exportDrivers.setGeometry(0,130,181,31)
        exportDrivers.setStyleSheet("QPushButton {background-color:white;border:2px solid black;font: 14pt 'Arial';} QPushButton:hover {background-color:#c8c8c8;}")
        exportDrivers.clicked.connect(self.exportAllDrivers)


        self.placeDriversFrameAndStuff()

        self.loadDrivers()
        self.driversFrame.show()
    def placeDriversFrameAndStuff(self):

        
        if self.width() <= 995 or self.height() <= 680:
            self.driversFrame.setGeometry((self.width()-847)//2,(self.mainFrame.height()-610)//2,847,610)
            self.driversTable.setGeometry(10,60,641,541)
            self.mainMenuDriversFrame.setGeometry(660,60,181,161)
            self.closeButtonDriversFrame.setGeometry(800,10,41,31)
        else:
            self.driversFrame.setGeometry(30,30,self.mainFrame.width()-60,self.mainFrame.height()-60)
            self.driversTable.setGeometry(10,60,self.driversFrame.width() - 206,self.driversFrame.height()-100)
            self.mainMenuDriversFrame.setGeometry(self.driversTable.width() + 20,60,181,161)
            self.closeButtonDriversFrame.setGeometry(self.driversTable.width() + 20 + 140,10,41,31)

        deserve = self.driversTable.columnCount()
        for i in range(self.driversTable.columnCount()):
            self.driversTable.setColumnWidth(i, (self.driversTable.width() - 20) // deserve)

        self.driversFrame.show()
        self.driversTable.show()
        self.mainMenuDriversFrame.show()
        self.closeButtonDriversFrame.show()
    def addSearchDriverEntries(self):
        try:
            self.searchEntryDriver.destroy()
            self.searchEntryDriver.hide()
        except:
            pass
        if self.comboSearchDriversBox.currentText() == "الكل":
            self.loadDrivers()
        else:
            self.searchEntryDriver = QLineEdit(self.driversFrame)
            self.searchEntryDriver.textChanged.connect(self.searchDriversFun)
            self.searchEntryDriver.setGeometry(340,30,150,20)
            self.searchEntryDriver.show()
    def searchDriversFun(self):
        if len(self.searchEntryDriver.text())==0:
            self.loadDrivers()
        else:
            self.driversTable.setRowCount(0)
            tempThing = [] 

            if self.comboSearchDriversBox.currentText()=="رقم الاقامة":
                cr.execute("SELECT identy FROM drivers")
            elif self.comboSearchDriversBox.currentText()=="رقم الجوال":
                cr.execute("SELECT phone FROM drivers")
            elif self.comboSearchDriversBox.currentText()=="الاسم":
                cr.execute("SELECT name FROM drivers")

            choices = cr.fetchall()
            posiple = []
            for o in choices:
                for n,i in enumerate(o):
                    try:
                        if o[n][:len(self.searchEntryDriver.text())]==self.searchEntryDriver.text():
                                if i not in posiple:
                                    posiple.append(i)
                    except:
                        pass

            for p in posiple:
                if self.comboSearchDriversBox.currentText()=="رقم الاقامة":
                    cr.execute("SELECT * FROM drivers WHERE identy = ?", [p])
                elif self.comboSearchDriversBox.currentText()=="رقم الجوال":
                    cr.execute("SELECT * FROM drivers WHERE phone = ?", [p])
                elif self.comboSearchDriversBox.currentText()=="الاسم":
                    cr.execute("SELECT * FROM drivers WHERE name = ?", [p])

                for i in cr.fetchall():
                    tempThing.append(i)

            for row,i in enumerate(tempThing):
                self.driversTable.insertRow(self.driversTable.rowCount())
                for col,val in enumerate(i):
                    self.driversTable.setItem(row,col,QTableWidgetItem(str(val)))
    def showMenuDriversTable(self, position):
        indexes = self.driversTable.selectedIndexes()
        for index in indexes:
            self.contextMenuDriversTable.exec(self.driversTable.viewport().mapToGlobal(position))
    def createButtonDriversTable(self):
        self.deleteButton = QAction(self.driversTable)
        self.deleteButton.setIcon(QIcon("assests/deleteUser.png"))
        self.deleteButton.setText("حذف")
        self.deleteButton.setFont(QFont("Arial" , 12))
        self.deleteButton.triggered.connect(self.deleteDriver)

        self.editButton = QAction(self.driversTable)
        self.editButton.setIcon(QIcon("assests/edit.png"))
        self.editButton.setText("تعديل")
        self.editButton.setFont(QFont("Arial" , 12))
        self.editButton.triggered.connect(self.editDriver)


        self.contextMenuDriversTable.addAction(self.deleteButton)
        self.contextMenuDriversTable.addAction(self.editButton)
    def addDriver(self):
        try:
            self.destroyFrame(self.addDriverFrame)
        except:
            pass

        self.addDriverFrame = QFrame(self.mainFrame)
        self.addDriverFrame.setGeometry((self.mainFrame.width()-350)//2,(self.mainFrame.height()-506)//2,350,506)
        self.addDriverFrame.setStyleSheet("background-color:white;border:2px solid black")

        closeButton = QPushButton(self.addDriverFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(300,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.addDriverFrame:self.destroyFrame(frame))
        
        #Start scrolAria
        
        self.frame = QFrame()

        layout = QVBoxLayout()
        self.frame.setLayout(layout)


        label = QLabel("اسم السائق")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")
        self.nameEntry = QLineEdit()

        layout.addWidget(label)
        layout.addWidget(self.nameEntry)

        label = QLabel("رقم الاقامة")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")

        self.identyEntry = QLineEdit()

        layout.addWidget(label)
        layout.addWidget(self.identyEntry)

        label = QLabel("رقم الجوال")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")
        self.phoneEntry = QLineEdit()

        layout.addWidget(label)
        layout.addWidget(self.phoneEntry)

        label = QLabel("الجنسية")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")
        self.nationalityEntry = QLineEdit()


        layout.addWidget(label)
        layout.addWidget(self.nationalityEntry)

        label = QLabel("تاريخ انتهاء الاقامة")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")

        self.identyExpireEntry = QDateEdit()
        self.identyExpireEntry.setCalendarPopup(True)
        self.identyExpireEntry.setDisplayFormat("yyyy/MM/dd")

        arabic_locale = QLocale(QLocale.Language.Arabic, QLocale.Country.SaudiArabia)

        self.identyExpireEntry.setLocale(arabic_locale)
        self.identyExpireEntry.setFont(QFont("Arial",12))
        self.identyExpireEntry.setStyleSheet("background-color:white;color:black")

        self.todayButton = QPushButton("اليوم",clicked=lambda:self.identyExpireEntry.calendarWidget().setSelectedDate(QDate().currentDate()))
        self.todayButton.setStyleSheet("background-color:green;")

        self.identyExpireEntry.calendarWidget().layout().addWidget(self.todayButton)
        self.identyExpireEntry.calendarWidget().setSelectedDate(QDate().currentDate())

        layout.addWidget(label)
        layout.addWidget(self.identyExpireEntry)

        label = QLabel("تاريخ انتهاء التأمين")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")


        self.insuranceExpireEntry = QDateEdit()
        self.insuranceExpireEntry.setCalendarPopup(True)
        self.insuranceExpireEntry.setDisplayFormat("yyyy/MM/dd")

        self.todayButtonInsurance = QPushButton("اليوم",clicked=lambda:self.insuranceExpireEntry.calendarWidget().setSelectedDate(QDate().currentDate()))
        self.todayButtonInsurance.setStyleSheet("background-color:green;")

        self.insuranceExpireEntry.setLocale(arabic_locale)
        self.insuranceExpireEntry.setFont(QFont("Arial",12))
        self.insuranceExpireEntry.setStyleSheet("background-color:white;color:black")
        
        self.insuranceExpireEntry.calendarWidget().layout().addWidget(self.todayButtonInsurance)
        self.insuranceExpireEntry.calendarWidget().setSelectedDate(QDate().currentDate())


        layout.addWidget(label)
        layout.addWidget(self.insuranceExpireEntry)

        label = QLabel("بطاقة السائق")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")

        self.driverCardDateEntry = QDateEdit()
        self.driverCardDateEntry.setCalendarPopup(True)
        self.driverCardDateEntry.setDisplayFormat("yyyy/MM/dd")

        self.todayButtonDriverCard = QPushButton("اليوم",clicked=lambda:self.driverCardDateEntry.calendarWidget().setSelectedDate(QDate().currentDate()))
        self.todayButtonDriverCard.setStyleSheet("background-color:green;")

        self.driverCardDateEntry.setLocale(arabic_locale)
        self.driverCardDateEntry.setFont(QFont("Arial",12))
        self.driverCardDateEntry.setStyleSheet("background-color:white;color:black")
        
        self.driverCardDateEntry.calendarWidget().layout().addWidget(self.todayButtonDriverCard)
        self.driverCardDateEntry.calendarWidget().setSelectedDate(QDate().currentDate())


        layout.addWidget(label)
        layout.addWidget(self.driverCardDateEntry)

        addButton = QPushButton(text="اضافة")
        addButton.clicked.connect(self.completeAddDriver)
        addButton.setStyleSheet("QPushButton:hover {background-color:#c8c8c8;}")        

        layout.addWidget(addButton)

        self.scroolAria = QScrollArea(self.addDriverFrame)
        self.scroolAria.setWidget(self.frame)
        self.scroolAria.setStyleSheet("border:1px solid gray")
        self.scroolAria.move(20,50)
        self.scroolAria.resize(321,431)

        self.scroolAria.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)


        self.scroolAria.setWidgetResizable(True)


        #End scrolAria
        self.addDriverFrame.show()
    def completeAddDriver(self):
        if len(self.nameEntry.text()) > 0 and len(self.identyEntry.text()) > 0 and len(self.phoneEntry.text()) > 0 and len(self.nationalityEntry.text()) and len(self.identyExpireEntry.text()) > 0 and len(self.insuranceExpireEntry.text()) > 0 and len(self.driverCardDateEntry.text()) > 0:
            cr.execute("SELECT name FROM drivers WHERE identy =?",[self.identyEntry.text()])
            if cr.fetchall() == []:
                cr.execute("INSERT INTO drivers (name,identy,phone,nationality,identyExpire,insuranceExpire,driverCard) values (?,?,?,?,?,?,?)",(self.nameEntry.text(),self.identyEntry.text(),self.phoneEntry.text(),self.nationalityEntry.text(),self.identyExpireEntry.text(),self.insuranceExpireEntry.text(),self.driverCardDateEntry.text()))
                con.commit()
                message = QMessageBox(parent=self,text="تمت الاضافة بنجاح")
                message.setIcon(QMessageBox.Icon.Information)
                message.setWindowTitle("نجاح")
                message.exec()
                self.loadDrivers()
            else:
                message = QMessageBox(parent=self,text="يوجد بالفعل سائق بنفس رقم الهوية")
                message.setIcon(QMessageBox.Icon.Critical)
                message.setWindowTitle("فشل")
                message.exec()
        else:
            message = QMessageBox(parent=self,text="يرجى تعبئة جميع الحقول")
            message.setIcon(QMessageBox.Icon.Critical)
            message.setWindowTitle("فشل")
            message.exec()
    def loadDrivers(self):
        self.driversTable.setRowCount(0)     
        
        cr.execute("SELECT * FROM drivers")
        tempThing = [] 
        for i in cr.fetchall():
            tempThing.append(i)
        for row,i in enumerate(tempThing):
            self.driversTable.insertRow(self.driversTable.rowCount())
            for col,val in enumerate(i):
                self.driversTable.setItem(row,col,QTableWidgetItem(str(val)))
    def deleteDriver(self):
        DriverIdDelete = self.driversTable.item(self.driversTable.selectedIndexes()[0].row(),1).text()
        d = QMessageBox(parent=self,text=f"تأكيد حذف {self.driversTable.item(self.driversTable.selectedIndexes()[0].row(),0).text()}")
        d.setIcon(QMessageBox.Icon.Information)
        d.setWindowTitle("تأكيد")
        d.setStyleSheet("background-color:white")
        d.setStandardButtons(QMessageBox.StandardButton.Cancel|QMessageBox.StandardButton.Ok)
        important = d.exec()
        if important == QMessageBox.StandardButton.Ok:
            cr.execute("DELETE FROM drivers WHERE identy=?",[DriverIdDelete])
            con.commit()
            self.loadDrivers()
            d = QMessageBox(parent=self,text="تم الحذف بنجاح")
            d.setWindowTitle("نجاح")
            d.setIcon(QMessageBox.Icon.Information)
            d.setStyleSheet("background-color:white")
            ret = d.exec()
    def editDriver(self):
        try:
            self.destroyFrame(self.editDriverFrame)
        except:
            pass
        self.editDriverFrame = QFrame(self.mainFrame)
        self.editDriverFrame.setGeometry((self.mainFrame.width()-350)//2,(self.mainFrame.height()-506)//2,350,506)
        self.editDriverFrame.setStyleSheet("background-color:white;border:2px solid black")

        closeButton = QPushButton(self.editDriverFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(300,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.editDriverFrame:self.destroyFrame(frame))
        
        #Start scrolAria
        
        self.frame = QFrame()

        layout = QVBoxLayout()
        self.frame.setLayout(layout)

        label = QLabel("اسم السائق")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")
        self.nameEntry = QLineEdit()

        layout.addWidget(label)
        layout.addWidget(self.nameEntry)

        label = QLabel("رقم الاقامة")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")

        self.identyEntry = QLineEdit()
        self.identyEntry.setDisabled(True)

        layout.addWidget(label)
        layout.addWidget(self.identyEntry)

        label = QLabel("رقم الجوال")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")
        self.phoneEntry = QLineEdit()

        layout.addWidget(label)
        layout.addWidget(self.phoneEntry)

        label = QLabel("الجنسية")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")
        self.nationalityEntry = QLineEdit()

        layout.addWidget(label)
        layout.addWidget(self.nationalityEntry)

        label = QLabel("تاريخ انتهاء الاقامة")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")

        self.identyExpireEntry = QDateEdit()
        self.identyExpireEntry.setCalendarPopup(True)
        self.identyExpireEntry.setDisplayFormat("yyyy/MM/dd")

        arabic_locale = QLocale(QLocale.Language.Arabic, QLocale.Country.SaudiArabia)

        self.identyExpireEntry.setLocale(arabic_locale)
        self.identyExpireEntry.setFont(QFont("Arial",12))
        self.identyExpireEntry.setStyleSheet("background-color:white;color:black")

        self.todayButton = QPushButton("اليوم",clicked=lambda:self.identyExpireEntry.calendarWidget().setSelectedDate(QDate().currentDate()))
        self.todayButton.setStyleSheet("background-color:green;")

        self.identyExpireEntry.calendarWidget().layout().addWidget(self.todayButton)
        self.identyExpireEntry.calendarWidget().setSelectedDate(QDate().currentDate())

        layout.addWidget(label)
        layout.addWidget(self.identyExpireEntry)

        label = QLabel("تاريخ انتهاء التأمين")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")

        self.insuranceExpireEntry = QDateEdit()
        self.insuranceExpireEntry.setCalendarPopup(True)
        self.insuranceExpireEntry.setDisplayFormat("yyyy/MM/dd")

        self.todayButtonInsurance = QPushButton("اليوم",clicked=lambda:self.insuranceExpireEntry.calendarWidget().setSelectedDate(QDate().currentDate()))
        self.todayButtonInsurance.setStyleSheet("background-color:green;")

        self.insuranceExpireEntry.setLocale(arabic_locale)
        self.insuranceExpireEntry.setFont(QFont("Arial",12))
        self.insuranceExpireEntry.setStyleSheet("background-color:white;color:black")
        
        self.insuranceExpireEntry.calendarWidget().layout().addWidget(self.todayButtonInsurance)
        self.insuranceExpireEntry.calendarWidget().setSelectedDate(QDate().currentDate())

        layout.addWidget(label)
        layout.addWidget(self.insuranceExpireEntry)

        label = QLabel("بطاقة السائق")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")

        self.driverCardDateEntry = QDateEdit()
        self.driverCardDateEntry.setCalendarPopup(True)
        self.driverCardDateEntry.setDisplayFormat("yyyy/MM/dd")

        self.todayButtonDriverCard = QPushButton("اليوم",clicked=lambda:self.driverCardDateEntry.calendarWidget().setSelectedDate(QDate().currentDate()))
        self.todayButtonDriverCard.setStyleSheet("background-color:green;")

        self.driverCardDateEntry.setLocale(arabic_locale)
        self.driverCardDateEntry.setFont(QFont("Arial",12))
        self.driverCardDateEntry.setStyleSheet("background-color:white;color:black")
        
        self.driverCardDateEntry.calendarWidget().layout().addWidget(self.todayButtonDriverCard)
        self.driverCardDateEntry.calendarWidget().setSelectedDate(QDate().currentDate())

        layout.addWidget(label)
        layout.addWidget(self.driverCardDateEntry)

        editButton = QPushButton(text="تعديل")
        editButton.clicked.connect(self.completeEditDriver)
        editButton.setStyleSheet("QPushButton:hover {background-color:#c8c8c8;}")        

        layout.addWidget(editButton)

        self.scroolAria = QScrollArea(self.editDriverFrame)
        self.scroolAria.setWidget(self.frame)
        self.scroolAria.setStyleSheet("border:1px solid gray")
        self.scroolAria.move(20,50)
        self.scroolAria.resize(321,431)

        self.scroolAria.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)


        self.scroolAria.setWidgetResizable(True)

        BenefitIdEdit = self.driversTable.item(self.driversTable.selectedIndexes()[0].row(),1).text()
        cr.execute("SELECT * FROM drivers WHERE identy = ?",[BenefitIdEdit])
        values = cr.fetchall()[0]

        self.nameEntry.setText(values[0])
        self.identyEntry.setText(values[1])
        self.phoneEntry.setText(values[2])
        self.nationalityEntry.setText(values[3])

        split = str(values[4]).split("/")

        self.identyExpireEntry.setDate(QDate(int(split[0]), int(split[1]), int(split[2])))
        
        split = str(values[5]).split("/")
        self.insuranceExpireEntry.setDate(QDate(int(split[0]), int(split[1]), int(split[2])))\
        
        split = str(values[6]).split("/")

        self.driverCardDateEntry.setDate(QDate(int(split[0]),int(split[1]),int(split[2])))

        #End scrolAria
        self.editDriverFrame.show()
    def completeEditDriver(self):
        if len(self.nameEntry.text()) > 0 and len(self.identyEntry.text()) > 0 and len(self.phoneEntry.text()) > 0 and len(self.nationalityEntry.text()) and len(self.identyExpireEntry.text()) > 0 and len(self.insuranceExpireEntry.text()) > 0 and len(self.driverCardDateEntry.text()) > 0:
            cr.execute("UPDATE drivers set name=?, phone=?, nationality=?, identyExpire=?, insuranceExpire=?, driverCard=? WHERE identy=?",(self.nameEntry.text(),self.phoneEntry.text(),self.nationalityEntry.text(),self.identyExpireEntry.text(),self.insuranceExpireEntry.text(),self.driverCardDateEntry.text(), self.identyEntry.text()))
            con.commit()
            message = QMessageBox(parent=self,text="تم التعديل بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
            self.loadDrivers()
    def exportAllDrivers(self):
        try:
            self.destroyFrame(self.exportDriverFrame)
        except:
            pass
        self.exportDriverFrame = QFrame(parent=self.mainFrame)
        self.exportDriverFrame.setGeometry((self.mainFrame.width()-160)//2,(self.mainFrame.height()-174)//2,160,147)
        self.exportDriverFrame.setStyleSheet("background-color:white;border:2px solid black")

        closeButton = QPushButton(self.exportDriverFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:8px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 18px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(120,10,31,21)
        closeButton.clicked.connect(lambda x, frame=self.exportDriverFrame:self.destroyFrame(frame))

        label = QLabel(parent=self.exportDriverFrame,text="الصيغة")
        label.setStyleSheet('font: 14pt "Arial";border:none')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setGeometry(20,50,121,20)

        self.formatComboBox = QComboBox(self.exportDriverFrame)
        self.formatComboBox.addItems(["Word","Pdf","Excel"])
        self.formatComboBox.setGeometry(8,80,141,22)
        
        exportButton = QPushButton(parent=self.exportDriverFrame,text="تصدير")
        exportButton.setGeometry(30,110,101,31)
        exportButton.setStyleSheet("QPushButton:hover {background-color:#c8c8c8;}")
        exportButton.clicked.connect(self.completeExportAllDrivers)

        self.exportDriverFrame.show()
    def completeExportAllDrivers(self):
        filePath = QFileDialog.getExistingDirectory(self,"Select a Directory")
        if len(filePath) > 0:
            cr.execute("SELECT * FROM drivers")
            drivers = cr.fetchall()
            if self.formatComboBox.currentText() == "Excel":
                headers = ["الاسم","الهوية","الجوال","الجنسية","تاريخ انتهاء الاقامة","تاريخ انتهاء التأمين","بطاقة السائق"]

                wb = Workbook()
                sheet = wb.active
                sheet.title = "sheet1"
                col = 1
                #write the headers
                for header in headers:
                    cell = sheet.cell(row=1, column=col)
                    cell.value = header
                    col+=2
                #End headers

                for row,benefit in enumerate(drivers):
                    col = 1
                    for j in benefit:
                        cell = sheet.cell(row=row+2, column=col)
                        cell.value = j
                        col+=2
                wb.save(f"{filePath}/جميع السائقين.xlsx")    
            elif self.formatComboBox.currentText() == "Word" or self.formatComboBox.currentText() == "Pdf":

                doc = docx.Document()

                sections = doc.sections
                sections.page_height = 11.69
                sections.page_width = 8.27
                sections = sections[-1]
                sections.orientation = docx.enum.section.WD_ORIENT.LANDSCAPE


                new_width,new_height = sections.page_height,sections.page_width
                sections.page_width = new_width
                sections.page_height = new_height

                sections = doc.sections

                for section in sections:
                    section.top_margin = docx.shared.Cm(0.3)
                    section.bottom_margin = docx.shared.Cm(0.3)
                    section.left_margin = docx.shared.Cm(0.3)
                    section.right_margin = docx.shared.Cm(0.3)

                benefits_table = doc.add_table(rows=1,cols=8)
                benefits_table.style = "Table Grid"
                hdr_Cells = benefits_table.rows[0].cells
                hdr_Cells[7].text = "م"
                hdr_Cells[6].text = "الاسم"
                hdr_Cells[5].text = "الهوية"
                hdr_Cells[4].text = "الجوال"
                hdr_Cells[3].text = "الجنسية"
                hdr_Cells[2].text = "تاريخ انتهاء الاقامة"
                hdr_Cells[1].text = "تاريخ انتهاء التأمين"
                hdr_Cells[0].text = "بطاقة السائق"

                for cell in hdr_Cells:
                    self.set_arabic_format(cell)

                b = 0
                
                for i in drivers:
                    b+=1   
                    row_Cells = benefits_table.add_row().cells
                    row_Cells[0].size = docx.shared.Pt(15)
                    row_Cells[1].size = docx.shared.Pt(15)
                    row_Cells[2].size = docx.shared.Pt(15)
                    row_Cells[3].size = docx.shared.Pt(15)
                    row_Cells[4].size = docx.shared.Pt(15)
                    row_Cells[5].size = docx.shared.Pt(15)
                    row_Cells[6].size = docx.shared.Pt(15)
                    row_Cells[7].size = docx.shared.Pt(15)

                    row_Cells[7].text = str(b)
                    row_Cells[6].text = str(i[0])
                    row_Cells[5].text = str(i[1])
                    row_Cells[4].text = str(i[2])
                    row_Cells[3].text = str(i[3])
                    row_Cells[2].text = str(i[4])
                    row_Cells[1].text = str(i[5])
                    row_Cells[0].text = str(i[6])

                    for cell in row_Cells:
                        self.set_arabic_format(cell)

                widths = (docx.shared.Inches(4), docx.shared.Inches(4), docx.shared.Inches(4), docx.shared.Inches(4), docx.shared.Inches(4), docx.shared.Inches(4),docx.shared.Inches(3),docx.shared.Inches(0.5))
                for row in benefits_table.rows:
                    for idx, width in enumerate(widths):
                        row.cells[idx].width = width
                for row in benefits_table.rows:
                    for cell in row.cells:
                        paragraphs = cell.paragraphs
                        for paragraph in paragraphs:
                            for run in paragraph.runs:
                                font = run.font
                                font.size= docx.shared.Pt(17)

                doc.save(f"{filePath}\جميع السائقين.docx")

            if self.formatComboBox.currentText() == "Pdf":
                with suppress_output():
                    convert(f"{filePath}\جميع السائقين.docx",f"{filePath}\جميع السائقين.pdf")

                os.remove(f"{filePath}\جميع السائقين.docx")

            message = QMessageBox(parent=self,text="تم التصدير بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
    def exportDriversReport(self):
        try:
            self.destroyFrame(self.exportDriverReportFrame)
        except:
            pass

        arabic_locale = QLocale(QLocale.Language.Arabic, QLocale.Country.SaudiArabia)

        self.exportDriverReportFrame = QFrame(parent=self.mainFrame)
        self.exportDriverReportFrame.setGeometry((self.mainFrame.width()-210)//2,(self.mainFrame.height()-230)//2,210,230)
        self.exportDriverReportFrame.setStyleSheet("background-color:white;border:2px solid black")

        closeButton = QPushButton(self.exportDriverReportFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:8px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 18px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(160,10,31,21)
        closeButton.clicked.connect(lambda x, frame=self.exportDriverReportFrame:self.destroyFrame(frame))

        label = QLabel(parent=self.exportDriverReportFrame,text="من تاريخ")
        label.setStyleSheet('font: 18pt "Arial";border:none')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.move(50,50)

        self.fromDateExportDriver = QDateEdit(parent=self.exportDriverReportFrame)
        self.fromDateExportDriver.setCalendarPopup(True)
        self.fromDateExportDriver.setDisplayFormat("yyyy/MM/dd")

        self.todayButtonFromDateDriver = QPushButton("اليوم",clicked=lambda:self.fromDateExportDriver.calendarWidget().setSelectedDate(QDate().currentDate()))
        self.todayButtonFromDateDriver.setStyleSheet("background-color:green;")

        self.fromDateExportDriver.setLocale(arabic_locale)
        self.fromDateExportDriver.setFont(QFont("Arial",12))
        self.fromDateExportDriver.setStyleSheet("background-color:white;color:black")
        
        self.fromDateExportDriver.calendarWidget().layout().addWidget(self.todayButtonFromDateDriver)
        self.fromDateExportDriver.calendarWidget().setSelectedDate(QDate().currentDate())
        self.fromDateExportDriver.setGeometry(20,80,160,31)

        label = QLabel(parent=self.exportDriverReportFrame,text="الى تاريخ")
        label.setStyleSheet('font: 18pt "Arial";border:none')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.move(50,120)

        self.toDateExportDriver = QDateEdit(parent=self.exportDriverReportFrame)
        self.toDateExportDriver.setCalendarPopup(True)
        self.toDateExportDriver.setDisplayFormat("yyyy/MM/dd")

        self.todayButtonToDateDriver = QPushButton("اليوم",clicked=lambda:self.toDateExportDriver.calendarWidget().setSelectedDate(QDate().currentDate()))
        self.todayButtonToDateDriver.setStyleSheet("background-color:green;")

        self.toDateExportDriver.setLocale(arabic_locale)
        self.toDateExportDriver.setFont(QFont("Arial",12))
        self.toDateExportDriver.setStyleSheet("background-color:white;color:black")
        
        self.toDateExportDriver.calendarWidget().layout().addWidget(self.todayButtonToDateDriver)
        self.toDateExportDriver.calendarWidget().setSelectedDate(QDate().currentDate())
        self.toDateExportDriver.setGeometry(20,150,160,31)

        exportButton = QPushButton(parent=self.exportDriverReportFrame,text="تصدير")
        exportButton.setGeometry(50,190,101,31)
        exportButton.setStyleSheet("QPushButton:hover {background-color:#c8c8c8;}")
        exportButton.clicked.connect(self.completeExportDriversReport)


        self.exportDriverReportFrame.show()
    def completeExportDriversReport(self):
        filePath = QFileDialog.getExistingDirectory(self,"Select a Directory")
        if len(filePath) > 0: 
            doc = docx.Document()
            sections = doc.sections
            sections.page_height = 11.69
            sections.page_width = 8.27
            sections = sections[-1]
            sections.orientation = docx.enum.section.WD_ORIENT.LANDSCAPE
            
            driversIds = []
            fromDate = str(self.fromDateExportDriver.text()).split("/")
            fromDateGoodFormat = date(int(fromDate[0]),int(fromDate[1]),int(fromDate[2]))

            toDate = str(self.toDateExportDriver.text()).split("/")
            toDateGoodFormat = date(int(toDate[0]),int(toDate[1]),int(toDate[2]))

            new_width,new_height = sections.page_height,sections.page_width
            sections.page_width = new_width
            sections.page_height = new_height

            sections = doc.sections

            for section in sections:
                section.top_margin = docx.shared.Cm(0.3)
                section.bottom_margin = docx.shared.Cm(0.3)
                section.left_margin = docx.shared.Cm(0.3)
                section.right_margin = docx.shared.Cm(0.3)

            cr.execute("SELECT identy,identyExpire,insuranceExpire,driverCard FROM drivers")
            for i in cr.fetchall():
                for j in i[1:]:
                    date1 = str(j).split("/")
                    date2 = date(int(date1[0]),int(date1[1]),int(date1[2]))
                    
                    if date2>=fromDateGoodFormat and date2<=toDateGoodFormat:
                        driversIds.append(i[0])
                    
                    
            benefits_table = doc.add_table(rows=1,cols=8)
            benefits_table.style = "Table Grid"
            hdr_Cells = benefits_table.rows[0].cells
            hdr_Cells[7].text = "م"
            hdr_Cells[6].text = "الاسم"
            hdr_Cells[5].text = "الهوية"
            hdr_Cells[4].text = "الجوال"
            hdr_Cells[3].text = "الجنسية"
            hdr_Cells[2].text = "تاريخ انتهاء الاقامة"
            hdr_Cells[1].text = "تاريخ انتهاء التأمين"
            hdr_Cells[0].text = "بطاقة السائق"

            for cell in hdr_Cells:
                self.set_arabic_format(cell)

            b = 0
            drivers = []
            for driverId in driversIds:
                cr.execute("SELECT * FROM drivers WHERE identy=?",[driverId])
                drivers.append(list(cr.fetchall()[0]))

            for i in drivers:
                b+=1   
                row_Cells = benefits_table.add_row().cells
                row_Cells[0].size = docx.shared.Pt(15)
                row_Cells[1].size = docx.shared.Pt(15)
                row_Cells[2].size = docx.shared.Pt(15)
                row_Cells[3].size = docx.shared.Pt(15)
                row_Cells[4].size = docx.shared.Pt(15)
                row_Cells[5].size = docx.shared.Pt(15)
                row_Cells[6].size = docx.shared.Pt(15)
                row_Cells[7].size = docx.shared.Pt(15)

                row_Cells[7].text = str(b)
                row_Cells[6].text = str(i[0])
                row_Cells[5].text = str(i[1])
                row_Cells[4].text = str(i[2])
                row_Cells[3].text = str(i[3])
                row_Cells[2].text = str(i[4])
                row_Cells[1].text = str(i[5])
                row_Cells[0].text = str(i[6])

                for cell in row_Cells:
                    self.set_arabic_format(cell)

            widths = (docx.shared.Inches(4), docx.shared.Inches(4), docx.shared.Inches(4), docx.shared.Inches(4), docx.shared.Inches(4), docx.shared.Inches(4),docx.shared.Inches(3),docx.shared.Inches(0.5))
            for row in benefits_table.rows:
                for idx, width in enumerate(widths):
                    row.cells[idx].width = width
            for row in benefits_table.rows:
                for cell in row.cells:
                    paragraphs = cell.paragraphs
                    for paragraph in paragraphs:
                        for run in paragraph.runs:
                            font = run.font
                            font.size= docx.shared.Pt(17)

            doc.save(f"{filePath}\تقرير السائقين.docx")
            with suppress_output():
                convert(f"{filePath}\تقرير السائقين.docx",f"{filePath}\تقرير السائقين.pdf")

            os.remove(f"{filePath}\تقرير السائقين.docx")
 
            message = QMessageBox(parent=self,text="تم التصدير بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
    def destroyFrame(self,frame):

        for i in frame.children():
            i.deleteLater()

        frame.destroy()
        frame.deleteLater()