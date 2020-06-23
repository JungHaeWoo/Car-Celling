class Score:
    
    def __init__(self, data):
        items = data.split(',')

        self._sid = items[0] #학생번호
        self._name = items[1] #학생이름
        self._kor = int(items[2]) # 국어점수
        self._eng = int(items[3]) # 영어점수
        self._math = int(items[4]) #수학점수

    @property
    def sid(self):
        return self._sid

    @property
    def name(self):
        return self._name

    @property
    def kor(self):
        return self._kor

    @property
    def eng(self):
        return self._eng

    @property
    def math(self):
        return self._math

    @property        #총점
    def total(self): 
        return self._kor + self._eng + self._math
        
    @property        #평균
    def avg(self): 
        return (self._kor + self._eng + self._math) / 3