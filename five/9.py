def make_readable(seconds):
    if seconds in range(0, 86400):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = (seconds % 3600) % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    else:
        return "Invalid input"


print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))
