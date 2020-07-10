full_seconds = int(input("Введите время в секундах: "))

hours = full_seconds // 3600
if hours < 10:
    hours = "0" + str(hours)
full_seconds -= int(hours)*3600;

minutes = full_seconds // 60
if minutes < 10:
    minutes = "0" + str(minutes)
full_seconds -= int(minutes)*60;
seconds = full_seconds

if seconds < 10:
    seconds = "0" + str(seconds)

print(f"{hours}:{minutes}:{seconds}")
