class Price:
    def __init__(self,row) -> None:
        splitted = row.strip().split(';')
        self.date = splitted[0]
        splittedDate = self.date.split('.')
        self.dateYear = int(splittedDate[0])
        self.dateMonth = int(splittedDate[1])
        self.dateDay = int(splittedDate[2])
        self.petrol = int(splitted[1])
        self.diesel = int(splitted[2])
        self.difference = abs(self.petrol-self.diesel)

        if self.dateYear % 4 == 0 and self.dateDay == 24 and self.dateMonth == 2:
            self.leepDay = True
        else:
            self.leepDay = False