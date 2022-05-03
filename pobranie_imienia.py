def pobranie_imienia():
    while True:
        pytanie = input('Proszę podaj swoje imię ')
        if pytanie.isalpha():
            if pytanie[-1] == 'a':
                print(f'Imię które wpisałas to : {pytanie}')
                print(f'Miło mi Cię poznać!, {pytanie} ^^')
                break
            if pytanie[-1] != 'a':
                print(f'Imię które wpisałeś to : {pytanie}')
                print(f'Miło mi Cię poznać!, {pytanie} ^^')
                break
        else:
            print('Podany zwrot to nie imię, lecz login')

pobranie_imienia()



