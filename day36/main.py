from email import message
import os, datetime as dt, requests, smtplib

week_day_array = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
today = dt.datetime.now()
day = today.day
weekday = today.weekday()

data_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "apikey": "demo"
}
request = requests.get('https://www.alphavantage.co/query', params=data_params)
request.raise_for_status()
response = request.json()
date_list = list(response["Time Series (Daily)"])

day1 = date_list[0]
day2 = date_list[1]

my_email = "dbb0227b750917"
my_pass = "f422092661e498"

day1close = response["Time Series (Daily)"][day1]["4. close"]
day2close = response["Time Series (Daily)"][day2]["4. close"]

status = (float(day1close) / float(day2close)) * 100 + 50

# if round(status, 2) > 110:
#     message = "Great new your stock has high value you can sell it \n\n enjoy"
# else:
#     message = "It's not good time to sell stock\nkeep holding"

# with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as connection:
#     connection.starttls()
#     connection.login(my_email, my_pass)
#     connection.sendmail(
#         from_addr="ashfatul@outlook.com",
#         to_addrs="test@example.com",
#         msg=f"Subject: About your IBM stock\n\n{message}"

#         )

# print('Hello There!\nYou have stock of IBM we are now checking your stock price in last two working days\nPlease wait ...')
# print("================================")
# print(f"Yesterday the closing value was ${day1close}")
# print(f"Day before Yesterday the closing value was ${day2close}")
# print("================================")
# print("We are sending you an email.")
# print("Mail send!\nDone")

news_params = {
    "q": "IBM",
    "from": day2,
    "sortBy": "publishedAt",
    "apiKey": "38223ad62117404ba71338988d7c39e1"
}

headline = []
if round(status, 2) > 105 or round(status, 2) < 95:
    res = requests.get("https://newsapi.org/v2/everything", news_params)
    data = res.json()
    
    articles = data["articles"]
    for a in articles:
        headline.append(a["title"])
        print("============================================")
        print(a["title"])
        print("============================================")


    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as connection:
        connection.starttls()
        connection.login(my_email, my_pass)
        connection.sendmail(
            from_addr="ashfatul@outlook.com",
            to_addrs="test@example.com",
            msg=f"Subject: About your IBM stock\n\nThis is message"

            )
        
    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as connection:
        connection.starttls()
        connection.login(my_email, my_pass)

        connection.sendmail(
            from_addr="ashfatul@outlook.com",
            to_addrs="test@example.com",
            msg=f"Subject: News about IBM\n\n{headline}"
        )


        # understand