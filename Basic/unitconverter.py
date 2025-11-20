# Start Program
while True:
    print("Please choose from the following available conversion")
    print("A: Distance(km/miles)")
    print("B; Temperature")
    print("C: Weight")
    print("D: Time")

    inp = str(input("Please state the unit conversion u wanna choose:- ")).lower()

#-----------------------------Distance--------------------------------------------------------

    if inp == "a":
        dis = str(input("Please state unit you want to convert (km/miles):- ")).lower()
        
        try:
            if dis == "km":
                km = float(input("Please state the data u want to convert to miles:- "))
                miles = (km*0.621371)
                print(f'The {km}km is converted to {miles}miles')

            elif dis == "miles":
                mil = float(input("Please state the data u want to convert to kilometer:- "))
                kilom = (mil*1.60934)
                print(f'The {mil}mil is converted to {kilom}kilom')

            else:
                pass
        
        except ValueError:
            print("Please state data in just number format")

#--------------------------------Temperature------------------------------------------------------------

    elif inp == "b":
        temp = str(input("Please state unit you want to convert (Celsius/Fahrenheit):- ")).lower()
        try:
            if temp == "celsius":
                cel = float(input("Please state the data u want to convert to Fahrenheit:- "))
                farh = ((cel*1.8) + 32) 
                print(f'The {cel}C is converted to {farh}F ')

            elif temp == "fahrenheit":
                celsius = float(input("Please state the data u want to convert to celsius:- "))
                fahrenheit = ((celsius-32)*1.8) 
                print(f'The {fahrenheit}F is converted to {celsius}C ')

            else:
                pass

        except ValueError:
            print("Please state data in just number format")

#-----------------------------------Weight----------------------------------------------------------------

    elif inp == "c":
        wei = str(input("Please state unit you want to convert (Kilogram/Pound):- ")).lower()
        try:
            if wei == "pound":
                kilo = float(input("Please state the data u want to convert to Pound:- "))
                pou = (kilo*2.20462)                                                                # Continue from here
                print(f'The {kilo}kg is converted to {pou}p ')

            elif wei == "kilogram":
                p = float(input("Please state the data u want to convert to Kilogram:- "))
                kg = (p*0.453592) 
                print(f'The {p}p is converted to {kg}kg ')

            else:
                pass

        except ValueError:
            print("Please state data in just number format")

#----------------------------------------------Time--------------------------------------------------

    elif inp == "d":
        time = str(input("Please state unit you want to convert (Hours/Minutes/Seconds):- ")).lower()
        try:
            if time == "hours":
                hr = float(input("Please state the data u want to convert to Minutes and Seconds:- "))

                minu = (hr*60) 
                print(f'The {hr}hr is converted to {minu}min')

                sec = (minu*60) 
                print(f'The {hr}hr is converted to {sec}sec ')

            elif time == "minutes":
                minu = float(input("Please state the data u want to convert to Hours and Seconds:- "))

                hr = (minu/60) 
                print(f'The {minu}minu is converted to {hr}hr')

                sec = (minu*60) 
                print(f'The {minu}minu is converted to {sec}sec')

            elif time == "seconds":
                sec = float(input("Please state the data u want to convert to Hours and Minutes:- "))

                hr = (sec/3600) 
                print(f'The {sec}sec is converted to {hr}hr')

                minu = (sec/60)
                print(f'The {sec}sec is converted to {minu}minu')

            else:
                pass

        except ValueError:
            print("Please state data in just number format")

    else:
        print("Please choose a correct option (A/B/C/D)")

    y = input("Do you want to continue yes or no: -  ").lower()

    if y == "no":
        break
    else:
        pass

print("Thanks For Trying my Project")
