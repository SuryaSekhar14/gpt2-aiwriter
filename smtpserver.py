import smtplib
from GPT2_Pytorch_From_scratch import testcall

sender="suryasekhar.b150@gmail.com"        
receiver="suryasekhardatta22@gmail.com"
password="Surya@1412"    

def sendmail():
    subject=testcall.emailsub() 
    data=testcall.emailbody()

    smtpserver=smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(sender,password)
    msg= f'Subject:{subject} \n\n {data}'

    smtpserver.sendmail(sender,receiver,msg)
    print('Sent')
    smtpserver.close()
