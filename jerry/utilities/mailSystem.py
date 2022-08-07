from mailjet_rest import Client
from utilities import mailkey
import os
api_secret = mailkey.api_secret
api_key = mailkey.api_key

messagesDict = {
    'hello' : 'Hello, World!',
    'approval' : 'Congratulation , Your registration request is sucessfuly accepted ! Welcome to We-fix-it family',
    'disapproval' : 'Your registeration is disapproved for following reason',
}

messageHead = {
    'hello': 'Hello by We-fix-it ',
    'approval' :'Your registration is Approved',
    'disapproval' : 'Your registration request is Disapproved'

}
sender_mailAddr = mailkey.senderAddr

mailjet = Client(auth=(api_key, api_secret), version='v3.1')


def message(reciever , context , message ):
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
        "Subject":messageHead[context],
        "TextPart":messagesDict[context]+"\n"+ message,
        # "HTMLPart": "<h3>Dear passenger 1, welcome to <a href=\"https://www.mailjet.com/\">Mailjet</a>!</h3><br />May the delivery force be with you!"
        }
    ]
    }
    result = mailjet.send.create(data=data)
    if result.status_code == 200:
        status = 'sucess'
    else:
        status = 'error'
    return status
