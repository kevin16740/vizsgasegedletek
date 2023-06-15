class Player:
    def __init__(self,row) -> None:
        splitted = row.strip().split(';')
        self.name = splitted[0]
        self.category = splitted[1]
        self.club = splitted[2]
        self.points = []
        for item in splitted[3:]:
            self.points.append(int(item))
        
    def totalPoints(self):
        orderedPoints = self.points
        orderedPoints.sort()
        sum = 0
        for i in orderedPoints[2:]:
            sum += i
        if orderedPoints[0] != 0:
            sum += 10
        elif orderedPoints[1] != 0:
            sum += 10
        return sum