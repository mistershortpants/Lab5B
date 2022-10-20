def main():
    miles_to_km()
    fah_to_cel()
    gal_to_lit()
    pounds_to_kg()
    inches_to_cm()
    
def miles_to_km():
    miles = float(input('How many miles do you want to conver to kilometers?: '))
    kilometers = float(miles * 1.61)
    print(miles, 'is equal to', kilometers , 'kilometers')

def fah_to_cel():
    fah = float(input('How many degrees in fahrenheit do you want to convert to celsius?: '))
    cel = float((fah - 32) * 5/9)
    print(fah, 'is equal to', cel, 'celsius')
    
def gal_to_lit():
    gallons = float(input('How many gallons do you want to convert to liters?: '))
    liters = float(gallons * 3.785)
    print(gallons, 'is equal to', liters, 'liters')
    
def pounds_to_kg():
    pounds = float(input('How many pounds to you want to convert to kilograms?: '))
    kg = float(pounds * 0.454)
    print(pounds, 'pounds is equal to', kg, 'kilograms')
    
def inches_to_cm():
    inches = float(input('How many inches to you want to convert to centimeters?: '))
    cm = float(inches * 2.54)
    print(inches, 'inches is equal to', cm, 'centimeters')

main()
