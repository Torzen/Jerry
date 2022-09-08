import hashlib
import mailkey
import randoms
class Mail:


    api_key = mailkey.api_key
    api_secreat = mailkey.api_secret
    rndom = randoms()



    class mailTemplate:
        headings = {
            "hello" : "Hello",
            'userRegistration' : "Your registration Code"
        }

        def userRegistration(self,message):
            self.msg = f'''{__class__.headings['userResgistration']}\n\t{message}           
            '''
            return self.msg             
            
        def userLogin(self ,message):
            self.msg = f'''{__class__.headings['userLogin']}\n\t{message}            
            '''
            return self.msg

    def __init__(self , recieverAddr , type , message):
        self.recieverAddr = recieverAddr
        self.messageType = type
        self.message = message

    def userRegistration(self):
        self.registrationApprovalcode = randoms.userApprovalRandom()

        
    def userLogin(self):
        pass
