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

class Place(object):
    
    def __init__(self,name,location,price,review):#nut
        self.nameofplace= nameofplace
        self.location   = location
        self.price      = price
        self.review     = review
        
class Accommodation(object):#korn
    
    def __init__(self,nameofacc,location,promotion,review):
        self.nameofacc      = nameofacc
        self.location       = location
        self.promotion      = promotion
        self.review         = review
        
class Gallery(object):#tops
    def __init__(self,picture,message,video):
        self.picture = picture
        self.message = message
        self.video   = video

class Promotion(object):#Petch
    def __init__(self,price,location,condition,accommodation):
        self.price           = price
        self.location        = location
        self.condition       = condition
        self.accommodation   = accommodation

class Trip(object):#Tuk
    def __init__(self,user, gallory, accommodation, place, promotion, plan, tag, chat):
        self.user           = user
        self.gallory        = gallory
        self.accommodation  = accommodation
        self.place          = place
        self.promotion      = promotion
        self.plan           = plan
        self.tag            = tag
        self.chat           = chat