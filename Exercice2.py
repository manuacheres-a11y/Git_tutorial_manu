humanyears = 10
# Cas de la première année
if humanYears == 1:
        catYears = 15
        dogYears = 15
# Cas de la deuxième année
    elif humanYears == 2:
        catYears = 15 + 9
        dogYears = 15 + 9
    # Cas général (3 ans et plus)
    else:
        catYears = 15 + 9 + (humanYears - 2) * 4
        dogYears = 15 + 9 + (humanYears - 2) * 5
    
    return [humanYears, catYears, dogYears]         