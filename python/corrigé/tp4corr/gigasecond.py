from datetime import datetime, timedelta

def add_gigasecond(date_str):
    format = "%Y-%m-%d %H:%M:%S"
    d1=datetime.strptime(date_str, format)
    d2=d1+timedelta(seconds=1e9)
    return d2.strftime(format)
