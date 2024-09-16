
def format_date(date, format="dmy"):
    year, month, day = date.split("-")
    if format == "dmy":
        return f"{day}{month}{year}"
    elif format == "mdy":
        return f"{month}{day}{year}"
    elif format == "ymd":
        return f"{year}{month}{day}"
    else:
        return date


print(format_date("2023-07-01"))
# 01072023
print(format_date("2023-07-01", format="dmy"))
# 01072023
print(format_date("2023-07-01", format="mdy"))
# 07012023
print(format_date("2023-07-01", format="ymd"))
# 20230701
print(format_date('2023-07-15', format = 'xyz'))


