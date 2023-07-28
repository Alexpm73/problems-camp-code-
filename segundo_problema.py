def parse_time(time_str):
    hour = time_str[:-6]
    minute = time_str[-5:-3]
    meridian= time_str[-2:] 
    return int(hour), int(minute), meridian

def parse_time2(time_str):
    hour = time_str[:-3]
    minute = time_str[-2:]
    return int(hour), int(minute)



def add_time(start_time, duration, starting_day=None):
    
    start_time_hour, start_time_minute, start_time_meridian = parse_time(start_time)

    
    duration_hour, duration_minute = parse_time2(duration)[:2]

    
    if start_time_meridian == "PM" and start_time_hour != 12:
        start_time_hour += 12

    
    total_minutes = start_time_hour * 60 + start_time_minute + duration_hour * 60 + duration_minute


    new_time_hour = total_minutes // 60 % 24
    new_time_minute = total_minutes % 60
    new_time_meridian = "AM" if new_time_hour < 12 else "PM"
    if new_time_hour > 12:
        new_time_hour -= 12
    elif new_time_hour == 0:
        new_time_hour = 12


    days_later = total_minutes // (24 * 60)


    if starting_day is not None:
        starting_day = starting_day.capitalize()
        days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        starting_index = days_of_week.index(starting_day)
        new_day_index = (starting_index + days_later) % 7
        new_day = days_of_week[new_day_index]


    result = f"{new_time_hour}:{new_time_minute:02d} {new_time_meridian}"

    if starting_day:
        result += f", {new_day}"

    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"

    return result

# Test cases
print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
