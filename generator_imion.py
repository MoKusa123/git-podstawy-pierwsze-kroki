import random
import sys

mozliwe = ['Janek Wisniewski', 'Predator', 'Motylia', 'DragandDropper', 'Tupalski', 'Marek Dywanik', 'Bombonierka']

def wybieranie():
    wybor = random.choice(mozliwe)
    print(f'Otoz, Twoje imie to: {wybor}')

def dogrywka():
    pytanie_2 = input('Chcesz zagrać jeszcze raz? (Y/N) ')
    if pytanie_2 == 'N':
        print(f'No to narka!')
        sys.exit(0)
    elif pytanie_2 == 'Y':
        wybieranie()
    else:
        print('Wybierz "Y" albo "N"')


def generator_imion():
    try:
        while True:
            pytanie_1 = input('Chcesz wiedzieć jakie jest Twoje imie i nazwisko w rownoleglej rzeczywistosci? (Y/N) ')
            if pytanie_1 == 'N':
                print('No to do nastepnego razu!')
                sys.exit(0)
            if pytanie_1 == 'Y':
                wybieranie()
                dogrywka()
            else:
                print('Wybierz "Y" albo "N"')
    except ValueError as e:
        print('Podana wartosc musi byc literą, bo:', e)

generator_imion()


