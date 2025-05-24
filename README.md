# AutoMailer

A simple Python script to send automated HTML emails to multiple recipients using SMTP and a CSV file. This tool is ideal for sending newsletters, announcements, invitations, or any bulk emails with a customizable HTML body.

## 🚀 Features

- Sends HTML-formatted emails to a list of recipients
- Uses Gmail's SMTP server for email dispatch
- Reads email addresses from a CSV file
- Logs success messages for each email sent

## 📂 Project Structure

BulkEmailSender/
├── email_sender.py         # Main Python script
├── recipients.csv          # CSV file containing email addresses
└── README.md               # Project documentation

## 🛠️ Requirements

- Python 3.x
- `pandas` module

Install dependencies with:

```bash
pip install pandas

📄 Setup Instructions
	1.	Clone the Repository

git clone https://github.com/your-username/BulkEmailSender.git
cd BulkEmailSender

	2.	Update Your Credentials

In the email_sender.py file:

from_add = 'your-email@gmail.com'
password = 'your-app-password'

⚠️ Use an App Password: You must enable 2-Step Verification for your Gmail account and generate an App Password for this to work.

	3.	Prepare Your CSV File

Ensure recipients.csv exists in the project folder with the following format:

email
recipient1@example.com
recipient2@example.com
...

	4.	Run the Script

python email_sender.py

📨 Email Content

The email body is written in HTML for better formatting. You can customize it in the script:

<html>
  <body>
    Greetings!<br><br>
    This is Vishnu.<br><br>
    This is my example email template using Python to send automatic emails.<br><br>
    Thank you!<br><br>
    --<br>
    <a href="https://my-project-2168c.web.app/">Vishnu</a>
  </body>
</html>

✅ Output

The script prints a confirmation message for each successful email sent:

Mail sent to recipient1@example.com
Mail sent to recipient2@example.com
...

🛡️ Security Note
	•	Never share your email or app password in a public repository.
	•	Consider using environment variables or a .env file to manage sensitive data securely.

📃 License

This project is licensed under the MIT License. You are free to use, modify, and distribute it.

⸻

Happy Emailing! 💌
