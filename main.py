#utworzenie pliku

#przypisanie do zmiennej plik wyniku funkcji open
#plik = open("test.txt") tak domyślnie otwiera plik do odczytu
#do zapisu z parametrem "w" jak write z czyszczeniem tego co było wcześniej zawarte
plik = open("Plik.txt", "a") #tryb a - append czyli dołączać. Będziemy nadpisywać plik
#plik = open("D:/Plik1.txt", "w")
print(plik.writable()) #funkcja zwraca czy obiekt plik jest możliwy do zapisu

if plik.writable():
    plik.write(input("Wprowadź tekst ") + "\n")

#zapisanie w zmiennej ilosci wprowadzonych znaków
if plik.writable():
    ileZnakow = plik.write(input("Wrzuć tekst") + "\n")
    print("znaków we wprowadzonym wyrazie: ", ileZnakow)

#zamknięcie pliku dla zwolnienia pamięci
plik.close()

#odczyt zawartosci pliku
plik = open("Plik.txt", "r")
#if plik.readable():
 #   tekst = plik.read()
#    print(tekst)
print("--- \n")

# inne sposoby odczytu pliku. Tworzenie listy
#if plik.readable():
   # print("Zawartosc pliku: ")
   # tekst = plik.readlines()
   # print(tekst)

#petla dla wyswietlania zawartosci w pliku
#for l in tekst:
#    print(l)

if plik.readable():
    print("Zawartość plikuu: ")
    for l in plik:
        print(l)

