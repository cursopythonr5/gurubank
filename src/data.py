def ask_movement():
    account_deposit = input("Ingresa un monto para depositar: ")
    if account_deposit.isdigit() and int(account_deposit) > 0:
        print(f'El monto es {account_deposit}. ¡El monto que ingresaste es válido!')
        return int(account_deposit)

    else:
        print("El monto que ingresaste es inválido. Debes ingresar un monto válido")