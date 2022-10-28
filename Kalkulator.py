
print("Wybierz działanie: ")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")

operation = input()

if operation == "1":
    num1 = input("Wpisz pierwsza liczbe: ")
    num2 = input("Wpisz druga liczbe: ")
    print("Wynik to " + str(int(num1) + int(num2)))
    #kod na dodawanie
elif operation == "2":
    num1 = input("Wpisz pierwsza liczbe: ")
    num2 = input("Wpisz druga liczbe: ")
    print("Wynik to " + str(int(num1) - int(num2)))
    #kod na odejmowanie
elif operation == "3":
    num1 = input("Wpisz pierwsza liczbe: ")
    num2 = input("Wpisz druga liczbe: ")
    print("Wynik to " + str(int(num1) * int(num2)))
    #kod na Mnożenie
elif operation == "4":
    num1 = input("Wpisz pierwsza liczbe: ")
    num2 = input("Wpisz druga liczbe: ")
    print("Wynik to " + str(int(num1) / int(num2)))
    #kod na DZielenie
else:
    print("Nie poprawne dane")