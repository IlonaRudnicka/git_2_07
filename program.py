plec = input("Podaj płeć (Kobieta/Mężczyzna/Inna/Odrzuć odpowiedź): ")
wiek = input("Podaj wiek użytkownika: ")
region = input("Wpisz region USA lub EUR: ")
# Sprwadzamy czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
    exit("Wiek musi być podany jako liczba")
wiek = int(wiek)
if wiek >= 21 and wiek <= 50 and region == 'USA':
    print("Jesteś w USA! Witaj w naszym sklepie z alkoholem")
elif wiek >= 18 and wiek <= 50 and region != 'USA':
    print("Witaj w naszym sklepie z alkoholem")
elif wiek > 50 and wiek <=120:
    print("Witaj w naszym sklepie z alkoholem")
    print("W Twoim wieku alkohol jest już szkodliwy")
elif wiek > 120:
    exit("Niemożliwe! Nasi klienci tak długo nie żyją")
else:
    exit("Jesteś za młody na alkohol!")
