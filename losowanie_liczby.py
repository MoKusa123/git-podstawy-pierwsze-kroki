import random
import sys

def loteria():
    try:
        while True:
            bottom_number = int(input('Podaj dolny przedział losowania: '))
            top_number = int(input('Podaj dolny przedział losowania: '))
            guessed = random.randint(bottom_number, top_number)
            my_guess = int(input('Podaj liczbę z okreslonego uprzednio przedziału: '))
            if my_guess < bottom_number or my_guess > top_number:
                print('Wybrałeś numer spoza skali. Gramy od nowa.')
            elif my_guess in range(bottom_number, top_number):
                while my_guess != guessed:
                    if my_guess > guessed:
                        print('Podana liczba jest za duza')
                        my_guess = int(input('Podaj liczbę: '))
                    if my_guess < guessed:
                        print('Podana liczba jest za mala')
                        my_guess = int(input('Podaj liczbę: '))
                else:
                    print('Brawo, udalo Ci sie zgadnac!')
                    break
    except ValueError as e:
        print('Podana wartosc musi byc liczbą, bo:', e)

def dogrywka():
    while True:
        ensuite = input('Chcesz grać dalej? Y/N ')
        if ensuite == 'N':
            input('No to narka! (Press Enter to finish the code)')
            sys.exit(0)
        if ensuite == 'Y':
            loteria()
        else:
            print('Musisz wybrac : Y/N')

def execution():
    try:
        loteria()
    except ValueError as e:
        print('Podana wartosc musi byc liczbą, bo:', e)
    try:
        dogrywka()
    except ValueError as e:
        print('Podana wartosc musi byc liczbą, bo:', e)

execution()
