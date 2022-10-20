import Lab
def main():
    miles_to_con = miles_to_km()
    km_to_con = miles_to_con * 1.61
    print(miles_to_con, 'is equal to', km_to_con , 'kilometers')
    
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
    
main()
