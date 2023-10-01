from datetime import datetime, timedelta
def generate_datetime_list(x):
    current_date = datetime.now()
    datetime_list = []
    for i in range(20):
        datetime_list.append(current_date)
        current_date += timedelta(days=x)
    return datetime_list

x = 5
date_list = generate_datetime_list(x)
for date in date_list:
    print(date)
