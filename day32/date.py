from calendar import month
import datetime
arryofday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
currentTime = datetime.datetime.now()

day = currentTime.day
month = currentTime.month
year = currentTime.year

dayofweek = currentTime.weekday()


# print(arryofday[dayofweek])