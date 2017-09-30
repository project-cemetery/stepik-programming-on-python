def get_alarm_hours_and_minutes(sleep_duration_minutes, bedtime_hours, bedtime_minutes):
    bedtime_full_minutes = bedtime_hours * 60 + bedtime_minutes
    alarm_minutes = bedtime_full_minutes + sleep_duration_minutes

    return (alarm_minutes // 60), (alarm_minutes % 60)

for param in get_alarm_hours_and_minutes(int(input()), int(input()), int(input())):
    print(param)
