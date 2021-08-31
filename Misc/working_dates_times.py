"""""
name: The name of the visitor.
appt_made_date: The date and time that the appointment was created.
appt_start_date: The date and time that the appointment was scheduled to start.
appt_end_date: The date and time that the appointment was scheduled to end.
visitee_namelast: The last name of the visitee (the person the visitor was meeting with).
visitee_namefirst: The first name of the visitee.
meeting_room: The room in which the appointment was scheduled.
description: Optional comments added by the WAVES operator.
"""""

#### 1
# from csv import reader

# opened_file = open("potus_visitors_2015.csv")
# read_file = reader(opened_file)
# potus = list(read_file)
# potus = potus[1:]

#### 3
# import datetime as dt

#### 4
# import datetime as dt

# ibm_founded = dt.datetime(1911,6,16)
# man_on_moon = dt.datetime(1969, 7,20, 20,17)

# print(ibm_founded)
# print(man_on_moon)

#### 5
# from csv import reader
# import datetime as dt

# opened_file = open("potus_visitors_2015.csv")
# read_file = reader(opened_file)
# potus = list(read_file)
# potus = potus[1:]

# print(potus[-1][2])

# date_format = "%m/%d/%y %H:%M"
# for row in potus:
#     start_date = row[2]
#     start_date = dt.datetime.strptime(start_date, date_format)
#     row[2] = start_date

# print(potus[-1][2])

#### 6
# from csv import reader
# import datetime as dt

# opened_file = open("potus_visitors_2015.csv")
# read_file = reader(opened_file)
# potus = list(read_file)
# potus = potus[1:]

# date_format = "%m/%d/%y %H:%M"
# for row in potus:
#     start_date = row[2]
#     start_date = dt.datetime.strptime(start_date, date_format)
#     row[2] = start_date

# visitors_per_month = {}

# for row in potus:
#     month_dt = row[2]
#     month_str = month_dt.strftime("%B, %Y")
#     if month_str not in visitors_per_month:
#         visitors_per_month[month_str] = 1
#     else:
#         visitors_per_month[month_str] += 1

# print(visitors_per_month)


#### 7
# from csv import reader
# import datetime as dt

# opened_file = open("potus_visitors_2015.csv")
# read_file = reader(opened_file)
# potus = list(read_file)
# potus = potus[1:]

# date_format = "%m/%d/%y %H:%M"
# for row in potus:
#     start_date = row[2]
#     start_date = dt.datetime.strptime(start_date, date_format)
#     row[2] = start_date


# appt_times = []

# for row in potus:
#     time_obj = row[2]
#     appt_dt = time_obj.time()
#     appt_times.append(appt_dt)

# print(appt_times[-1])

#### 8

# from csv import reader
# import datetime as dt

# opened_file = open("potus_visitors_2015.csv")
# read_file = reader(opened_file)
# potus = list(read_file)
# potus = potus[1:]

# date_format = "%m/%d/%y %H:%M"
# for row in potus:
#     start_date = row[2]
#     start_date = dt.datetime.strptime(start_date, date_format)
#     row[2] = start_date


# appt_times = []

# for row in potus:
#     time_obj = row[2]
#     appt_dt = time_obj.time()
#     appt_times.append(appt_dt)

# min_time = min(appt_times)
# print(min_time)
# max_time = max(appt_times)
# print(max_time)

#### 9
# import datetime as dt
# dt_1 = dt.datetime(1981, 1, 31)
# dt_2 = dt.datetime(1984, 6, 28)
# dt_3 = dt.datetime(2016, 5, 24)
# dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)

# answer_1 = dt_2 - dt_1
# print(answer_1)
# answer_2 = dt_3 + dt.timedelta(days=56)
# print(answer_2)
# answer_3 = dt_4 - dt.timedelta(seconds=3600)
# print(answer_3)

#### 10
from csv import reader
import datetime as dt

opened_file = open("potus_visitors_2015.csv")
read_file = reader(opened_file)
potus = list(read_file)
potus = potus[1:]

date_format = "%m/%d/%y %H:%M"
for row in potus:
    start_date = row[2]
    start_date = dt.datetime.strptime(start_date, date_format)
    row[2] = start_date


for row in potus:
    end_date = row[3]
    end_date = dt.datetime.strptime(end_date, "%m/%d/%y %H:%M")
    row[3] = end_date

appt_lengths = {}

for row in potus:
    appt_start_date = row[2]
    appt_end_date = row[3]
    length = appt_end_date - appt_start_date
    if length not in appt_lengths:
        appt_lengths[length]= 1
    elif length in appt_lengths:
        appt_lengths[length] += 1

min_length = min(appt_lengths)
max_length = max(appt_lengths)
print(min_length)
print(max_length)

