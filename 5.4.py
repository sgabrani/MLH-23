import datetime

start_time_str = "2021-05-30 12:22:00"
end_time_str = "2021-05-30 12:33:12"

start_time = datetime.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
end_time = datetime.datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")

with open("apache_access", "r") as file:
    for line in file:
        parts = line.split()
        time_str = parts[3].lstrip("[")
        log_time = datetime.datetime.strptime(time_str, "%d/%b/%Y:%H:%M:%S")
        if start_time <= log_time <= end_time:
            print(line.strip())
