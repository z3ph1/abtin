### Skriv en inledande kommentar som talar om vad programmet gör.
'''
Programmet läser in data från en CSV-fil som innehåller information om PISA-undersökningen.
Det tillhandahåller olika alternativ för att analysera och visualisera datan.
'''


### Placera dina modulimpoter här:
import csv #för att kunna hantera störra mängd data.
import matplotlib.pyplot as plt #för att kunna göra grafer mm...


### Deluppgift 1: Funktioner från deluppgift 1 i ordning.
### Skriv din kod här:


# 1a)
#val av datafil
def read_file(data_csv):
    pisadata = []                                    
    with open(data_csv, 'r', encoding = 'UTF-8') as file:   #öppnar filen, gör at den kan läsa även svenska tecken
        csv_reader = csv.reader(file, delimiter= ';')      
        for rad in csv_reader:                              
            rad_int = []                                  
            for value in rad:                            
                if value.isdigit():                        
                    rad_int.append(int(value))            #konvertera och lägg till värdet i den nya listan
                else:
                    rad_int.append(value)                  
            pisadata.append(rad_int)
                                     
        return pisadata                                   #kör koden ovan




### Deluppgift 2: Funktioner från deluppgift 2 i ordning.
### Skriv din kod här:


#2a)
#funktion för att ta fram 10 bästa reapektive sämsta länder år 2018
def sortera_lista(lista):
    
    # Skapa en ny lista där varje element är en sträng av formatet "resultat land"
    lista13 = [(x[13], x[0]) for x in lista[2:]]


    # Sortera listan baserat på den 13:e kolumnen i fallande ordning
    sorted_13 = sorted(lista13, key=lambda x: int(x[0]), reverse=True)


    # Skriv ut de tio bästa resultaten
    print("De tio länder som hade bäst resultat år 2018")
    print("--------------------------------------------")
    print("Land                         Resultat")
    print("--------------------------------------------")
    for item in sorted_13[:10]:
        print(f"{item[1]:<30} {item[0]}")
   
    # Skriv ut de tio sämsta resultaten
    print("\nDe tio länder som hade sämst resultat år 2018")
    print("--------------------------------------------")
    print("Land                         Resultat")
    print("--------------------------------------------")
    for item in sorted_13[-1:-11:-1]: # sclings ändrad från kamratrespons för att få ut  sämsta länder i rätt ordning
        print(f"{item[1]:<30} {item[0]}")






### Deluppgift 3: Funktioner från deluppgift 3 i ordning.
### Skriv din kod här:


#3a)
#funktion för att beräkna medelvärdet på en kolumn i listan
def kolumnmedel(list,index):
    kolumn  = []
    for i in list[2:]:
        kolumn.append(i[index])
    medel = sum(kolumn)//len(kolumn) # heltals division för att undvika decimaler
    return medel


#3b)
#funktion för att få fram alla medelvärden från 2018 - 2003
def armedel(lista):
    lista_armedel = []
    lista_2 = []
    for rad in lista[0:]:
        lista_armedel.append(rad)
    for x in range(13, 19):      # går ingeom index för rätt år 2003 till 2018
        lista_2.append(kolumnmedel(lista_armedel, x))
    return lista_2


#3c)
#nordiska länder som medelvärdet ska synas för i grafen och tabellen senare
nordiska_länder = ["Sweden", "Norway", "Denmark", "Finland", "Iceland"]


#funktion för att skriva ut en tabell för nordiska länders medelvärde samt alla andra länder i samma kolumn
def nordtabell(pisadata, armedel, nordiska_länder):
    uppdelning_årtal_land = []


    # Skriv ut rubriken för tabellen
    print("\nKunskapsutveckling i matematik enligt PISA-undersökningen 2003 - 2018.")
    print("------------------------------------------------------------------------")
    print("\n                           Länder:")
    print("\nÅr  ", end=" ")
    for land in nordiska_länder:
        print(land, end=" ")
    print("Medelvärde \n                                           alla länder")
    print("------------------------------------------------------------------------")
    # kod nedan för att fixa formatet på utskriften av tabellen
    for k in range(13, 19):
        print("{:<4}".format(pisadata[0][k]), end="    ")  # justerar rubriker


        for i in nordiska_länder:
            for row in pisadata:
                if i == row[0]:
                    print("{:<6}".format(row[k]), end=" ")  # justerar bredden


        print("{:<6}".format(armedel[k-13]))  # Printar medelvärderna


#3d)
#funktion för att kunna se de relevanta ländernas utveckling senare i plotting
def nordgraf(pisadata, armedel, nordiska_länder):
    # Uppdelning av årtal och länder
    årtal = pisadata[0][13:]  # År 2003-2018
    land_resultat = {}


    # Samla in resultaten för varje nordiskt land
    for land in nordiska_länder:
        land_resultat[land] = []


        for row in pisadata[1:]:
            if row[0] == land:
                land_resultat[land].extend(row[13:])




    # Skapa en lista för medelvärdet för varje år
    medelvärden = armedel


    # Skapa plottar för varje land och medelvärde
    for land, resultat in land_resultat.items():
        plt.plot(årtal, resultat, label=land)




    # Plotta medelvärde som en streckad linje
    plt.plot(årtal, medelvärden, 'k--', label='Medelvärde alla länder')


    # Lägg till titel och etiketter för axlarna
    plt.title('Kunskapsutveckling i matematik enligt PISA-undersökningen 2003 - 2018')
    plt.xlabel('År')
    plt.ylabel('Poäng')
    plt.legend()
    plt.grid(True)


    # Visa plotten
    plt.show()




### Deluppgift 4: Funktioner från deluppgift 4 i ordning.
### Skriv din kod här:


def battreSamre(lista, forbattring):
    # Identifiera index för åren i listan
    år_index = list(range(13, 19)) # skriver ut indexen


    # Skriv ut rubrik för förbättringar eller försämringar
    if forbattring:
        print("\nLänder som hela tiden har förbättrat sina resultat mellan 2003 - 2018")
    else:
        print("\nLänder där resultatet har försämrats mellan 2003 - 2018")


    print("------------------------------------------------------------------------")
    print("                        År och resultat:")
    print("\n{:<15}".format("Land"), end="")
    for år in (pisadata[0][13:]):
        print("{:<6}".format(år), end="")
    print("\n------------------------------------------------------------------------")




# Kontrollera för varje land om resultaten förbättrats eller försämrats konsekvent
    for rad in lista[2:]:
        for år in range(1, len(år_index)):
            if (forbattring and rad[år_index[år]] >= rad[år_index[år - 1]]) or \
                    (not forbattring and rad[år_index[år]] <= rad[år_index[år - 1]]):
                continue
            else:
                break
        else:
            # Om for-loopen inte bryts betyder det att resultaten förbättrats eller försämrats konsekvent
            print("{:<15}".format(rad[0]), end="")
            for år in reversed(år_index):
                print("{:<6}".format(rad[år]), end="")
            print()




### Deluppgift 5: Funktioner från deluppgift 5 i ordning.
### Skriv din kod här:


def kvinna_man(data):
    # Skriv ut rubrik för tabellen
    print("\nResultat där kvinnors resultat är högre än männens resultat år 2018-2003:")
    print("---------------------------------------------------------------------------")
    print("{:<8} {:<15} {:<12} {:<8}".format("År", "Land", "Kvinnor", "Män"'\n'))




    # Skriv ut resultaten för år 2018
    for j in range(1, len(data)):
        år_2018 = "2018"
        land = data[j][0]  #Landet är det första elementet i varje rad
        kvinnor_2018 = data[j][2]  # Resultatet för kvinnor år 2018
        män_2018 = data[j][1]  # Resultatet för män år 2018


        # Jämför resultaten för män och kvinnor för år 2018
        if kvinnor_2018 > män_2018:
            print("{:<8} {:<15} {:<12} {:<8}".format(år_2018, land, kvinnor_2018, män_2018))
           
    print(42*'-')


    # Skriv ut resultaten för år 2015
    for j in range(1, len(data)):
        år_2015 = "2015"
        land = data[j][0]  # Landet är det första elementet i varje rad
        kvinnor_2015 = data[j][4]  # Resultatet för kvinnor år 2015
        män_2015 = data[j][3]  # Resultatet för män år 2015


        # Jämför resultaten för män och kvinnor för år 2015
        if kvinnor_2015 > män_2015:
            print("{:<8} {:<15} {:<12} {:<8}".format(år_2015, land, kvinnor_2015, män_2015))
   
    print(42*'-')
   
    for j in range(1, len(data)):
        år_2012 = "2012"
        land = data[j][0]  # Landet är det första elementet i varje rad
        kvinnor_2012 = data[j][6]  # Resultatet för kvinnor år 2012
        män_2012= data[j][5]  # Resultatet för män år 2012


        # Jämför resultaten för män och kvinnor för år 2012
        if kvinnor_2012 > män_2012:
            print("{:<8} {:<15} {:<12} {:<8}".format(år_2012, land, kvinnor_2012, män_2012))
           
    print(42*'-')
   
    for j in range(1, len(data)):
        år_2009 = "2009"  
        land = data[j][0]  # Landet är det första elementet i varje rad
        kvinnor_2009 = data[j][8]  # Resultatet för kvinnor år 2009
        män_2009= data[j][7]  # Resultatet för män år 2009


        # Jämför resultaten för män och kvinnor för år 2009
        if kvinnor_2009 > män_2009:
            print("{:<8} {:<15} {:<12} {:<8}".format(år_2009, land, kvinnor_2009, män_2009))
           
    print(42*'-')
   
    for j in range(1, len(data)):
        år_2006 = "2006"
        land = data[j][0]  # Landet är det första elementet i varje rad
        kvinnor_2006 = data[j][10]  # Resultatet för kvinnor år 2006
        män_2006= data[j][9]  # Resultatet för män år 2006


        # Jämför resultaten för män och kvinnor för år 2006
        if kvinnor_2006 > män_2006:
            print("{:<8} {:<15} {:<12} {:<8}".format(år_2006, land, kvinnor_2006, män_2006))
   
    print(42*'-')
   
    for j in range(1, len(data)):
        år_2003 = "2003"
        land = data[j][0]  # Landet är det första elementet i varje rad
        kvinnor_2003 = data[j][12]  # Resultatet för kvinnor år 2003
        män_2003= data[j][11]  # Resultatet för män år 2003


        # Jämför resultaten för män och kvinnor för år 2003
        if kvinnor_2003 > män_2003:
            print("{:<8} {:<15} {:<12} {:<8}".format(år_2003, land, kvinnor_2003, män_2003))






### Huvudprogram med Meny från deluppgift 0. Använd menyrubriker enl. uppgiftsbeskrivningen.
### Skriv din kod här:
# skapa en meny så användare kan göra ett val av information personen är ute efter
read = False
while True:
    print('\nProgram för att läsa in och analysera data från PISA-undersökningen')
    print(f'\n  1. Läs in csv-filen.')
    print('  2. Bästa resp. sämsta resultat år 2018.')
    print('  3. Matematikkunskaper i norden år 2003 - 2018.')
    print('  4. Kontinuerligt förbättrat resp. försämrat år 2003 - 2018.')
    print('  5. Kvinnor presterar bättre än män under åren 2003 - 2018.')
    print('  6. Avsluta programmet.')
    val = input(f'\nVälj ett menyalternativ (1 - 6): ')


    # om man väljer alternativ 1
    if val == '1':
        # Läs in csv-filen igen om användaren vill göra det
        while True:
            filename = input('Ange filnamn eller tryck bara Enter för pisadata.csv: ')
            print('Get current working directory : ', os.getcwd())  
            if filename == "":
                filename = "pisadata.csv"
            try:
                pisadata = read_file(filename)
                read = True  # sätt read till True när filen har lästs in
                print("\nDe fem första raderna i pisadata är: ")
                for rad in pisadata[:5]:
                    print(rad)
                break
            except FileNotFoundError:
                print('Filen hittas ej,(tryck enter om du vill komma åt filen)')


    # om man väljer alternativ 2
    elif val == '2':
        if read == False:
            print("Var vänlig och läs in filen först (alternativ 1 i menyn).")
        else:
            sortera_lista(pisadata)


    # om man väljer alternativ 3
    elif val == '3':
        if not read:
            print("Var vänlig och läs in filen först (alternativ 1 i menyn).")
        else:
            nordtabell(pisadata, armedel(pisadata), nordiska_länder)
            print("\n")
            nordgraf(pisadata, armedel(pisadata), nordiska_länder)


    # om man väljer alternativ 4
    if val == '4':
        if not read:
            print("Var vänlig och läs in filen först (alternativ 1 i menyn).")
        else:
        # Anropa funktionen för förbättringar
            battreSamre(pisadata, True)


        # Anropa funktionen för försämringar
            battreSamre(pisadata, False)
           
    #om man man väljer alternativ 5
    elif val == '5':
        if not read:
            print("Var vänlig och läs in filen först (alternativ 1 i menyn).")
        else:
            kvinna_man(pisadata)


    # om man väljer alternativ 6
    elif val == '6':
        break


    else:
        print("Ange en giltig siffra") #kraschsäkrar programmet


































