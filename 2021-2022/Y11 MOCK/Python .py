Timings = ["8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
Days = ["mon","tue","wed","thu","fri","sat","sun"]

#task 1 functions

def day_of_the_week():
  Day = input("what day of the week is it? mon/tue/wed/thur/fri/sat/sun \n")
  while Day not in Days:
          Day = input("invalid entry! What day is it? mon/tue/wed/thu/fri/sat/sun \n" )

  return Day


def Time_Arrived():
  Time = input("what time did you park (Just the hour in 24hour format e.g 3:45 is 15) \n")
  while Time not in Timings:
          Time = input("invalid entry! What time is it? \n")
  return Time

def Time_Parked():
  Hours_Parked = int(input("How many hours did you park for?"))
  while Hours_Parked not in [1,2,3,4,5,6,7,8]:
      Hours_Parked = int(input("Invalid entry! How many hours did you park for?"))
  while Day in ["mon"] and Time in ["8","9","10","11","12","13","14","15"] and Hours_Parked > 2:
         Hours_Parked = int(input("you cannot park for more than 2 hours on a monday morning. How many hours did you park for?"))
  while Day in ["tue"] and Time in ["8","9","10","11","12","13","14","15"] and Hours_Parked > 2:
         Hours_Parked = int(input("you cannot park for more than 2 hours on a tuesday morning. How many hours did you park for?"))
  while Day in ["wed"] and Time in ["8","9","10","11","12","13","14","15"] and Hours_Parked > 2:
         Hours_Parked = int(input("you cannot park for more than 2 hours on a wednesday morning. How many hours did you park for?"))
  while Day in ["thu"] and Time in ["8","9","10","11","12","13","14","15"] and Hours_Parked > 2:
         Hours_Parked = int(input("you cannot park for more than 2 hours on a thursday morning. How many hours did you park for?"))
  while Day in ["fri"] and Time in ["8","9","10","11","12","13","14","15"] and Hours_Parked > 2:
         Hours_Parked = int(input("you cannot park for more than 2 hours on a friday morning. How many hours did you park for?"))
  while Day in ["sat"] and Time in ["8","9","10","11","12","13","14","15"] and Hours_Parked > 4:
         Hours_Parked = int(input("you cannot park for more than 4 hours on a saturday morning. How many hours did you park for?"))
  while Day in ["sun"] and Time in ["8","9","10","11","12","13","14","15"] and Hours_Parked > 8:
         Hours_Parked = int(input("you cannot park for more than 8 hours on a sunday. How many hours did you park for?"))

  return Hours_Parked

def modulo11():

  ISBN = input("please input your frequent parking number:")
  while len(ISBN) != 5:
      ISBN = input("your frequent parking number must be 5 numbers:")
  num1 = int(ISBN[0])
  num2 = int(ISBN[1])
  num3 = int(ISBN[2])
  num4 = int(ISBN[3])
  multiplied1 = (num1*5)
  multiplied2 = (num2*4)
  multiplied3 = (num3*3)
  multiplied4 = (num4*2)
  allnum = (multiplied1+multiplied2+multiplied3+multiplied4)
  modulo = allnum%11
  finalnumber = 11-modulo
  number=int(ISBN[4])

  if finalnumber==number:
      print("parking number identified, discount applied")
      parking_number = 1
  else:
      print("Invalid parking number, no discount was applied")
      parking_number = 0

  return parking_number

def calc_charge():

    if Day in ["sun"] and Time in ["8", "9", "10", "11", "12","13","14","15"]:
         Charge = 2
         MCharge = 0
    if Day in ["mon", "tue", "wed", "thu", "fri"] and Time in ["8", "9", "10", "11", "12","13","14","15"]:
        Charge = 10
        MCharge = 0
    if Day in ["sat"] and Time in ["8", "9", "10", "11", "12", "13","14","15"]:
         Charge = 3
         MCharge = 0

    elif Day in Days and Time in ["16", "17", "18", "19", "20", "21", "22", "23"]:
         MCharge = 2
         Charge = 0

    time_park = int(Time)
    hour_park = int(Hours_Parked)
    final_hour = 0

    if time_park + hour_park > 16:
        afterfour = (time_park + hour_park) - 16
        final_hour = hour_park - afterfour
        Charge = 2 + (Charge * final_hour)
        if parking_number == 1:
            Charge = Charge*0.9
    else:
        if parking_number == 1:
            Charge = Charge*0.9
            MCharge = MCharge*0.5
        Charge = MCharge + (Charge * hour_park)

    return Charge

total_paid = 0
end = []

while end != 909:


    Day = day_of_the_week()
    Time = Time_Arrived()
    Hours_Parked = Time_Parked()
    parking_number = modulo11()
    Charge = calc_charge()

    print("$",Charge)
    paid = int(input("You need to pay the amount above:"))
    new_charge = Charge - paid
    total_paid = total_paid + paid
    while new_charge > 0:
        print("$",new_charge)
        paid = int(input("please pay the remaining balance stated above:"))
        new_charge = new_charge - paid
        total_paid = total_paid + paid


    end = int(input("put in the admin password to end the day (909) :"))

print("we earned $", total_paid)
