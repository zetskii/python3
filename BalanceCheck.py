import pyupbit

access = "MpxoZr3htLZV2IIpCt6JIbDKwfxzEadosCGQ6bzt"
secret = "3hkxepxaNw7mxQe5IxS2TsYKUZMHIwS9YHJTmlyl"
upbit = pyupbit.Upbit(access, secret)

balance = upbit.get_balances()

for i in range(len(balance)):
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(balance[i])
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
