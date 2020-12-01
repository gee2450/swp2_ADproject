import pickle

class DB():
    dbfilename = 'DB.dat'
    db = [] # id, pw, score db
    idDb = [] # id db

    def __init__(self):
        fh = open(self.dbfilename, 'rb')
        self.db = pickle.load(fh)
        # id 모음 리스트 생성
        for i in self.db:
            self.idDb.append(i['id'])
        fh.close()

    # 입력 id, password, score로 DB 추가
    def addDB(self, dic):
        self.db.append(dic)

    # db score 입력 점수로 초기화
    def editScore(self, id, score):
        for i in self.db:
            if i['id'] == id:
                if i['score']<int(score):
                    i['score'] = int(score)
                break

    # 마지막으로 data 저장
    def writeDB(self):
        fh = open(self.dbfilename, 'wb')
        pickle.dump(self.db, fh)
        fh.close()

    def getDb(self):
        return self.db

    def getIdDb(self):
        return self.idDb

    def getRanking(self):
        x = sorted(self.db, key=lambda x: x['score'], reverse = True)
        return x


if __name__=='__main__':
    db = DB()
    db.addDB({"id":'1', 'password':'2', 'score':10})
    print(db.db)
    db.editScore('1',50)
    print(db.db)