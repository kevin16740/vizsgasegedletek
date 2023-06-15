class User:
    def __init__(self,row:str) -> None:
        #id;name;email;phone;department;job_title
        splitted = row.split(';')
        self.id = splitted[0]
        self.name = splitted[1]
        self.email = splitted[2]
        self.phone = splitted[3]
        self.department = splitted[4]
        self.job_title = splitted[5]
        splitted_phone = self.phone.split(' ')
        self.area = splitted_phone[0] 