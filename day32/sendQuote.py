import smtplib, random, datetime as dt
arryofday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
today = dt.datetime.now()
dayofweek = today.weekday()
with open("quotes.txt", "r") as file:
    quotes = file.readlines()

# test mailtrap

my_email = "dbb0227b750917"
my_pass = "f422092661e498"

for mail in range(1,21):
    with smtplib.SMTP("smtp.mailtrap.io", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(
            from_addr="ashfatul.islam@gmail.com",
            to_addrs="turquoisejaneta@powerscrews.com",
            msg=f"Subject: {arryofday[dayofweek]} Motivation\n\nMotivation #{mail}\n\n{random.choice(quotes)}\n\nHave a nice day :)"
        )