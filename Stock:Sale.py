from time import sleep

omzet = 0
maanden = 0 


vooraad = input("Hoeveel T-shirts zijn er ingekocht? ")
vooraad = int(vooraad)

maat_tshirt = input("Welke maat is er ingekocht? s/m/l ")

aantal_verkochte_tshirts = input("Hoeveel T-shirts zijn er verkocht?")
aantal_verkochte_tshirts = int(aantal_verkochte_tshirts)

tshirt_s = 15.00
tshirt_m = 20.00
tshirt_l = 25.00
winstpercentage = 0.10

verkoopprijssmall = tshirt_s + (tshirt_s * winstpercentage)
omzet_tshirt_small = verkoopprijssmall * aantal_verkochte_tshirts
#print(omzet_tshirt_small

verkoopprijsmedium = tshirt_m + (tshirt_m * winstpercentage)
omzet_tshirt_medium = verkoopprijsmedium * aantal_verkochte_tshirts
#print(omzet_tshirt_medium)

verkoopprijslarge = tshirt_l + (tshirt_l * winstpercentage)
omzet_tshirt_large = verkoopprijslarge * aantal_verkochte_tshirts
#print(omzet_tshirt_large)

while (omzet <= 1000) and (maanden <12):
    if (maat_tshirt == 's'):
        maand_omzet_tshirt_s = aantal_verkochte_tshirts * verkoopprijssmall
        omzet = omzet + maand_omzet_tshirt_s
        maanden = maanden + 1
        vooraad = vooraad - aantal_verkochte_tshirts
        sleep(0.5)
        print("Na", maanden, "maand is de voorraad:", vooraad, "omzet:", omzet)

    if (maat_tshirt == 'm'):
        maand_omzet_tshirt_m = aantal_verkochte_tshirts * verkoopprijsmedium
        omzet = omzet + maand_omzet_tshirt_m
        maanden = maanden + 1
        vooraad = vooraad - aantal_verkochte_tshirts
        sleep(0.5)
        print("Na" , maanden, "maand is de voorraad:" , vooraad, "omzet:" , omzet)

    if (maat_tshirt == "l"):
        maand_omzet_tshirt_l = aantal_verkochte_tshirts * verkoopprijslarge
        omzet = omzet + maand_omzet_tshirt_l
        maanden = maanden + 1
        vooraad = vooraad - aantal_verkochte_tshirts
        sleep(0.5)
        print("Na" , maanden, "maand is de voorraad:" , vooraad, "omzet:" , omzet)

