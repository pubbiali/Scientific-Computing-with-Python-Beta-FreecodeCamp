def add_time(start, duration, starting_day=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Parse start time
    start_hour, start_minute = map(int, start[:-2].split(":"))
    period = start[-2:]
    if period == "PM":
        start_hour += 12
    
    # Parse duration time
    duration_hour, duration_minute = map(int, duration.split(":"))

    # Calculate total minutes and hours
    end_minute = start_minute + duration_minute
    end_hour = start_hour + duration_hour + end_minute // 60
    end_minute %= 60
    days_later = end_hour // 24
    end_hour %= 24
    
    # Determine AM/PM
    if end_hour >= 12:
        period = "PM"
        end_hour -= 12
    else:
        period = "AM"
    
    if end_hour == 0:
        end_hour = 12

    # Format time
    new_time = f"{end_hour}:{end_minute:02d} {period}"
    
    if starting_day:
        starting_day_index = days_of_week.index(starting_day.capitalize())
        new_day = days_of_week[(starting_day_index + days_later) % 7]
        new_time += f", {new_day}"
    
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time

# Test examples
print(add_time("3:00 PM", "3:10")) # Expected: 6:10 PM
print(add_time("11:30 AM", "2:32", "Monday")) # Expected: 2:02 PM, Monday
print(add_time("11:43 AM", "00:20")) # Expected: 12:03 PM
print(add_time("10:10 PM", "3:30")) # Expected: 1:40 AM (next day)
print(add_time("11:43 PM", "24:20", "Tuesday")) # Expected: 12:03 AM, Thursday (2 days later)
print(add_time("6:30 PM", "205:12")) # Expected: 7:42 AM (9 days later)
