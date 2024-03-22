import time
import datetime
import json
import sys
def seconds_to_timer(seconds):
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return '{:02}:{:02}:{:02}:{:02}'.format(int(days), int(hours), int(minutes), int(seconds))

def seconds_left():
    current_time = time.time()  
    current_year = time.localtime(current_time).tm_year  
    end_of_year = time.mktime((current_year+1, 1, 1, 0, 0, 0, 0, 0, 0))  
    seconds_left = end_of_year - current_time  
    return seconds_left

def weekends_remaining():
    today = datetime.date.today()
    remaining_days = (datetime.date(today.year, 12, 31) - today).days + 1
    remaining_weeks = remaining_days // 7
    remaining_weekends = remaining_weeks * 2
    
    # Adjust for the case where the end of the year falls on a weekend
    if (datetime.date(today.year, 12, 31) - today).days % 7 < 2:
        remaining_weekends -= 2
    
    return remaining_days

def free_seconds_left(days_remaining):
    
    work_seconds = days_remaining * 5 * 3600
    free_seconds = seconds_left() - work_seconds
    return free_seconds

def main():
    while True:
        DR=weekends_remaining()
        data = {
    "Temps restant dans l'annee": seconds_to_timer(seconds_left()),
    "Temps Libre restant dans l'annee": seconds_to_timer(free_seconds_left(DR))
        }
        print(data, flush=True)
        time.sleep(1)  # Attend une seconde avant la prochaine mise à jour du timer
if __name__ == "__main__":
    main()
