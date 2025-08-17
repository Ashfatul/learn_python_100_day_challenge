import smtplib, random, datetime as dt, pandas as pd

today = dt.datetime.today()
day = today.day
month = today.month
year = today.year

my_email = "dbb0227b750917"
my_password = "f422092661e498"

data = pd.read_csv("friendList.csv")
todayBirthday = data[(data.day == day) & (data.month == month)]

def wishFriend(data):
    age = year - data['year']
    def get_ordinal(age):
        if 11 <= age % 100 <= 13:
            return "th"
        last_digit = age % 10
        if last_digit == 1:
            return "st"
        elif last_digit == 2:
            return "nd"
        elif last_digit == 3:
            return "rd"
        else:
            return "th"
    subject_line = f"Happy {age}{get_ordinal(age)} Birthday, {data['name']}"
    footer = "\n\nYour Friend\nPython Program"
    with(open("wishlist.txt", "r") as wishes):
        pickedWish = random.choice(wishes.readlines())
        pickedWish = pickedWish.encode('ascii', errors='ignore').decode('ascii')

        
    with smtplib.SMTP("smtp.mailtrap.io", 587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr="ashfatul.islam@gmail.com",
            to_addrs=data['email'],
            msg=f"Subject: {subject_line}\n\nDear {data['name']},\n{pickedWish}\n{footer}"
        )


for index, row in todayBirthday.iterrows():
    wishFriend(row)
