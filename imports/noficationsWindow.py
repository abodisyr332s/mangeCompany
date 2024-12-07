from .stuff import *

class noficationsWindow():
    def showNofications(self):
        try:
            self.destroyFrame(self.noficationsFrame)
        except:
            pass

        self.noficationsFrame = QFrame(self.mainFrame)
        
        self.closeButtonBenefetsFrame = QPushButton(self.noficationsFrame)
        self.closeButtonBenefetsFrame.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        self.closeButtonBenefetsFrame.clicked.connect(lambda x, frame=self.noficationsFrame:self.destroyFrame(frame))

        label = QLabel(parent=self.noficationsFrame, text="التنبيهات")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("border:none;font: 15pt 'Arial';color:red")

        self.noficationsFrame.setStyleSheet("background-color:white")

        self.noficationsTable = QTableWidget(self.noficationsFrame)

        self.noficationsTable.setColumnCount(1)
        self.noficationsTable.setHorizontalHeaderLabels(["التنبيه"])
        self.noficationsTable.setColumnWidth(0,395)

        self.noficationsTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.noficationsTable.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.noficationsTable.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)


        label.move(190,20)
        self.noficationsFrame.setGeometry((self.width()-410)//2,(self.mainFrame.height()-300)//2,410,370)
        self.noficationsTable.setGeometry(10,50,395,300)
        self.closeButtonBenefetsFrame.setGeometry(360,10,41,31)


        self.loadNofications()
        self.noficationsFrame.show()
    def returnNoficationsMessagesToDisplayList(self):
        today = date.today()
        messagesTrucks = []
        messagesDrivers = []
        cr.execute("SELECT formExpire,examExpire,insuranceExpire,carNumber FROM trucks")
        noficationsMessagesToDisplayList = []

        for formExpire, examExpire, insuranceExpire, carNumber in cr.fetchall():


            formExpireAsList = str(formExpire).split('/')
            formExpireDateFormat = date(int(formExpireAsList[0]),int(formExpireAsList[1]),int(formExpireAsList[2]))

            examExpireAsList = str(examExpire).split('/')
            examExpireDateFormat = date(int(examExpireAsList[0]),int(examExpireAsList[1]),int(examExpireAsList[2]))

            insuranceExpireAsList = str(insuranceExpire).split('/')
            insuranceExpireDateFormat = date(int(insuranceExpireAsList[0]),int(insuranceExpireAsList[1]),int(insuranceExpireAsList[2]))

            if today + timedelta(days=14) >= formExpireDateFormat :

                if (formExpireDateFormat - today).days > 0:
                    messagesTrucks.append(f" باقي على انتهاء استمارة كرت التشغيل في الشاحنة رقم{carNumber} {(formExpireDateFormat - today).days} يوم")
                else:
                    messagesTrucks.append(f" الشاحنة رقم {carNumber} منتهي فيها استمارة كرت التشغيل منذ  {(today - formExpireDateFormat).days} يوم")

            if today + timedelta(days=14) >= examExpireDateFormat:
                if (examExpireDateFormat - today).days > 0:
                    messagesTrucks.append(f" باقي على انتهاء الفحص الدوري في الشاحنة رقم {carNumber} {(examExpireDateFormat - today).days} يوم")
                else:
                    messagesTrucks.append(f" الشاحنة رقم {carNumber} منتهي فيها الفحص الدوري منذ {(today - examExpireDateFormat).days} يوم")

            if today + timedelta(days=14) >= insuranceExpireDateFormat:
                if (insuranceExpireDateFormat - today).days > 0:
                    messagesTrucks.append(f" باقي على التأمين في الشاحنة رقم {carNumber} {(insuranceExpireDateFormat - today).days} يوم")
                else:
                    messagesTrucks.append(f" الشاحنة رقم {carNumber} منتهي فيها التأمين منذ {(today - insuranceExpireDateFormat).days} يوم")
            
        for messageTruck in messagesTrucks:
            noficationsMessagesToDisplayList.append(messageTruck)
        
        ##################################
        cr.execute("SELECT identyExpire, insuranceExpire,driverCard, identy FROM drivers")

        for identyExpire, insuranceExpire,driverCardExpire, identy in cr.fetchall():

            identyExpireAsList = str(identyExpire).split('/')
            identyExpireDateFormat = date(int(identyExpireAsList[0]),int(identyExpireAsList[1]),int(identyExpireAsList[2]))

            insuranceExpireAsList = str(insuranceExpire).split('/')
            insuranceExpireDateFormat = date(int(insuranceExpireAsList[0]),int(insuranceExpireAsList[1]),int(insuranceExpireAsList[2]))

            driverCardExpireAsList = str(driverCardExpire).split('/')
            driverCardExpireDateFormat = date(int(driverCardExpireAsList[0]),int(driverCardExpireAsList[1]),int(driverCardExpireAsList[2]))

            if today + timedelta(days=14) >= identyExpireDateFormat :
                if (identyExpireDateFormat - today).days > 0:
                    messagesDrivers.append(f"باقي على انتهاء الاقامة للسائق صاحب الهوية رقم {identy} {(identyExpireDateFormat - today).days} يوم")
                else:
                    messagesDrivers.append(f"الاقامة منتهية للسائق صاحب الهوية رقم {identy} منذ {(today - identyExpireDateFormat).days} يوم")

            if today + timedelta(days=14) >= insuranceExpireDateFormat:
                if (insuranceExpireDateFormat - today).days > 0:
                    messagesDrivers.append(f"باقي على انتهاء التأمين الطبي للسائق صاحب الهوية رقم {identy} {(insuranceExpireDateFormat - today).days} يوم")
                else:
                    messagesDrivers.append(f"التأمين الطبي منتهي للسائق صاحب الهوية رقم {identy} منذ {(today - insuranceExpireDateFormat).days} يوم")

            if today + timedelta(days=14) >= driverCardExpireDateFormat:
                if (driverCardExpireDateFormat - today).days > 0:
                    messagesDrivers.append(f"باقي على انتهاء بطاقة السائق للسائق صاحب الهوية رقم {identy} {(driverCardExpireDateFormat - today).days} يوم")
                else:
                    messagesDrivers.append(f"بطاقة السائق منتهية للسائق صاحب الهوية رقم {identy} منذ {(today - driverCardExpireDateFormat).days} يوم")
        
        for messageDriver in messagesDrivers:
            noficationsMessagesToDisplayList.append(messageDriver)            

        #######################################
        cr.execute("SELECT oilDuration, lubricationDuration, filterDuration FROM noficationsDuration")
        oilDuration, lubricationDuration, filterDuration = cr.fetchall()[0]
        

        cr.execute("SELECT oil, lubrication, filter FROM notifications")
        values = cr.fetchall()

        if values == []:
            cr.execute("INSERT INTO notifications (oil, lubrication, filter) VALUES (?,?,?)", (today + timedelta(days=oilDuration), today + timedelta(lubricationDuration), today+ timedelta(filterDuration)))
            con.commit()
        else:
            oil, lubrication, filterExpire = values[0]
            
            oilAsList = str(oil).split('-')
            lubricationAsList = str(lubrication).split('-')
            filterExpireAsList = str(filterExpire).split('-')

            if (date.today() >= date(int(oilAsList[0]), int(oilAsList[1]), int(oilAsList[2]))):
                noficationsMessagesToDisplayList.append("حان موعد تغيير الزيت")
            if (date.today() >= date(int(lubricationAsList[0]), int(lubricationAsList[1]), int(lubricationAsList[2]))):
                noficationsMessagesToDisplayList.append("حان موعد التشحيم")
            if (date.today() >= date(int(filterExpireAsList[0]), int(filterExpireAsList[1]), int(filterExpireAsList[2]))):
                noficationsMessagesToDisplayList.append("حان موعد تغيير فلتر الديزيل")
        
            if (date.today() > date(int(oilAsList[0]), int(oilAsList[1]), int(oilAsList[2])) + timedelta(days=2)):
                cr.execute("UPDATE notifications SET oil=?",[today + timedelta(days=oilDuration)])
            if (date.today() > date(int(lubricationAsList[0]), int(lubricationAsList[1]), int(lubricationAsList[2]))+ timedelta(days=2)):
                cr.execute("UPDATE notifications SET lubrication=?",[today + timedelta(days=lubricationDuration)])
            if (date.today() > date(int(filterExpireAsList[0]), int(filterExpireAsList[1]), int(filterExpireAsList[2]))+ timedelta(days=2)):
                cr.execute("UPDATE notifications SET filter=?",[today + timedelta(days=filterDuration)])

            con.commit()
        return noficationsMessagesToDisplayList
    def loadNofications(self):
        noficationsMessagesToDisplayList = self.returnNoficationsMessagesToDisplayList()
        self.noficationsTable.setRowCount(0)     
        for row,val in enumerate(noficationsMessagesToDisplayList):
            self.noficationsTable.insertRow(self.noficationsTable.rowCount())
            self.noficationsTable.setItem(row,0,QTableWidgetItem(str(val))) 
