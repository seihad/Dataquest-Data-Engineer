
import datetime as dt
eg_2 = dt.datetime.strptime("1/26/2016 19:30", "%m/%d/%Y %H:%M")
print(eg_2)

hour_dt = eg_2.strftime("%H")
print(hour_dt)