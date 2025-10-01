first = "hello world"
# "this is a comment"
print("I'm a computer")
print(1<2 and 4>2)
nope = None
resultat = True and False
print(resultat)
chaine = "What's my length?"
longueur = len(chaine)
print(longueur)
list = "i'm shooting"
list = list.upper()
print(list)
chaine = "1000"
nombre = int(chaine)
print(chaine)
nombre = 4
texte = "real"
resultat = str(nombre) + texte
print(resultat)
print("cool cool cool")
try:
    calcul = 1 / 0
    print(calcul)
except:
    print(False)
print(type([]))
name = "manu"
print(name)
nombre = int(5)
if nombre < 0:
    print("that number is less than 0")
elif nombre > 0:
    print("that number is greater than 0")
else:
    print("you picked 0")
mot = "apple"
print(mot.index("l")) 
mot = "xylophone"
if "y" in mot:
    print("Yes, 'y' is in 'xylophone'")
else:
    print("No, 'y' is not in 'xylophone'") 
my_string = "bonjour"
if my_string.islower():
    print("La chaîne est en minuscules.")
else:
    print("La chaîne n'est pas entièrement en minuscules.")
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