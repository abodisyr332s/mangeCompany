from imports.login import *
import ctypes
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False 
def run():
    global app,window
    app = QApplication(sys.argv)
    
    window = LoginWindow()
    window.show()
    
    app.exec()
if __name__ == "__main__":
    if is_admin():
        run()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)