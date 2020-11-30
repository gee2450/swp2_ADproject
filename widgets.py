from PyQt5.QtWidgets import QLineEdit, QHBoxLayout, QVBoxLayout, QWidget, QPushButton,  QGroupBox, QLabel
from PyQt5.QtWidgets import QGridLayout, QTextEdit
from PyQt5.QtGui import QPixmap
import os

from game import game

characterList = [
    "벚꽃맛 쿠키",
    "블랙베리맛 쿠키",
    "양파맛 쿠키",
]
characterIntroduce = [
    "달리기 속도가 빠르다",
    "체력 감소가 느리다",
    "달리기 점수가 추가된다",
]
# db example
"""
idDb = ['gee2450']
db = [{'id': 'id1', 'password': 'pw1', 'score': 1}, ]
"""

class loginWidget(QWidget):
    def __init__(self, parent, db_idDb, db_db):
        super().__init__()
        self.parent = parent

        self.idDb = db_idDb
        self.db = db_db

        # LineEdit and Button
        self.idEdit = QLineEdit()
        self.idEdit.setFixedSize(400,40)
        self.passwordEdit = QLineEdit()
        self.passwordEdit.setFixedSize(400,40)
        login = QPushButton("LOGIN", self)
        login.setFixedSize(215,40)
        login.clicked.connect(self.loginClicked) # 함수 세분화
        signup = QPushButton("SIGNUP", self)
        signup.setFixedSize(215,40)
        signup.clicked.connect(self.signUpClicked) # 함수 세분화

        # Layout
        idLayout = QHBoxLayout()
        idLayout.addWidget(QLabel('ID: '))
        idLayout.addWidget(self.idEdit)
        passwordLayout = QHBoxLayout()
        passwordLayout.addWidget(QLabel('PW: '))
        passwordLayout.addWidget(self.passwordEdit)
        loginSignupLayout = QHBoxLayout()
        loginSignupLayout.addWidget(login)
        loginSignupLayout.addWidget(signup)

        # Login Layout
        LoginLayout = QVBoxLayout()
        LoginLayout.addLayout(idLayout)
        LoginLayout.addLayout(passwordLayout)
        LoginLayout.addLayout(loginSignupLayout)

        # Set Window
        self.setLayout(LoginLayout)

        self.show()

    def loginClicked(self):
        if self.idEdit.text() not in self.idDb:
            self.idEdit.clear()
            self.idEdit.setPlaceholderText("Wrong ID")
            return
        if self.passwordEdit.text() != self.db[self.idDb.index(self.idEdit.text())]['password']:
            self.passwordEdit.clear()
            self.passwordEdit.setPlaceholderText("Wrong PW")
            return

        self.parent.set_info(self.idEdit.text(), self.passwordEdit.text())
        self.close()
        self.parent.set_content("Character Choose")

    def signUpClicked(self):
        self.close()
        self.parent.set_content("SignUp")

class signupWidget(QWidget):
    def __init__(self, parent, db_idDb):
        super().__init__()
        self.parent = parent

        self.idDb = db_idDb

        # LineEdit and Button
        self.idEdit = QLineEdit()
        self.idEdit.setFixedSize(400,40)
        self.passwordEdit = QLineEdit()
        self.passwordEdit.setFixedSize(400,40)
        self.rePasswordEdit = QLineEdit()
        self.rePasswordEdit.setFixedSize(400, 40)
        self.signup = QPushButton("SIGNUP", self)
        self.signup.clicked.connect(self.signUpClicked)

        # Layout
        idLayout = QHBoxLayout()
        passwordLayout = QHBoxLayout()
        rePasswordLayout = QHBoxLayout()
        idLayout.addWidget(QLabel('ID: '))
        idLayout.addWidget(self.idEdit)
        passwordLayout.addWidget(QLabel('PW: '))
        passwordLayout.addWidget(self.passwordEdit)
        rePasswordLayout.addWidget(QLabel('PW re-Check: '))
        rePasswordLayout.addWidget(self.rePasswordEdit)

        # Main Layout
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(idLayout)
        mainLayout.addLayout(passwordLayout)
        mainLayout.addLayout(rePasswordLayout)
        mainLayout.addWidget(self.signup)

        # Set Window
        self.setLayout(mainLayout)

        self.show()

    def signUpClicked(self):
        if self.idEdit.text() in self.idDb:
            self.idEdit.clear()
            self.idEdit.setPlaceholderText("Duplicate ID")
            return
        if self.passwordEdit.text() != self.rePasswordEdit.text():
            self.passwordEdit.clear()
            self.rePasswordEdit.clear()
            self.passwordEdit.setPlaceholderText("PW != rePW")
            self.rePasswordEdit.setPlaceholderText("PW != rePW")
            return

        self.parent.set_info(self.idEdit.text(), self.passwordEdit.text())
        self.parent.db_add({'id':self.idEdit.text(),
                            'password':self.passwordEdit.text(),
                            'score':0})
        self.close()
        self.parent.set_content("Character Choose")

class chooseCharacterWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        # characters
        characterOneLayout = QVBoxLayout()
        characterOneImage = QLabel(self)
        pixmap = QPixmap(os.path.join("images/CherryBlossom/CherryBlossomCookie.png"))
        characterOneImage.resize(140, 140)
        characterOneImage.setPixmap(pixmap.scaled(characterOneImage.size()))
        characterOneEdit = QLineEdit()
        characterOneEdit.setText(characterIntroduce[0])
        characterOneEdit.setReadOnly(True)
        self.charaterOneButton = QPushButton(characterList[0], self)
        self.charaterOneButton.clicked.connect(self.buttonClicked)
        characterOneLayout.addWidget(characterOneImage)
        characterOneLayout.addWidget(characterOneEdit)
        characterOneLayout.addWidget(self.charaterOneButton)

        characterTwoLayout = QVBoxLayout()
        characterTwoImage = QLabel(self)
        pixmap = QPixmap(os.path.join("images/BlackBerry/BlackBerryCookie.png"))
        characterTwoImage.resize(140, 140)
        characterTwoImage.setPixmap(pixmap.scaled(characterTwoImage.size()))
        characterTwoEdit = QLineEdit()
        characterTwoEdit.setText(characterIntroduce[1])
        characterTwoEdit.setReadOnly(True)
        self.charaterTwoButton = QPushButton(characterList[1], self)
        self.charaterTwoButton.clicked.connect(self.buttonClicked)
        characterTwoLayout.addWidget(characterTwoImage)
        characterTwoLayout.addWidget(characterTwoEdit)
        characterTwoLayout.addWidget(self.charaterTwoButton)

        characterThreeLayout = QVBoxLayout()
        characterThreeImage = QLabel(self)
        pixmap = QPixmap(os.path.join("images/Onion/OnionCookie.png"))
        characterThreeImage.resize(140, 140)
        characterThreeImage.setPixmap(pixmap.scaled(characterThreeImage.size()))
        characterThreeEdit = QLineEdit()
        characterThreeEdit.setText(characterIntroduce[2])
        characterThreeEdit.setReadOnly(True)
        self.charaterThreeButton = QPushButton(characterList[2], self)
        self.charaterThreeButton.clicked.connect(self.buttonClicked)
        characterThreeLayout.addWidget(characterThreeImage)
        characterThreeLayout.addWidget(characterThreeEdit)
        characterThreeLayout.addWidget(self.charaterThreeButton)

        # main character choose layout
        ChooseCharacterLayout = QHBoxLayout()
        ChooseCharacterLayout.addLayout(characterOneLayout)
        ChooseCharacterLayout.addLayout(characterTwoLayout)
        ChooseCharacterLayout.addLayout(characterThreeLayout)

        self.setLayout(ChooseCharacterLayout)

        self.show()

    def buttonClicked(self):
        global character
        character = self.sender().text()
        self.close()
        self.parent.set_content("Game")

class gameWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        global character

        self.id, self.password = self.parent.get_info()

        ranking = self.parent.get_ranking()
        for i in range(len(ranking)):
            if ranking[i]['id'] == self.id:
                bestScore = ranking[i]['score']
                myRanking = i+1

        # my best score : xxxx , current score : xxxx , current ranking : xx
        myBestScore = QGroupBox('My Best Score')
        myBestScoreEdit = QLineEdit()
        myBestScoreEdit.setReadOnly(True)
        myBestScoreEdit.setText(str(bestScore))
        layout = QHBoxLayout()
        layout.addWidget(myBestScoreEdit)
        myBestScore.setLayout(layout)

        currentRanking = QGroupBox('Ranking')
        currentRankingEdit = QLineEdit()
        currentRankingEdit.setReadOnly(True)
        currentRankingEdit.setText(str(myRanking))
        layout = QHBoxLayout()
        layout.addWidget(currentRankingEdit)
        currentRanking.setLayout(layout)

        # game main layout
        self.gameLayout = QGridLayout()
        self.gameLayout.addWidget(myBestScore, 0,0)
        self.gameLayout.addWidget(currentRanking, 0,1)
        # self.gameLayout.add   (gameWindow)

        # Set Window
        self.setLayout(self.gameLayout)

        self.show()

        self.game()

    def game(self):
        mainGame = game(character)
        result = mainGame.mainGame()
        if result == True:
            global score
            score = mainGame.getScore()
            self.gameFinished()

    def gameFinished(self):
        self.close()
        global score
        self.parent.edit_score(score)
        self.parent.set_content("Result")

class resultWidget(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent

        global score

        # game result layout
        scoreEdit = QLineEdit()
        scoreEdit.setReadOnly(True)
        scoreEdit.setText(str(score))
        restartButton = QPushButton('ReStart', self)
        restartButton.clicked.connect(self.restartButtonClicked)
        finishButton = QPushButton('Finish', self)
        finishButton.clicked.connect(self.finishButtonClicked)

        characterImage = QLabel(self)
        if character == "벚꽃맛 쿠키": file = "CherryBlossom"
        elif character == "블랙베리맛 쿠키": file = "BlackBerry"
        elif character == "양파맛 쿠키": file = "Onion"
        pixmap = QPixmap(os.path.join("images/" + file + "/finish6.png"))

        gameResultLayout = QGridLayout()
        gameResultLayout.addWidget(QLabel("게임결과"),0,0,1,2)
        gameResultLayout.addWidget(scoreEdit, 1,0,1,2)
        characterImage.resize(140, 140)
        characterImage.setPixmap(pixmap.scaled(characterImage.size()))
        gameResultLayout.addWidget(characterImage, 2,0)
        gameResultLayout.addWidget(restartButton, 3,0)
        gameResultLayout.addWidget(finishButton, 3,1)

        # ranking layout
        rankingEdit = QTextEdit()
        rankingEdit.setReadOnly(True)
        rankList = self.parent.get_ranking()
        x =''
        for rank in range(len(rankList)):
            x = x + str(rank+1) + '위. ' + rankList[rank]['id'] + \
                '      ' + str(rankList[rank]['score']) +'\n'
        rankingEdit.setText(x)
        rankingLayout = QVBoxLayout()
        rankingLayout.addWidget(QLabel("현재 순위"))
        rankingLayout.addWidget(rankingEdit)


        # main result layout
        resultLayout = QHBoxLayout()
        resultLayout.addLayout(gameResultLayout)
        resultLayout.addLayout(rankingLayout)

        # Set Window
        self.setLayout(resultLayout)

        self.show()

    def restartButtonClicked(self):
        self.close()
        self.parent.set_content("Game")

    def finishButtonClicked(self):
        self.close()
        self.parent.set_content("Finished")