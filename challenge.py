import random
from unicodedata import lookup
vowel=['a','e','i','o','u','y']
capvow=list('AEIOUY')
consonant=list('bcdfghjklmnprstvyz')
capcon=list('BCDFGHJKLMNPRSTVWYZ')
specialbeg=['tr','th','st','ph', 'nt', 'ch', 'qu', 'sh']
capspec=['Tr', 'Th', 'St', 'Ph', 'Ch', 'Qu', 'Sh' ]
global emailIdentitySender
global emailIdentityReceiver
def make_random_name(n=5):
    nameList=[]
    weird=0
    lettype=random.choice([capvow, capcon, capspec]) #Determines whether beginning is a vowel or consonant.
    coolcoolcool=['', '']
    while (len(list(''.join(coolcoolcool))))<n: #Is the current list of letters longer than the desired length?
        if coolcoolcool[-1]=='y': #Ensures that 'y' is not repeated twice.
            letter=random.choice(list(filter(lambda x: x!='y', lettype)))
        else:	
            letter=random.choice(lettype)
        coolcoolcool.append(letter)
        if lettype==vowel or lettype==capvow:
            if len(coolcoolcool)>4:
                lettype=random.choice([consonant, specialbeg])
            else:
                lettype=consonant
        else:
            lettype=vowel
        if (len(list(''.join(coolcoolcool))))+1==n and (lettype==consonant or lettype==specialbeg):
            coolcoolcool.append(random.choice(list(filter(lambda x: x!='tr', filter(lambda x: x!='o', lettype)))))
        name =''.join(coolcoolcool)
        if name in nameList:
            make_random_name()
            weird+=1
        if weird==3:
            make_random_name(7)
            weird=0
            nameList.append(name)
    return name
        
def translate_name_sender(email):
    random_name=make_random_name()
    from_email = email.split()[1]
    emailIdentitySender=[from_email,random_name]
    return emailIdentitySender

def translate_name_receiver(email):
    random_name=make_random_name()
    to_email = email.split()[3]
    emailIdentityReceiver=[to_email,random_name]
    return emailIdentityReceiver

def email_starter(email):
    global emailIdentitySender
    global emailIdentityReceiver
    emailIdentitySender=translate_name_sender(email)
    emailIdentityReceiver=translate_name_receiver(email)
    print("from:",emailIdentitySender[0])
    print("to:",emailIdentityReceiver[1])
    subject_str=""
    emailList=email.split()
    text_str=""
    for i in email.split()[5:emailList.index('text:')]:
            subject_str=subject_str+" "+i
    print("subject:"+subject_str)
    for i in email.split()[emailList.index('text:')+1:]:
        text_str=text_str+" "+i
    print("text:"+text_str)
    print("\n")
    received_email(emailIdentitySender[1],emailIdentityReceiver[0],email)

def received_email(sender,receiver,email):
    print("from:",sender)
    print("to:",receiver)
    subject_str=""
    emailList=email.split()
    text_str=""
    for i in email.split()[5:emailList.index('text:')]:
            subject_str=subject_str+" "+i
    print("subject:"+subject_str)
    for i in email.split()[emailList.index('text:')+1:]:
        text_str=text_str+" "+i
    print("text:"+text_str)

def email_maker(emailIdentitySender,emailIdentityReceiver,email):
    print("from:",emailIdentityReceiver[1])
    print("to:",emailIdentitySender[0])
    subject_str=""
    emailList=email.split()
    text_str=""
    for i in email.split()[5:emailList.index('text:')]:
            subject_str=subject_str+" "+i
    print("subject:"+subject_str)
    for i in email.split()[emailList.index('text:')+1:]:
        text_str=text_str+" "+i
    print("text:"+text_str)
    print("\n")
    char_email=list(email)

def email_maker_caller(email):
       global emailIdentitySender
       global emailIdentityReceiver
       emailIdentitySender = emailIdentityReceiver
       emailIdentityReceiver = emailIdentitySender
       email_maker(emailIdentitySender,emailIdentityReceiver,email)
       
       
       
            
    
    
    

