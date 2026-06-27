import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
#------------------------------------------------------------------
# 1. File renaming module
#------------------------------------------------------------------
def rename_files(directory, prefix = "file"):
    for i, filename in enumerate(os.listdir(directory), start=1):
        old_path = os.path.join(directory, filename)
        if os.path.isfile(old_path):
            ext = os.path.splitext(filename)[1]
            new_name = f"{prefix}_{i}{ext}"
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} to {new_name}")

#------------------------------------------------------------------
# 2. File downloading module
#------------------------------------------------------------------
def download_file(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {save_path}")
    else:
        print(f"Failed to download: {url}")

#------------------------------------------------------------------
# 3. Email sending module
#------------------------------------------------------------------
def send_email(sender, password, recipient, subject, body, attachment_path=None):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    if attachment_path:
        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
            msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

#------------------------------------------------------------------
# Main function to demonstrate the modules
#------------------------------------------------------------------
if __name__ == "__main__":
    # Example usage of the modules
    # 1. Rename files in a directory
    rename_files(r"C:\Users\Vexy Technology\Desktop\Bantu AI\Symptom_checker\ML projects\downloads", prefix="report")

    # 2. Download a file from a URL
    download_file("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf", r"C:\Users\Vexy Technology\Desktop\Bantu AI\Symptom_checker\ML projects\downloads\sample.pdf")

    # 3. Send an email with an optional attachment
    send_email(
        sender="ursalasyanyaka@gmail.com",
        password="ouwcuwirszqtpwae",
        recipient="ursulaenterprise@gmail.com",
        subject="automated report",
        body="This is the latest automated report.",
        attachment_path=r"C:\Users\Vexy Technology\Desktop\Bantu AI\Symptom_checker\ML projects\downloads\sample.pdf"
    )