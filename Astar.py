#4-3 Water Jug Problem
#Naven Prasad (1132702464)
#AI Fundamentals


class Node:
    nodeId =-1

    def __init__(self, data4, data3, cost):
        self.data4 = data4
        self.data3 = data3
        self.cost = cost
        self.parent = None
        Node.nodeId += 1
        self.id = Node.nodeId



    def getData4(self):
        return self.data4

    def setData4(self, val):
        self.data4 = val

    def setData3(self, val):
        self.data3 = val

    def getData3(self):
        return self.data3

    def getCost(self):
        return self.cost

    def setCost(self, val):
        self.cost = val

    def setChild(self, Node):
        self.children.append(Node)

    def setParent(self, Node):
        self.parent = Node

    def getParent(self):
        return self.parent


goalData4 = 2
goalData3 = 0
states = []

######## COMBINATORIAL EXPLOSION CHECK #######
def newState(four,three):
    new = True
    for state in states:
        if state.getData4() == four and state.getData3() == three:
            new = False
    return new

def dispAllStates ():
    print "states: "
    for state in states:
        print state.getData4(),"|", state.getData3()

######### RULES #########
def expandNode(parentNode,childNode):
    four = parentNode.getData4()
    three = parentNode.getData3()

    if four < 4 and newState(4,three) == True:
        childNode.setData4(4)
        childNode.setData3(three)
        print "FILL JUG 4"
        states.append(childNode)
        return childNode
    if three < 3 and newState(four,3) == True:
        childNode.setData4(four)
        childNode.setData3(3)
        print "FILL JUG 3"
        states.append(childNode)
        return childNode
    if four > 0 and newState(0,three) == True:
        childNode.setData4(0)
        childNode.setData3(three)
        print "EMPTY JUG 4"
        states.append(childNode)
        return childNode
    if three > 0 and newState(four,0) == True:
        childNode.setData4(four)
        childNode.setData3(0)
        print "EMPTY JUG 3"
        states.append(childNode)
        return childNode

    if four > 0 and three < 3:
        newFour = four - (3-three)
        if newFour <0:
            newFour = 0
        newThree = (four-newFour)+three
        if newThree >3:
            newThree=3
        if newState(newFour, newThree) == True:
            childNode.setData4(newFour)
            childNode.setData3(newThree)
            print "FILL JUG 3 FROM JUG 4"
            states.append(childNode)
            return childNode

    if three > 0 and four < 4:
        newThree = three - (4-four)
        if newThree < 0:
            newThree = 0
        newFour = (three - newThree)+ four
        if newFour > 4:
            newFour = 4
        if newState(newFour, newThree) == True:
            childNode.setData4(newFour)
            childNode.setData3(newThree)
            print "FILL JUG 4 FROM JUG 3"
            states.append(childNode)
            return childNode

    if  four >0:
        newThree = three + four
        if newThree >3:
            newThree =3
        newFour = 0
        if newState(newFour, newThree) == True:
            childNode.setData4(newFour)
            childNode.setData3(newThree)
            print "EMPTY JUG 4 INTO JUG 3"
            states.append(childNode)
            return childNode

    if  three >0:
        newFour = four + three
        if newFour > 4:
            newFour =4
        newThree = 0
        if newState(newFour, newThree) == True:
            childNode.setData4(newFour)
            childNode.setData3(newThree)
            print "EMPTY JUG 3 INTO JUG 4"
            states.append(childNode)
            return childNode
    else:
        return None

#######



level = 1
branch = []
parentNode = Node(0,0,0)
parentNode.setParent(None)
states.append(parentNode)
branch.append(parentNode)

####### Expand each branch and connect nodes
def expandBranch(parentNode, newBranch, level):
    while True:
        childNode = Node(None,None,level)
        childNode = expandNode(parentNode,childNode)
        if childNode == None:
            break
        newBranch.append(childNode)
        for n in newBranch:
            if n.id != parentNode.id:
                n.setParent(parentNode)
    return newBranch


#A* Search with heuristic
def heuristic(aBranch):
    lowest = Node(100,100,100)
    unopenedNodes = []
    for item in aBranch:
        newCost = item.cost + abs(goalData4 - item.getData4())
        item.setCost(newCost)
        if item.cost <= lowest.cost and item.getData4() < lowest.getData4():
            lowest = item
        else:
            unopenedNodes.append(item)
    return lowest

def genTree():
    a = expandBranch(parentNode, [], 1)
    b = expandBranch(heuristic(a), [], 2)
    c = expandBranch(heuristic(b), [], 3)
    d = expandBranch(heuristic(c), [], 4)
    e = expandBranch(heuristic(d), [], 5)
    f = expandBranch(heuristic(e), [], 6)




#traceBack to top
def traceBack(states):

    finalTrace = []
    for state in states:
        if state.getData4() == goalData4:
            print "FOUND!"
            print state.id, "<---- Found Node ID"
            finalTrace.append(state)
            while state.id != 0:
                state = state.getParent()
                finalTrace.append(state)

    print "---------------------------------------------"
    print "              FINAL SOLUTION                  "
    print "----------------------------------------------"
    finalTrace.reverse()
    for trace in finalTrace:
        print trace.getData4(), "|" , trace.getData3()


#RUN
genTree()
dispAllStates()
traceBack(states)
print "Opened nodes : ", len(states)
