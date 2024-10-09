from datetime import datetime, timedelta
import re
def add_gigasecond(date_str):
    pattern=r"(\d){4}(-)(\d){2}(-)(\d){2}(\s)((\d){2}(:)){2}(\d){2}"
    if re.fullmatch(pattern,date_str):
        