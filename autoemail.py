import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.headerregistry import Address


def data():
	data = pd.read_csv(r'C:\Users....' ) # Location to your csv file 
	df = pd.DataFrame(data) # Converting the data to usable dataframe
	l = df['email'].tolist() # Then fetching the coloumn and converting that to list
	return l

def email():
	#example emails
	#to_addList = ['abc@gmail.com', '123@gmail.com']
	to_addList = data() # Fetching the data from data function

	# Subject of the email
	email_subject = 'Hi there'
	email_from = '"Vishnu"'
	from_add = '799vishnu530@gmail.com'
	# to get temporay password from email ans use it in your python code get your password from your gmail account Watch this video for reference https://www.youtube.com/watch?v=qk8nJmIRbxk
	password= 'abcxyz' #ofcourse not my password
	# body of the email using html so that we can style the email accordingly
	email_body = """
					<html>
					<head></head>
					<body>
					Greetings!
					<br>
					<br>
					This is Vishnu. 

					<br>
					<br>
					This is my example email template using python to send automatic emails
					
					<br>
					Thank you
					<br>
					<br>
					--
					<br>
					<a href="https://my-project-2168c.web.app/">Vishnu</a>
					</body>
					</html>
	"""

	# Use loops and intialise the object each and everytime for new everyemail id. So that it will ensure that the emails are sent in a separate threads
	for to_add in to_addList:
		#Initalise the object
		msg = MIMEMultipart('alternative')
		msg['Subject'] = email_subject
		msg['From'] = email_from
		msg['To'] = to_add
		msg1 = MIMEText(email_body ,'html')
		msg.attach(msg1)

		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(from_add, password)
		server.sendmail(from_add, to_add, msg.as_string())
		server.quit()
		
		print('Mail sent to ', to_add)

def main():
	email()

if __name__=="__main__":
    main()