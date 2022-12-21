def add_time(start, duration, current_day=""):
    start_hour = start.split(':')[0]
    start_minute = start.split(':')[1].split(' ')[0]
    time_of_a_day = start.split(':')[1].split(' ')[1]
    duration_hour = duration.split(':')[0]
    duration_minute = duration.split(':')[1]
    new_time_hour = str(int(start_hour) + int(duration_hour))
    new_time_minute = str((int(start_minute) + int(duration_minute))).rjust(2, '0')
    if int(new_time_minute) >= 60:
        new_time_minute = str((int(new_time_minute) % 60)).rjust(2, '0')
        new_time_hour = str(int(new_time_hour) + 1)
    if time_of_a_day == "AM":
        if int(new_time_hour) < 12:
            time_of_a_day = 'AM'
        elif 12 <= int(new_time_hour) < 24:
            new_time_hour = str(int(new_time_hour) % 12)
            time_of_a_day = "PM"
            if new_time_hour == "0":
                new_time_hour = str(int(new_time_hour) + 12)
        elif 24 <= int(new_time_hour) < 36:
            new_time_hour = str(int(new_time_hour) % 12)
            time_of_a_day = "AM (next day)"
            if new_time_hour == "0":
                new_time_hour = str(int(new_time_hour) + 12)
        elif int(new_time_hour) == 36:
            time_of_a_day = "PM"
        elif 36 < int(new_time_hour) < 48:
            new_time_hour = str(int(new_time_hour) % 12)
            time_of_a_day = "PM (next day)"
            if new_time_hour == "0":
                new_time_hour = str(int(new_time_hour) + 12)
        elif int(new_time_hour) >= 48:
            days = str(int(new_time_hour) // 24)
            if (int(new_time_hour) // 12) % 2 == 0:
                time_of_a_day = "AM (" + days + " days later)"
            else:
                time_of_a_day = "PM (" + days + " days later)"
            new_time_hour = str(int(new_time_hour) % 12)
            if new_time_hour == "0":
                new_time_hour = str(int(new_time_hour) + 12)
    elif time_of_a_day == "PM":
        if int(new_time_hour) < 12:
            time_of_a_day = 'PM'
        elif 12 <= int(new_time_hour) < 24:
            new_time_hour = str(int(new_time_hour) % 12)
            time_of_a_day = "AM (next day)"
            if new_time_hour == "0":
                new_time_hour = str(int(new_time_hour) + 12)
        elif int(new_time_hour) == 24:
            time_of_a_day = "PM"
        elif 24 < int(new_time_hour) < 36:
            new_time_hour = str(int(new_time_hour) % 12)
            if new_time_hour == "0":
                new_time_hour = str(int(new_time_hour) + 12)
            time_of_a_day = "PM (next day)"
        elif int(new_time_hour) >= 36:
            days = str(int(new_time_hour) // 24)
            if (int(new_time_hour) // 12) % 2 == 0:
                time_of_a_day = "PM (" + days + " days later)"
            else:
                days = str(int(days) + 1)
                time_of_a_day = "AM (" + days + " days later)"
            new_time_hour = str(int(new_time_hour) % 12)
            if new_time_hour == "0":
                new_time_hour = str(int(new_time_hour) + 12)

    # Adding day of the week
    days_of_the_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    current_day = current_day.lower()
    if current_day in days_of_the_week:
        i = days_of_the_week.index(current_day)
        if time_of_a_day == "AM" or time_of_a_day == "PM":
            time_of_a_day = time_of_a_day + ", " + days_of_the_week[i].title()
        elif time_of_a_day == "AM (next day)" or time_of_a_day == "PM (next day)":
            new_index = i + 1
            if new_index > 6:
                new_index = (i + 1) - 7
            new_day = days_of_the_week[new_index]
            time_of_a_day = time_of_a_day[0:2] + ", " + new_day.title() + time_of_a_day[2:]
        elif time_of_a_day == "AM (" + days + " days later)" or time_of_a_day == "PM (" + days + " days later)":
            if int(days) < 7:
                new_index = i + int(days)
                if new_index > 7:
                    new_index = (i + int(days)) - 7
                new_day = days_of_the_week[new_index]
                time_of_a_day = time_of_a_day[0:2] + ", " + new_day.title() + time_of_a_day[2:]
            else:
                new_index = i + (int(days) % 7)
                if new_index > 6:
                    new_index = (i + (int(days) % 7)) - 7
                new_day = days_of_the_week[new_index]
                time_of_a_day = time_of_a_day[0:2] + ", " + new_day.title() + time_of_a_day[2:]
        elif time_of_a_day == "AM" or time_of_a_day == "PM":
            time_of_a_day = time_of_a_day + ", " + days_of_the_week[i].title()
    new_time = new_time_hour + ':' + new_time_minute + ' ' + time_of_a_day

    return print(new_time)


add_time("3:30 PM", "2:12", "Monday")


