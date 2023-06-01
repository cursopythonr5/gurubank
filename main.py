from src.data import ask_movement
from src.utils import save_deposit, save_withdraw, get_printstatement

options = 0

while options != 4:

    options = int(input("Que quieres hacer? \n 1. Deposito \n 2. Retiro \n 3. Ver extracto \n 4. Salir \n"))

    if options == 1:
        save_deposit(ask_movement())

    elif options == 2:
        save_withdraw(ask_movement())

    elif options == 3:
        get_printstatement()

    else:
        print("No elegiste una opción.")

print("Saliste")