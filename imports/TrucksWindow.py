from .stuff import *

class TrucksWindow():
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
    def addSearchTrucksEntries(self):
        try:
            self.searchEntryTruck.destroy()
            self.searchEntryTruck.hide()
        except:
            pass
        if self.comboSearchTrucksBox.currentText() == "الكل":
            self.loadTrucks()
        else:
            self.searchEntryTruck = QLineEdit(self.trucksFrame)
            self.searchEntryTruck.textChanged.connect(self.searchTrucksFun)
            self.searchEntryTruck.setGeometry(340,30,150,20)
            self.searchEntryTruck.show()
    def searchTrucksFun(self):
        if len(self.searchEntryTruck.text())==0:
            self.loadTrucks()
        else:
            self.trucksTable.setRowCount(0)
            tempThing = [] 
            cr.execute("SELECT carNumber From trucks")
            choices = cr.fetchall()
            posiple = []
            for o in choices:
                for n,i in enumerate(o):
                    try:
                        if o[n][:len(self.searchEntryTruck.text())]==self.searchEntryTruck.text():
                                if i not in posiple:
                                    posiple.append(i)
                    except:
                        pass

            for p in posiple:
                cr.execute("SELECT * FROM trucks WHERE carNumber = ?", [p])
                for i in cr.fetchall():
                    tempThing.append(i)

            for row,i in enumerate(tempThing):
                self.trucksTable.insertRow(self.trucksTable.rowCount())
                for col,val in enumerate(i):
                    self.trucksTable.setItem(row,col,QTableWidgetItem(str(val)))
    def showTrucks(self):
        try:
            self.destroyFrame(self.mainMenuTrucksFrame)
            self.destroyFrame(self.trucksFrame)
        except:
            pass

        self.trucksFrame = QFrame(self.mainFrame)
        
        self.closeButtonTtrucksFrame = QPushButton(self.trucksFrame)
        self.closeButtonTtrucksFrame.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        self.closeButtonTtrucksFrame.clicked.connect(lambda x, frame=self.trucksFrame:self.destroyFrame(frame))

        self.comboSearchTrucksBox = QComboBox(self.trucksFrame)
        self.comboSearchTrucksBox.setGeometry(500,30,150,20)
        self.comboSearchTrucksBox.addItems(["الكل", "رقم الشاحنة"])
        self.comboSearchTrucksBox.activated.connect(self.addSearchTrucksEntries)

        self.trucksFrame.setStyleSheet("background-color:white")

        self.trucksTable = QTableWidget(self.trucksFrame)

        self.trucksTable.setColumnCount(7)
        self.trucksTable.setHorizontalHeaderLabels(["id","رقم السيارة","اللوحة","استمارة كرت التشغيل","انتهاء الاستمارة","انتهاء الفحص الدوري","انتهاء التأمين"])
        
        self.trucksTable.setColumnHidden(0,True)

        self.trucksTable.setColumnWidth(0, 80)
        self.trucksTable.setColumnWidth(1, 80)
        self.trucksTable.setColumnWidth(2, 140)
        self.trucksTable.setColumnWidth(3, 120)
        self.trucksTable.setColumnWidth(4, 130)
        self.trucksTable.setColumnWidth(5, 80)


        self.contextMenutrucksTable = QMenu(self.trucksTable)
        self.contextMenutrucksTable.setStyleSheet("background-color:grey")
        self.createButtontrucksTable()

        self.trucksTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.trucksTable.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.trucksTable.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.trucksTable.customContextMenuRequested.connect(self.showMenutrucksTable)

        #Start minMenu Buttons style
        self.mainMenuTrucksFrame = QFrame(self.trucksFrame)
        self.mainMenuTrucksFrame.setStyleSheet("background-color:white;border:2px solid black")
        
        label = QLabel(self.mainMenuTrucksFrame,text="القائمة الرئيسيه")
        label.setStyleSheet("background-color:white;border-bottom:none;font: 14pt 'Arial';")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setGeometry(0,0,181,31)

        addTruckButton = QPushButton(self.mainMenuTrucksFrame,text="اضافة شاحنة")
        addTruckButton.setGeometry(0,50,181,31)
        addTruckButton.setStyleSheet("QPushButton {background-color:white;border:2px solid black;font: 14pt 'Arial';} QPushButton:hover {background-color:#c8c8c8;}")
        addTruckButton.clicked.connect(self.addTruck)

        exportTrucks = QPushButton(self.mainMenuTrucksFrame,text="تصدير معلومات الشاحنات")
        exportTrucks.setGeometry(0,90,181,31)
        exportTrucks.setStyleSheet("QPushButton {background-color:white;border:2px solid black;font: 14pt 'Arial';} QPushButton:hover {background-color:#c8c8c8;}")
        exportTrucks.clicked.connect(self.exportAllTrucks)

        exportTrucksReport = QPushButton(self.mainMenuTrucksFrame,text="تصدير تقرير الشاحنات")
        exportTrucksReport.setGeometry(0,130,181,31)
        exportTrucksReport.setStyleSheet("QPushButton {background-color:white;border:2px solid black;font: 14pt 'Arial';} QPushButton:hover {background-color:#c8c8c8;}")
        exportTrucksReport.clicked.connect(self.exportTrucksReport)

        #End minMenu Buttons style

        self.putTrucksFrameAndStuff()
        
        self.loadTrucks()
        self.trucksFrame.show()
    def exportTrucksReport(self):
        try:
            self.destroyFrame(self.exportTruckReportFrame)
        except:
            pass

        arabic_locale = QLocale(QLocale.Language.Arabic, QLocale.Country.SaudiArabia)

        self.exportTruckReportFrame = QFrame(parent=self.mainFrame)
        self.exportTruckReportFrame.setGeometry((self.mainFrame.width()-210)//2,(self.mainFrame.height()-230)//2,210,230)
        self.exportTruckReportFrame.setStyleSheet("background-color:white;border:2px solid black")

        closeButton = QPushButton(self.exportTruckReportFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:8px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 18px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(160,10,31,21)
        closeButton.clicked.connect(lambda x, frame=self.exportTruckReportFrame:self.destroyFrame(frame))

        label = QLabel(parent=self.exportTruckReportFrame,text="من تاريخ")
        label.setStyleSheet('font: 18pt "Arial";border:none')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.move(50,50)

        self.fromDateExportTruck = QDateEdit(parent=self.exportTruckReportFrame)
        self.fromDateExportTruck.setCalendarPopup(True)
        self.fromDateExportTruck.setDisplayFormat("yyyy/MM/dd")

        self.todayButtonFromDateTruck = QPushButton("اليوم",clicked=lambda:self.fromDateExportTruck.calendarWidget().setSelectedDate(QDate().currentDate()))
        self.todayButtonFromDateTruck.setStyleSheet("background-color:green;")

        self.fromDateExportTruck.setLocale(arabic_locale)
        self.fromDateExportTruck.setFont(QFont("Arial",12))
        self.fromDateExportTruck.setStyleSheet("background-color:white;color:black")
        
        self.fromDateExportTruck.calendarWidget().layout().addWidget(self.todayButtonFromDateTruck)
        self.fromDateExportTruck.calendarWidget().setSelectedDate(QDate().currentDate())
        self.fromDateExportTruck.setGeometry(20,80,160,31)

        label = QLabel(parent=self.exportTruckReportFrame,text="الى تاريخ")
        label.setStyleSheet('font: 18pt "Arial";border:none')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.move(50,120)

        self.toDateExportTruck = QDateEdit(parent=self.exportTruckReportFrame)
        self.toDateExportTruck.setCalendarPopup(True)
        self.toDateExportTruck.setDisplayFormat("yyyy/MM/dd")

        self.todayButtonToDateTruck = QPushButton("اليوم",clicked=lambda:self.toDateExportTruck.calendarWidget().setSelectedDate(QDate().currentDate()))
        self.todayButtonToDateTruck.setStyleSheet("background-color:green;")

        self.toDateExportTruck.setLocale(arabic_locale)
        self.toDateExportTruck.setFont(QFont("Arial",12))
        self.toDateExportTruck.setStyleSheet("background-color:white;color:black")
        
        self.toDateExportTruck.calendarWidget().layout().addWidget(self.todayButtonToDateTruck)
        self.toDateExportTruck.calendarWidget().setSelectedDate(QDate().currentDate())
        self.toDateExportTruck.setGeometry(20,150,160,31)

        exportButton = QPushButton(parent=self.exportTruckReportFrame,text="تصدير")
        exportButton.setGeometry(50,190,101,31)
        exportButton.setStyleSheet("QPushButton:hover {background-color:#c8c8c8;}")
        exportButton.clicked.connect(self.completeExportTruckReport)


        self.exportTruckReportFrame.show()
    def completeExportTruckReport(self):
        filePath = QFileDialog.getExistingDirectory(self,"Select a Directory")
        if len(filePath) > 0:
            valuesToWrite = []
            totalPriceToWrite = 0
            fromDate = str(self.fromDateExportTruck.text()).split("/")
            fromDateGoodFormat = date(int(fromDate[0]),int(fromDate[1]),int(fromDate[2]))

            toDate = str(self.toDateExportTruck.text()).split("/")
            toDateGoodFormat = date(int(toDate[0]),int(toDate[1]),int(toDate[2]))

            #[itemPrice,itemName, installDate, bigTruckNumber]

            cr.execute("SELECT itemName,itemPrice,installDate,truckId FROM trucksParts")
            for i in cr.fetchall():
                date1 = str(i[2]).split("/")
                date2 = date(int(date1[0]),int(date1[1]),int(date1[2]))

                if date2>= fromDateGoodFormat and date2<=toDateGoodFormat:
                    cr.execute("SELECT carNumber FROM trucks WHERE id=?",[i[3]])
                    valuesToWrite.append([i[0],str(round(float(i[1]),2)),i[2],cr.fetchone()[0]])
                    totalPriceToWrite+=round(float(i[1]),2)
            
            cr.execute("SELECT itemName,itemPrice,installDate,truckId FROM trucksToOil")
            for i in cr.fetchall():
                date1 = str(i[2]).split("/")
                date2 = date(int(date1[0]),int(date1[1]),int(date1[2]))

                if date2>= fromDateGoodFormat and date2<=toDateGoodFormat:
                    cr.execute("SELECT carNumber FROM trucks WHERE id=?",[i[3]])
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
            hdr_Cells[0].text = "رقم الشاحنة"

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
            para = doc.add_paragraph().add_run(f"اجمالي الصرف على الشاحنات:{round(totalPriceToWrite,2)}")
            para.font.name = "Arial"
            para.font.size = docx.shared.Pt(20)
            
            doc.save(f"{filePath}\تقرير الشاحنات.docx")
            with suppress_output():
                convert(f"{filePath}\تقرير الشاحنات.docx",f"{filePath}\تقرير الشاحنات.pdf")
            os.remove(f"{filePath}\تقرير الشاحنات.docx")

            message = QMessageBox(parent=self,text="تم التصدير بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
    def putTrucksFrameAndStuff(self):
        
        if self.width() <= 995 or self.height() <= 680:
            self.trucksFrame.setGeometry((self.width()-847)//2,(self.mainFrame.height()-610)//2,847,610)
            self.trucksTable.setGeometry(10,60,641,541)
            self.mainMenuTrucksFrame.setGeometry(660,60,181,161)
            self.closeButtonTtrucksFrame.setGeometry(800,10,41,31)
        else:
            self.trucksFrame.setGeometry(30,30,self.mainFrame.width()-60,self.mainFrame.height()-60)
            self.trucksTable.setGeometry(10,60,self.trucksFrame.width() - 206,self.trucksFrame.height()-100)
            self.mainMenuTrucksFrame.setGeometry(self.trucksTable.width() + 20,60,181,161)
            self.closeButtonTtrucksFrame.setGeometry(self.trucksTable.width() + 20 + 140,10,41,31)

        deserve = self.trucksTable.columnCount() - 1
        for i in range(self.trucksTable.columnCount()):
            self.trucksTable.setColumnWidth(i, (self.trucksTable.width() - 20) // deserve)

        self.trucksFrame.show()
        self.trucksTable.show()
        self.mainMenuTrucksFrame.show()
        self.closeButtonTtrucksFrame.show()

    def loadTrucks(self):
        self.trucksTable.setRowCount(0)     
        
        cr.execute("SELECT * FROM trucks")
        tempThing = [] 
        for i in cr.fetchall():
            tempThing.append(i)
        for row,i in enumerate(tempThing):
            self.trucksTable.insertRow(self.trucksTable.rowCount())
            for col,val in enumerate(i):
                self.trucksTable.setItem(row,col,QTableWidgetItem(str(val)))    
    def addTruck(self):
        try:
            self.destroyFrame(self.addTruckFrame)
        except:
            pass

        self.addTruckFrame = QFrame(self.mainFrame)
        self.addTruckFrame.setGeometry((self.mainFrame.width()-350)//2,(self.mainFrame.height()-506)//2,350,506)
        self.addTruckFrame.setStyleSheet("background-color:white;border:2px solid black")

        closeButton = QPushButton(self.addTruckFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(300,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.addTruckFrame:self.destroyFrame(frame))
        
        #Start scrolAria
        


        self.frame = QFrame()

        layout = QVBoxLayout()
        self.frame.setLayout(layout)


        label = QLabel("رقم السيارة")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")
        self.carNumberEntry = QLineEdit()

        layout.addWidget(label)
        layout.addWidget(self.carNumberEntry)

        label = QLabel("رقم اللوحة")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")

        self.carPlateEntry = QLineEdit()

        layout.addWidget(label)
        layout.addWidget(self.carPlateEntry)

        label = QLabel("استمارة كرت التشغيل")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")
        self.playCardEntry = QLineEdit()

        layout.addWidget(label)
        layout.addWidget(self.playCardEntry)

        label = QLabel("انتهاء الاستمارة")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")


        self.formExpireEntry = QDateEdit()
        self.formExpireEntry.setCalendarPopup(True)
        self.formExpireEntry.setDisplayFormat("yyyy/MM/dd")

        arabic_locale = QLocale(QLocale.Language.Arabic, QLocale.Country.SaudiArabia)

        self.formExpireEntry.setLocale(arabic_locale)
        self.formExpireEntry.setFont(QFont("Arial",12))
        self.formExpireEntry.setStyleSheet("background-color:white;color:black")

        self.todayButton12 = QPushButton("اليوم",clicked=lambda:self.formExpireEntry.calendarWidget().setSelectedDate(QDate().currentDate()))
        self.todayButton12.setStyleSheet("background-color:green;")

        self.formExpireEntry.calendarWidget().layout().addWidget(self.todayButton12)
        self.formExpireEntry.calendarWidget().setSelectedDate(QDate().currentDate())

        layout.addWidget(label)
        layout.addWidget(self.formExpireEntry)

        label = QLabel("انتهاء الفحص الدوري")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")

        self.examExpireEntry = QDateEdit()
        self.examExpireEntry.setCalendarPopup(True)
        self.examExpireEntry.setDisplayFormat("yyyy/MM/dd")

        self.examExpireEntry.setLocale(arabic_locale)
        self.examExpireEntry.setFont(QFont("Arial",12))
        self.examExpireEntry.setStyleSheet("background-color:white;color:black")

        self.todayButton = QPushButton("اليوم",clicked=lambda:self.examExpireEntry.calendarWidget().setSelectedDate(QDate().currentDate()))
        self.todayButton.setStyleSheet("background-color:green;")

        self.examExpireEntry.calendarWidget().layout().addWidget(self.todayButton)
        self.examExpireEntry.calendarWidget().setSelectedDate(QDate().currentDate())

        layout.addWidget(label)
        layout.addWidget(self.examExpireEntry)

        label = QLabel("انتهاء التأمين")
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

        addButton = QPushButton(text="اضافة")
        addButton.clicked.connect(self.completeAddTruck)
        addButton.setStyleSheet("QPushButton:hover {background-color:#c8c8c8;}")        

        layout.addWidget(addButton)

        self.scroolAria = QScrollArea(self.addTruckFrame)
        self.scroolAria.setWidget(self.frame)
        self.scroolAria.setStyleSheet("border:1px solid gray")
        self.scroolAria.move(20,50)
        self.scroolAria.resize(321,431)

        self.scroolAria.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)


        self.scroolAria.setWidgetResizable(True)


        #End scrolAria
        self.addTruckFrame.show()
    def completeAddTruck(self):
        if len(self.carNumberEntry.text()) > 0 and len(self.carPlateEntry.text()) > 0 and len(self.playCardEntry.text()) > 0 and len(self.formExpireEntry.text()) and len(self.examExpireEntry.text()) > 0 and len(self.insuranceExpireEntry.text()) > 0:
            cr.execute("INSERT INTO trucks (carNumber,carPlate,playCard,formExpire,examExpire,insuranceExpire) values (?,?,?,?,?,?)",(self.carNumberEntry.text(),self.carPlateEntry.text(),self.playCardEntry.text(),self.formExpireEntry.text(),self.examExpireEntry.text(),self.insuranceExpireEntry.text()))
            con.commit()
            message = QMessageBox(parent=self,text="تمت الاضافة بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
            self.loadTrucks()
        else:
            message = QMessageBox(parent=self,text="يرجى تعبئة جميع الحقول")
            message.setIcon(QMessageBox.Icon.Critical)
            message.setWindowTitle("فشل")
            message.exec()
    def exportAllTrucks(self):
        try:
            self.destroyFrame(self.exportTrucksFrame)
        except:
            pass
        self.exportTrucksFrame = QFrame(parent=self.mainFrame)
        self.exportTrucksFrame.setGeometry((self.mainFrame.width()-160)//2,(self.mainFrame.height()-174)//2,160,147)
        self.exportTrucksFrame.setStyleSheet("background-color:white;border:2px solid black")

        closeButton = QPushButton(self.exportTrucksFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:8px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 18px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(120,10,31,21)
        closeButton.clicked.connect(lambda x, frame=self.exportTrucksFrame:self.destroyFrame(frame))

        label = QLabel(parent=self.exportTrucksFrame,text="الصيغة")
        label.setStyleSheet('font: 14pt "Arial";border:none')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setGeometry(20,50,121,20)

        self.formatComboBox = QComboBox(self.exportTrucksFrame)
        self.formatComboBox.addItems(["Word","Pdf","Excel"])
        self.formatComboBox.setGeometry(8,80,141,22)
        
        exportButton = QPushButton(parent=self.exportTrucksFrame,text="تصدير")
        exportButton.setGeometry(30,110,101,31)
        exportButton.setStyleSheet("QPushButton:hover {background-color:#c8c8c8;}")
        exportButton.clicked.connect(self.completeExportTrucks)

        self.exportTrucksFrame.show()
    def completeExportTrucks(self):
        filePath = QFileDialog.getExistingDirectory(self,"Select a Directory")
        if len(filePath) > 0:
            cr.execute("SELECT carNumber,carPlate,playCard, formExpire, examExpire, insuranceExpire FROM trucks")
            drivers = cr.fetchall()
            if self.formatComboBox.currentText() == "Excel":

                headers = ["رقم السيارة","اللوحة","استمارة كرت التشغيل","انتهاء الاستمارة","انتهاء الفحص الدوري","انتهاء التأمين"]

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
                wb.save(f"{filePath}/جميع الشاحنات.xlsx")    
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

    

                benefits_table = doc.add_table(rows=1,cols=7)
                benefits_table.style = "Table Grid"
                hdr_Cells = benefits_table.rows[0].cells
                hdr_Cells[6].text = "م"
                hdr_Cells[5].text = "رقم السيارة"
                hdr_Cells[4].text = "اللوحة"
                hdr_Cells[3].text = "استمارة كرت التشغيل"
                hdr_Cells[2].text = "انتهاء الاستمارة"
                hdr_Cells[1].text = "انتهاء الفحص الدوري"
                hdr_Cells[0].text = "انتهاء التأمين"

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

                    row_Cells[6].text = str(b)
                    row_Cells[5].text = str(i[0])
                    row_Cells[4].text = str(i[1])
                    row_Cells[3].text = str(i[2])
                    row_Cells[2].text = str(i[3])
                    row_Cells[1].text = str(i[4])
                    row_Cells[0].text = str(i[5])

                    for cell in row_Cells:
                        self.set_arabic_format(cell)

                widths = (docx.shared.Inches(4), docx.shared.Inches(4), docx.shared.Inches(4), docx.shared.Inches(4), docx.shared.Inches(4), docx.shared.Inches(4),docx.shared.Inches(0.5))
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

                doc.save(f"{filePath}\جميع الشاحنات.docx")

            if self.formatComboBox.currentText() == "Pdf":
                with suppress_output():
                    convert(f"{filePath}\جميع الشاحنات.docx",f"{filePath}\جميع الشاحنات.pdf")

                os.remove(f"{filePath}\جميع الشاحنات.docx")

            message = QMessageBox(parent=self,text="تم التصدير بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
    def createButtontrucksTable(self):
        self.deleteButton = QAction(self.trucksTable)
        self.deleteButton.setIcon(QIcon("assests/trash.png"))
        self.deleteButton.setText("حذف")
        self.deleteButton.setFont(QFont("Arial" , 12))
        self.deleteButton.triggered.connect(self.deleteTruck)

        self.editButton = QAction(self.trucksTable)
        self.editButton.setIcon(QIcon("assests/edit.png"))
        self.editButton.setText("تعديل")
        self.editButton.setFont(QFont("Arial" , 12))
        self.editButton.triggered.connect(self.editTruck)

        self.addNoteButton = QAction(self.trucksTable)
        self.addNoteButton.setIcon(QIcon("assests/addNote.png"))
        self.addNoteButton.setText("اضافة ملاحظة")
        self.addNoteButton.setFont(QFont("Arial" , 12))
        self.addNoteButton.triggered.connect(self.showTrucksNote)

        self.showPartsButton = QAction(self.trucksTable)
        self.showPartsButton.setText("اظهار القطع")
        self.showPartsButton.setFont(QFont("Arial" , 12))
        self.showPartsButton.triggered.connect(self.showTrucksParts)

        self.contextMenutrucksTable.addAction(self.deleteButton)
        self.contextMenutrucksTable.addAction(self.editButton)
        self.contextMenutrucksTable.addAction(self.addNoteButton)
        self.contextMenutrucksTable.addAction(self.showPartsButton)
    def showTrucksParts(self):
        try:
            self.showTrucksPartsFrame.deleteLater()
        except:
            pass

        self.truckIdToShowItemsToTrucks = self.trucksTable.item(self.trucksTable.selectedIndexes()[0].row(),0).text()
        self.truckNumber = self.trucksTable.item(self.trucksTable.selectedIndexes()[0].row(),1).text()

        self.showTrucksPartsFrame = QFrame(self.trucksFrame)
        self.showTrucksPartsFrame.setGeometry((self.trucksFrame.width()-450)//2,(self.trucksFrame.height()-450)//2,450,450)
        # self.showTrucksNoteFrame.setStyleSheet("background-color:white;border:2px solid black")
        
        closeButton = QPushButton(self.showTrucksPartsFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(400,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.showTrucksPartsFrame:self.destroyFrame(frame))

        self.showTrucksPartsFrame.setStyleSheet("background-color:white")

        self.trucksPartsTable = QTableWidget(self.showTrucksPartsFrame)
        self.trucksPartsTable.setGeometry(10,60,410,240)

        self.trucksPartsTable.setColumnCount(6)
        self.trucksPartsTable.setHorizontalHeaderLabels(["اسم الصنف","الكود", "السعر","مكان التركيب","تاريخ التركيب","type"])
        self.trucksPartsTable.setColumnHidden(5,True)

        self.contextMenuTrucksPartsTable = QMenu(self.trucksPartsTable)
        self.contextMenuTrucksPartsTable.setStyleSheet("background-color:grey")
        self.createButtonTrucksPartsTable()

        self.trucksPartsTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.trucksPartsTable.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.trucksPartsTable.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.trucksPartsTable.customContextMenuRequested.connect(self.showMenuTruckPartsTable)

        self.totalPriceVar = 0

        self.totalPriceTruck = QLabel(parent=self.showTrucksPartsFrame,text=f"اجمالي الصرف على الشاحنة:{self.totalPriceVar}")
        self.totalPriceTruck.setStyleSheet('font: 14pt "Arial";border:none')
        self.totalPriceTruck.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.totalPriceTruck.move(150,340)

        exportTruckReportButton = QPushButton(self.showTrucksPartsFrame,text="تصدير التقرير")
        exportTruckReportButton.setGeometry(150,380,181,31)
        exportTruckReportButton.setStyleSheet("QPushButton {background-color:white;border:2px solid black;font: 14pt 'Arial';} QPushButton:hover {background-color:#c8c8c8;}")
        exportTruckReportButton.clicked.connect(self.exportTruckReport)

        #End minMenu Buttons style
        self.loadItemToTrucks(self.truckIdToShowItemsToTrucks)
        self.showTrucksPartsFrame.show()
    def showMenuTruckPartsTable(self,position):
        indexes = self.trucksPartsTable.selectedIndexes()
        for index in indexes:
            self.contextMenuTrucksPartsTable.exec(self.trucksPartsTable.viewport().mapToGlobal(position))
    def createButtonTrucksPartsTable(self):
        deleteButton = QAction(self.trucksPartsTable)
        deleteButton.setText("حذف")
        deleteButton.setFont(QFont("Arial" , 12))
        deleteButton.triggered.connect(self.deleteItemToTruck)

        showNotesButton = QAction(self.trucksPartsTable)
        showNotesButton.setText("اظهار الملاحظات")
        showNotesButton.setFont(QFont("Arial" , 12))
        showNotesButton.triggered.connect(self.showNotesTrucksToItems)

        self.contextMenuTrucksPartsTable.addAction(showNotesButton)
        self.contextMenuTrucksPartsTable.addAction(deleteButton)
    def showNotesTrucksToItems(self):
        try:
            self.showNotesTrucksToItemsFrame.deleteLater()
        except:
            pass
        self.itemIdShowNote = self.trucksPartsTable.item(self.trucksPartsTable.selectedIndexes()[0].row(),1).text()
        self.itemType = self.trucksPartsTable.item(self.trucksPartsTable.selectedIndexes()[0].row(),5).text()

        self.showNotesTrucksToItemsFrame = QFrame(self.trucksFrame)
        self.showNotesTrucksToItemsFrame.setGeometry((self.trucksFrame.width()-450)//2,(self.trucksFrame.height()-400)//2,450,400)
        # self.showTrucksNoteFrame.setStyleSheet("background-color:white;border:2px solid black")
        
        closeButton = QPushButton(self.showNotesTrucksToItemsFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(400,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.showNotesTrucksToItemsFrame:self.destroyFrame(frame))

        self.showNotesTrucksToItemsFrame.setStyleSheet("background-color:white")

        self.notesTextEdit = QTextEdit(self.showNotesTrucksToItemsFrame)
        self.notesTextEdit.setGeometry(10,60,410,240)
        if self.itemType == "oil":
            cr.execute("SELECT notes FROM trucksToOil WHERE oilCode=? and truckId = ?",(self.itemIdShowNote, self.truckIdToShowItemsToTrucks))
        elif self.itemType=="item":
            cr.execute("SELECT notes FROM trucksParts WHERE itemId=? and truckId = ?",(self.itemIdShowNote, self.truckIdToShowItemsToTrucks))
        
        self.notesTextEdit.setText(str(cr.fetchone()[0]))

        addNoteButton = QPushButton("تعديل ملاحظة",self.showNotesTrucksToItemsFrame)
        addNoteButton.setStyleSheet("QPushButton {border:2px solid black;font:14pt 'Arial'}QPushButton:hover {background-color:#c8c8c8;}")        
        addNoteButton.setGeometry(120,310,180,31)
        addNoteButton.clicked.connect(self.completeEditNoteTruckParts)

        #End minMenu Buttons style
        self.showNotesTrucksToItemsFrame.show()
    def completeEditNoteTruckParts(self):
        cr.execute("UPDATE trucksParts set notes=? WHERE itemId=? and truckId = ?",(self.notesTextEdit.toPlainText(),self.itemIdShowNote, self.truckIdToShowItemsToTrucks))
        con.commit()
        message = QMessageBox(parent=self,text="تمت الاضافة بنجاح")
        message.setIcon(QMessageBox.Icon.Information)
        message.setWindowTitle("نجاح")
        message.exec()
        for child in self.showNotesTrucksToItemsFrame.children():
            child.deleteLater()
        self.showNotesTrucksToItemsFrame.deleteLater()
    def showButtonTrucksPartsTable(self, position):
        indexes = self.trucksTable.selectedIndexes()
        for index in indexes:
            self.contextMenuTrucksPartsTable.exec(self.trucksTable.viewport().mapToGlobal(position))
    def deleteItemToTruck(self):
        itemId = self.trucksPartsTable.item(self.trucksPartsTable.selectedIndexes()[0].row(),1).text()
        OilOrItem = self.trucksPartsTable.item(self.trucksPartsTable.selectedIndexes()[0].row(),5).text()
        d = QMessageBox(parent=self,text=f"تأكيد حذف القطعة من الشاحنة")
        d.setIcon(QMessageBox.Icon.Information)
        d.setWindowTitle("تأكيد")
        d.setStyleSheet("background-color:white")
        d.setStandardButtons(QMessageBox.StandardButton.Cancel|QMessageBox.StandardButton.Ok)
        important = d.exec()
        if important == QMessageBox.StandardButton.Ok:
            cr.execute("SELECT carNumber FROM trucks WHERE id = ?",[self.truckIdToShowItemsToTrucks])
            carNumber = str(cr.fetchone()[0])
            if OilOrItem == 'oil':
                cr.execute("Select quantity FROM trucksToOil WHERE oilCode=? and truckId=?",(itemId,self.truckIdToShowItemsToTrucks))
                oilQuantity = cr.fetchone()[0]
                cr.execute("INSERT INTO itemsLifecycle (itemId, date, action) VALUES (?,?,?)",(itemId, str(date.today()).replace('-','/'), f'تم تفريغ {oilQuantity} من الزيت من سيارة رقم {carNumber}'))
            elif OilOrItem == 'item':
                cr.execute("INSERT INTO itemsLifecycle (itemId, date, action) VALUES (?,?,?)",(itemId, str(date.today()).replace('-','/'), f'تم فك القطعة من شاحنة رقم {carNumber} '))
            
            if OilOrItem == 'oil':
                cr.execute("SELECT quantity FROM trucksToOil WHERE oilCode=? and truckId=?",(itemId,self.truckIdToShowItemsToTrucks))
                cr.execute(f"UPDATE oil set remeaningQuantity=remeaningQuantity+{cr.fetchone()[0]} WHERE code=?",[itemId])
                cr.execute("DELETE FROM trucksToOil WHERE oilCode=? and truckId=?",(itemId,self.truckIdToShowItemsToTrucks))
            elif OilOrItem == 'item':
                cr.execute("DELETE FROM trucksParts WHERE itemId=? and truckId=?",(itemId,self.truckIdToShowItemsToTrucks))
            con.commit()
            self.loadItemToTrucks(self.truckIdToShowItemsToTrucks)
            d = QMessageBox(parent=self,text="تم الحذف بنجاح")
            d.setWindowTitle("نجاح")
            d.setIcon(QMessageBox.Icon.Information)
            d.setStyleSheet("background-color:white")
            ret = d.exec()
    def loadItemToTrucks(self,truckIdToShowItemsToTrucks):
        self.totalPriceVar = 0
        self.trucksPartsTable.setRowCount(0)     
        cr.execute("SELECT itemName,itemId,itemPrice,installPlace,installDate FROM trucksParts WHERE truckId = ?",[truckIdToShowItemsToTrucks])
        tempThing = [] 
        for i in cr.fetchall():
            i = list(i)
            i.append("item")
            tempThing.append(i)

        cr.execute("SELECT itemName,oilCode,itemPrice,installPlace,installDate FROM trucksToOil WHERE truckId = ?",[truckIdToShowItemsToTrucks])
        for i in cr.fetchall():
            i = list(i)
            i.append("oil")
            tempThing.append(i)

        for row,i in enumerate(tempThing):
            self.trucksPartsTable.insertRow(self.trucksPartsTable.rowCount())
            for col,val in enumerate(i):
                if col==2:
                    self.totalPriceVar+=float(val)
                self.trucksPartsTable.setItem(row,col,QTableWidgetItem(str(val))) 
        self.totalPriceVar = round(self.totalPriceVar,2)
        self.totalPriceTruck.setText(f"اجمالي الصرف على الشاحنة:{self.totalPriceVar}")
    def showTrucksNote(self):
        try:
            self.showTrucksNoteFrame.deleteLater()
        except:
            pass
        self.truckIdAddNote = self.trucksTable.item(self.trucksTable.selectedIndexes()[0].row(),0).text()
        
        self.showTrucksNoteFrame = QFrame(self.trucksFrame)
        self.showTrucksNoteFrame.setGeometry((self.trucksFrame.width()-450)//2,(self.trucksFrame.height()-400)//2,450,400)
        # self.showTrucksNoteFrame.setStyleSheet("background-color:white;border:2px solid black")
        
        closeButton = QPushButton(self.showTrucksNoteFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(400,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.showTrucksNoteFrame:self.destroyFrame(frame))

        self.showTrucksNoteFrame.setStyleSheet("background-color:white")

        self.notesTable = QTableWidget(self.showTrucksNoteFrame)
        self.notesTable.setGeometry(10,60,410,240)

        self.notesTable.setColumnCount(3)
        self.notesTable.setHorizontalHeaderLabels(["id","الملاحظة", "تاريخ الملاحظة"])
        self.notesTable.setColumnHidden(0,True)
        self.notesTable.setColumnWidth(1, 300)


        self.contextMenuNotesTable = QMenu(self.notesTable)
        self.contextMenuNotesTable.setStyleSheet("background-color:grey")
        self.createButtonNotesTable()

        self.notesTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.notesTable.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.notesTable.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.notesTable.customContextMenuRequested.connect(self.showMenuNotesTable)
        
        addNoteButton = QPushButton("اضافة ملاحظة",self.showTrucksNoteFrame)
        addNoteButton.setStyleSheet("QPushButton {border:2px solid black;font:14pt 'Arial'}QPushButton:hover {background-color:#c8c8c8;}")        
        addNoteButton.setGeometry(120,310,180,31)
        addNoteButton.clicked.connect(self.addNote)

        #End minMenu Buttons style
        self.loadNotes(self.truckIdAddNote)
        self.showTrucksNoteFrame.show()
    def loadNotes(self, truckId):
        self.notesTable.setRowCount(0)     
        cr.execute("SELECT id,note,date FROM trucksNotes WHERE truckId = ?",[truckId])
        tempThing = [] 
        for i in cr.fetchall():
            tempThing.append(i)
        for row,i in enumerate(tempThing):
            self.notesTable.insertRow(self.notesTable.rowCount())
            for col,val in enumerate(i):
                self.notesTable.setItem(row,col,QTableWidgetItem(str(val))) 
    def deleteNote(self):
        noteIdDelete = self.notesTable.item(self.notesTable.selectedIndexes()[0].row(),0).text()
        d = QMessageBox(parent=self,text=f"تأكيد حذف الملاحظة")
        d.setIcon(QMessageBox.Icon.Information)
        d.setWindowTitle("تأكيد")
        d.setStyleSheet("background-color:white")
        d.setStandardButtons(QMessageBox.StandardButton.Cancel|QMessageBox.StandardButton.Ok)
        important = d.exec()
        if important == QMessageBox.StandardButton.Ok:
            cr.execute("DELETE FROM trucksNotes WHERE id=?",[noteIdDelete])
            con.commit()
            self.loadNotes(self.truckIdAddNote)
            d = QMessageBox(parent=self,text="تم الحذف بنجاح")
            d.setWindowTitle("نجاح")
            d.setIcon(QMessageBox.Icon.Information)
            d.setStyleSheet("background-color:white")
            ret = d.exec()
    def addNote(self):
        try:
            self.addNoteFrame.deleteLater()
        except:
            pass
        self.addNoteFrame = QFrame(self.trucksFrame)
        self.addNoteFrame.setGeometry((self.trucksFrame.width()-340)//2,(self.trucksFrame.height()-360)//2,340,360)
        # self.showTrucksNoteFrame.setStyleSheet("background-color:white;border:2px solid black")

        closeButton = QPushButton(self.addNoteFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(290,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.addNoteFrame:self.destroyFrame(frame))

        self.addNoteFrame.setStyleSheet("background-color:white;border: 2px solid black")


        label = QLabel('الملاحظة',self.addNoteFrame)
        label.setStyleSheet("border:0px")
        label.move(150,20)
        label.setFont(QFont("Arial", 16))

        self.notesText = QTextEdit(self.addNoteFrame)
        self.notesText.setGeometry(10,60,320,150)

        label = QLabel('تاريخ الملاحظة',self.addNoteFrame)
        label.setStyleSheet("border:0px")
        label.move(120,230)
        label.setFont(QFont("Arial", 16))

        arabic_locale = QLocale(QLocale.Language.Arabic, QLocale.Country.SaudiArabia)
        
        self.noteDateEntry = QDateEdit(self.addNoteFrame)


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


        completeAddNoteButton = QPushButton("اضافة ملاحظة",self.addNoteFrame)
        completeAddNoteButton.setStyleSheet("QPushButton {border:2px solid black;font:14pt 'Arial'}QPushButton:hover {background-color:#c8c8c8;}")        
        completeAddNoteButton.setGeometry(80,310,180,31)
        completeAddNoteButton.clicked.connect(self.completeAddNote)

        #End minMenu Buttons style
        self.loadNotes(self.truckIdAddNote)
        self.addNoteFrame.show()
    def completeAddNote(self):
        if (len(self.notesText.toPlainText()) > 0): 
            cr.execute("INSERT INTO trucksNotes (truckId,note,date) VALUES (?,?,?)",(self.truckIdAddNote, self.notesText.toPlainText(), self.noteDateEntry.text()))
            con.commit()
            message = QMessageBox(parent=self,text="تمت الاضافة بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
            self.loadNotes(self.truckIdAddNote)
        else:
            message = QMessageBox(parent=self,text="يرجى تعبئة جميع الحقول")
            message.setIcon(QMessageBox.Icon.Critical)
            message.setWindowTitle("فشل")
            message.exec()
    def createButtonNotesTable(self):
        deleteNoteButton = QAction(self.notesTable)
        deleteNoteButton.setIcon(QIcon("assests/deleteNote.png"))
        deleteNoteButton.setText("حذف")
        deleteNoteButton.setFont(QFont("Arial" , 12))
        deleteNoteButton.triggered.connect(self.deleteNote)

        editNoteButton = QAction(self.notesTable)
        editNoteButton.setIcon(QIcon("assests/edit.png"))
        editNoteButton.setText("تعديل")
        editNoteButton.setFont(QFont("Arial" , 12))
        editNoteButton.triggered.connect(self.editNote)
        
        self.contextMenuNotesTable.addAction(deleteNoteButton)
        self.contextMenuNotesTable.addAction(editNoteButton)
    def editNote(self):
        self.noteIdEdit = self.notesTable.item(self.notesTable.selectedIndexes()[0].row(),0).text()
        try:
            self.editNoteFrame.deleteLater()
        except:
            pass
        self.editNoteFrame = QFrame(self.trucksFrame)
        self.editNoteFrame.setGeometry((self.trucksFrame.width()-340)//2,(self.trucksFrame.height()-360)//2,340,360)
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

        cr.execute("SELECT note, date FROM trucksNotes WHERE id=?",[self.noteIdEdit])
        values = cr.fetchall()[0]
        self.notesText.setText(values[0])
        noteDate = str(values[1]).split("/")
        self.noteDateEntry.setDate(QDate(int(noteDate[0]), int(noteDate[1]), int(noteDate[2])))




        completeEditNoteButton = QPushButton("تعديل ملاحظة",self.editNoteFrame)
        completeEditNoteButton.setStyleSheet("QPushButton {border:2px solid black;font:14pt 'Arial'}QPushButton:hover {background-color:#c8c8c8;}")        
        completeEditNoteButton.setGeometry(80,310,180,31)
        completeEditNoteButton.clicked.connect(self.completeEditNote)

        #End minMenu Buttons style
        self.editNoteFrame.show()
    def completeEditNote(self):
        if (len(self.notesText.toPlainText()) > 0): 
            cr.execute("UPDATE trucksNotes set note=?, date=? WHERE id=?",(self.notesText.toPlainText(),self.noteDateEntry.text(),self.noteIdEdit))
            con.commit()
            message = QMessageBox(parent=self,text="تم التعديل بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
            self.loadNotes(self.truckIdAddNote)
        else:
            message = QMessageBox(parent=self,text="يرجى تعبئة جميع الحقول")
            message.setIcon(QMessageBox.Icon.Critical)
            message.setWindowTitle("فشل")
            message.exec()
    def showMenuNotesTable(self, position):
        indexes = self.notesTable.selectedIndexes()
        for index in indexes:
            self.contextMenuNotesTable.exec(self.notesTable.viewport().mapToGlobal(position))
    def exportTruckReport(self):
        filePath = QFileDialog.getExistingDirectory(self,"Select a Directory")
        if len(filePath) > 0:
            cr.execute("SELECT itemName,itemId,itemPrice,installPlace,installDate FROM trucksParts WHERE truckId = ?",[self.truckIdToShowItemsToTrucks])
            values = cr.fetchall() # [()]
            cr.execute("SELECT itemName,oilId,itemPrice,installPlace,installDate FROM trucksToOil WHERE truckId = ?",[self.truckIdToShowItemsToTrucks])
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
            para = doc.add_paragraph().add_run(f"اجمالي الصرف على الشاحنة:{self.totalPriceVar}")
            para.font.name = "Arial"
            para.font.size = docx.shared.Pt(20)
            
            doc.save(f"{filePath}\تقرير شاحنة رقم {self.truckNumber}.docx")
            with suppress_output():
                convert(f"{filePath}\تقرير شاحنة رقم {self.truckNumber}.docx",f"{filePath}\تقرير شاحنة رقم {self.truckNumber}.pdf")
            os.remove(f"{filePath}\تقرير شاحنة رقم {self.truckNumber}.docx")

            message = QMessageBox(parent=self,text="تم التصدير بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
    def deleteTruck(self):
        truckIdDelete = self.trucksTable.item(self.trucksTable.selectedIndexes()[0].row(),0).text()
        d = QMessageBox(parent=self,text=f"تأكيد حذف {self.trucksTable.item(self.trucksTable.selectedIndexes()[0].row(),1).text()}")
        d.setIcon(QMessageBox.Icon.Information)
        d.setWindowTitle("تأكيد")
        d.setStyleSheet("background-color:white")
        d.setStandardButtons(QMessageBox.StandardButton.Cancel|QMessageBox.StandardButton.Ok)
        important = d.exec()
        if important == QMessageBox.StandardButton.Ok:
            cr.execute("DELETE FROM trucks WHERE id=?",[truckIdDelete])
            cr.execute("DELETE FROM trucksNotes WHERE truckId=?",[truckIdDelete])
            cr.execute("DELETE FROM trucksParts WHERE truckId=?",[truckIdDelete])
            cr.execute("DELETE FROM trucksToOil WHERE truckId=?",[truckIdDelete])
            con.commit()
            self.loadTrucks()
            d = QMessageBox(parent=self,text="تم الحذف بنجاح")
            d.setWindowTitle("نجاح")
            d.setIcon(QMessageBox.Icon.Information)
            d.setStyleSheet("background-color:white")
            ret = d.exec()
    def editTruck(self):
        try:
            self.destroyFrame(self.editTruckFrame)
        except:
            pass
        self.idEditTruck = self.trucksTable.item(self.trucksTable.selectedIndexes()[0].row(),0).text()

        self.editTruckFrame = QFrame(self.mainFrame)
        self.editTruckFrame.setGeometry((self.mainFrame.width()-350)//2,(self.mainFrame.height()-506)//2,350,506)
        self.editTruckFrame.setStyleSheet("background-color:white;border:2px solid black")

        closeButton = QPushButton(self.editTruckFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(300,10,41,31)
        closeButton.clicked.connect(lambda x, frame=self.editTruckFrame:self.destroyFrame(frame))
        
        #Start scrolAria
        


        self.frame = QFrame()

        layout = QVBoxLayout()
        self.frame.setLayout(layout)


        label = QLabel("رقم السيارة")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")
        self.carNumberEntry = QLineEdit()
        self.carNumberEntry.setDisabled(True)

        layout.addWidget(label)
        layout.addWidget(self.carNumberEntry)

        label = QLabel("رقم اللوحة")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")

        self.carPlateEntry = QLineEdit()

        layout.addWidget(label)
        layout.addWidget(self.carPlateEntry)

        label = QLabel("استمارة كرت التشغيل")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")
        self.playCardEntry = QLineEdit()

        layout.addWidget(label)
        layout.addWidget(self.playCardEntry)

        label = QLabel("انتهاء الاستمارة")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")


        self.formExpireEntry = QDateEdit()
        self.formExpireEntry.setCalendarPopup(True)
        self.formExpireEntry.setDisplayFormat("yyyy/MM/dd")

        arabic_locale = QLocale(QLocale.Language.Arabic, QLocale.Country.SaudiArabia)

        self.formExpireEntry.setLocale(arabic_locale)
        self.formExpireEntry.setFont(QFont("Arial",12))
        self.formExpireEntry.setStyleSheet("background-color:white;color:black")

        self.todayButton12 = QPushButton("اليوم",clicked=lambda:self.formExpireEntry.calendarWidget().setSelectedDate(QDate().currentDate()))
        self.todayButton12.setStyleSheet("background-color:green;")

        self.formExpireEntry.calendarWidget().layout().addWidget(self.todayButton12)
        self.formExpireEntry.calendarWidget().setSelectedDate(QDate().currentDate())

        layout.addWidget(label)
        layout.addWidget(self.formExpireEntry)

        label = QLabel("انتهاء الفحص الدوري")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';")

        self.examExpireEntry = QDateEdit()
        self.examExpireEntry.setCalendarPopup(True)
        self.examExpireEntry.setDisplayFormat("yyyy/MM/dd")

        self.examExpireEntry.setLocale(arabic_locale)
        self.examExpireEntry.setFont(QFont("Arial",12))
        self.examExpireEntry.setStyleSheet("background-color:white;color:black")

        self.todayButton = QPushButton("اليوم",clicked=lambda:self.examExpireEntry.calendarWidget().setSelectedDate(QDate().currentDate()))
        self.todayButton.setStyleSheet("background-color:green;")

        self.examExpireEntry.calendarWidget().layout().addWidget(self.todayButton)
        self.examExpireEntry.calendarWidget().setSelectedDate(QDate().currentDate())

        layout.addWidget(label)
        layout.addWidget(self.examExpireEntry)

        label = QLabel("انتهاء التأمين")
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

        addButton = QPushButton(text="تعديل")
        addButton.clicked.connect(self.completeEditTruck)
        addButton.setStyleSheet("QPushButton:hover {background-color:#c8c8c8;}")        

        layout.addWidget(addButton)

        self.scroolAria = QScrollArea(self.editTruckFrame)
        self.scroolAria.setWidget(self.frame)
        self.scroolAria.setStyleSheet("border:1px solid gray")
        self.scroolAria.move(20,50)
        self.scroolAria.resize(321,431)

        self.scroolAria.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.scroolAria.setWidgetResizable(True)


        cr.execute(f"SELECT * FROM trucks WHERE id=?",[self.idEditTruck])
        values = cr.fetchall()[0]
        self.carNumberEntry.setText(values[1])
        self.carPlateEntry.setText(values[2])
        self.playCardEntry.setText(values[3])
        
        split = str(values[4]).split('/')
        self.formExpireEntry.setDate(QDate(int(split[0]), int(split[1]), int(split[2])))
        
        split = str(values[5]).split('/')
        self.examExpireEntry.setDate(QDate(int(split[0]), int(split[1]), int(split[2])))

        split = str(values[6]).split('/')
        self.insuranceExpireEntry.setDate(QDate(int(split[0]), int(split[1]), int(split[2])))

        #End scrolAria
        self.editTruckFrame.show()
    def completeEditTruck(self):
        if len(self.carNumberEntry.text()) > 0 and len(self.carPlateEntry.text()) > 0 and len(self.playCardEntry.text()) > 0 and len(self.formExpireEntry.text()) and len(self.examExpireEntry.text()) > 0 and len(self.insuranceExpireEntry.text()) > 0:
            cr.execute("UPDATE trucks set carNumber=?, carPlate=?, playCard=?, formExpire=?, examExpire=?, insuranceExpire=? WHERE id=?",(self.carNumberEntry.text(),self.carPlateEntry.text(),self.playCardEntry.text(),self.formExpireEntry.text(),self.examExpireEntry.text(),self.insuranceExpireEntry.text(), self.idEditTruck))
            con.commit()
            message = QMessageBox(parent=self,text="تم التعديل بنجاح")
            message.setIcon(QMessageBox.Icon.Information)
            message.setWindowTitle("نجاح")
            message.exec()
            self.loadTrucks()
        else:
            message = QMessageBox(parent=self,text="يرجى تعبئة جميع الحقول")
            message.setIcon(QMessageBox.Icon.Critical)
            message.setWindowTitle("فشل")
            message.exec()
    def showMenutrucksTable(self, position):
        indexes = self.trucksTable.selectedIndexes()
        for index in indexes:
            self.contextMenutrucksTable.exec(self.trucksTable.viewport().mapToGlobal(position))
    def destroyFrame(self,frame):
        for i in frame.children():
            i.deleteLater()

        frame.destroy()
        frame.deleteLater()