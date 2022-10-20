from my_module import * 

def main():
    miles = float(input('How many miles do you want to convert to kilometers?: '))
    kilometers =  miles_to_km(miles)
    print(miles, 'is equal to', kilometers , 'kilometers')
    
    fah_to_con = fah_to_cel()
    cel_to_con = (fah_to_con - 32) * 5/9
    print(fah_to_con, 'is equal to', cel_to_con, 'celsius')
    
    gal_to_con = gal_to_lit()
    lit_to_con = gal_to_con * 3.785
    print(gal_to_con, 'is equal to', lit_to_con, 'liters')
    
    pounds_to_con = pounds_to_kg()
    kg_to_con = pounds_to_con *0.454
    print(pounds_to_con, 'pounds is equal to', kg_to_con, 'kilograms')
    
    in_to_con = inches_to_cm()
    cm_to_con = in_to_con * 2.54
    print(in_to_con, 'inches is equal to', cm_to_con, 'centimeters')

def fah_to_cel():
    fah = float(input('How many degrees in fahrenheit do you want to convert to celsius?: '))
    return fah

def gal_to_lit():
    gallons = float(input('How many gallons do you want to convert to liters?: '))
    return gallons
    
def pounds_to_kg():
    pounds = float(input('How many pounds to you want to convert to kilograms?: '))
    return pounds
    
    
def inches_to_cm():
    inches = float(input('How many inches to you want to convert to centimeters?: '))
    return inches
    

main()
