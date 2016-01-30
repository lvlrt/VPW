#!/usr/bin/env python3

# variabelen
i = 0
j = 0
k = 0
l = 0
bonnen = []
prijs = 0

# functions


#invoer
xbestellingen = int(input("aantal bestellingen? "))
for i in range(xbestellingen):                  #bestellingen afgaan
    pizzas = input("geef het aantal pizza's en de prijzen ")
    pizzas = pizzas.split( )                    #opsplitsen op spatie
    pizzas = [int(i) for i in pizzas]           #omzetten naar integer
    xpizzas = pizzas[0]                         #aantal pizzas eruit halen
    pizzas.remove(pizzas[0])
    pizzas = sorted(pizzas, reverse=True)       # sorteren descending
    xbonnen = input("geef het aantal kortingsbonnen in: ")
    xbonnen = int(xbonnen)
    for j in range(xbonnen):
        bon = input("geef bon in: ").split( )   #korting bonnen laten ingeven
        bon = [int(i) for i in bon]

        #filter te grote nutteloze bonnen
        if xpizzas >= (bon[0] + bon[1]):
            bonnen.append(bon)
            pass #filter afgerond
    pass#alle bonnen ingevoerd
    bonnen.sort()
    bonnen.sort(key=lambda x: x[1], reverse=True)             #sorteren op colomn 2 hoogste eerst

    print(pizzas)
    print(bonnen)
    while k < len(bonnen): #bonnen afgaan
        if len(pizzas)>=(bonnen[k][0]+bonnen[k][1]): #te veel in bonnen bon negeren
            for l in range(0,bonnen[k][0]):             #betalende pizza
                print(bonnen[k][0])
                print(pizzas[0])

                prijs = prijs + pizzas[0]           #prijs optellen
                pizzas.remove(pizzas[0])            #eruit halen zo dat die niet opnieuw getelt word.
            pass
            for l in range(0,bonnen[k][1]):             #gratis pizzas
                print(bonnen[k][1])
                print(pizzas[0])
                pizzas.remove(pizzas[0])            #eruit halen zo dat die niet opnieuw getelt word.
            pass
        pass
        k = k + 1
    pass
    if pizzas:
        for l in range(0,len(pizzas)):
            prijs = prijs + pizzas[0]           #prijs optellen
            print(pizzas[0])
            pizzas.remove(pizzas[0])            #eruit halen zo dat die niet opnieuw getelt word.
        pass
    pass
    print(prijs)
pass
