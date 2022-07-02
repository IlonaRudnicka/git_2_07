wiek = input("Podaj wiek użytkownika: ")
# Sprwadzamy czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
    exit("Wiek musi być podany jako liczba")
wiek = int(wiek)
if wiek >= 18 and wiek <= 50:
    print("Witaj w naszym sklepie z alkoholem")
elif wiek > 50:
    print("Witaj w naszym sklepie z alkoholem")
    print("W Twoim wieku alkohol jest już szkodliwy")
else:
    exit("Jesteś za młody na alkohol!")
