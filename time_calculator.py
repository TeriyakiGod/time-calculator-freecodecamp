def add_time(start, duration, day=""):
  startingTime = {
    "hour" : int(start.split()[0].split(":")[0]),
    "minute" : int(start.split()[0].split(":")[1]),
    "half" : start.split()[1]
  }
  durationTime = {
    "hour" : int(duration.split(":")[0]),
    "minute" : int(duration.split(":")[1]),
  }
  weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")



  newMinute = startingTime["minute"] + durationTime["minute"]
  divMinute =int(newMinute / 60)
  modMinute = newMinute % 60
  newHour = (startingTime["hour"] + durationTime["hour"] + divMinute)
  divHour = int(newHour/12)
  modHour = newHour%12

  newHalf = (0 if startingTime["half"] == "AM" else 1) + divHour
  nDays = int(newHalf/2)
  correctedDay = day.casefold().capitalize()
  newDay = ", " + weekDays[(weekDays.index(correctedDay) + nDays)%7] if day != "" else ""
  newN = ""
  if nDays == 1:
    newN = " (next day)"
  elif nDays > 1:
    newN = " (" + str(nDays) + " days later)"
  else: newN = ""
  newTime = {
    "hour" :  12 if modHour == 0 else modHour,
    "minute" : modMinute,
    "half" : (" AM" if newHalf % 2 == 0 else " PM"),
    "day" : newDay,
    "n" : newN
  }
  newTimeString = str(newTime["hour"]) + ":" + (str(newTime["minute"]) if newTime["minute"] > 9 else "0" + str(newTime["minute"])) + newTime["half"] + newTime["day"] + newTime["n"]
  return newTimeString