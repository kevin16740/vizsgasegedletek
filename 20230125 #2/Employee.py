class Employee:
    def __init__(self,row) -> None:
        splittedData = row.strip().split(';')
        self.name = splittedData[0]
        self.department = splittedData[1]
        self.category = int(splittedData[2])
        self.amount = int(splittedData[3])