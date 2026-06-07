months = [
    'January','February','March','April','May','June',
    'July','August','September','October','November','December'
]

while True:
    date = input("Data: ")
    try:
        if "/" in date:
            mm,dd,yyyy = date.split("/")#4/22/2000
        elif "-" in date:
            mmdd,yyyy = date.split(", ")#january 1, 2024
            mm,dd = mmdd.split(" ")
            mm = months.index(mm)+1

        if int(mm) > 12 or int (dd) > 31:
            raise ValueError
        else:
            print(f"{int(yyyy):04}-{int(mm):02}-{int(dd):02}")

    except (ValueError, KeyError,NameError):
        pass