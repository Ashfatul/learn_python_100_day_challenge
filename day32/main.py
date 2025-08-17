# import smtplib

# my_email = "sandbox.smtp.mailtrap.io"
# my_pass = "f422092661e498"
# with smtplib.SMTP("smtp-relay.brevo.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_pass)
#     connection.sendmail(from_addr="ashfatul.islam@gmail.com", to_addrs="turquoisejaneta@powerscrews.com", msg="Subject: working\n\nworking")


import smtplib

# Mailtrap credentials
my_email = "dbb0227b750917"
my_pass = "f422092661e498"

with smtplib.SMTP("smtp.mailtrap.io", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_pass)
    connection.sendmail(
        from_addr="anyname@example.com",
        to_addrs="receiver@example.com",
        msg="Subject: Test Email\n\nThis is a test email sent to Mailtrap."
    )

print("Email sent to Mailtrap inbox successfully!")




