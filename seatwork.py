def convert_currency(dollar):
    yen_rate = 146.67
    peso_rate = 57.17

    yen = dollar * yen_rate
    peso = dollar * peso_rate

    return peso, yen


user_input_amount = input("Enter currency in ($): ")

dollar_amounts = [float(d.strip()) for d in user_input_amount.split(",")]

print("\n{:<12} {:<15} {:<15}".format("Dollar($)", "Phil Peso(₱)", "Jpn Yen(¥)"))

for d in dollar_amounts:
    peso, yen = convert_currency(d)
    print(f"{d:<12,.2f} {peso:<15,.2f} {yen:<15,.2f}")

