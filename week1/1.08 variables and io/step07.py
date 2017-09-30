def get_hours_and_minutes_by_minutes(minutes):
    return (minutes // 60), (minutes % 60)


for param in get_hours_and_minutes_by_minutes(int(input())):
    print(param)
