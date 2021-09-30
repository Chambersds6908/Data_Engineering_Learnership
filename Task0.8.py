def hours_and_minutes(n):
    if n < 60:
        hours = 0 
        minutes = n
    else:
        hours = n // 60
        minutes = n % 60
    if hours == 1:
        hourstr = str(hours) + " hour"
    else:
        hourstr = str(hours) + " hours"
    if minutes == 1:
        minutestr = str(minutes) + " minute"
    else:
        minutestr = str(minutes) + " minutes"
    return hourstr + ", " + minutestr 

hours_and_minutes(320)
