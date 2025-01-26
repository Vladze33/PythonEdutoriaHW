from datetime import datetime


def to_datetime(date_str, date_format):
    return datetime.strptime(date_str, date_format)


def date_diff(date1, date2):
    difference = date2 - date1
    return difference.days


def current_datetime():
    return datetime.now()


# Usage example
str_date1 = "01 Feb 2025 (18:00:00)"
str_date2 = "01 Mar 2025 (06:00:00)"
print("date 1:", str_date1)
print("date 2:", str_date2)

print()
str_format = "%d %b %Y (%X)"
dt1 = to_datetime(str_date1, str_format)
dt2 = to_datetime(str_date2, str_format)
print("Date days difference:", date_diff(dt1, dt2))
print("Date secs difference:", (dt2-dt1).total_seconds())

print()
print("Current datetime:", current_datetime())