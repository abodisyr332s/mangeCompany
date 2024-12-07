#import modules
from email.message import EmailMessage
import ssl
import smtplib
from .mainWindow import *

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        #load the login window
        uic.loadUi("assests/login.ui",self)
        
        self.changeEmail.clicked.connect(self.changeEmailFun)
        self.changeEmail.setToolTip("تغير الايميل")

        self.changePassword.clicked.connect(self.changePasswordFun)
        self.changePassword.setToolTip("تغير كلمة المرور")

        self.sendPassword.clicked.connect(self.sendPasswordFun)
        self.sendPassword.setToolTip("ارسال كلمة المرور للبريد")

        self.loginButton.clicked.connect(self.login)

        self.loginButton.setShortcut("Return")
        self.passwordEntry.setEchoMode(QLineEdit.EchoMode.Password)
        self.userEntry.setFont(QFont("Arial" , 13))
        self.userEntry.setText("admin")
        self.userEntry.setDisabled(True)
        self.setFixedSize(839,490)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))
    def login(self):
        cr.execute("SELECT username from users WHERE username = ? and password = ?",(self.userEntry.text() , self.passwordEntry.text()))
        value = cr.fetchone()
        if value !=None:
            self.destroy()
            self.close()
            self.mainWindow = MainWindow()
            self.mainWindow.show()
        else:
            message = QMessageBox(parent=self,text="عذرا تأكد من كلمة السر واسم المستخدم")
            message.setIcon(QMessageBox.Icon.Critical)
            message.setWindowTitle("فشل")
            message.exec()
    def sendPasswordFun(self):
        cr.execute("SELECT email from users WHERE username = ?",[self.userEntry.text()])
        email_sender = "abodi3313@gmail.com"
        email_pass = "dduviygcxsmyxekr"

        email_recevier = f"{cr.fetchone()[0]}"
        subjet = "كلمة المرور"
        cr.execute("SELECT password FROM users WHERE username = ?",[self.userEntry.text()])
        body = f"""
        اهلا وسهلا بك في برنامج ادارة المعتمرين بجمعية البصر 
        كلمة سر الدخول هي{cr.fetchone()[0]}
        """

        em = EmailMessage()
        em['From']=email_sender
        em['To']=email_recevier
        em['subject'] = subjet
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender, email_pass)
            smtp.sendmail(email_sender, email_recevier, em.as_string())
        d = QMessageBox(parent=self,text="تم الارسال بنجاح")
        d.setWindowTitle("نجاح")
        d.setIcon(QMessageBox.Icon.Information)
        d.setStyleSheet("background-color:white")
        d.exec()
    def changeEmailFun(self):
        self.changeEmailFrame = QFrame(self)
        self.changeEmailFrame.setWindowTitle(title)
        self.changeEmailFrame.setWindowIcon(QIcon(icon))
        self.changeEmailFrame.setGeometry((self.width() - 280 )//2, (self.height() - 300)//2, 280, 300)
        self.changeEmailFrame.setStyleSheet("background-color:white; border:2px solid black")

        closeButton = QPushButton(self.changeEmailFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(230,10,31,31)
        closeButton.clicked.connect(lambda x:self.changeEmailFrame.deleteLater())

        userLabel = QLabel("اسم المستخدم",self.changeEmailFrame)
        userLabel.setStyleSheet("font:25px Arial;border:none")
        userLabel.move(85,10)

        self.userNameEntry = QLineEdit(self.changeEmailFrame)
        self.userNameEntry.setStyleSheet("font-size:20px;width:240px")
        self.userNameEntry.setText("admin")
        self.userNameEntry.setDisabled(True)
        self.userNameEntry.move(10,50)

        passwordLabel = QLabel("كلمة المرور",self.changeEmailFrame)
        passwordLabel.setStyleSheet("font:25px Arial;border:none")
        passwordLabel.move(85,90)

        self.userPassword = QLineEdit(self.changeEmailFrame)
        self.userPassword.setStyleSheet("font-size:20px;width:240px")
        self.userPassword.move(10,130)
        self.userPassword.setEchoMode(QLineEdit.EchoMode.Password)

        newEmail_label1 = QLabel("الايميل الجديد",self.changeEmailFrame)
        newEmail_label1.setStyleSheet("font:25px Arial;border:none")
        newEmail_label1.move(85,170)

        self.newEmail = QLineEdit(self.changeEmailFrame)
        self.newEmail.setStyleSheet("font-size:20px;width:240px")
        self.newEmail.move(10,210)

        submitButton = QPushButton("تغيير",self.changeEmailFrame,clicked=self.changeEmailComplete)
        submitButton.setStyleSheet("QPushButton {font:20px Arial;width:150px} QPushButton:hover {background-color:#c8c8c8;}")
        submitButton.move(60,260)

        self.changeEmailFrame.show()
    def changeEmailComplete(self):
        cr.execute("SELECT password FROM users WHERE username = ?", [self.userNameEntry.text()])
        curentPassword = cr.fetchone()[0]
        if self.userPassword.text() == curentPassword:
            if len(self.newEmail.text()) != 0:
                cr.execute("UPDATE users SET email =? WHERE username = ?",(self.newEmail.text(), self.userNameEntry.text()))
                d = QMessageBox(parent =self , text="تم تغيير الايميل بنجاح")
                d.setWindowTitle("نجاح")
                d.setIcon(QMessageBox.Icon.Information)
                d.setStyleSheet("background-color:white")
                ret = d.exec()
                con.commit()
                self.changeEmailFrame.destroy()
        else:
            d = QMessageBox(parent=self,text="كلمة المرور خاطئة")
            d.setWindowTitle("ERROR")
            d.setIcon(QMessageBox.Icon.Critical)
            d.setStyleSheet("background-color:white")
            ret = d.exec()
    def changePasswordFun(self):
        self.changePasswordFrame = QFrame(self)
        self.changePasswordFrame.setWindowTitle(title)
        self.changePasswordFrame.setWindowIcon(QIcon(icon))
        self.changePasswordFrame.setGeometry((self.width() - 280 )//2, (self.height() - 300)//2, 280, 300)
        self.changePasswordFrame.setStyleSheet("background-color:white; border:2px solid black")

        closeButton = QPushButton(self.changePasswordFrame)
        closeButton.setStyleSheet("QPushButton {border:2px solid black;font-size:12px;qproperty-icon: url('assests/close.png');qproperty-iconSize: 26px}QPushButton:hover {background-color:#c8c8c8;}")        
        closeButton.setGeometry(230,10,31,31)
        closeButton.clicked.connect(lambda x:self.changePasswordFrame.deleteLater())

        userLabel = QLabel("اسم المستخدم",self.changePasswordFrame)
        userLabel.setStyleSheet("font:25px Arial;border:none")
        userLabel.move(85,10)

        self.userNameEntry = QLineEdit(self.changePasswordFrame)
        self.userNameEntry.setStyleSheet("font-size:20px;width:240px")
        self.userNameEntry.setText("admin")
        self.userNameEntry.setDisabled(True)
        self.userNameEntry.move(10,50)

        passwordLabel = QLabel("كلمة المرور",self.changePasswordFrame)
        passwordLabel.setStyleSheet("font:25px Arial;border:none")
        passwordLabel.move(85,90)

        self.userPassword = QLineEdit(self.changePasswordFrame)
        self.userPassword.setStyleSheet("font-size:20px;width:240px")
        self.userPassword.move(10,130)
        self.userPassword.setEchoMode(QLineEdit.EchoMode.Password)

        newPassword_label1 = QLabel("كلمة المرور الجديدة",self.changePasswordFrame)
        newPassword_label1.setStyleSheet("font:25px Arial;border:none")
        newPassword_label1.move(55,170)

        self.newPassword = QLineEdit(self.changePasswordFrame)
        self.newPassword.setStyleSheet("font-size:20px;width:240px")
        self.newPassword.move(10,210)

        submitButton = QPushButton("تغيير",self.changePasswordFrame,clicked=self.changePassWordComplete)
        submitButton.setStyleSheet("QPushButton {font:20px Arial;width:150px} QPushButton:hover {background-color:#c8c8c8;}")
        submitButton.move(60,260)

        self.changePasswordFrame.show()
    def changePassWordComplete(self):
        cr.execute("SELECT password from users WHERE username = ?",[self.userNameEntry.text()])
        oldPassword = cr.fetchone()[0]

        if oldPassword == self.userPassword.text():
            if len(self.newPassword.text()) > 0:
                cr.execute(f"UPDATE users SET password = '{self.newPassword.text()}' WHERE username = ?",[self.userNameEntry.text()])
                d = QMessageBox(parent =self , text="تم تغيير كلمة المرور بنجاح")
                d.setWindowTitle("نجاح")
                d.setIcon(QMessageBox.Icon.Information)
                d.setStyleSheet("background-color:white")
                ret = d.exec()
                con.commit()
                self.changePasswordFrame.destroy()
        else:
            d = QMessageBox(parent=self,text="كلمة المرور خاطئة")
            d.setWindowTitle("ERROR")
            d.setIcon(QMessageBox.Icon.Critical)
            d.setStyleSheet("background-color:white")
            ret = d.exec()