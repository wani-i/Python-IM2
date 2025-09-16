# import math

# # def greetings(str):
# #     print(f'Hello Philippines, {str}')

# # greetings('Aldwane')

# # def get_student(id, name, prog):
# #     print(f'idnum = {id} name= {name} course = {prog}')

# # get_student(id='21-UR-1457',name='Aldwane',prog='IT')

# # # def get_student(**student):
# # #     print(f'Id number{student['id']} Name {student['str']} Program {student['prog']})

# # # get_student(id='21-UR-1457',name='Aldwane',prog='IT')

# # def calculate(x,y):
# #     sum = x + y 
# #     avg = sum / 2
# #     return (sum, avg)

# # sum1, avg1 = calculate(10.5, 7.7)
# # print(f'Sum: {sum1}, Average: {avg1}')

# #s
# str = 'Philippines'
# print(str.count('i'))
# print(str.lower().count('p'))

# str = ' Aldwane  '
# print(str.strip())
# print(str.replace('a', 'A'))

# list_name = ['Aldwane', 'Tendido', 'Figuracion']
# print('_'.join(list_name))

# str4 = 'Aldwane,Tendido,Figuracion'
# print(str4.split(','))

# #iterator functions

# list_num = [1,67,45,2,9]
# print(f'Sum {sum(list_num)} Max {max(list_num)} Min {min(list_num)}')

# print(math.ceil(78.67))
# print(math.floor(78.4))
# print(math.sqrt(2))
# print(math.pow(2, 7))


# def convert_currency(dollar):
#     yen_rate = 57.17
#     peso_rate = 146.67

#     yen = dollar * yen_rate
#     peso = dollar * peso_rate

#     return peso, yen

# user_input_amount = float(input('Enter currency in ($): '))

# peso, yen = convert_currency(user_input_amount)

# print(f'Dollar($): {user_input_amount:,.2f}')
# print(f'Phil Peso(₱): {peso:,.2f}')
# print(f'Jpn Yen(¥): {yen:,.2f}')

def convert_currency(dollar):
    # Conversion rates
    yen_rate = 146.67
    peso_rate = 57.17

    # Conversion
    yen = dollar * yen_rate
    peso = dollar * peso_rate

    return peso, yen


# User enters values separated by commas
dollar_input = input("Enter currency in ($): ")

# Split by comma and strip spaces
dollar_amounts = [float(d.strip()) for d in dollar_input.split(",")]

# Print header
print("\n{:<12} {:<15} {:<15}".format("Dollar($)", "Phil Peso(₱)", "Jpn Yen(¥)"))

# Process each value
for d in dollar_amounts:
    peso, yen = convert_currency(d)
    print(f"{d:<12,.2f} {peso:<15,.2f} {yen:<15,.2f}")

