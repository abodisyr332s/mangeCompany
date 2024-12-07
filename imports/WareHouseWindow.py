from .stuff import *


class WareHouseWindow():
    def showWareHouse(self):
        try:
            self.destroyFrame(self.mainMenuWareHouse)
            self.destroyFrame(self.wareHouseFrame)
        except:
            pass
        self.wareHouseFrame = QFrame(self.mainFrame)
        
        self.closeButtonWareHouseFrame = QPushButton(self.wareHouseFrame)
        self.closeButtonWareHouseFrame.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        self.closeButtonWareHouseFrame.clicked.connect(lambda x, frame=self.wareHouseFrame:self.destroyFrame(frame))

        self.comboSearchWareHouseBox = QComboBox(self.wareHouseFrame)
        self.comboSearchWareHouseBox.setGeometry(500,30,150,20)
        self.comboSearchWareHouseBox.addItems(["الكل", "كود الصنف"])
        self.comboSearchWareHouseBox.activated.connect(self.addSearchWareHouseEntries)

        self.comboStatusBoxWareHouse = QComboBox(self.wareHouseFrame)
        self.comboStatusBoxWareHouse.setGeometry(100,30,150,20)
        self.comboStatusBoxWareHouse.addItems(["الكل", "جديد","تالف","تم البيع"])
        self.comboStatusBoxWareHouse.activated.connect(self.loadItems)

        self.wareHouseFrame.setStyleSheet("background-color:white")

        self.itemsTable = QTableWidget(self.wareHouseFrame)

        self.itemsTable.setColumnCount(5)
        self.itemsTable.setHorizontalHeaderLabels(["اسم الصنف","الكود","الوحدة", 'السعر', 'الحالة'])

        self.itemsTable.setColumnWidth(0, 110)
        self.itemsTable.setColumnWidth(1, 110)
        self.itemsTable.setColumnWidth(2, 110)
        self.itemsTable.setColumnWidth(3, 115)
        self.itemsTable.setColumnWidth(4, 150)


        self.contextMenuitemsTable = QMenu(self.itemsTable)
        self.contextMenuitemsTable.setStyleSheet("background-color:grey")
        self.createButtonitemsTable()

        self.itemsTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.itemsTable.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.itemsTable.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.itemsTable.customContextMenuRequested.connect(self.showMenuitemsTable)

        #Start minMenu Buttons style
        self.mainMenuWareHouse = QFrame(self.wareHouseFrame)
        self.mainMenuWareHouse.setStyleSheet("background-color:white;border:2px solid black")
        
        label = QLabel(self.mainMenuWareHouse,text="القائمة الرئيسيه")
        label.setStyleSheet("background-color:white;border-bottom:none;font: 14pt 'Arial';")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setGeometry(0,0,181,31)

        addItemsButton = QPushButton(self.mainMenuWareHouse,text="اضافة صنف")
        addItemsButton.setGeometry(0,50,181,31)
        addItemsButton.setStyleSheet("QPushButton {background-color:white;border:2px solid black;font: 14pt 'Arial';} QPushButton:hover {background-color:#c8c8c8;}")
        addItemsButton.clicked.connect(self.addItem)

        exportItems = QPushButton(self.mainMenuWareHouse,text="تصدير الأصناف")
        exportItems.setGeometry(0,90,181,31)
        exportItems.setStyleSheet("QPushButton {background-color:white;border:2px solid black;font: 14pt 'Arial';} QPushButton:hover {background-color:#c8c8c8;}")
        exportItems.clicked.connect(self.exportAllItems)

        statButton = QPushButton(self.mainMenuWareHouse,text="احصائيات")
        statButton.setGeometry(0,130,181,31)
        statButton.setStyleSheet("QPushButton {background-color:white;border:2px solid black;font: 14pt 'Arial';} QPushButton:hover {background-color:#c8c8c8;}")
        statButton.clicked.connect(self.showStats)

        statButton = QPushButton(self.mainMenuWareHouse,text="تصدير تقرير المستودع")
        statButton.setGeometry(0,170,181,31)
        statButton.setStyleSheet("QPushButton {background-color:white;border:2px solid black;font: 14pt 'Arial';} QPushButton:hover {background-color:#c8c8c8;}")
        statButton.clicked.connect(self.exportWareHouseReport)

        #End minMenu Buttons style
        self.putWareHouseFrameAndStuff()
        
        self.loadItems()
        self.wareHouseFrame.show()
    def putWareHouseFrameAndStuff(self):
        if self.width() <= 995 or self.height() <= 680:
            self.wareHouseFrame.setGeometry((self.width()-847)//2,(self.mainFrame.height()-610)//2,847,610)
            self.itemsTable.setGeometry(10,60,641,541)
            self.mainMenuWareHouse.setGeometry(660,60,181,230)
            self.closeButtonWareHouseFrame.setGeometry(800,10,41,31)
        else:
            self.wareHouseFrame.setGeometry(30,30,self.mainFrame.width()-60,self.mainFrame.height()-60)
            self.itemsTable.setGeometry(10,60,self.wareHouseFrame.width() - 206,self.wareHouseFrame.height()-100)
            self.mainMenuWareHouse.setGeometry(self.itemsTable.width() + 20,60,181,230)
            self.closeButtonWareHouseFrame.setGeometry(self.itemsTable.width() + 20 + 140,10,41,31)

        deserve = self.itemsTable.columnCount()
        for i in range(self.itemsTable.columnCount()):
            self.itemsTable.setColumnWidth(i, (self.itemsTable.width() - 20) // deserve)

        self.wareHouseFrame.show()
        self.itemsTable.show()
        self.mainMenuWareHouse.show()
        self.closeButtonWareHouseFrame.show()
    def exportWareHouseReport(self):
        try:
            self.destroyFrame(self.exportWareHouseFrame)
        except:
            pass

        arabic_locale = QLocale(QLocale.Language.Arabic, QLocale.Country.SaudiArabia)

        self.exportWareHouseFrame = QFrame(parent=self.mainFrame)
        self.exportWareHouseFrame.setGeometry((self.mainFrame.width()-210)//2,(self.mainFrame.height()-230)//2,210,230)
        self.exportWareHouseFrame.setStyleSheet("background-color:white;border:2px solid black")

        closeButton = QPushButton(self.exportWareHouseFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:8px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 18px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(160,10,31,21)
        closeButton.clicked.connect(lambda x, frame=self.exportWareHouseFrame:self.destroyFrame(frame))

        label = QLabel(parent=self.exportWareHouseFrame,text="من تاريخ")
        label.setStyleSheet('font: 18pt "Arial";border:none')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.move(50,50)

        self.fromDateExportWareHouse = QDateEdit(parent=self.exportWareHouseFrame)
        self.fromDateExportWareHouse.setCalendarPopup(True)
        self.fromDateExportWareHouse.setDisplayFormat("yyyy/MM/dd")

        self.todayButtonFromDateWareHouse = QPushButton("اليوم",clicked=lambda:self.fromDateExportWareHouse.calendarWidget().setSelectedDate(QDate().currentDate()))
        self.todayButtonFromDateWareHouse.setStyleSheet("background-color:green;")

        self.fromDateExportWareHouse.setLocale(arabic_locale)
        self.fromDateExportWareHouse.setFont(QFont("Arial",12))
        self.fromDateExportWareHouse.setStyleSheet("background-color:white;color:black")
        
        self.fromDateExportWareHouse.calendarWidget().layout().addWidget(self.todayButtonFromDateWareHouse)
        self.fromDateExportWareHouse.calendarWidget().setSelectedDate(QDate().currentDate())
        self.fromDateExportWareHouse.setGeometry(20,80,160,31)

        label = QLabel(parent=self.exportWareHouseFrame,text="الى تاريخ")
        label.setStyleSheet('font: 18pt "Arial";border:none')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.move(50,120)

        self.toDateExportWareHouse = QDateEdit(parent=self.exportWareHouseFrame)
        self.toDateExportWareHouse.setCalendarPopup(True)
        self.toDateExportWareHouse.setDisplayFormat("yyyy/MM/dd")

        self.todayButtonToDateWareHouse = QPushButton("اليوم",clicked=lambda:self.toDateExportWareHouse.calendarWidget().setSelectedDate(QDate().currentDate()))
        self.todayButtonToDateWareHouse.setStyleSheet("background-color:green;")

        self.toDateExportWareHouse.setLocale(arabic_locale)
        self.toDateExportWareHouse.setFont(QFont("Arial",12))
        self.toDateExportWareHouse.setStyleSheet("background-color:white;color:black")
        
        self.toDateExportWareHouse.calendarWidget().layout().addWidget(self.todayButtonToDateWareHouse)
        self.toDateExportWareHouse.calendarWidget().setSelectedDate(QDate().currentDate())
        self.toDateExportWareHouse.setGeometry(20,150,160,31)

        exportButton = QPushButton(parent=self.exportWareHouseFrame,text="تصدير")
        exportButton.setGeometry(50,190,101,31)
        exportButton.setStyleSheet("QPushButton:hover {background-color:#c8c8c8;}")
        exportButton.clicked.connect(self.completeExportReportWareHouse)

        self.exportWareHouseFrame.show()
    def completeExportReportWareHouse(self):
        filePath = QFileDialog.getExistingDirectory(self,"Select a Directory")
        if len(filePath) > 0:
            valuesToWrite = []
            itemsIds = []
            totalPriceToWrite = 0
            fromDate = str(self.fromDateExportWareHouse.text()).split("/")
            fromDateGoodFormat = date(int(fromDate[0]),int(fromDate[1]),int(fromDate[2]))

            toDate = str(self.toDateExportWareHouse.text()).split("/")
            toDateGoodFormat = date(int(toDate[0]),int(toDate[1]),int(toDate[2]))

            #[itemPrice,itemName, installDate, bigTruckNumber]

            cr.execute("SELECT itemId,itemAddDate FROM itemsDate")
            for i in cr.fetchall():
                date1 = str(i[1]).split("-")
                date2 = date(int(date1[0]),int(date1[1]),int(date1[2]))

                if date2>=fromDateGoodFormat and date2 <= toDateGoodFormat:
                    itemsIds.append(i[0])

            for itemId in itemsIds:
                cr.execute("SELECT name,code,price FROM items WHERE code=?",[itemId])
                result = list(cr.fetchall()[0])
                cr.execute("SELECT itemAddDate FROM itemsDate WHERE itemId=?",[itemId])
                result.append(cr.fetchone()[0])
                valuesToWrite.append([result[0],result[1],str(round(float(result[2]),2)),result[3]])
                totalPriceToWrite+=round(float(result[2]),2)

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

            benefits_table = doc.add_table(rows=1,cols=5)
            benefits_table.style = "Table Grid"
            hdr_Cells = benefits_table.rows[0].cells

            hdr_Cells[4].text = "م"
            hdr_Cells[3].text = "اسم الصنف"
            hdr_Cells[2].text = "الكود"
            hdr_Cells[1].text = "السعر"
            hdr_Cells[0].text = "تاريخ الشراء"

            for cell in hdr_Cells:
                self.set_arabic_format(cell)

            b = 0
            
            for i in valuesToWrite:
                b+=1   
                row_Cells = benefits_table.add_row().cells
                row_Cells[0].size = docx.shared.Pt(15)
                row_Cells[1].size = docx.shared.Pt(15)
                row_Cells[2].size = docx.shared.Pt(15)
                row_Cells[3].size = docx.shared.Pt(15)
                row_Cells[4].size = docx.shared.Pt(15)

                row_Cells[4].text = str(b)
                row_Cells[3].text = str(i[0])
                row_Cells[2].text = str(i[1])
                row_Cells[1].text = str(i[2])
                row_Cells[0].text = str(i[3])

                for cell in row_Cells:
                    self.set_arabic_format(cell)

            widths = (docx.shared.Inches(4), docx.shared.Inches(4), docx.shared.Inches(4), docx.shared.Inches(4),docx.shared.Inches(0.5))
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
            para = doc.add_paragraph().add_run(f"اجمالي الصرف على مستودع الاصناف:{round(totalPriceToWrite,2)}")
            para.font.name = "Arial"
            para.font.size = docx.shared.Pt(20)
            
            doc.save(f"{filePath}\تقرير مستودع الاصناف.docx")
            with suppress_output():
                convert(f"{filePath}\تقرير مستودع الاصناف.docx",f"{filePath}\تقرير مستودع الاصناف.pdf")
            os.remove(f"{filePath}\تقرير مستودع الاصناف.docx")

            message = QMessageBox(parent=self,text="تم التصدير بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
    def changeStatus(self):
        self.itemIdchangeStatus = self.itemsTable.item(self.itemsTable.selectedIndexes()[0].row(),1).text()
        try:
            self.changeStatusFrame.deleteLater()
        except:
            pass
        self.changeStatusFrame = QFrame(self.wareHouseFrame)
        self.changeStatusFrame.setGeometry((self.wareHouseFrame.width()-340)//2,(self.wareHouseFrame.height()-160)//2,340,160)
        # self.showTrucksNoteFrame.setStyleSheet("background-color:white;border:2px solid black")

        closeButton = QPushButton(self.changeStatusFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(290,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.changeStatusFrame:self.destroyFrame(frame))

        self.changeStatusFrame.setStyleSheet("background-color:white;border: 2px solid black")

        label = QLabel('الحالة',self.changeStatusFrame)
        label.setStyleSheet("border:0px")
        label.move(150,20)
        label.setFont(QFont("Arial", 16))

        self.comboChangeStatusBox = QComboBox(self.changeStatusFrame)
        self.comboChangeStatusBox.setGeometry(60,50,200,30)
        self.comboChangeStatusBox.addItems(["جديد","تالف","تم البيع"])

        cr.execute("SELECT condition FROM items WHERE code=?",[self.itemIdchangeStatus])
        self.comboChangeStatusBox.setCurrentText(cr.fetchone()[0])

        completeeditItemNoteButton = QPushButton("تغيير الحالة",self.changeStatusFrame)
        completeeditItemNoteButton.setStyleSheet("QPushButton {border:2px solid black;font:14pt 'Arial'}QPushButton:hover {background-color:#c8c8c8;}")        
        completeeditItemNoteButton.setGeometry(70,110,180,31)
        completeeditItemNoteButton.clicked.connect(self.completeEditStatus)

        #End minMenu Buttons style
        self.changeStatusFrame.show()
    def completeEditStatus(self):
        cr.execute("SELECT condition FROM items WHERE code=?",[self.itemIdchangeStatus])
        oldItemStatus = cr.fetchone()[0]
        cr.execute("UPDATE items set condition=? WHERE code=?",(self.comboChangeStatusBox.currentText(),self.itemIdchangeStatus))

        if self.comboChangeStatusBox.currentText()!="جديد":
            cr.execute("DELETE FROM trucksParts WHERE itemId=?",[self.itemIdchangeStatus])
            cr.execute("DELETE FROM bigTrucksParts WHERE itemId=?",[self.itemIdchangeStatus])
            cr.execute("INSERT INTO itemsLifecycle (itemId, date, action) values (?,?,?)",(self.itemIdchangeStatus, str(date.today()).replace("-","/"), f"تم تغيير حالة المنتج من {oldItemStatus} الى {self.comboChangeStatusBox.currentText()}"))


        con.commit()
        message = QMessageBox(parent=self,text="تم التعديل بنجاح")
        message.setIcon(QMessageBox.Icon.Information)
        message.setWindowTitle("نجاح")
        message.exec()
        self.loadItems()
    def addSearchWareHouseEntries(self):
        try:
            self.searchEntryItems.destroy()
            self.searchEntryItems.hide()
        except:
            pass
        if self.comboSearchWareHouseBox.currentText() == "الكل":
            self.loadItems()
        else:
            self.searchEntryItems = QLineEdit(self.wareHouseFrame)
            self.searchEntryItems.textChanged.connect(self.searchItemsFun)
            self.searchEntryItems.setGeometry(340,30,150,20)
            self.searchEntryItems.show()
    def searchItemsFun(self):
        if len(self.searchEntryItems.text())==0:
            self.loadItems()
        else:
            self.itemsTable.setRowCount(0)
            tempThing = [] 
            cr.execute("SELECT code From items")
            choices = cr.fetchall()
            posiple = []
            for o in choices:
                for n,i in enumerate(o):
                    try:
                        if o[n][:len(self.searchEntryItems.text())]==self.searchEntryItems.text():
                                if i not in posiple:
                                    posiple.append(i)
                    except:
                        pass

            for p in posiple:
                cr.execute("SELECT * FROM items WHERE code = ?", [p])
                for i in cr.fetchall():
                    tempThing.append(i)

            for row,i in enumerate(tempThing):
                self.itemsTable.insertRow(self.itemsTable.rowCount())
                for col,val in enumerate(i):
                    self.itemsTable.setItem(row,col,QTableWidgetItem(str(val)))
            self.changeBackgroundColorsToItemsTable()
    def showStats(self):
        try:
            self.destroyFrame(self.showStatsFrame)
        except:
            pass

        self.showStatsFrame = QFrame(self.wareHouseFrame)
        
        closeButtonWareHouseFrame = QPushButton(self.showStatsFrame)
        closeButtonWareHouseFrame.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButtonWareHouseFrame.clicked.connect(lambda x, frame=self.showStatsFrame:self.destroyFrame(frame))
        closeButtonWareHouseFrame.setGeometry(270,10,30,30)
        self.showStatsFrame.setStyleSheet("background-color:white")

        self.statsTable = QTableWidget(self.showStatsFrame)

        self.statsTable.setColumnCount(3)
        self.statsTable.setHorizontalHeaderLabels(["اسم الصنف","الكمية","اجمالي الصرف"])

        self.statsTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.statsTable.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.statsTable.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.statsTable.setGeometry(0,40,300,200)
        #Start minMenu Buttons style
        
        self.showStatsFrame.setGeometry((self.wareHouseFrame.width() - 400)//2,(self.wareHouseFrame.height() - 250)//2,400,250)
        self.loadStats()
        self.showStatsFrame.show()
    def loadStats(self):
        self.statsTable.setRowCount(0)     
        statsList = []
        cr.execute("SELECT name,price FROM items WHERE condition='جديد'")
        for name,price in cr.fetchall():
            if len(statsList) == 0:
                statsList.append([name,1,int(price)])
            else:
                for index,i in enumerate(statsList):
                    if i[0] == name:
                        i[1]+=1
                        i[2]+=int(price)
                        break
                    if index ==len(statsList) - 1:
                        statsList.append([name,1,int(price)])
                        break
        for row,i in enumerate(statsList):
            self.statsTable.insertRow(self.statsTable.rowCount())
            for col,val in enumerate(i):
                self.statsTable.setItem(row,col,QTableWidgetItem(str(val))) 
    def addItem(self):
        try:
            self.destroyFrame(self.addItemFrame)
        except:
            pass

        self.addItemFrame = QFrame(self.mainFrame)
        self.addItemFrame.setGeometry((self.mainFrame.width()-350)//2,(self.mainFrame.height()-506)//2,350,506)
        self.addItemFrame.setObjectName("addItem")
        self.addItemFrame.setStyleSheet("QFrame#addItem {background-color:white;border:2px solid black}")

        closeButton = QPushButton(self.addItemFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px;background-color:white;}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(300,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.addItemFrame:self.destroyFrame(frame))
        
        #Start scrolAria

        self.frame = QFrame()

        layout = QVBoxLayout()
        self.frame.setLayout(layout)


        label = QLabel("اسم الصنف")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';background-color:white")
        self.itemName = QLineEdit()
        
        layout.addWidget(label)
        layout.addWidget(self.itemName)

        label = QLabel("الكمية")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';background-color:white")

        self.itemsQuantity = QLineEdit()
        self.itemsQuantity.setValidator(QIntValidator(0,999999999))

        layout.addWidget(label)
        layout.addWidget(self.itemsQuantity)

        label = QLabel("الوحدة")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';background-color:white")
        self.itemUnit = QLineEdit()

        layout.addWidget(label)
        layout.addWidget(self.itemUnit)

        label = QLabel("السعر")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';background-color:white")
        self.itemPrice = QLineEdit()
        self.itemPrice.setValidator(QIntValidator(0,999999999))

        layout.addWidget(label)
        layout.addWidget(self.itemPrice)

        addButton = QPushButton(text="اضافة")
        addButton.clicked.connect(self.completeAddIetmStep1)
        addButton.setStyleSheet("QPushButton:hover {background-color:#c8c8c8;}")        

        layout.addWidget(addButton)

        self.scroolAria = QScrollArea(self.addItemFrame)
        self.scroolAria.setWidget(self.frame)
        self.scroolAria.setStyleSheet("border:1px solid gray;background-color:white")
        self.scroolAria.move(20,50)
        self.scroolAria.resize(321,431)

        self.scroolAria.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)


        self.scroolAria.setWidgetResizable(True)


        #End scrolAria
        self.addItemFrame.show()
    def completeAddIetmStep1(self):
        self.itemNameText = self.itemName.text()
        self.itemUnitText = self.itemUnit.text()
        self.itemPriceText = self.itemPrice.text()

        if (len(self.itemName.text()) > 0 and len(self.itemsQuantity.text()) > 0 and len(self.itemUnit.text()) > 0 and len(self.itemPrice.text()) > 0):
            for child in self.addItemFrame.children():
                child.deleteLater()

            closeButton = QPushButton(self.addItemFrame)
            closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px;background-color:white;}QPushButton:hover {background-color:#c8c8c8;}")                
            closeButton.setGeometry(300,10,41,31)
            closeButton.clicked.connect(lambda x, frame=self.addItemFrame:self.destroyFrame(frame))
            closeButton.show()

            self.codesTableEntry = QTableWidget(self.addItemFrame)
            self.codesTableEntry.setColumnCount(1)
            self.codesTableEntry.setHorizontalHeaderLabels(["يرجى ادخال الأكواد"])
            self.codesTableEntry.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
            self.codesTableEntry.setStyleSheet("background-color:white")
            self.codesTableEntry.setColumnWidth(0,308)
            self.codesTableEntry.setGeometry(10,50,331,200)
            self.codesTableEntry.show()

            addButton = QPushButton(text="اضافة",parent=self.addItemFrame)
            addButton.clicked.connect(self.completeAddItemStep2)
            addButton.setStyleSheet("QPushButton {background-color:white}QPushButton:hover {background-color:#c8c8c8;}")        
            addButton.setGeometry(10,280,331,31)
            addButton.show()
             
            for i in range(int(self.itemsQuantity.text())):
                self.codesTableEntry.insertRow(self.codesTableEntry.rowCount())
    def completeAddItemStep2(self):
        errorMessage = ""

        itemCodes = []
        itemCodesFromDataBase =[]
        for row in range(self.codesTableEntry.rowCount()):
            if self.codesTableEntry.item(row,0) != None:
                if self.codesTableEntry.item(row,0).text()=="":
                    errorMessage = "يرجى تعبئة جميع الحقول"
                    break
                else:
                    if self.codesTableEntry.item(row,0).text() in itemCodes:
                        errorMessage = "يوجد بالفعل اصناف بنفس رقم الكود داخل الحقول"
                        break
                    else:
                        itemCodes.append(self.codesTableEntry.item(row,0).text())
            else:
                errorMessage = "يرجى تعبئة جميع الحقول"
                break
        
        cr.execute("SELECT code FROM items")
        for itemCodeDataBase in cr.fetchall():
            itemCodesFromDataBase.append(str(itemCodeDataBase[0]))

        for itemCode in itemCodes:
            if itemCode in itemCodesFromDataBase:
                errorMessage = f"يوجد بالفعل صنف بنفس رقم الكود {itemCode} داخل النظام"
                break

        if errorMessage=="":
                for itemCode in itemCodes:
                    cr.execute("SELECT name FROM items WHERE code =?",[itemCode])
                    if cr.fetchall() == []:
                        cr.execute("INSERT INTO items (name,code,unit,price,condition) VALUES (?,?,?,?,?)",(self.itemNameText,itemCode,self.itemUnitText,self.itemPriceText,"جديد"))
                        cr.execute("INSERT INTO itemsLifecycle (itemId, date, action) VALUES (?,?,?)",(itemCode, str(date.today()).replace("-","/"), "تم اضافة اضافة الصنف الى النظام"))
                        cr.execute("INSERT INTO itemsDate (itemId,itemAddDate) VALUES (?,?)",(itemCode,str(date.today())))
                        con.commit()
                    else:
                        message = QMessageBox(parent=self,text=f"يوجد بالفعل صنف بنفس رفم الكود داخل النظام ({itemCode})")
                        message.setIcon(QMessageBox.Icon.Critical)
                        message.setWindowTitle("فشل")
                        message.exec()
                self.loadItems()
                message = QMessageBox(parent=self,text="تمت الاضافة بنجاح")
                message.setIcon(QMessageBox.Icon.Information)
                message.setWindowTitle("نجاح")
                message.exec()
        else:
            message = QMessageBox(parent=self,text=errorMessage)
            message.setIcon(QMessageBox.Icon.Critical)
            message.setWindowTitle("فشل")
            message.exec()
    def createButtonitemsTable(self):
        deleteItemButton = QAction(self.itemsTable)
        deleteItemButton.setIcon(QIcon("assests/trash.png"))
        deleteItemButton.setText("حذف")
        deleteItemButton.setFont(QFont("Arial" , 12))
        deleteItemButton.triggered.connect(self.deleteItem)
        
        AddItemToTruckButton = QAction(self.itemsTable)
        AddItemToTruckButton.setText("اضافة لشاحنة")
        AddItemToTruckButton.setFont(QFont("Arial" , 12))
        AddItemToTruckButton.triggered.connect(self.AddItemToTruck)

        showNotes = QAction(self.itemsTable)
        showNotes.setIcon(QIcon("assests/addNote.png"))
        showNotes.setText("اضافة ملاحظة")
        showNotes.setFont(QFont("Arial" , 12))
        showNotes.triggered.connect(self.showItemsNote)

        changeConditionButton = QAction(self.itemsTable)
        changeConditionButton.setText("تغيير الحالة")
        changeConditionButton.setFont(QFont("Arial" , 12))
        changeConditionButton.triggered.connect(self.changeStatus)

        showItemLifecycle = QAction(self.itemsTable)
        showItemLifecycle.setText("اظهار دورة حياة")
        showItemLifecycle.setFont(QFont("Arial" , 12))
        showItemLifecycle.triggered.connect(self.showItemLifecycycle)

        showItemPlace = QAction(self.itemsTable)
        showItemPlace.setText("اظهار مكان الاستخدام")
        showItemPlace.setFont(QFont("Arial" , 12))
        showItemPlace.triggered.connect(self.showItemsInTrucks)

        self.contextMenuitemsTable.addAction(AddItemToTruckButton)
        self.contextMenuitemsTable.addAction(changeConditionButton)
        self.contextMenuitemsTable.addAction(showNotes)
        self.contextMenuitemsTable.addAction(showItemPlace)
        self.contextMenuitemsTable.addAction(deleteItemButton)
        self.contextMenuitemsTable.addAction(showItemLifecycle)
    def showItemLifecycycle(self):
        try:
            self.showItemLifecycycleFrame.deleteLater()
        except:
            pass

        self.itemIdShowLifecycle = self.itemsTable.item(self.itemsTable.selectedIndexes()[0].row(),1).text()
        self.itemNameShowLifecycle = self.itemsTable.item(self.itemsTable.selectedIndexes()[0].row(),0).text()


        self.showItemLifecycycleFrame = QFrame(self.wareHouseFrame)
        self.showItemLifecycycleFrame.setGeometry((self.wareHouseFrame.width()-500)//2,(self.wareHouseFrame.height()-450)//2,500,450)
        # self.showTrucksNoteFrame.setStyleSheet("background-color:white;border:2px solid black")
        
        closeButton = QPushButton(self.showItemLifecycycleFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(400,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.showItemLifecycycleFrame:self.destroyFrame(frame))

        self.showItemLifecycycleFrame.setStyleSheet("background-color:white")

        self.itemLifecycleTable = QTableWidget(self.showItemLifecycycleFrame)
        self.itemLifecycleTable.setGeometry(10,60,460,240)

        self.itemLifecycleTable.setColumnCount(2)
        self.itemLifecycleTable.setHorizontalHeaderLabels(["التاريخ","الحدث"])
        self.itemLifecycleTable.setColumnWidth(0,120)
        self.itemLifecycleTable.setColumnWidth(1,330)

        self.itemLifecycleTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.itemLifecycleTable.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.itemLifecycleTable.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)

        exportItemsLifecycleReportButton = QPushButton(self.showItemLifecycycleFrame,text="تصدير التقرير")
        exportItemsLifecycleReportButton.setGeometry(150,380,181,31)
        exportItemsLifecycleReportButton.setStyleSheet("QPushButton {background-color:white;border:2px solid black;font: 14pt 'Arial';} QPushButton:hover {background-color:#c8c8c8;}")
        exportItemsLifecycleReportButton.clicked.connect(self.exportItemsLifecycleReport)

        #End minMenu Buttons style
        self.loadItemLifecycle()
        self.showItemLifecycycleFrame.show()
    def exportItemsLifecycleReport(self):
        filePath = QFileDialog.getExistingDirectory(self,"Select a Directory")
        if len(filePath) > 0:
            cr.execute("SELECT date,action FROM itemsLifecycle WHERE itemId = ?",[self.itemIdShowLifecycle])
            values = cr.fetchall()
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

            para = doc.add_paragraph()

            paraRun = para.add_run(f"دورة حياة الصنف {self.itemNameShowLifecycle}")
            paraRun.font.name = "Arial"
            paraRun.font.size = docx.shared.Pt(20)

            para.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER

            benefits_table = doc.add_table(rows=1,cols=3)
            benefits_table.style = "Table Grid"
            hdr_Cells = benefits_table.rows[0].cells
            hdr_Cells[2].text = "م"
            hdr_Cells[1].text = "التاريخ"
            hdr_Cells[0].text = "الحدث"

            for cell in hdr_Cells:
                self.set_arabic_format(cell)

            b = 0
            
            for i in values:
                b+=1   
                row_Cells = benefits_table.add_row().cells
                row_Cells[0].size = docx.shared.Pt(15)
                row_Cells[1].size = docx.shared.Pt(15)
                row_Cells[2].size = docx.shared.Pt(15)

                row_Cells[2].text = str(b)
                row_Cells[1].text = str(i[0])
                row_Cells[0].text = str(i[1])

                for cell in row_Cells:
                    self.set_arabic_format(cell)

            widths = (docx.shared.Inches(6),docx.shared.Inches(2),docx.shared.Inches(0.5))
            for row in benefits_table.rows:
                for idx, width in enumerate(widths):
                    row.cells[idx].width = width
            for row in benefits_table.rows:
                for cell in row.cells:
                    paragraphs = cell.paragraphs
                    for paragraph in paragraphs:
                        for run in paragraph.runs:
                            font = run.font
                            font.size= docx.shared.Pt(20)
                            
            benefits_table.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
            
            doc.save(f"{filePath}\دورة حياة الصنف {self.itemNameShowLifecycle}.docx")
            with suppress_output():
                convert(f"{filePath}\دورة حياة الصنف {self.itemNameShowLifecycle}.docx",f"{filePath}\دورة حياة الصنف {self.itemNameShowLifecycle}.pdf")
            os.remove(f"{filePath}\دورة حياة الصنف {self.itemNameShowLifecycle}.docx")

            message = QMessageBox(parent=self,text="تم التصدير بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
    def loadItemLifecycle(self):
        self.itemLifecycleTable.setRowCount(0)     
        
        cr.execute("SELECT date,action FROM itemsLifecycle WHERE itemId = ?",[self.itemIdShowLifecycle])
        tempThing = [] 
        for i in cr.fetchall():
            tempThing.append(i)
        for row,i in enumerate(tempThing):
            self.itemLifecycleTable.insertRow(self.itemLifecycleTable.rowCount())
            for col,val in enumerate(i):
                self.itemLifecycleTable.setItem(row,col,QTableWidgetItem(str(val))) 
    def showMenuItemsnotesTable(self, position):
        indexes = self.ItemsnotesTable.selectedIndexes()
        for index in indexes:
            self.contextMenuItemsnotesTable.exec(self.ItemsnotesTable.viewport().mapToGlobal(position))
    def showItemsNote(self):
        try:
            self.showItemsNoteFrame.deleteLater()
        except:
            pass
        self.itemIdNotes = self.itemsTable.item(self.itemsTable.selectedIndexes()[0].row(),1).text()
        
        self.showItemsNoteFrame = QFrame(self.wareHouseFrame)
        self.showItemsNoteFrame.setGeometry((self.wareHouseFrame.width()-450)//2,(self.wareHouseFrame.height()-400)//2,450,400)
        # self.showItemsNoteFrame.setStyleSheet("background-color:white;border:2px solid black")
        
        closeButton = QPushButton(self.showItemsNoteFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(400,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.showItemsNoteFrame:self.destroyFrame(frame))

        self.showItemsNoteFrame.setStyleSheet("background-color:white")

        self.ItemsnotesTable = QTableWidget(self.showItemsNoteFrame)
        self.ItemsnotesTable.setGeometry(10,60,410,240)

        self.ItemsnotesTable.setColumnCount(3)
        self.ItemsnotesTable.setHorizontalHeaderLabels(["id","الملاحظة", "تاريخ الملاحظة"])
        self.ItemsnotesTable.setColumnHidden(0,True)
        self.ItemsnotesTable.setColumnWidth(1, 300)

        self.contextMenuItemsnotesTable = QMenu(self.ItemsnotesTable)
        self.contextMenuItemsnotesTable.setStyleSheet("background-color:grey")
        self.createButtonItemsnotesTable()

        self.ItemsnotesTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.ItemsnotesTable.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ItemsnotesTable.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.ItemsnotesTable.customContextMenuRequested.connect(self.showMenuItemsnotesTable)
        
        addItemsNoteButton = QPushButton("اضافة ملاحظة",self.showItemsNoteFrame)
        addItemsNoteButton.setStyleSheet("QPushButton {border:2px solid black;font:14pt 'Arial'}QPushButton:hover {background-color:#c8c8c8;}")        
        addItemsNoteButton.setGeometry(120,310,180,31)
        addItemsNoteButton.clicked.connect(self.addItemsNote)

        #End minMenu Buttons style
        self.loadItemsNotes(self.itemIdNotes)
        self.showItemsNoteFrame.show()
    def createButtonItemsnotesTable(self):
        deleteItemNoteButton = QAction(self.ItemsnotesTable)
        deleteItemNoteButton.setIcon(QIcon("assests/deleteNote.png"))
        deleteItemNoteButton.setText("حذف")
        deleteItemNoteButton.setFont(QFont("Arial" , 12))
        deleteItemNoteButton.triggered.connect(self.deleteItemNote)

        editItemNoteButton = QAction(self.ItemsnotesTable)
        editItemNoteButton.setIcon(QIcon("assests/edit.png"))
        editItemNoteButton.setText("تعديل")
        editItemNoteButton.setFont(QFont("Arial" , 12))
        editItemNoteButton.triggered.connect(self.editItemNote)
        
        self.contextMenuItemsnotesTable.addAction(deleteItemNoteButton)
        self.contextMenuItemsnotesTable.addAction(editItemNoteButton)
    def deleteItemNote(self):
        noteIdDelete = self.ItemsnotesTable.item(self.ItemsnotesTable.selectedIndexes()[0].row(),0).text()
        d = QMessageBox(parent=self,text=f"تأكيد حذف الملاحظة")
        d.setIcon(QMessageBox.Icon.Information)
        d.setWindowTitle("تأكيد")
        d.setStyleSheet("background-color:white")
        d.setStandardButtons(QMessageBox.StandardButton.Cancel|QMessageBox.StandardButton.Ok)
        important = d.exec()
        if important == QMessageBox.StandardButton.Ok:
            cr.execute("DELETE FROM itemsNotes WHERE id=?",[noteIdDelete])
            con.commit()
            self.loadItemsNotes(self.itemIdNotes)
            d = QMessageBox(parent=self,text="تم الحذف بنجاح")
            d.setWindowTitle("نجاح")
            d.setIcon(QMessageBox.Icon.Information)
            d.setStyleSheet("background-color:white")
            ret = d.exec()
    def editItemNote(self):
        self.noteIdEdit = self.ItemsnotesTable.item(self.ItemsnotesTable.selectedIndexes()[0].row(),0).text()
        try:
            self.editItemNoteFrame.deleteLater()
        except:
            pass
        self.editItemNoteFrame = QFrame(self.wareHouseFrame)
        self.editItemNoteFrame.setGeometry((self.wareHouseFrame.width()-340)//2,(self.wareHouseFrame.height()-360)//2,340,360)
        # self.showTrucksNoteFrame.setStyleSheet("background-color:white;border:2px solid black")

        closeButton = QPushButton(self.editItemNoteFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(290,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.editItemNoteFrame:self.destroyFrame(frame))

        self.editItemNoteFrame.setStyleSheet("background-color:white;border: 2px solid black")


        label = QLabel('الملاحظة',self.editItemNoteFrame)
        label.setStyleSheet("border:0px")
        label.move(150,20)
        label.setFont(QFont("Arial", 16))

        self.notesTextWareHouse = QTextEdit(self.editItemNoteFrame)
        self.notesTextWareHouse.setGeometry(10,60,320,150)

        label = QLabel('تاريخ الملاحظة',self.editItemNoteFrame)
        label.setStyleSheet("border:0px")
        label.move(120,230)
        label.setFont(QFont("Arial", 16))

        arabic_locale = QLocale(QLocale.Language.Arabic, QLocale.Country.SaudiArabia)
        
        self.noteDateEntry = QDateEdit(self.editItemNoteFrame)


        self.noteDateEntry.setCalendarPopup(True)
        self.noteDateEntry.setDisplayFormat("yyyy/MM/dd")

        self.todayButtonNoteDate = QPushButton("اليوم",clicked=lambda:self.noteDateEntry.calendarWidget().setSelectedDate(QDate().currentDate()))
        self.todayButtonNoteDate.setStyleSheet("background-color:green;")

        self.noteDateEntry.setLocale(arabic_locale)
        self.noteDateEntry.setFont(QFont("Arial",12))
        self.noteDateEntry.setStyleSheet("background-color:white;color:black;border:1px solid black")

        self.noteDateEntry.calendarWidget().layout().addWidget(self.todayButtonNoteDate)
        self.noteDateEntry.calendarWidget().setSelectedDate(QDate().currentDate())
        self.noteDateEntry.setGeometry(60, 260, 210, 30)

        cr.execute("SELECT note, date FROM itemsNotes WHERE id=?",[self.noteIdEdit])
        values = cr.fetchall()[0]
        self.notesTextWareHouse.setText(values[0])
        noteDate = str(values[1]).split("/")
        self.noteDateEntry.setDate(QDate(int(noteDate[0]), int(noteDate[1]), int(noteDate[2])))


        completeeditItemNoteButton = QPushButton("تعديل ملاحظة",self.editItemNoteFrame)
        completeeditItemNoteButton.setStyleSheet("QPushButton {border:2px solid black;font:14pt 'Arial'}QPushButton:hover {background-color:#c8c8c8;}")        
        completeeditItemNoteButton.setGeometry(80,310,180,31)
        completeeditItemNoteButton.clicked.connect(self.completeEditItemNotes)

        #End minMenu Buttons style
        self.editItemNoteFrame.show()
    def completeEditItemNotes(self):
        if (len(self.notesTextWareHouse.toPlainText()) > 0): 
            cr.execute("UPDATE itemsNotes set note=?, date=? WHERE id=?",(self.notesTextWareHouse.toPlainText(),self.noteDateEntry.text(),self.noteIdEdit))
            con.commit()
            message = QMessageBox(parent=self,text="تم التعديل بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
            self.loadItemsNotes(self.itemIdNotes)
        else:
            message = QMessageBox(parent=self,text="يرجى تعبئة جميع الحقول")
            message.setIcon(QMessageBox.Icon.Critical)
            message.setWindowTitle("فشل")
            message.exec()
    def addItemsNote(self):
        try:
            self.addItemsNoteFrame.deleteLater()
        except:
            pass
        self.addItemsNoteFrame = QFrame(self.wareHouseFrame)
        self.addItemsNoteFrame.setGeometry((self.wareHouseFrame.width()-340)//2,(self.wareHouseFrame.height()-360)//2,340,360)
        # self.showTrucksNoteFrame.setStyleSheet("background-color:white;border:2px solid black")

        closeButton = QPushButton(self.addItemsNoteFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(290,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.addItemsNoteFrame:self.destroyFrame(frame))

        self.addItemsNoteFrame.setStyleSheet("background-color:white;border: 2px solid black")


        label = QLabel('الملاحظة',self.addItemsNoteFrame)
        label.setStyleSheet("border:0px")
        label.move(150,20)
        label.setFont(QFont("Arial", 16))

        self.notesTextWareHouse = QTextEdit(self.addItemsNoteFrame)
        self.notesTextWareHouse.setGeometry(10,60,320,150)

        label = QLabel('تاريخ الملاحظة',self.addItemsNoteFrame)
        label.setStyleSheet("border:0px")
        label.move(120,230)
        label.setFont(QFont("Arial", 16))

        arabic_locale = QLocale(QLocale.Language.Arabic, QLocale.Country.SaudiArabia)
        
        self.noteDateEntry = QDateEdit(self.addItemsNoteFrame)


        self.noteDateEntry.setCalendarPopup(True)
        self.noteDateEntry.setDisplayFormat("yyyy/MM/dd")

        self.todayButtonNoteDate = QPushButton("اليوم",clicked=lambda:self.noteDateEntry.calendarWidget().setSelectedDate(QDate().currentDate()))
        self.todayButtonNoteDate.setStyleSheet("background-color:green;")

        self.noteDateEntry.setLocale(arabic_locale)
        self.noteDateEntry.setFont(QFont("Arial",12))
        self.noteDateEntry.setStyleSheet("background-color:white;color:black;border:1px solid black")

        self.noteDateEntry.calendarWidget().layout().addWidget(self.todayButtonNoteDate)
        self.noteDateEntry.calendarWidget().setSelectedDate(QDate().currentDate())
        self.noteDateEntry.setGeometry(60, 260, 210, 30)


        completeaddItemsNoteButton = QPushButton("اضافة ملاحظة",self.addItemsNoteFrame)
        completeaddItemsNoteButton.setStyleSheet("QPushButton {border:2px solid black;font:14pt 'Arial'}QPushButton:hover {background-color:#c8c8c8;}")        
        completeaddItemsNoteButton.setGeometry(80,310,180,31)
        completeaddItemsNoteButton.clicked.connect(self.completeaddItemsNote)

        #End minMenu Buttons style
        self.loadItemsNotes(self.itemIdNotes)
        self.addItemsNoteFrame.show()
    def completeaddItemsNote(self):
        if (len(self.notesTextWareHouse.toPlainText()) > 0): 
            cr.execute("INSERT INTO itemsNotes (itemId,note,date) VALUES (?,?,?)",(self.itemIdNotes, self.notesTextWareHouse.toPlainText(), self.noteDateEntry.text()))
            con.commit()
            message = QMessageBox(parent=self,text="تمت الاضافة بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
            self.loadItemsNotes(self.itemIdNotes)
        else:
            message = QMessageBox(parent=self,text="يرجى تعبئة جميع الحقول")
            message.setIcon(QMessageBox.Icon.Critical)
            message.setWindowTitle("فشل")
            message.exec()
    def loadItemsNotes(self, itemId):
        self.ItemsnotesTable.setRowCount(0)     
        
        cr.execute("SELECT id,note,date FROM itemsNotes WHERE itemId = ?",[itemId])
        tempThing = [] 
        for i in cr.fetchall():
            tempThing.append(i)
        for row,i in enumerate(tempThing):
            self.ItemsnotesTable.insertRow(self.ItemsnotesTable.rowCount())
            for col,val in enumerate(i):
                self.ItemsnotesTable.setItem(row,col,QTableWidgetItem(str(val))) 
    def deleteItem(self):
        itemIdDelete = self.itemsTable.item(self.itemsTable.selectedIndexes()[0].row(),1).text()
        d = QMessageBox(parent=self,text=f"تأكيد حذف الصنف")
        d.setIcon(QMessageBox.Icon.Information)
        d.setWindowTitle("تأكيد")
        d.setStyleSheet("background-color:white")
        d.setStandardButtons(QMessageBox.StandardButton.Cancel|QMessageBox.StandardButton.Ok)
        important = d.exec()
        if important == QMessageBox.StandardButton.Ok:
            cr.execute("DELETE FROM items WHERE code=?",[itemIdDelete])
            cr.execute("DELETE FROM itemsLifecycle WHERE itemId=?",[itemIdDelete])
            cr.execute("DELETE FROM bigTrucksParts WHERE itemId=?",[itemIdDelete])
            cr.execute("DELETE FROM itemsNotes WHERE itemId=?",[itemIdDelete])
            cr.execute("DELETE FROM trucksParts WHERE itemId=?",[itemIdDelete])
            cr.execute("DELETE FROM itemsDate WHERE itemId=?",[itemIdDelete])
            con.commit()
            self.loadItems()
            d = QMessageBox(parent=self,text="تم الحذف بنجاح")
            d.setWindowTitle("نجاح")
            d.setIcon(QMessageBox.Icon.Information)
            d.setStyleSheet("background-color:white")
            d.exec()
    def AddItemToTruck(self):
        try:
            self.destroyFrame(self.addItemToTruckFrame)
        except:
            pass
        
        self.currentIdTruckWarehouse = None
        

        self.itemId = self.itemsTable.item(self.itemsTable.selectedIndexes()[0].row(),1).text()
        self.itemName = self.itemsTable.item(self.itemsTable.selectedIndexes()[0].row(),0).text()
        self.itemPrice = self.itemsTable.item(self.itemsTable.selectedIndexes()[0].row(),3).text()
        
        cr.execute("SELECT truckId FROM trucksParts WHERE itemId = ?",[self.itemId])
        trucksParts = cr.fetchall()
        cr.execute("SELECT bigTruckId FROM bigTrucksParts WHERE itemId=?",[self.itemId])
        bigTrucksParts = cr.fetchall()


        if len(trucksParts) != 0 or len(bigTrucksParts)!=0:
            message = QMessageBox(parent=self,text="القطعة مركبة بشاحنة/تيدر بالفعل")
            message.setIcon(QMessageBox.Icon.Critical)
            message.setWindowTitle("فشل")
            message.exec()
            return

        self.addItemToTruckFrame = QFrame(self.mainFrame)
        self.addItemToTruckFrame.setGeometry((self.mainFrame.width()-360)//2,(self.mainFrame.height()-550)//2,360,550)
        self.addItemToTruckFrame.setObjectName("addItemToTruckFrame")
        self.addItemToTruckFrame.setStyleSheet("QFrame#addItemToTruckFrame {background-color:white;border:2px solid black}")

        closeButton = QPushButton(self.addItemToTruckFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px;background-color:#fdfdfd}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(323,10,31,31)
        closeButton.clicked.connect(lambda x, frame=self.addItemToTruckFrame:self.destroyFrame(frame))

        label = QLabel(parent=self.addItemToTruckFrame, text="اختر الشاحنة")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font: 14pt 'Arial';background-color:white")
        label.setGeometry(108,40,151,31)

        self.comboBoxChoicesWareHouse = QComboBox(parent=self.addItemToTruckFrame)
        self.comboBoxChoicesWareHouse.setStyleSheet("background-color:#fdfdfd")
        self.comboBoxChoicesWareHouse.addItems(["الكل", "رقم الشاحنة"])
        self.comboBoxChoicesWareHouse.setGeometry(256,70,101,22)
        self.comboBoxChoicesWareHouse.currentIndexChanged.connect(self.addSearchEntryAddTruckToItems)


        self.trucksTableToChoiceWareHouse = QTableWidget(parent=self.addItemToTruckFrame)
        self.trucksTableToChoiceWareHouse.setStyleSheet("background-color:white")
        self.trucksTableToChoiceWareHouse.setColumnCount(4)
        self.trucksTableToChoiceWareHouse.setColumnHidden(0,True)
        self.trucksTableToChoiceWareHouse.setColumnWidth(1,40)
        self.trucksTableToChoiceWareHouse.setColumnWidth(2,140)
        self.trucksTableToChoiceWareHouse.setColumnWidth(3,140)

        self.trucksTableToChoiceWareHouse.setHorizontalHeaderLabels(["id", "", "رقم السيارة","نوعه"])
        self.trucksTableToChoiceWareHouse.setGeometry(11,100,346,121)

        label = QLabel('تاريخ التركيب',self.addItemToTruckFrame)
        label.setStyleSheet("border:0px;background-color:#fdfdfd")
        label.move(140,230)
        label.setFont(QFont("Arial", 16))

        arabic_locale = QLocale(QLocale.Language.Arabic, QLocale.Country.SaudiArabia)

        self.installDateEntryWareHouse = QDateEdit(self.addItemToTruckFrame)


        self.installDateEntryWareHouse.setCalendarPopup(True)
        self.installDateEntryWareHouse.setDisplayFormat("yyyy/MM/dd")

        todayButtonNoteDate = QPushButton("اليوم",clicked=lambda:self.installDateEntryWareHouse.calendarWidget().setSelectedDate(QDate().currentDate()))
        todayButtonNoteDate.setStyleSheet("background-color:green;")

        self.installDateEntryWareHouse.setLocale(arabic_locale)
        self.installDateEntryWareHouse.setFont(QFont("Arial",12))
        self.installDateEntryWareHouse.setStyleSheet("background-color:#fdfdfd;color:black;border:1px solid black")

        self.installDateEntryWareHouse.calendarWidget().layout().addWidget(todayButtonNoteDate)
        self.installDateEntryWareHouse.calendarWidget().setSelectedDate(QDate().currentDate())
        self.installDateEntryWareHouse.setGeometry(80, 260, 210, 30)

        label = QLabel('مكان التركيب',self.addItemToTruckFrame)
        label.setStyleSheet("border:0px;background-color:#fdfdfd")
        label.move(140,290)
        label.setFont(QFont("Arial", 16))

        self.installPlaceWareHouse = QLineEdit(self.addItemToTruckFrame)
        self.installPlaceWareHouse.setStyleSheet("background-color:#fdfdfd")
        self.installPlaceWareHouse.setFont(QFont("Arial", 18))
        self.installPlaceWareHouse.setGeometry(80,320,210,30)

        label = QLabel('ملاحظات',self.addItemToTruckFrame)
        label.setStyleSheet("border:0px;background-color:#fdfdfd")
        label.move(150,350)
        label.setFont(QFont("Arial", 16))

        self.notesTextWareHouse = QTextEdit(self.addItemToTruckFrame)
        self.notesTextWareHouse.setStyleSheet("background-color:#ffffff")
        self.notesTextWareHouse.setGeometry(11,380,346,100)

        addItemToTruckButton = QPushButton(parent=self.addItemToTruckFrame, text="اضافة")
        addItemToTruckButton.setStyleSheet("background-color:#fdfdfd")
        addItemToTruckButton.clicked.connect(self.completeAddItemToTruck)
        addItemToTruckButton.setGeometry(118,490,131,31)

        self.loadItemToTrucksWareHouse()
        self.addItemToTruckFrame.show()
    def addSearchEntryAddTruckToItems(self):
        if self.comboBoxChoicesWareHouse.currentText() == "الكل":
            try:
                self.choiceEntryWareHouse.destroy()
                self.choiceEntryWareHouse.close()
            except:
                pass
            self.loadItemToTrucksWareHouse()
        else:
            try:
                self.choiceEntryWareHouse.destroy()
                self.choiceEntryWareHouse.close()
            except:
                pass
            self.choiceEntryWareHouse = QLineEdit(parent=self.addItemToTruckFrame)
            self.choiceEntryWareHouse.textChanged.connect(self.searchTruckToAddTruckToItem)
            self.choiceEntryWareHouse.setStyleSheet("background-color:white;")
            self.choiceEntryWareHouse.setGeometry(120,70,121,20)
            self.choiceEntryWareHouse.show()
    def searchTruckToAddTruckToItem(self):
        if len(self.choiceEntryWareHouse.text())==0:
            self.loadItemToTrucksWareHouse()
        else:
            self.trucksTableToChoiceWareHouse.setRowCount(0)
            tempThing = [] 
            cr.execute("SELECT carNumber From trucks")
            choices = cr.fetchall()
            posiple = []
            for o in choices:
                for n,i in enumerate(o):
                    try:
                        if o[n][:len(self.choiceEntryWareHouse.text())]==self.choiceEntryWareHouse.text():
                                if i not in posiple:
                                    posiple.append(i)
                    except:
                        pass

            #bigTrucks search
            cr.execute("SELECT number From bigTrucks")
            choices = cr.fetchall()
            for o in choices:
                for n,i in enumerate(o):
                    try:
                        if o[n][:len(self.choiceEntryWareHouse.text())]==self.choiceEntryWareHouse.text():
                                if i not in posiple:
                                    posiple.append(i)
                    except:
                        pass

            for p in posiple:
                cr.execute("SELECT id, carNumber FROM trucks WHERE carNumber = ?", [p])
                for i in cr.fetchall():
                    i = list(i)
                    i.insert(1,"")
                    i.append("شاحنة")
                    tempThing.append(i)

            #search bigh trcks
            for p in posiple:
                cr.execute("SELECT id, number FROM bigTrucks WHERE number = ?", [p])
                for i in cr.fetchall():
                    i = list(i)
                    i.insert(1,"")
                    i.append("تيدر")
                    tempThing.append(i)

            for row in range(len(tempThing)):
                self.trucksTableToChoiceWareHouse.insertRow(self.trucksTableToChoiceWareHouse.rowCount())
                for col in range(self.trucksTableToChoiceWareHouse.columnCount()):
                    self.trucksTableToChoiceWareHouse.setItem(row,col,QTableWidgetItem(str(tempThing[row][col])))
                    if col==1:
                        button = QRadioButton()
                        button.clicked.connect(lambda ch,truckId=tempThing[row][0]:self.changeCurrentId(truckId))
                        if tempThing[row][0] == self.currentIdTruckWarehouse:
                            button.setChecked(True)
                        self.trucksTableToChoiceWareHouse.setIndexWidget(self.trucksTableToChoiceWareHouse.model().index(row,1),button)           
    def completeAddItemToTruck(self):
        self.carTypeWareHouse = None
        for row in range(self.trucksTableToChoiceWareHouse.rowCount()):
            if self.trucksTableToChoiceWareHouse.cellWidget(row,1).isChecked():
                self.carTypeWareHouse = self.trucksTableToChoiceWareHouse.item(row,3).text()
                
        if (self.currentIdTruckWarehouse != None and len(self.installDateEntryWareHouse.text()) > 0 and len(self.installPlaceWareHouse.text())) > 0 and self.carTypeWareHouse!=None:
            if self.carTypeWareHouse == "شاحنة":
                cr.execute("INSERT INTO trucksParts (itemId, truckId, itemPrice, itemName, installPlace,installDate,notes,type) VALUES (?,?,?,?,?,?,?,?)",(self.itemId, self.currentIdTruckWarehouse, self.itemPrice, self.itemName, self.installPlaceWareHouse.text(), self.installDateEntryWareHouse.text(),self.notesTextWareHouse.toPlainText(),'item'))
            elif self.carTypeWareHouse == "تيدر":
                cr.execute("INSERT INTO bigTrucksParts (itemId, bigTruckId, itemPrice, itemName, installPlace,installDate,notes,type) VALUES (?,?,?,?,?,?,?,?)",(self.itemId, self.currentIdTruckWarehouse, self.itemPrice, self.itemName, self.installPlaceWareHouse.text(), self.installDateEntryWareHouse.text(),self.notesTextWareHouse.toPlainText(),'item'))
            
            if self.carTypeWareHouse == "شاحنة":
                cr.execute("SELECT carNumber FROM trucks WHERE id=?",[self.currentIdTruckWarehouse])
                cr.execute("INSERT INTO itemsLifecycle (itemId,date,action) VALUES (?,?,?)",(self.itemId, str(date.today()).replace("-","/"), f"تم تركيب القطعة على شاحنة رقم {str(cr.fetchone()[0])} ومكان التركيب هو {self.installPlaceWareHouse.text()}"))
            elif self.carTypeWareHouse  == "تيدر":
                cr.execute("SELECT number FROM bigTrucks WHERE id=?",[self.currentIdTruckWarehouse])
                cr.execute("INSERT INTO itemsLifecycle (itemId,date,action) VALUES (?,?,?)",(self.itemId, str(date.today()).replace("-","/"), f"تم تركيب القطعة على تيدر رقم {str(cr.fetchone()[0])} ومكان التركيب هو {self.installPlaceWareHouse.text()}"))
            
            con.commit()
            message = QMessageBox(parent=self,text="تمت الاضافة بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
            try:
                for child in self.addItemToTruckFrame.children():
                    child.deleteLater()
                self.addItemToTruckFrame.deleteLater()
            except:
                pass
        else:
            message = QMessageBox(parent=self,text="يرجى تعبئة جميع الحقول")
            message.setIcon(QMessageBox.Icon.Critical)
            message.setWindowTitle("فشل")
            message.exec()
    def loadItemToTrucksWareHouse(self):
        self.trucksTableToChoiceWareHouse.setRowCount(0)
        cr.execute("SELECT id, carNumber FROM trucks")
        
        tempThing = []
        for i in cr.fetchall():
            i = list(i)
            i.insert(1,"")
            i.append("شاحنة")
            tempThing.append(i)

        cr.execute("SELECT id, number FROM bigTrucks")

        for i in cr.fetchall():
            i = list(i)
            i.insert(1,"")
            i.append("تيدر")
            tempThing.append(i)

        for row in range(len(tempThing)):
            self.trucksTableToChoiceWareHouse.insertRow(self.trucksTableToChoiceWareHouse.rowCount())
            for col in range(self.trucksTableToChoiceWareHouse.columnCount()):
                self.trucksTableToChoiceWareHouse.setItem(row,col,QTableWidgetItem(str(tempThing[row][col])))
                if col==1:
                    button = QRadioButton()
                    button.clicked.connect(lambda ch,truckId=tempThing[row][0]:self.changeCurrentId(truckId))
                    if tempThing[row][0] == self.currentIdTruckWarehouse:
                        button.setChecked(True)
                    self.trucksTableToChoiceWareHouse.setIndexWidget(self.trucksTableToChoiceWareHouse.model().index(row,1),button)
    def changeCurrentId(self, truckId):
        self.currentIdTruckWarehouse = truckId
    def showMenuitemsTable(self, position):
        indexes = self.itemsTable.selectedIndexes()
        for index in indexes:
            if self.itemsTable.item(self.itemsTable.selectedIndexes()[0].row(),4).text() == 'تالف' or self.itemsTable.item(self.itemsTable.selectedIndexes()[0].row(),4).text() == 'تم البيع':
                self.contextMenuitemsTable.actions()[0].setVisible(False)
            else:
                self.contextMenuitemsTable.actions()[0].setVisible(True)
            self.contextMenuitemsTable.exec(self.itemsTable.viewport().mapToGlobal(position))
    def exportAllItems(self):
        try:
            self.destroyFrame(self.exportAllItemsFrame)
        except:
            pass
        self.exportAllItemsFrame = QFrame(parent=self.mainFrame)
        self.exportAllItemsFrame.setGeometry((self.mainFrame.width()-160)//2,(self.mainFrame.height()-174)//2,160,147)
        self.exportAllItemsFrame.setStyleSheet("background-color:white;border:2px solid black")

        closeButton = QPushButton(self.exportAllItemsFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:8px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 18px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(120,10,31,21)
        closeButton.clicked.connect(lambda x, frame=self.exportAllItemsFrame:self.destroyFrame(frame))

        label = QLabel(parent=self.exportAllItemsFrame,text="الصيغة")
        label.setStyleSheet('font: 14pt "Arial";border:none')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setGeometry(20,50,121,20)

        self.formatComboBox = QComboBox(self.exportAllItemsFrame)
        self.formatComboBox.addItems(["Word","Pdf","Excel"])
        self.formatComboBox.setGeometry(8,80,141,22)
        
        exportButton = QPushButton(parent=self.exportAllItemsFrame,text="تصدير")
        exportButton.setGeometry(30,110,101,31)
        exportButton.setStyleSheet("QPushButton:hover {background-color:#c8c8c8;}")
        exportButton.clicked.connect(self.completeExportAllItems)

        self.exportAllItemsFrame.show()
    def completeExportAllItems(self):
        filePath = QFileDialog.getExistingDirectory(self,"Select a Directory")
        if len(filePath) > 0:
            cr.execute("SELECT * FROM items")
            items = cr.fetchall()
            if self.formatComboBox.currentText() == "Excel":

                headers = ["اسم الصنف","الكود","الوحدة","السعر","الحالة"]

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

                for row,items in enumerate(items):
                    col = 1
                    for j in items:
                        cell = sheet.cell(row=row+2, column=col)
                        cell.value = j
                        col+=2
                wb.save(f"{filePath}/جميع الأصناف.xlsx")    
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

                headers = ["اسم الصنف","الكود","الوحدة","السعر","الحالة"]

                benefits_table = doc.add_table(rows=1,cols=6)
                benefits_table.style = "Table Grid"
                hdr_Cells = benefits_table.rows[0].cells
                hdr_Cells[5].text = "م"
                hdr_Cells[4].text = "اسم الصنف"
                hdr_Cells[3].text = "الكود"
                hdr_Cells[2].text = "الوحدة"
                hdr_Cells[1].text = "السعر"
                hdr_Cells[0].text = "الحالة"

                for cell in hdr_Cells:
                    self.set_arabic_format(cell)

                b = 0
                
                for i in items:
                    b+=1   
                    row_Cells = benefits_table.add_row().cells
                    row_Cells[0].size = docx.shared.Pt(15)
                    row_Cells[1].size = docx.shared.Pt(15)
                    row_Cells[2].size = docx.shared.Pt(15)
                    row_Cells[3].size = docx.shared.Pt(15)
                    row_Cells[4].size = docx.shared.Pt(15)
                    row_Cells[5].size = docx.shared.Pt(15)

                    row_Cells[5].text = str(b)
                    row_Cells[4].text = str(i[0])
                    row_Cells[3].text = str(i[1])
                    row_Cells[2].text = str(i[2])
                    row_Cells[1].text = str(i[3])
                    row_Cells[0].text = str(i[4])

                    for cell in row_Cells:
                        self.set_arabic_format(cell)

                widths = (docx.shared.Inches(4), docx.shared.Inches(4), docx.shared.Inches(4), docx.shared.Inches(4), docx.shared.Inches(4),docx.shared.Inches(0.5))
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

                doc.save(f"{filePath}\جميع الأصناف.docx")

            if self.formatComboBox.currentText() == "Pdf":
                with suppress_output():
                    convert(f"{filePath}\جميع الأصناف.docx",f"{filePath}\جميع الأصناف.pdf")

                os.remove(f"{filePath}\جميع الأصناف.docx")

            message = QMessageBox(parent=self,text="تم التصدير بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
    def changeBackgroundColorsToItemsTable(self):
        for row in range(self.itemsTable.rowCount()):
            if self.itemsTable.item(row,4).text() == 'تالف':
                for col in range(self.itemsTable.columnCount()):
                    self.itemsTable.item(row,col).setBackground(QColor(255,0,0))
            elif self.itemsTable.item(row,4).text() == 'تم البيع':
                for col in range(self.itemsTable.columnCount()):
                    self.itemsTable.item(row,col).setBackground(QColor(0,255,0))
    def loadItems(self):
        self.itemsTable.setRowCount(0)
        if self.comboStatusBoxWareHouse.currentText() != 'الكل':
            cr.execute(f"SELECT * FROM items WHERE condition='{self.comboStatusBoxWareHouse.currentText()}'")
        else:
            cr.execute("SELECT * FROM items")
        tempThing = [] 
        for i in cr.fetchall():
            tempThing.append(i)
        for row,i in enumerate(tempThing):
            self.itemsTable.insertRow(self.itemsTable.rowCount())
            for col,val in enumerate(i):                    
                self.itemsTable.setItem(row,col,QTableWidgetItem(str(val)))
        self.changeBackgroundColorsToItemsTable()
    def showItemsInTrucks(self):
        try:
            self.showItemsInTrucksFrame.deleteLater()
        except:
            pass

        self.showItemsInTrucksFrame = QFrame(self.wareHouseFrame)
        self.showItemsInTrucksFrame.setGeometry((self.wareHouseFrame.width()-500)//2,(self.wareHouseFrame.height()-450)//2,320,450)
        # self.showTrucksNoteFrame.setStyleSheet("background-color:white;border:2px solid black")
        self.ItemIdShowItemsInTrucks = self.itemsTable.item(self.itemsTable.selectedIndexes()[0].row(),1).text()

        closeButton = QPushButton(self.showItemsInTrucksFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(270,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.showItemsInTrucksFrame:self.destroyFrame(frame))

        self.showItemsInTrucksFrame.setStyleSheet("background-color:white")

        self.itemsInTruksTable = QTableWidget(self.showItemsInTrucksFrame)
        self.itemsInTruksTable.setGeometry(10,60,250,240)

        self.itemsInTruksTable.setColumnCount(2)
        self.itemsInTruksTable.setHorizontalHeaderLabels(["رقم الشاحنة/التيدر","نوع المركبة"])
        self.itemsInTruksTable.setColumnWidth(0,150)
        self.itemsInTruksTable.setColumnWidth(1,80)

        self.itemsInTruksTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.itemsInTruksTable.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.itemsInTruksTable.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)

        #End minMenu Buttons style
        self.loadItemsInTrucks()
        self.showItemsInTrucksFrame.show()
    def loadItemsInTrucks(self):
        self.itemsInTruksTable.setRowCount(0)     
        trucksIds= []
        bigTrucksIds = []
        tempThing = []

        cr.execute("SELECT truckId FROM trucksParts WHERE itemId=?",[self.ItemIdShowItemsInTrucks])
        for i in cr.fetchall():
            trucksIds.append(i[0])


        for truckId in trucksIds:
            cr.execute("SELECT carNumber FROM trucks WHERE id=?",[truckId])
            val = list(cr.fetchall()[0])
            val.append("شاحنة")
            tempThing.append(val)

        cr.execute("SELECT bigTruckId FROM bigTrucksParts WHERE itemId=?",[self.ItemIdShowItemsInTrucks])
        for i in cr.fetchall():
            bigTrucksIds.append(i[0])


        for bigTruckId in bigTrucksIds:
            cr.execute("SELECT number FROM bigTrucks WHERE id=?",[bigTruckId])
            val = list(cr.fetchall()[0])
            val.append("تيدر")
            tempThing.append(val)

        for row,i in enumerate(tempThing):
            self.itemsInTruksTable.insertRow(self.itemsInTruksTable.rowCount())
            for col,val in enumerate(i):
                self.itemsInTruksTable.setItem(row,col,QTableWidgetItem(str(val))) 
    def destroyFrame(self,frame):
        for i in frame.children():
            i.deleteLater()

        frame.destroy()
        frame.deleteLater()
