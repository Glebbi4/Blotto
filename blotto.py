import fileinput
import random
import time


class Strategy(object):
    def __init__(self):
        self.strategy = []
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.score = 0

    def __str__(self):
        result = str(self.strategy) + " " + str(self.wins * 1.0 / self.score) +  " " + str(self.draws * 1.0 / self.score) + " "  + str(self.losses * 1.0 / self.score)
        return result

    def setStrategy(self,strategy):
        self.strategy = strategy

    def getStrategy(self):
        return self.strategy

    def changeWins(self, value):
        self.wins += value

    def changeDraws(self, value):
        self.draws += value

    def changeLosses(self, value):
        self.losses += value

    def changeScore(self, value):
        self.score += value

    def getWins(self):
        return self.wins

    def getDraws(self):
        return self.draws

    def getLosses(self):
        return self.losses

    def getScore(self):
        return self.score

    def battle(self,enemy):
        match = 0
        enstrategy = enemy.getStrategy()
        for i in range(0,len(self.strategy)):
            result = self.strategy[i] - enstrategy[i]
            if result < 0:
                match += -1
            if result > 0:
                match += 1
            if result == 0:
                match += 0

        self.changeScore(1)
        enemy.changeScore(1)

        if match > 0:
            self.changeWins(1)
            enemy.changeLosses(1)
        if match < 0:
            self.changeLosses(1)
            enemy.changeWins(1)
        if match == 0:
            self.changeDraws(1)
            enemy.changeDraws(1)

def st_compare_wins(x, y):
   if x.getWins() > y.getWins():
      return -1
   if x.getWins() == y.getWins():
      return 0
   if x.getWins() < y.getWins():
       return 1

def loadStrategies(f):
    firstLine = True
    result = []
    for line in f:
        if firstLine == True:
            firstLine = False
            continue
        begin = 1
        end = line.find('"',2)
        strategy = line[begin:end]
        parts = strategy.split(",")

        one_strategy = []
        for i in range(0,len(parts)):
            temp = int(float(parts[i].strip()))
            one_strategy.append(temp)

        st = Strategy()
        st.setStrategy(one_strategy)
        result.append(st)

    return result

def sumTotal(Arr):
    sum = 0
    for A in Arr:
        sum += A
    return sum

def getStrategy():
    Arr = []
    temp = 100
    param = 0
    COUNT = 100

    for i in range(1, 10):
        if i == 9 and temp > 0:
            Arr.append(COUNT - sumTotal(Arr))
            break
        if temp > 0:
            param = random.randrange(0, temp, 1)
            Arr.append(param)
            temp = temp - param
        else:
            Arr.append(0)
            continue

    if sumTotal(Arr) != COUNT:
        print Arr
        print sumTotal(Arr)
        print 'MISTAKE!'
        exit()
    return Arr


def battle(my, others):
    st_my = Strategy()
    st_my.setStrategy(my)
    others.append(st_my)
    Arr = others
    for i in range(0,len(Arr)-1,1):
        for j in range(i+1, len(Arr),1):
            #print i, j
            Arr[i].battle(Arr[j])

    Arr.sort(st_compare_wins)
    pos = 0
    my_pos = 0
    for param in Arr:
        pos += 1
        if param.getStrategy() == my:
            my_pos = pos
            print "---------------------- my strategy below"
        print pos, param
    print "my place is ", my_pos, my

f1 = open("blotto2_results.csv",'r')
f2 = open("blotto_results.csv",'r')

st1 = loadStrategies(f1)
st2 = loadStrategies(f2)

st = st1 + st2
print len(st)

myst = [3, 16, 3, 17, 2, 17, 21, 18, 3] #[16, 18, 3, 3, 3, 18, 3, 18, 18]

print getStrategy()
battle(myst,st)
