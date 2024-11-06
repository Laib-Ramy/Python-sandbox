from datetime import datetime, timedelta
import re
def add_gigasecond(date_str):
    pattern=r"(\d){4}((-)(\d){2}){2}(\s)((\d){2}(:)){2}(\d){2}"
    date_format = r"%Y-%m-%d %H:%M:%S"
    time_to_add=timedelta(seconds=10**9)
    if re.fullmatch(pattern,date_str):
        date_obj = datetime.strptime(date_str, date_format)
        res=date_obj+time_to_add
        return(res.strftime(date_format))
    else:
        raise ValueError
    
