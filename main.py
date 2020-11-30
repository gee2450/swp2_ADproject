import sys
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QWidget

from widgets import (chooseCharacterWidget, loginWidget,
                     signupWidget, gameWidget, resultWidget)
from database import DB

black = (0,0,0)
white = (255,255,255)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.classDb = DB()
        self.idDb = self.classDb.getIdDb()
        self.db = self.classDb.getDb()
        self.set_content("Login")
        self.show()

    def set_info(self, id, password):
        self.id = id
        self.password = password

    def get_info(self):
        return self.id, self.password

    def edit_score(self, score):
        self.score = score
        self.classDb.editScore(self.id, score)

    def db_add(self, dic):
        self.classDb.addDB(dic)

    def get_ranking(self):
        return self.classDb.getRanking()

    def db_reset(self):
        self.classDb.writeDB()
        self.classDb = DB()

    def set_content(self, new_content):
        if new_content == "Login":
            self.content = loginWidget(self, self.idDb, self.db)
            self.layout.addWidget(self.content)
            self.setWindowTitle('CookieRun - Login')
        elif new_content == "SignUp":
            self.content = signupWidget(self, self.idDb)
            self.layout.addWidget(self.content)
            self.setWindowTitle('CookieRun - SIGN UP')
        elif new_content == "Character Choose":
            self.db_reset()
            self.content = chooseCharacterWidget(self)
            self.layout.addWidget(self.content)
            self.setWindowTitle('CookieRun - Choose Character')
        elif new_content == "Game":
            self.content = gameWidget(self)
            self.layout.addWidget(self.content)
            self.setWindowTitle('CookieRun')
        elif new_content == "Result":
            self.classDb.editScore(self, self.score)
            self.db_reset()
            self.content = resultWidget(self)
            self.layout.addWidget(self.content)
            self.setWindowTitle('Result')
        elif new_content == "Finished":
            self.classDb.writeDB()
            QApplication.quit()


if __name__=='__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())


