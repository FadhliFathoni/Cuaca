from datetime import datetime, timedelta

def countdown():
    # event_date = datetime(2023, 2, 23, 20, 35, 0) # set your event date here
    # current_time = datetime.now()
    # time_left = event_date - current_time
    # seconds_left = time_left.total_seconds()
    now = datetime.now().timestamp()
    end_time = now + 300
    return end_time

print(countdown())
# if countdown() <= 0:
#     print("Complete")