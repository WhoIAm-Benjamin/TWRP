from PySide2 import QtWidgets, QtGui, QtCore
import design

import subprocess
import sys

args = sys.argv

'''
subprocess.call("adb reboot bootloader")
input()
subprocess.call(["adb flash recovery", args[1]])
input()
'''

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        find_device = self.find_device
        trwp = self.twrp_start
        find_device.clicked.connect(self.finder)

    def finder(self):
        devices = None
        subprocess.Popen(["adb", "devices"], shell=False, stdout=devices)
        self.list_devices.addItem(devices)


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = App()
    window.show()
    sys.exit(app.exec_())
