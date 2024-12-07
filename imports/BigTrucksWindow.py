from .stuff import *

class BigTrucksWindow():
    def showBigTrucks(self):
        try:
            self.destroyFrame(self.mainMenuBigTrucksFrame)
            self.destroyFrame(self.bigTrucksFrame)
        except:
            pass
        self.bigTrucksFrame = QFrame(self.mainFrame)
        self.closeButtonBigTrucksFrame = QPushButton(self.bigTrucksFrame)
        self.closeButtonBigTrucksFrame.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        self.closeButtonBigTrucksFrame.clicked.connect(lambda x, frame=self.bigTrucksFrame:self.destroyFrame(frame))

        self.comboSearchBigTrucksBox = QComboBox(self.bigTrucksFrame)
        self.comboSearchBigTrucksBox.setGeometry(300,30,150,20)
        self.comboSearchBigTrucksBox.addItems(["الكل", "رقم التيدر"])
        self.comboSearchBigTrucksBox.activated.connect(self.addSearchBigTrucksEntries)

        self.bigTrucksFrame.setStyleSheet("background-color:white")

        self.bigTrucksTable = QTableWidget(self.bigTrucksFrame)

        self.bigTrucksTable.setColumnCount(4)
        self.bigTrucksTable.setHorizontalHeaderLabels(["id","رقم التيدر","نوعه","الشاحنة المرتبطة"])
        
        self.bigTrucksTable.setColumnHidden(0,True)

        self.bigTrucksTable.setColumnWidth(1, 80)
        self.bigTrucksTable.setColumnWidth(2, 80)
        self.bigTrucksTable.setColumnWidth(3,150)

        self.contextMenubigTrucksTable = QMenu(self.bigTrucksTable)
        self.contextMenubigTrucksTable.setStyleSheet("background-color:grey")
        self.createButtonbigTrucksTable()

        self.bigTrucksTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.bigTrucksTable.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.bigTrucksTable.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.bigTrucksTable.customContextMenuRequested.connect(self.showMenubigTrucksTable)

        #Start minMenu Buttons style
        self.mainMenuBigTrucksFrame = QFrame(self.bigTrucksFrame)
        self.mainMenuBigTrucksFrame.setStyleSheet("background-color:white;border:2px solid black")
        
        label = QLabel(self.mainMenuBigTrucksFrame,text="القائمة الرئيسيه")
        label.setStyleSheet("background-color:white;border-bottom:none;font: 14pt 'Arial';")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setGeometry(0,0,181,31)

        addTruckButton = QPushButton(self.mainMenuBigTrucksFrame,text="اضافة تيدر")
        addTruckButton.setGeometry(0,50,181,31)
        addTruckButton.setStyleSheet("QPushButton {background-color:white;border:2px solid black;font: 14pt 'Arial';} QPushButton:hover {background-color:#c8c8c8;}")
        addTruckButton.clicked.connect(self.addBigTruck)

        exportBigTruckReportButton = QPushButton(self.mainMenuBigTrucksFrame,text="تصدير تقرير للتيادر")
        exportBigTruckReportButton.setGeometry(0,90,181,31)
        exportBigTruckReportButton.setStyleSheet("QPushButton {background-color:white;border:2px solid black;font: 14pt 'Arial';} QPushButton:hover {background-color:#c8c8c8;}")
        exportBigTruckReportButton.clicked.connect(self.exportBigTruckReportMoney)

        #End minMenu Buttons style

        self.putBigTrucksFrameAndStuff()
        
        self.loadBigTrucks()
        self.bigTrucksFrame.show()
    def putBigTrucksFrameAndStuff(self):

        
        if self.width() <= 995 or self.height() <= 680:
            self.bigTrucksFrame.setGeometry((self.width()-550)//2,(self.mainFrame.height()-610)//2,550,610)
            self.bigTrucksTable.setGeometry(10,60,320,541)
            self.mainMenuBigTrucksFrame.setGeometry(350,60,181,161)
            self.closeButtonBigTrucksFrame.setGeometry(510,10,41,31)
        else:
            self.bigTrucksFrame.setGeometry(30,30,self.mainFrame.width()-60,self.mainFrame.height()-60)
            self.bigTrucksTable.setGeometry(10,60,self.bigTrucksFrame.width() - 206,self.bigTrucksFrame.height()-100)
            self.mainMenuBigTrucksFrame.setGeometry(self.bigTrucksTable.width() + 20,60,181,161)
            self.closeButtonBigTrucksFrame.setGeometry(self.bigTrucksTable.width() + 20 + 140,10,41,31)

        deserve = self.bigTrucksTable.columnCount() - 1
        for i in range(self.bigTrucksTable.columnCount()):
            self.bigTrucksTable.setColumnWidth(i, (self.bigTrucksTable.width() - 20) // deserve)
            
        self.bigTrucksFrame.show()
        self.bigTrucksTable.show()
        self.mainMenuBigTrucksFrame.show()
        self.closeButtonBigTrucksFrame.show()
    def exportBigTruckReportMoney(self):
        try:
            self.destroyFrame(self.exportBigTruckReportFrame)
        except:
            pass

        arabic_locale = QLocale(QLocale.Language.Arabic, QLocale.Country.SaudiArabia)

        self.exportBigTruckReportFrame = QFrame(parent=self.mainFrame)
        self.exportBigTruckReportFrame.setGeometry((self.mainFrame.width()-210)//2,(self.mainFrame.height()-230)//2,210,230)
        self.exportBigTruckReportFrame.setStyleSheet("background-color:white;border:2px solid black")

        closeButton = QPushButton(self.exportBigTruckReportFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:8px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 18px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(160,10,31,21)
        closeButton.clicked.connect(lambda x, frame=self.exportBigTruckReportFrame:self.destroyFrame(frame))

        label = QLabel(parent=self.exportBigTruckReportFrame,text="من تاريخ")
        label.setStyleSheet('font: 18pt "Arial";border:none')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.move(50,50)

        self.fromDateExportBigTruck = QDateEdit(parent=self.exportBigTruckReportFrame)
        self.fromDateExportBigTruck.setCalendarPopup(True)
        self.fromDateExportBigTruck.setDisplayFormat("yyyy/MM/dd")

        self.todayButtonFromDateBigTruck = QPushButton("اليوم",clicked=lambda:self.fromDateExportBigTruck.calendarWidget().setSelectedDate(QDate().currentDate()))
        self.todayButtonFromDateBigTruck.setStyleSheet("background-color:green;")

        self.fromDateExportBigTruck.setLocale(arabic_locale)
        self.fromDateExportBigTruck.setFont(QFont("Arial",12))
        self.fromDateExportBigTruck.setStyleSheet("background-color:white;color:black")
        
        self.fromDateExportBigTruck.calendarWidget().layout().addWidget(self.todayButtonFromDateBigTruck)
        self.fromDateExportBigTruck.calendarWidget().setSelectedDate(QDate().currentDate())
        self.fromDateExportBigTruck.setGeometry(20,80,160,31)

        label = QLabel(parent=self.exportBigTruckReportFrame,text="الى تاريخ")
        label.setStyleSheet('font: 18pt "Arial";border:none')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.move(50,120)

        self.toDateExportBigTruck = QDateEdit(parent=self.exportBigTruckReportFrame)
        self.toDateExportBigTruck.setCalendarPopup(True)
        self.toDateExportBigTruck.setDisplayFormat("yyyy/MM/dd")

        self.todayButtonToDateBigTruck = QPushButton("اليوم",clicked=lambda:self.toDateExportBigTruck.calendarWidget().setSelectedDate(QDate().currentDate()))
        self.todayButtonToDateBigTruck.setStyleSheet("background-color:green;")

        self.toDateExportBigTruck.setLocale(arabic_locale)
        self.toDateExportBigTruck.setFont(QFont("Arial",12))
        self.toDateExportBigTruck.setStyleSheet("background-color:white;color:black")
        
        self.toDateExportBigTruck.calendarWidget().layout().addWidget(self.todayButtonToDateBigTruck)
        self.toDateExportBigTruck.calendarWidget().setSelectedDate(QDate().currentDate())
        self.toDateExportBigTruck.setGeometry(20,150,160,31)

        exportButton = QPushButton(parent=self.exportBigTruckReportFrame,text="تصدير")
        exportButton.setGeometry(50,190,101,31)
        exportButton.setStyleSheet("QPushButton:hover {background-color:#c8c8c8;}")
        exportButton.clicked.connect(self.completeExportBigTrucksReport)


        self.exportBigTruckReportFrame.show()
    def completeExportBigTrucksReport(self):
        filePath = QFileDialog.getExistingDirectory(self,"Select a Directory")
        if len(filePath) > 0:
            valuesToWrite = []
            totalPriceToWrite = 0
            fromDate = str(self.fromDateExportBigTruck.text()).split("/")
            fromDateGoodFormat = date(int(fromDate[0]),int(fromDate[1]),int(fromDate[2]))

            toDate = str(self.toDateExportBigTruck.text()).split("/")
            toDateGoodFormat = date(int(toDate[0]),int(toDate[1]),int(toDate[2]))

            #[itemPrice,itemName, installDate, bigTruckNumber]

            cr.execute("SELECT itemName,itemPrice,installDate,bigTruckId FROM bigTrucksParts")
            for i in cr.fetchall():
                date1 = str(i[2]).split("/")
                date2 = date(int(date1[0]),int(date1[1]),int(date1[2]))

                if date2>= fromDateGoodFormat and date2<=toDateGoodFormat:
                    cr.execute("SELECT number FROM bigTrucks WHERE id=?",[i[3]])
                    valuesToWrite.append([i[0],str(round(float(i[1]),2)),i[2],cr.fetchone()[0]])
                    totalPriceToWrite+=round(float(i[1]),2)
            
            cr.execute("SELECT itemName,itemPrice,installDate,bigTruckId FROM bigTrucksToOil")
            for i in cr.fetchall():
                date1 = str(i[2]).split("/")
                date2 = date(int(date1[0]),int(date1[1]),int(date1[2]))

                if date2>= fromDateGoodFormat and date2<=toDateGoodFormat:
                    cr.execute("SELECT number FROM bigTrucks WHERE id=?",[i[3]])
                    valuesToWrite.append([i[0],str(round(float(i[1]),2)),i[2],cr.fetchone()[0]])
                    totalPriceToWrite+=round(float(i[1]),2)

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

            #[itemPrice,itemName, installDate, bigTruckNumber]

            hdr_Cells[4].text = "م"
            hdr_Cells[3].text = "اسم الصنف"
            hdr_Cells[2].text = "سعر الصنف"
            hdr_Cells[1].text = "تاريخ التركيب"
            hdr_Cells[0].text = "رقم التيدر"

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
            para = doc.add_paragraph().add_run(f"اجمالي الصرف على التيادر:{round(totalPriceToWrite,2)}")
            para.font.name = "Arial"
            para.font.size = docx.shared.Pt(20)
            
            doc.save(f"{filePath}\تقرير التيادر.docx")
            with suppress_output():
                convert(f"{filePath}\تقرير التيادر.docx",f"{filePath}\تقرير التيادر.pdf")
            os.remove(f"{filePath}\تقرير التيادر.docx")

            message = QMessageBox(parent=self,text="تم التصدير بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
    def addSearchBigTrucksEntries(self):
        try:
            self.searchEntryBigTruck.destroy()
            self.searchEntryBigTruck.hide()
        except:
            pass
        if self.comboSearchBigTrucksBox.currentText() == "الكل":
            self.loadBigTrucks()
        else:
            self.searchEntryBigTruck = QLineEdit(self.bigTrucksFrame)
            self.searchEntryBigTruck.textChanged.connect(self.searchBigTrucksFun)
            self.searchEntryBigTruck.setGeometry(80,30,150,20)
            self.searchEntryBigTruck.show()
    def searchBigTrucksFun(self):
        if len(self.searchEntryBigTruck.text())==0:
            self.loadBigTrucks()
        else:
            self.bigTrucksTable.setRowCount(0)
            tempThing = [] 
            cr.execute("SELECT number From bigTrucks")
            choices = cr.fetchall()
            posiple = []
            for o in choices:
                for n,i in enumerate(o):
                    try:
                        if o[n][:len(self.searchEntryBigTruck.text())]==self.searchEntryBigTruck.text():
                                if i not in posiple:
                                    posiple.append(i)
                    except:
                        pass

            for p in posiple:
                cr.execute("SELECT * FROM bigTrucks WHERE number = ?", [p])
                for i in cr.fetchall():
                    i = list(i)
                    cr.execute("SELECT truckNumber FROM bigTruckToTruck WHERE bigTruckId=?",[i[0]])
                    tempNumberTruck = cr.fetchone()
                    if tempNumberTruck!=None:
                        i.append(tempNumberTruck[0])
                    else:
                        i.append('لايوجد')
                    tempThing.append(i)

            for row,i in enumerate(tempThing):
                self.bigTrucksTable.insertRow(self.bigTrucksTable.rowCount())
                for col,val in enumerate(i):
                    self.bigTrucksTable.setItem(row,col,QTableWidgetItem(str(val)))
    def addBigTruck(self):
        try:
            self.destroyFrame(self.addBigTruckFrame)
        except:
            pass

        self.addBigTruckFrame = QFrame(self.mainFrame)
        self.addBigTruckFrame.setGeometry((self.mainFrame.width()-350)//2,(self.mainFrame.height()-506)//2,350,506)
        self.addBigTruckFrame.setStyleSheet("background-color:white;border:2px solid black")

        closeButton = QPushButton(self.addBigTruckFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(300,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.addBigTruckFrame:self.destroyFrame(frame))
        
        #Start scrolAria

        self.frame = QFrame()

        layout = QVBoxLayout()
        self.frame.setLayout(layout)

        label = QLabel("رقم التيدر")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")
        self.bigTruckNumberEntry = QLineEdit()

        layout.addWidget(label)
        layout.addWidget(self.bigTruckNumberEntry)

        label = QLabel("نوعه")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")
        self.bigTruckTypeEntry = QLineEdit()

        layout.addWidget(label)
        layout.addWidget(self.bigTruckTypeEntry)


        addButton = QPushButton(text="اضافة")
        addButton.clicked.connect(self.completeAddBigTruck)
        addButton.setStyleSheet("QPushButton:hover {background-color:#c8c8c8;}")        

        layout.addWidget(addButton)

        self.scroolAria = QScrollArea(self.addBigTruckFrame)
        self.scroolAria.setWidget(self.frame)
        self.scroolAria.setStyleSheet("border:1px solid gray")
        self.scroolAria.move(20,50)
        self.scroolAria.resize(321,431)

        self.scroolAria.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)


        self.scroolAria.setWidgetResizable(True)


        #End scrolAria
        self.addBigTruckFrame.show()
    def completeAddBigTruck(self):
        if len(self.bigTruckNumberEntry.text()) > 0 and len(self.bigTruckTypeEntry.text()) > 0:
            cr.execute("INSERT INTO bigTrucks (number,type) values (?,?)",(self.bigTruckNumberEntry.text(),self.bigTruckTypeEntry.text()))
            con.commit()
            message = QMessageBox(parent=self,text="تمت الاضافة بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
            self.loadBigTrucks()
        else:
            message = QMessageBox(parent=self,text="يرجى تعبئة جميع الحقول")
            message.setIcon(QMessageBox.Icon.Critical)
            message.setWindowTitle("فشل")
            message.exec()
    def showMenubigTrucksTable(self,position):
        indexes = self.bigTrucksTable.selectedIndexes()
        for index in indexes:
            self.contextMenubigTrucksTable.exec(self.bigTrucksTable.viewport().mapToGlobal(position))
    def createButtonbigTrucksTable(self):
        deleteBugTruckButton = QAction(self.bigTrucksTable)
        deleteBugTruckButton.setIcon(QIcon("assests/trash.png"))
        deleteBugTruckButton.setText("حذف")
        deleteBugTruckButton.setFont(QFont("Arial" , 12))
        deleteBugTruckButton.triggered.connect(self.deleteBigTruck)

        editBigTruckButton = QAction(self.bigTrucksTable)
        editBigTruckButton.setIcon(QIcon("assests/edit.png"))
        editBigTruckButton.setText("تعديل")
        editBigTruckButton.setFont(QFont("Arial" , 12))
        editBigTruckButton.triggered.connect(self.editBigTruck)

        addBigTruckToATruckButton = QAction(self.bigTrucksTable)
        addBigTruckToATruckButton.setText("اضافة لشاحنة")
        addBigTruckToATruckButton.setFont(QFont("Arial" , 12))
        addBigTruckToATruckButton.triggered.connect(self.addBigTruckToATruck)

        addNoteButton = QAction(self.bigTrucksTable)
        addNoteButton.setIcon(QIcon("assests/addNote.png"))
        addNoteButton.setText("اضافة ملاحظة")
        addNoteButton.setFont(QFont("Arial" , 12))
        addNoteButton.triggered.connect(self.showBigTrucksNote)   

        removeTruckFromBigTruck = QAction(self.bigTrucksTable)
        removeTruckFromBigTruck.setText("حذف شاحنة من تيدر")
        removeTruckFromBigTruck.setFont(QFont("Arial" , 12))
        removeTruckFromBigTruck.triggered.connect(self.removeTruckFromBigTruck)

        showPartsButton = QAction(self.bigTrucksTable)
        showPartsButton.setText("اظهار القطع")
        showPartsButton.setFont(QFont("Arial" , 12))
        showPartsButton.triggered.connect(self.showBigTrucksParts)

        self.contextMenubigTrucksTable.addAction(deleteBugTruckButton)
        self.contextMenubigTrucksTable.addAction(editBigTruckButton)
        self.contextMenubigTrucksTable.addAction(addBigTruckToATruckButton)
        self.contextMenubigTrucksTable.addAction(showPartsButton)
        self.contextMenubigTrucksTable.addAction(removeTruckFromBigTruck)
        self.contextMenubigTrucksTable.addAction(addNoteButton)
    def loadItemToBigTrucks(self,bigTruckId):
        self.totalPriceVarBigTruck = 0
        self.bigTrucksPartsTable.setRowCount(0)     
        cr.execute("SELECT itemName,itemId,itemPrice,installPlace,installDate FROM bigTrucksParts WHERE truckId = ?",[bigTruckId])
        tempThing = [] 
        for i in cr.fetchall():
            i = list(i)
            i.append("item")
            tempThing.append(i)

        cr.execute("SELECT itemName,oilCode,itemPrice,installPlace,installDate FROM bigTrucksToOil WHERE truckId = ?",[bigTruckId])
        for i in cr.fetchall():
            i = list(i)
            i.append("oil")
            tempThing.append(i)

        for row,i in enumerate(tempThing):
            self.bigTrucksPartsTable.insertRow(self.bigTrucksPartsTable.rowCount())
            for col,val in enumerate(i):
                if col==2:
                    self.totalPriceVarBigTruck+=float(val)
                self.bigTrucksPartsTable.setItem(row,col,QTableWidgetItem(str(val))) 
        self.totalPriceVarBigTruck = round(self.totalPriceVarBigTruck,2)
        self.totalPriceTruck.setText(f"اجمالي الصرف على التيدر:{self.totalPriceVarBigTruck}")
    def showBigTrucksNote(self):
        try:
            self.showBigTrucksNoteFrame.deleteLater()
        except:
            pass
        self.BigtruckIdAddNote = self.bigTrucksTable.item(self.bigTrucksTable.selectedIndexes()[0].row(),0).text()
        
        self.showBigTrucksNoteFrame = QFrame(self.bigTrucksFrame)
        self.showBigTrucksNoteFrame.setGeometry((self.bigTrucksFrame.width()-450)//2,(self.bigTrucksFrame.height()-400)//2,450,400)
        # self.showTrucksNoteFrame.setStyleSheet("background-color:white;border:2px solid black")
        
        closeButton = QPushButton(self.showBigTrucksNoteFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(400,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.showBigTrucksNoteFrame:self.destroyFrame(frame))

        self.showBigTrucksNoteFrame.setStyleSheet("background-color:white")

        self.notesTableBigTrucks = QTableWidget(self.showBigTrucksNoteFrame)
        self.notesTableBigTrucks.setGeometry(10,60,410,240)

        self.notesTableBigTrucks.setColumnCount(3)
        self.notesTableBigTrucks.setHorizontalHeaderLabels(["id","الملاحظة", "تاريخ الملاحظة"])
        self.notesTableBigTrucks.setColumnHidden(0,True)
        self.notesTableBigTrucks.setColumnWidth(1, 300)


        self.contextMenuNotesTableBigTrucks = QMenu(self.notesTableBigTrucks)
        self.contextMenuNotesTableBigTrucks.setStyleSheet("background-color:grey")
        self.createButtondBigTrucksNotesTable()

        self.notesTableBigTrucks.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.notesTableBigTrucks.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.notesTableBigTrucks.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.notesTableBigTrucks.customContextMenuRequested.connect(self.showMenunotesTableBigTrucks)
        
        addNoteButton = QPushButton("اضافة ملاحظة",self.showBigTrucksNoteFrame)
        addNoteButton.setStyleSheet("QPushButton {border:2px solid black;font:14pt 'Arial'}QPushButton:hover {background-color:#c8c8c8;}")        
        addNoteButton.setGeometry(120,310,180,31)
        addNoteButton.clicked.connect(self.addNoteBigTruck)

        #End minMenu Buttons style
        self.loadBigTrucksNotes(self.BigtruckIdAddNote)
        self.showBigTrucksNoteFrame.show()
    def createButtondBigTrucksNotesTable(self):
        deleteNoteButton = QAction(self.notesTableBigTrucks)
        deleteNoteButton.setIcon(QIcon("assests/deleteNote.png"))
        deleteNoteButton.setText("حذف")
        deleteNoteButton.setFont(QFont("Arial" , 12))
        deleteNoteButton.triggered.connect(self.deleteBigTruckNote)

        editNoteButton = QAction(self.notesTableBigTrucks)
        editNoteButton.setIcon(QIcon("assests/edit.png"))
        editNoteButton.setText("تعديل")
        editNoteButton.setFont(QFont("Arial" , 12))
        editNoteButton.triggered.connect(self.editBigTruckNote)
        
        self.contextMenuNotesTableBigTrucks.addAction(deleteNoteButton)
        self.contextMenuNotesTableBigTrucks.addAction(editNoteButton)
    def showMenunotesTableBigTrucks(self,position):
        indexes = self.notesTableBigTrucks.selectedIndexes()
        for index in indexes:
            self.contextMenuNotesTableBigTrucks.exec(self.notesTableBigTrucks.viewport().mapToGlobal(position))
    def deleteBigTruckNote(self):
        noteIdDelete = self.notesTableBigTrucks.item(self.notesTableBigTrucks.selectedIndexes()[0].row(),0).text()
        d = QMessageBox(parent=self,text=f"تأكيد حذف الملاحظة")
        d.setIcon(QMessageBox.Icon.Information)
        d.setWindowTitle("تأكيد")
        d.setStyleSheet("background-color:white")
        d.setStandardButtons(QMessageBox.StandardButton.Cancel|QMessageBox.StandardButton.Ok)
        important = d.exec()
        if important == QMessageBox.StandardButton.Ok:
            cr.execute("DELETE FROM bigTrucksNotes WHERE id=?",[noteIdDelete])
            con.commit()
            self.loadBigTrucksNotes(self.BigtruckIdAddNote)
            d = QMessageBox(parent=self,text="تم الحذف بنجاح")
            d.setWindowTitle("نجاح")
            d.setIcon(QMessageBox.Icon.Information)
            d.setStyleSheet("background-color:white")
            ret = d.exec()
    def editBigTruckNote(self):
        self.noteIdEdit = self.notesTableBigTrucks.item(self.notesTableBigTrucks.selectedIndexes()[0].row(),0).text()
        try:
            self.editNoteFrame.deleteLater()
        except:
            pass
        self.editNoteFrame = QFrame(self.bigTrucksFrame)
        self.editNoteFrame.setGeometry((self.bigTrucksFrame.width()-340)//2,(self.bigTrucksFrame.height()-360)//2,340,360)
        # self.showTrucksNoteFrame.setStyleSheet("background-color:white;border:2px solid black")

        closeButton = QPushButton(self.editNoteFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(290,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.editNoteFrame:self.destroyFrame(frame))

        self.editNoteFrame.setStyleSheet("background-color:white;border: 2px solid black")


        label = QLabel('الملاحظة',self.editNoteFrame)
        label.setStyleSheet("border:0px")
        label.move(150,20)
        label.setFont(QFont("Arial", 16))

        self.notesText = QTextEdit(self.editNoteFrame)
        self.notesText.setGeometry(10,60,320,150)

        label = QLabel('تاريخ الملاحظة',self.editNoteFrame)
        label.setStyleSheet("border:0px")
        label.move(120,230)
        label.setFont(QFont("Arial", 16))

        arabic_locale = QLocale(QLocale.Language.Arabic, QLocale.Country.SaudiArabia)
        
        self.noteDateEntry = QDateEdit(self.editNoteFrame)


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

        cr.execute("SELECT note, date FROM bigTrucksNotes WHERE id=?",[self.noteIdEdit])
        values = cr.fetchall()[0]
        self.notesText.setText(values[0])
        noteDate = str(values[1]).split("/")
        self.noteDateEntry.setDate(QDate(int(noteDate[0]), int(noteDate[1]), int(noteDate[2])))

        completeEditNoteButton = QPushButton("تعديل ملاحظة",self.editNoteFrame)
        completeEditNoteButton.setStyleSheet("QPushButton {border:2px solid black;font:14pt 'Arial'}QPushButton:hover {background-color:#c8c8c8;}")        
        completeEditNoteButton.setGeometry(80,310,180,31)
        completeEditNoteButton.clicked.connect(self.completeEditBigTruckNotes)

        #End minMenu Buttons style
        self.editNoteFrame.show()    
    def completeEditBigTruckNotes(self):
        if (len(self.notesText.toPlainText()) > 0): 
            cr.execute("UPDATE bigTrucksNotes set note=?, date=? WHERE id=?",(self.notesText.toPlainText(),self.noteDateEntry.text(),self.noteIdEdit))
            con.commit()
            message = QMessageBox(parent=self,text="تم التعديل بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
            self.loadBigTrucksNotes(self.BigtruckIdAddNote)
        else:
            message = QMessageBox(parent=self,text="يرجى تعبئة جميع الحقول")
            message.setIcon(QMessageBox.Icon.Critical)
            message.setWindowTitle("فشل")
            message.exec()
    def addNoteBigTruck(self):
        try:
            self.addNoteBigTruckFrame.deleteLater()
        except:
            pass
        self.addNoteBigTruckFrame = QFrame(self.bigTrucksFrame)
        self.addNoteBigTruckFrame.setGeometry((self.bigTrucksFrame.width()-340)//2,(self.bigTrucksFrame.height()-360)//2,340,360)
        # self.showTrucksNoteFrame.setStyleSheet("background-color:white;border:2px solid black")

        closeButton = QPushButton(self.addNoteBigTruckFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(290,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.addNoteBigTruckFrame:self.destroyFrame(frame))

        self.addNoteBigTruckFrame.setStyleSheet("background-color:white;border: 2px solid black")


        label = QLabel('الملاحظة',self.addNoteBigTruckFrame)
        label.setStyleSheet("border:0px")
        label.move(150,20)
        label.setFont(QFont("Arial", 16))

        self.notesText = QTextEdit(self.addNoteBigTruckFrame)
        self.notesText.setGeometry(10,60,320,150)

        label = QLabel('تاريخ الملاحظة',self.addNoteBigTruckFrame)
        label.setStyleSheet("border:0px")
        label.move(120,230)
        label.setFont(QFont("Arial", 16))

        arabic_locale = QLocale(QLocale.Language.Arabic, QLocale.Country.SaudiArabia)
        
        self.noteDateEntry = QDateEdit(self.addNoteBigTruckFrame)


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


        completeAddNoteButton = QPushButton("اضافة ملاحظة",self.addNoteBigTruckFrame)
        completeAddNoteButton.setStyleSheet("QPushButton {border:2px solid black;font:14pt 'Arial'}QPushButton:hover {background-color:#c8c8c8;}")        
        completeAddNoteButton.setGeometry(80,310,180,31)
        completeAddNoteButton.clicked.connect(self.completeAddNoteBigTrucks)

        #End minMenu Buttons style
        self.loadBigTrucksNotes(self.BigtruckIdAddNote)
        self.addNoteBigTruckFrame.show()
    def completeAddNoteBigTrucks(self):
        if (len(self.notesText.toPlainText()) > 0): 
            cr.execute("INSERT INTO bigTrucksNotes (bigTruckId,note,date) VALUES (?,?,?)",(self.BigtruckIdAddNote, self.notesText.toPlainText(), self.noteDateEntry.text()))
            con.commit()
            message = QMessageBox(parent=self,text="تمت الاضافة بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
            self.loadBigTrucksNotes(self.BigtruckIdAddNote)
        else:
            message = QMessageBox(parent=self,text="يرجى تعبئة جميع الحقول")
            message.setIcon(QMessageBox.Icon.Critical)
            message.setWindowTitle("فشل")
            message.exec()
    def loadBigTrucksNotes(self,BigtruckId):
        self.notesTableBigTrucks.setRowCount(0)     
        cr.execute("SELECT id,note,date FROM bigTrucksNotes WHERE bigTruckId = ?",[BigtruckId])
        tempThing = [] 
        for i in cr.fetchall():
            tempThing.append(i)
        for row,i in enumerate(tempThing):
            self.notesTableBigTrucks.insertRow(self.notesTableBigTrucks.rowCount())
            for col,val in enumerate(i):
                self.notesTableBigTrucks.setItem(row,col,QTableWidgetItem(str(val))) 
    def deleteBigTruck(self):
        bigTruckIdDelete = self.bigTrucksTable.item(self.bigTrucksTable.selectedIndexes()[0].row(),0).text()
        d = QMessageBox(parent=self,text=f"تأكيد حذف {self.bigTrucksTable.item(self.bigTrucksTable.selectedIndexes()[0].row(),1).text()}")
        d.setIcon(QMessageBox.Icon.Information)
        d.setWindowTitle("تأكيد")
        d.setStyleSheet("background-color:white")
        d.setStandardButtons(QMessageBox.StandardButton.Cancel|QMessageBox.StandardButton.Ok)
        important = d.exec()
        if important == QMessageBox.StandardButton.Ok:
            cr.execute("DELETE FROM bigTrucks WHERE id=?",[bigTruckIdDelete])
            cr.execute("DELETE FROM bigTruckToTruck WHERE bigTruckId=?",[bigTruckIdDelete])
            cr.execute("DELETE FROM bigTrucksNotes WHERE bigTruckId=?",[bigTruckIdDelete])
            cr.execute("DELETE FROM bigTrucksParts WHERE bigTruckId=?",[bigTruckIdDelete])
            cr.execute("DELETE FROM bigTrucksToOil WHERE bigTruckId=?",[bigTruckIdDelete])
            con.commit()
            self.loadBigTrucks()
            d = QMessageBox(parent=self,text="تم الحذف بنجاح")
            d.setWindowTitle("نجاح")
            d.setIcon(QMessageBox.Icon.Information)
            d.setStyleSheet("background-color:white")
            ret = d.exec()
    def editBigTruck(self):
        try:
            self.destroyFrame(self.editBigTruckFrame)
        except:
            pass
        
        self.editBigTruckId = self.bigTrucksTable.item(self.bigTrucksTable.selectedIndexes()[0].row(),0).text()

        self.editBigTruckFrame = QFrame(self.mainFrame)
        self.editBigTruckFrame.setGeometry((self.mainFrame.width()-350)//2,(self.mainFrame.height()-506)//2,350,506)
        self.editBigTruckFrame.setStyleSheet("background-color:white;border:2px solid black")

        closeButton = QPushButton(self.editBigTruckFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(300,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.editBigTruckFrame:self.destroyFrame(frame))
        
        #Start scrolAria

        cr.execute("SELECT number,type FROM bigTrucks WHERE id=?",[self.editBigTruckId])
        values = cr.fetchone()
        self.frame = QFrame()

        layout = QVBoxLayout()
        self.frame.setLayout(layout)

        label = QLabel("رقم التيدر")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")
        self.bigTruckNumberEntry = QLineEdit()
        self.bigTruckNumberEntry.setText(values[0])
        self.bigTruckNumberEntry.setDisabled(True)
        
        layout.addWidget(label)
        layout.addWidget(self.bigTruckNumberEntry)

        label = QLabel("نوعه")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")
        self.bigTruckTypeEntry = QLineEdit()
        self.bigTruckTypeEntry.setText(values[1])
        
        layout.addWidget(label)
        layout.addWidget(self.bigTruckTypeEntry)


        addButton = QPushButton(text="تعديل")
        addButton.clicked.connect(self.completeEditBigTruck)
        addButton.setStyleSheet("QPushButton:hover {background-color:#c8c8c8;}")        

        layout.addWidget(addButton)

        self.scroolAria = QScrollArea(self.editBigTruckFrame)
        self.scroolAria.setWidget(self.frame)
        self.scroolAria.setStyleSheet("border:1px solid gray")
        self.scroolAria.move(20,50)
        self.scroolAria.resize(321,431)

        self.scroolAria.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)


        self.scroolAria.setWidgetResizable(True)


        #End scrolAria
        self.editBigTruckFrame.show()
    def completeEditBigTruck(self):
        if len(self.bigTruckNumberEntry.text()) > 0 and len(self.bigTruckTypeEntry.text()) > 0:
            cr.execute("UPDATE bigTrucks SET number=?, type=? WHERE id=?",[self.bigTruckNumberEntry.text(),self.bigTruckTypeEntry.text(),self.editBigTruckId])
            con.commit()
            message = QMessageBox(parent=self,text="تمت التعديل بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
            self.loadBigTrucks()
        else:
            message = QMessageBox(parent=self,text="يرجى تعبئة جميع الحقول")
            message.setIcon(QMessageBox.Icon.Critical)
            message.setWindowTitle("فشل")
            message.exec()
    def addBigTruckToATruck(self):
        try:
            self.destroyFrame(self.addBigTruckToTruckFrame)
        except:
            pass

        self.bigTruckIdAddBigTruckToTruck = self.bigTrucksTable.item(self.bigTrucksTable.selectedIndexes()[0].row(),0).text()
        self.currentIdTruckToAddBigTruck = None
        
        cr.execute("SELECT truckNumber FROM bigTruckToTruck WHERE bigTruckId = ?",[self.bigTruckIdAddBigTruckToTruck])

        if len(cr.fetchall()) != 0:
            message = QMessageBox(parent=self,text="التيدر مركب بشاحنة بالفعل")
            message.setIcon(QMessageBox.Icon.Critical)
            message.setWindowTitle("فشل")
            message.exec()
            return

        self.addBigTruckToTruckFrame = QFrame(self.mainFrame)
        self.addBigTruckToTruckFrame.setGeometry((self.mainFrame.width()-360)//2,(self.mainFrame.height()-300)//2,360,300)
        self.addBigTruckToTruckFrame.setObjectName("addBigTruckToTruckFrame")
        self.addBigTruckToTruckFrame.setStyleSheet("QFrame#addBigTruckToTruckFrame {background-color:white;border:2px solid black}")

        closeButton = QPushButton(self.addBigTruckToTruckFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px;background-color:#fdfdfd}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(323,10,31,31)
        closeButton.clicked.connect(lambda x, frame=self.addBigTruckToTruckFrame:self.destroyFrame(frame))

        label = QLabel(parent=self.addBigTruckToTruckFrame, text="اختر الشاحنة")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font: 14pt 'Arial';background-color:white")
        label.setGeometry(108,40,151,31)

        self.comboBoxChoicesAddBigTruckToTruck = QComboBox(parent=self.addBigTruckToTruckFrame)
        self.comboBoxChoicesAddBigTruckToTruck.setStyleSheet("background-color:#fdfdfd")
        self.comboBoxChoicesAddBigTruckToTruck.addItems(["الكل", "رقم الشاحنة"])
        self.comboBoxChoicesAddBigTruckToTruck.setGeometry(256,70,101,22)
        self.comboBoxChoicesAddBigTruckToTruck.currentIndexChanged.connect(self.addSearchEntryAddBigTruckToTruck)


        self.trucksTableToChoiceBigTrucks = QTableWidget(parent=self.addBigTruckToTruckFrame)
        self.trucksTableToChoiceBigTrucks.setStyleSheet("background-color:white")
        self.trucksTableToChoiceBigTrucks.setColumnCount(4)
        self.trucksTableToChoiceBigTrucks.setColumnHidden(0,True)
        self.trucksTableToChoiceBigTrucks.setColumnWidth(1,40)
        self.trucksTableToChoiceBigTrucks.setColumnWidth(2,140)
        self.trucksTableToChoiceBigTrucks.setColumnWidth(3,140)

        self.trucksTableToChoiceBigTrucks.setHorizontalHeaderLabels(["id", "", "رقم السيارة", "اللوحة"])
        self.trucksTableToChoiceBigTrucks.setGeometry(11,100,346,121)

        addItemToTruckButton = QPushButton(parent=self.addBigTruckToTruckFrame, text="اضافة")
        addItemToTruckButton.setStyleSheet("background-color:#fdfdfd")
        addItemToTruckButton.clicked.connect(self.completeAddBigTruckToATruck)
        addItemToTruckButton.setGeometry(118,260,131,31)

        self.loadAddBigTruckToTruck()
        self.addBigTruckToTruckFrame.show()
    def addSearchEntryAddBigTruckToTruck(self):
        if self.comboBoxChoicesAddBigTruckToTruck.currentText() == "الكل":
            try:
                self.truckNumberEntryAddBigTruckToTruck.destroy()
                self.truckNumberEntryAddBigTruckToTruck.close()
            except:
                pass
            self.loadItemToTrucksWareHouse()
        else:
            try:
                self.truckNumberEntryAddBigTruckToTruck.destroy()
                self.truckNumberEntryAddBigTruckToTruck.close()
            except:
                pass
            self.truckNumberEntryAddBigTruckToTruck = QLineEdit(parent=self.addBigTruckToTruckFrame)
            self.truckNumberEntryAddBigTruckToTruck.textChanged.connect(self.searchTruckToAddBigTruckToTruck)
            self.truckNumberEntryAddBigTruckToTruck.setStyleSheet("background-color:white;")
            self.truckNumberEntryAddBigTruckToTruck.setGeometry(120,70,121,20)
            self.truckNumberEntryAddBigTruckToTruck.show()
    def searchTruckToAddBigTruckToTruck(self):
        if len(self.truckNumberEntryAddBigTruckToTruck.text())==0:
            self.loadAddBigTruckToTruck()
        else:
            self.trucksTableToChoiceBigTrucks.setRowCount(0)
            tempThing = [] 
            cr.execute("SELECT carNumber From trucks")
            choices = cr.fetchall()
            posiple = []
            for o in choices:
                for n,i in enumerate(o):
                    try:
                        if o[n][:len(self.truckNumberEntryAddBigTruckToTruck.text())]==self.truckNumberEntryAddBigTruckToTruck.text():
                                if i not in posiple:
                                    posiple.append(i)
                    except:
                        pass

            for p in posiple:
                cr.execute("SELECT id, carNumber, carPlate FROM trucks WHERE carNumber = ?", [p])
                for i in cr.fetchall():
                    i = list(i)
                    i.insert(1,"")
                    tempThing.append(i)

            for row in range(len(tempThing)):
                self.trucksTableToChoiceBigTrucks.insertRow(self.trucksTableToChoiceBigTrucks.rowCount())
                for col in range(self.trucksTableToChoiceBigTrucks.columnCount()):
                    self.trucksTableToChoiceBigTrucks.setItem(row,col,QTableWidgetItem(str(tempThing[row][col])))
                    if col==1:
                        button = QRadioButton()
                        button.clicked.connect(lambda ch,truckId=tempThing[row][0]:self.changeCurrentTruckIdToAddTruck(truckId))
                        if tempThing[row][0] == self.currentIdTruckToAddBigTruck:
                            button.setChecked(True)
                        self.trucksTableToChoiceBigTrucks.setIndexWidget(self.trucksTableToChoiceBigTrucks.model().index(row,1),button)
    def changeCurrentTruckIdToAddTruck(self,truckId):
        self.currentIdTruckToAddBigTruck = truckId
    def completeAddBigTruckToATruck(self):
        if (self.currentIdTruckToAddBigTruck != None):
            cr.execute("SELECT carNumber FROM trucks WHERE id=?",[self.currentIdTruckToAddBigTruck])
            value = cr.fetchone()[0]
            cr.execute("INSERT INTO bigTruckToTruck (bigTruckId, truckId, truckNumber) VALUES (?,?,?)",(self.bigTruckIdAddBigTruckToTruck, self.currentIdTruckToAddBigTruck, value))
            con.commit()
            message = QMessageBox(parent=self,text="تمت الاضافة بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
            self.loadBigTrucks()
            try:
                for child in self.addBigTruckToTruckFrame.children():
                    child.deleteLater()
                self.addBigTruckToTruckFrame.deleteLater()
            except:
                pass
        else:
            message = QMessageBox(parent=self,text="يرجى تعبئة جميع الحقول")
            message.setIcon(QMessageBox.Icon.Critical)
            message.setWindowTitle("فشل")
            message.exec()
    def loadBigTrucks(self):
        self.bigTrucksTable.setRowCount(0)     
        
        cr.execute("SELECT * FROM bigTrucks")
        tempThing = [] 
        for i in cr.fetchall():
            cr.execute("SELECT truckNumber FROM bigTruckToTruck WHERE bigTruckId=?",[i[0]])
            value = cr.fetchone()
            i = list(i)
            if value!=None:
                i.append(value[0])
            else:
                i.append('لايوجد')
            tempThing.append(i)
            
        for row,i in enumerate(tempThing):
            self.bigTrucksTable.insertRow(self.bigTrucksTable.rowCount())
            for col,val in enumerate(i):
                self.bigTrucksTable.setItem(row,col,QTableWidgetItem(str(val)))
    def loadAddBigTruckToTruck(self):
        self.trucksTableToChoiceBigTrucks.setRowCount(0)
        cr.execute("SELECT id,carNumber,carPlate FROM trucks")
        
        tempThing = []
        for i in cr.fetchall():
            i = list(i)
            i.insert(1,"")
            tempThing.append(i)

        for row in range(len(tempThing)):
            self.trucksTableToChoiceBigTrucks.insertRow(self.trucksTableToChoiceBigTrucks.rowCount())
            for col in range(self.trucksTableToChoiceBigTrucks.columnCount()):
                self.trucksTableToChoiceBigTrucks.setItem(row,col,QTableWidgetItem(str(tempThing[row][col])))
                if col==1:
                    button = QRadioButton()
                    button.clicked.connect(lambda ch,truckId=tempThing[row][0]:self.changeCurrentTruckIdToAddTruck(truckId))
                    if tempThing[row][0] == self.currentIdTruckToAddBigTruck:
                        button.setChecked(True)
                    self.trucksTableToChoiceBigTrucks.setIndexWidget(self.trucksTableToChoiceBigTrucks.model().index(row,1),button)
    def removeTruckFromBigTruck(self):
        bigTruckIdRemoveTruck = self.bigTrucksTable.item(self.bigTrucksTable.selectedIndexes()[0].row(),0).text()
        cr.execute("SELECT truckId FROM bigTruckToTruck")
        if cr.fetchone() == None:
            message = QMessageBox(parent=self,text="لايوجد شاحنة مرتبطة بالتيدر")
            message.setIcon(QMessageBox.Icon.Critical)
            message.setWindowTitle("فشل")
            message.exec()
            return
        d = QMessageBox(parent=self,text=f"تأكيد حذف الشاحنة من التيدر")
        d.setIcon(QMessageBox.Icon.Information)
        d.setWindowTitle("تأكيد")
        d.setStyleSheet("background-color:white")
        d.setStandardButtons(QMessageBox.StandardButton.Cancel|QMessageBox.StandardButton.Ok)
        important = d.exec()
        if important == QMessageBox.StandardButton.Ok:
            cr.execute("DELETE FROM bigTruckToTruck WHERE bigTruckId=?",[bigTruckIdRemoveTruck])
            con.commit()
            self.loadBigTrucks()
            d = QMessageBox(parent=self,text="تم الحذف بنجاح")
            d.setWindowTitle("نجاح")
            d.setIcon(QMessageBox.Icon.Information)
            d.setStyleSheet("background-color:white")
            ret = d.exec()
    def showBigTrucksParts(self):
        try:
            self.showBigTrucksPartsFrame.deleteLater()
        except:
            pass

        self.BigTruckIdToShowItemsToBigTrucks = self.bigTrucksTable.item(self.bigTrucksTable.selectedIndexes()[0].row(),0).text()
        self.BigTruckNumber = self.bigTrucksTable.item(self.bigTrucksTable.selectedIndexes()[0].row(),1).text()

        self.showBigTrucksPartsFrame = QFrame(self.bigTrucksFrame)
        self.showBigTrucksPartsFrame.setGeometry((self.bigTrucksFrame.width()-450)//2,(self.bigTrucksFrame.height()-450)//2,450,450)
        # self.showTrucksNoteFrame.setStyleSheet("background-color:white;border:2px solid black")
        
        closeButton = QPushButton(self.showBigTrucksPartsFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(400,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.showBigTrucksPartsFrame:self.destroyFrame(frame))

        self.showBigTrucksPartsFrame.setStyleSheet("background-color:white")

        self.bigTrucksPartsTable = QTableWidget(self.showBigTrucksPartsFrame)
        self.bigTrucksPartsTable.setGeometry(10,60,410,240)

        self.bigTrucksPartsTable.setColumnCount(6)
        self.bigTrucksPartsTable.setHorizontalHeaderLabels(["اسم الصنف","الكود", "السعر","مكان التركيب","تاريخ التركيب","type"])
        self.bigTrucksPartsTable.setColumnHidden(5,True)

        self.contextMenuBigTrucksPartsTable = QMenu(self.bigTrucksPartsTable)
        self.contextMenuBigTrucksPartsTable.setStyleSheet("background-color:grey")
        self.createButtonBigTrucksPartsTable()

        self.bigTrucksPartsTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.bigTrucksPartsTable.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.bigTrucksPartsTable.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.bigTrucksPartsTable.customContextMenuRequested.connect(self.showMenuNotesBigTrucksPartsTable)

        self.totalPriceVarBigTrucks = 0

        self.totalPriceBigTruck = QLabel(parent=self.showBigTrucksPartsFrame,text=f"اجمالي الصرف على الشاحنة:{self.totalPriceVarBigTrucks}")
        self.totalPriceBigTruck.setStyleSheet('font: 14pt "Arial";border:none')
        self.totalPriceBigTruck.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.totalPriceBigTruck.move(150,340)

        exportTruckReportButton = QPushButton(self.showBigTrucksPartsFrame,text="تصدير التقرير")
        exportTruckReportButton.setGeometry(150,380,181,31)
        exportTruckReportButton.setStyleSheet("QPushButton {background-color:white;border:2px solid black;font: 14pt 'Arial';} QPushButton:hover {background-color:#c8c8c8;}")
        exportTruckReportButton.clicked.connect(self.exportBigTruckReport)

        #End minMenu Buttons style
        self.loadItemToBigTrucks(self.BigTruckIdToShowItemsToBigTrucks)
        self.showBigTrucksPartsFrame.show()
    def showMenuNotesBigTrucksPartsTable(self,position):
        indexes = self.bigTrucksPartsTable.selectedIndexes()
        for index in indexes:
            self.contextMenuBigTrucksPartsTable.exec(self.bigTrucksPartsTable.viewport().mapToGlobal(position))
    def createButtonBigTrucksPartsTable(self):
        deleteButton = QAction(self.bigTrucksTable)
        deleteButton.setText("حذف")
        deleteButton.setFont(QFont("Arial" , 12))
        deleteButton.triggered.connect(self.deleteItemFromBigTruck)

        showNotesButton = QAction(self.bigTrucksTable)
        showNotesButton.setText("اظهار الملاحظات")
        showNotesButton.setFont(QFont("Arial" , 12))
        showNotesButton.triggered.connect(self.showNotesBigTrucksToItems)

        self.contextMenuBigTrucksPartsTable.addAction(showNotesButton)
        self.contextMenuBigTrucksPartsTable.addAction(deleteButton)
    def deleteItemFromBigTruck(self):
        itemId = self.bigTrucksPartsTable.item(self.bigTrucksPartsTable.selectedIndexes()[0].row(),1).text()
        OilOrItem = self.bigTrucksPartsTable.item(self.bigTrucksPartsTable.selectedIndexes()[0].row(),5).text()
        d = QMessageBox(parent=self,text=f"تأكيد حذف القطعة من التيدر")
        d.setIcon(QMessageBox.Icon.Information)
        d.setWindowTitle("تأكيد")
        d.setStyleSheet("background-color:white")
        d.setStandardButtons(QMessageBox.StandardButton.Cancel|QMessageBox.StandardButton.Ok)
        important = d.exec()
        if important == QMessageBox.StandardButton.Ok:
            cr.execute("SELECT number FROM bigTrucks WHERE id = ?",[self.BigTruckIdToShowItemsToBigTrucks])
            carNumber = str(cr.fetchone()[0])
            if OilOrItem == 'oil':
                cr.execute("Select quantity FROM bigTrucksToOil WHERE oilCode=? and bigTruckId=?",(itemId,self.BigTruckIdToShowItemsToBigTrucks))
                oilQuantity = cr.fetchone()[0]
                cr.execute("INSERT INTO itemsLifecycle (itemId, date, action) VALUES (?,?,?)",(itemId, str(date.today()).replace('-','/'), f'تم تفريغ {oilQuantity} من الزيت من سيارة رقم {carNumber}'))
            elif OilOrItem == 'item':
                cr.execute("INSERT INTO itemsLifecycle (itemId, date, action) VALUES (?,?,?)",(itemId, str(date.today()).replace('-','/'), f'تم فك القطعة من شاحنة رقم {carNumber} '))
            
            if OilOrItem == 'oil':
                cr.execute("SELECT quantity FROM bigTrucksToOil WHERE oilCode=? and bigTruckId=?",(itemId,self.BigTruckIdToShowItemsToBigTrucks))
                cr.execute(f"UPDATE oil set remeaningQuantity=remeaningQuantity+{cr.fetchone()[0]} WHERE code=?",[itemId])
                cr.execute("DELETE FROM bigTrucksToOil WHERE oilCode=? and bigTruckId=?",(itemId,self.BigTruckIdToShowItemsToBigTrucks))
            elif OilOrItem == 'item':
                cr.execute("DELETE FROM bigTrucksParts WHERE itemId=? and bigTruckId=?",(itemId,self.BigTruckIdToShowItemsToBigTrucks))
            con.commit()
            self.loadItemToBigTrucks(self.BigTruckIdToShowItemsToBigTrucks)
            d = QMessageBox(parent=self,text="تم الحذف بنجاح")
            d.setWindowTitle("نجاح")
            d.setIcon(QMessageBox.Icon.Information)
            d.setStyleSheet("background-color:white")
            ret = d.exec()
    def showNotesBigTrucksToItems(self):
        try:
            self.showNotesBigTrucksToItemsFrame.deleteLater()
        except:
            pass
        self.itemIdShowNoteBigTruck = self.bigTrucksPartsTable.item(self.bigTrucksPartsTable.selectedIndexes()[0].row(),1).text()

        self.showNotesBigTrucksToItemsFrame = QFrame(self.bigTrucksFrame)
        self.showNotesBigTrucksToItemsFrame.setGeometry((self.bigTrucksFrame.width()-450)//2,(self.bigTrucksFrame.height()-400)//2,450,400)
        # self.showTrucksNoteFrame.setStyleSheet("background-color:white;border:2px solid black")
        
        closeButton = QPushButton(self.showNotesBigTrucksToItemsFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(400,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.showNotesBigTrucksToItemsFrame:self.destroyFrame(frame))

        self.showNotesBigTrucksToItemsFrame.setStyleSheet("background-color:white")

        self.notesTextEditBigTruck = QTextEdit(self.showNotesBigTrucksToItemsFrame)
        self.notesTextEditBigTruck.setGeometry(10,60,410,240)
        if(self.bigTrucksPartsTable.item(self.bigTrucksPartsTable.selectedIndexes()[0].row(),5).text() == 'item'):
            cr.execute("SELECT notes FROM bigTrucksParts WHERE itemId=? and bigTruckId = ?",(self.itemIdShowNoteBigTruck, self.BigTruckIdToShowItemsToBigTrucks))
        elif (self.bigTrucksPartsTable.item(self.bigTrucksPartsTable.selectedIndexes()[0].row(),5).text() == 'oil'):
            cr.execute("SELECT notes FROM bigTrucksToOil WHERE oilCode=? and bigTruckId = ?",(self.itemIdShowNoteBigTruck, self.BigTruckIdToShowItemsToBigTrucks))

        self.notesTextEditBigTruck.setText(str(cr.fetchone()[0]))

        addNoteButton = QPushButton("تعديل ملاحظة",self.showNotesBigTrucksToItemsFrame)
        addNoteButton.setStyleSheet("QPushButton {border:2px solid black;font:14pt 'Arial'}QPushButton:hover {background-color:#c8c8c8;}")        
        addNoteButton.setGeometry(120,310,180,31)
        addNoteButton.clicked.connect(self.completeEditNoteBigTruckParts)

        #End minMenu Buttons style
        self.showNotesBigTrucksToItemsFrame.show()
    def completeEditNoteBigTruckParts(self):
        if(self.bigTrucksPartsTable.item(self.bigTrucksPartsTable.selectedIndexes()[0].row(),5).text() == 'item'):
            cr.execute("UPDATE bigTrucksParts set notes=? WHERE itemId=? and bigTruckId = ?",(self.notesTextEditBigTruck.toPlainText(),self.itemIdShowNoteBigTruck, self.BigTruckIdToShowItemsToBigTrucks))
        elif (self.bigTrucksPartsTable.item(self.bigTrucksPartsTable.selectedIndexes()[0].row(),5).text() == 'oil'):
            cr.execute("UPDATE bigTrucksToOil set notes=? WHERE oilCode=? and bigTruckId = ?",(self.notesTextEditBigTruck.toPlainText(),self.itemIdShowNoteBigTruck, self.BigTruckIdToShowItemsToBigTrucks))
        
        con.commit()
        message = QMessageBox(parent=self,text="تمت الاضافة بنجاح")
        message.setIcon(QMessageBox.Icon.Information)
        message.setWindowTitle("نجاح")
        message.exec()

        for child in self.showNotesBigTrucksToItemsFrame.children():
            child.deleteLater()
        self.showNotesBigTrucksToItemsFrame.deleteLater()
    def loadItemToBigTrucks(self,BigTruckIdToShowItemsToBigTrucks):
        self.totalPriceVarBigTrucks = 0
        self.bigTrucksPartsTable.setRowCount(0)     
        cr.execute("SELECT itemName,itemId,itemPrice,installPlace,installDate FROM bigTrucksParts WHERE bigTruckId = ?",[BigTruckIdToShowItemsToBigTrucks])
        tempThing = [] 
        for i in cr.fetchall():
            i = list(i)
            i.append("item")
            tempThing.append(i)

        cr.execute("SELECT itemName,oilCode,itemPrice,installPlace,installDate FROM bigTrucksToOil WHERE bigTruckId = ?",[BigTruckIdToShowItemsToBigTrucks])
        for i in cr.fetchall():
            i = list(i)
            i.append("oil")
            tempThing.append(i)

        for row,i in enumerate(tempThing):
            self.bigTrucksPartsTable.insertRow(self.bigTrucksPartsTable.rowCount())
            for col,val in enumerate(i):
                if col==2:
                    self.totalPriceVarBigTrucks+=float(val)
                self.bigTrucksPartsTable.setItem(row,col,QTableWidgetItem(str(val))) 
        self.totalPriceVarBigTrucks = round(self.totalPriceVarBigTrucks,2)
        self.totalPriceBigTruck.setText(f"اجمالي الصرف على التيدر:{self.totalPriceVarBigTrucks}")
    def destroyFrame(self,frame):
        for i in frame.children():
            i.deleteLater()

        frame.destroy()
        frame.deleteLater()
    def exportBigTruckReport(self):
        filePath = QFileDialog.getExistingDirectory(self,"Select a Directory")
        if len(filePath) > 0:
            cr.execute("SELECT itemName,itemId,itemPrice,installPlace,installDate FROM bigTrucksParts WHERE bigTruckId = ?",[self.BigTruckIdToShowItemsToBigTrucks])
            values = cr.fetchall() # [()]
            cr.execute("SELECT itemName,oilCode,itemPrice,installPlace,installDate FROM bigTrucksToOil WHERE bigTruckId = ?",[self.BigTruckIdToShowItemsToBigTrucks])
            for tempVal in cr.fetchall():
                values.append(tempVal)
                
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

            benefits_table = doc.add_table(rows=1,cols=6)
            benefits_table.style = "Table Grid"
            hdr_Cells = benefits_table.rows[0].cells
            hdr_Cells[5].text = "م"
            hdr_Cells[4].text = "اسم الصنف"
            hdr_Cells[3].text = "الكود"
            hdr_Cells[2].text = "سعر الصنف"
            hdr_Cells[1].text = "مكان التركيب"
            hdr_Cells[0].text = "تاريخ التركيب"

            for cell in hdr_Cells:
                self.set_arabic_format(cell)

            b = 0
            
            for i in values:
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
            para = doc.add_paragraph().add_run(f"اجمالي الصرف على التيدر:{self.totalPriceVarBigTrucks}")
            para.font.name = "Arial"
            para.font.size = docx.shared.Pt(20)
            
            doc.save(f"{filePath}\تقرير التيدر رقم {self.BigTruckNumber}.docx")
            with suppress_output():
                convert(f"{filePath}\تقرير التيدر رقم {self.BigTruckNumber}.docx",f"{filePath}\تقرير التيدر رقم {self.BigTruckNumber}.pdf")
            os.remove(f"{filePath}\تقرير التيدر رقم {self.BigTruckNumber}.docx")

            message = QMessageBox(parent=self,text="تم التصدير بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()