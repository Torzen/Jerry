import mailkey
from mailjet_rest import Client
class mailTemplate:
        headings = {
            "hello" : "Hello",
            'userRegistration' : "Your registration Code",
        }

        def userRegistration(self,message):
            self.msg = f'''{__class__.headings['userRegistration']}\n\t{message}           
            '''
            return self.msg             
            
        def userLogin(self ,message):
            self.msg = f'''{__class__.headings['userLogin']}\n\t{message}            
            '''
            return self.msg


class Mail(mailTemplate):


    api_key = mailkey.api_key
    api_secreat = mailkey.api_secret

    def __init__(self , recieverAddr , type , message):
        self.recieverAddr = recieverAddr
        self.messageType = type
        self.msg = message

    def message(self , reciever,subject,message):
        data = {
        'Messages': [
            {
            "From": {
                "Email": mailkey.senderAddr,
                "Name": 'WE-Fix-It Mail Support'
            },
            "To": [
                {
                "Email": reciever,
                "Name": 'You'
                }
            ],
            "Subject":subject,
            "TextPart":message,
            }
        ]
        }
        mailjet = Client(auth=(mailkey.api_key , mailkey.api_secret), version='v3.1')
        result = mailjet.send.create(data=data)
        return result.status_code


    def userRegistration(self):
        result = self.message(self.recieverAddr ,"User Regisstration Code",super().userRegistration(self.msg))
        if result == 200:
            return "sucess"
        else:
            return "Error"

    def userLogin(self):
        pass


if __name__ == "__main__":
    a = Mail("anjalishahjhau12345@gmail.com","hello","Good day")
    print(a.userRegistration())
    