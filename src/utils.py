from datetime import datetime

movements = []

def save_deposit(deposit):
    if len(movements) == 0:
        # Agregar un movimiento por primera vez
        movement = (deposit, datetime.now(), deposit)
        movements.append(movement)
    else:
        # Agregar un movimiento
        last_movement = movements[-1]
        balance = last_movement[2] + deposit
        movement = (deposit, datetime.now(), balance)
        movements.append(movement)

def save_withdraw(deposit):
    last_movement = movements[-1]
    balance = last_movement[2]
    if len(movements) == 0:
        print(f"No tienes saldo en tu cuenta, haz un deposito primero")
    elif len(movements) != 0 and balance < deposit:
        print(f"No tienes saldo en tu cuenta, haz un deposito primero")
    else:
        # Agregar un movimiento
        deposit = deposit * -1
        balance = balance + deposit
        movement = (deposit, datetime.now(), balance)
        movements.append(movement)

def get_printstatement():
    # Imprimir todos los movimientos
    for movement in movements:
        print(f"Monto: {movement[0]}, Fecha: {movement[1]}, Saldo: {movement[2]}")
    """print("Date       || Amount || Balance")
    for movement in movements:
        date = movimiento[1].strftime("%d/%m/%Y")
        amount = str(movimiento[0])
        balance = str(movimiento[2])
        print("{:<11}|| {:<7}|| {:<7}".format(date, amount, balance))"""