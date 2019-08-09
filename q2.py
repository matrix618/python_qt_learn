import sys
from PyQt5.QtWidgets import QApplication,QWidget


if __name__=='__main__':
    
    app=QApplication(sys.argv)

    try:
        if len(sys.argv) < 2:
            raise ValueError
        else:
            title = " ".join(sys.argv[1:])
    except ValueError:
        title = "我的界面"

    w=QWidget()
    w.resize(500,300)
    w.move(1800,100)
    w.setWindowTitle(title)
    w.show()

    sys.exit(app.exec_())









