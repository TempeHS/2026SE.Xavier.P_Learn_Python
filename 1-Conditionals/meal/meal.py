def main():
    time = input("Time: ")
    time = convert(time)
    if time >= 7 and time <= 8:
        return print("breakfast time")
    elif time >= 12 and time <= 13:
        return print("lunch time")
    elif time >= 18 and time <= 19:
        return print("dinner time")
    else:
        return


def convert(time):
    hours, minutes = time.split(":")
    time = (float(minutes) / 60) + float(hours)
    return float(time)



main()