class Users(object):
    def __init__(self, username, password, first_name, 
    last_name, passport_id, pic_id):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.passport_id = passport_id
        self.pic_id = pic_id
    
    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password
    def getFirstName(self):
        return self.first_name
    def getLastName(self):
        return self.last_name
    def getPassportId(self):
        return self.passport_id
    def getPicId(self):
        return self.pic_id