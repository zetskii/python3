import time
import pyupbit
import datetime

access = "MpxoZr3htLZV2IIpCt6JIbDKwfxzEadosCGQ6bzt"
secret = "3hkxepxaNw7mxQe5IxS2TsYKUZMHIwS9YHJTmlyl"

# Now Time
now = datetime.datetime.now()

# Login
upbit = pyupbit.Upbit(access, secret)

print("-------------------------------------------------------------------------------------------------------")
print(f"{now} Login ... OK")
print("-------------------------------------------------------------------------------------------------------")


# 4hr 15MT Calculate Function Defined
def get_mt15(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="minute240", count=20)

    D1 = df.iloc[-1]
    D2 = df.iloc[-2]
    D3 = df.iloc[-3]
    D4 = df.iloc[-4]
    D5 = df.iloc[-5]
    D6 = df.iloc[-6]
    D7 = df.iloc[-7]
    D8 = df.iloc[-8]
    D9 = df.iloc[-9]
    D10 = df.iloc[-10]
    D11 = df.iloc[-11]
    D12 = df.iloc[-12]
    D13 = df.iloc[-13]
    D14 = df.iloc[-14]
    D15 = df.iloc[-15]

    sum1 = D1['open'] + D2['open'] + D3['open'] + D4['open'] + D5['open'] + D6['open'] + D7['open'] + D8['open'] + D9['open'] + D10['open']
    sum2 = D11['open'] + D12['open'] + D13['open'] + D14['open'] + D15['open']

    mt15 = (sum1 + sum2) / 15

    return mt15

# initialize

op_mode = True

ETH_hold = True
ADA_hold = True
TRX_hold = True
CHZ_hold = False
MANA_hold = True

BTC_price = pyupbit.get_current_price("KRW-BTC")
ETH_price = pyupbit.get_current_price("KRW-ETH")
ADA_price = pyupbit.get_current_price("KRW-ADA")
TRX_price = pyupbit.get_current_price("KRW-TRX")
CHZ_price = pyupbit.get_current_price("KRW-CHZ")
MANA_price = pyupbit.get_current_price("KRW-MANA")

print("Now Price Initialized ... OK")
print(f"Now Price : BTC {BTC_price} / ETH {ETH_price} / ADA {ADA_price} / TRX {TRX_price} / CHZ {CHZ_price} / MANA {MANA_price}")
print("-------------------------------------------------------------------------------------------------------")
time.sleep(0.5)

BTC_mt15 = get_mt15("KRW-BTC")
ETH_mt15 = get_mt15("KRW-ETH")
ADA_mt15 = get_mt15("KRW-ADA")
TRX_mt15 = get_mt15("KRW-TRX")
CHZ_mt15 = get_mt15("KRW-CHZ")
MANA_mt15 = get_mt15("KRW-MANA")

print("MT15 Initialized ... OK")
print(f"MT15 : BTC {BTC_mt15:.1f} / ETH {ETH_mt15:.1f} / ADA {ADA_mt15:.1f} / TRX {TRX_mt15:.1f} / CHZ {CHZ_mt15:.1f} / MANA {MANA_mt15:.1f}")
print("-------------------------------------------------------------------------------------------------------")
time.sleep(0.5)

KRW_balance = upbit.get_balance("KRW")
KRW_balance_div = KRW_balance / 5

print("KRW Balance Initialized ... OK")
print(f"Hold Status : ETH {ETH_hold} / ADA {ADA_hold} / TRX {TRX_hold} / CHZ {CHZ_hold} / MANA {MANA_hold}")
print(f"KRW_Balance: {KRW_balance:.1f} / KRW_balance_div: {KRW_balance_div:.1f}")
print("-------------------------------------------------------------------------------------------------------")
time.sleep(0.5)

print("[4hr 15MT Strategy] Auto Trade Start ... OK")
print("-------------------------------------------------------------------------------------------------------")


# Auto Trade Start (2sec Loop)
while True:

    try:

        # Now Time
        now = datetime.datetime.now()

        ### Daily 01:00, 05:00, 09:00, 13:00, 17:00, 21:00 Start #######################################################################################################

        # MT15 Update -> Now Price Update -> Sell -> KRW Update -> Buy
        if (now.hour == 1 or now.hour == 5 or now.hour == 9 or now.hour == 13 or now.hour == 17 or now.hour == 21) and now.minute == 0 and (7 <= now.second <= 17):

            # MT15 Update
            BTC_mt15 = get_mt15("KRW-BTC")
            ETH_mt15 = get_mt15("KRW-ETH")
            ADA_mt15 = get_mt15("KRW-ADA")
            TRX_mt15 = get_mt15("KRW-TRX")
            CHZ_mt15 = get_mt15("KRW-CHZ")
            MANA_mt15 = get_mt15("KRW-MANA")

            op_mode = True

            print(f"{now} MT15 Update ... OK")
            print(f"MT15 : BTC {BTC_mt15:.1f} / ETH {ETH_mt15:.1f} / ADA {ADA_mt15:.1f} / TRX {TRX_mt15:.1f} / CHZ {CHZ_mt15:.1f} / MANA {MANA_mt15:.1f}")
            print("-------------------------------------------------------------------------------------------------------")
            time.sleep(0.5)

            # Now Price Update
            BTC_price = pyupbit.get_current_price("KRW-BTC")
            ETH_price = pyupbit.get_current_price("KRW-ETH")
            ADA_price = pyupbit.get_current_price("KRW-ADA")
            TRX_price = pyupbit.get_current_price("KRW-TRX")
            CHZ_price = pyupbit.get_current_price("KRW-CHZ")
            MANA_price = pyupbit.get_current_price("KRW-MANA")

            print(f"{now} Now Price Update ... OK")
            print(f"Now Price : BTC {BTC_price} / ETH {ETH_price} / ADA {ADA_price} / TRX {TRX_price} / CHZ {CHZ_price} / MANA {MANA_price}")
            print("-------------------------------------------------------------------------------------------------------")
            time.sleep(0.5)

            # Now Price <= MT15 --> Sell
            if op_mode is True and ETH_hold is True and ETH_price <= ETH_mt15:
                eth_balance = upbit.get_balance("KRW-ETH")
                upbit.sell_market_order("KRW-ETH", eth_balance)
                print(f"{now} ETH Sell ... OK")
                print("-------------------------------------------------------------------------------------------------------")
                ETH_hold = False

            if op_mode is True and ADA_hold is True and ADA_price <= ADA_mt15:
                ada_balance = upbit.get_balance("KRW-ADA")
                upbit.sell_market_order("KRW-ADA", ada_balance)
                print(f"{now} ADA Sell ... OK")
                print("-------------------------------------------------------------------------------------------------------")
                ADA_hold = False

            if op_mode is True and TRX_hold is True and TRX_price <= TRX_mt15:
                trx_balance = upbit.get_balance("KRW-TRX")
                upbit.sell_market_order("KRW-TRX", trx_balance)
                print(f"{now} TRX Sell ... OK")
                print("-------------------------------------------------------------------------------------------------------")
                TRX_hold = False

            if op_mode is True and CHZ_hold is True and CHZ_price <= CHZ_mt15:
                chz_balance = upbit.get_balance("KRW-CHZ")
                upbit.sell_market_order("KRW-CHZ", chz_balance)
                print(f"{now} CHZ Sell ... OK")
                print("-------------------------------------------------------------------------------------------------------")
                CHZ_hold = False

            if op_mode is True and MANA_hold is True and MANA_price <= MANA_mt15:
                mana_balance = upbit.get_balance("KRW-MANA")
                upbit.sell_market_order("KRW-MANA", mana_balance)
                print(f"{now} MANA Sell ... OK")
                print("-------------------------------------------------------------------------------------------------------")
                MANA_hold = False
            time.sleep(0.5)

            # KRW Balance Update & Divide
            if CHZ_hold is False and ETH_hold is False and ADA_hold is False and TRX_hold is False and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 5

            elif CHZ_hold is False and ETH_hold is False and ADA_hold is False and TRX_hold is False and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 4

            elif CHZ_hold is False and ETH_hold is False and ADA_hold is False and TRX_hold is True and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 4

            elif CHZ_hold is False and ETH_hold is False and ADA_hold is True and TRX_hold is False and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 4

            elif CHZ_hold is False and ETH_hold is True and ADA_hold is False and TRX_hold is False and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 4

            elif CHZ_hold is True and ETH_hold is False and ADA_hold is False and TRX_hold is False and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 4

            elif CHZ_hold is False and ETH_hold is False and ADA_hold is False and TRX_hold is True and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 3

            elif CHZ_hold is False and ETH_hold is False and ADA_hold is True and TRX_hold is False and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 3

            elif CHZ_hold is False and ETH_hold is False and ADA_hold is True and TRX_hold is True and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 3

            elif CHZ_hold is False and ETH_hold is True and ADA_hold is False and TRX_hold is False and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 3

            elif CHZ_hold is False and ETH_hold is True and ADA_hold is False and TRX_hold is True and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 3

            elif CHZ_hold is False and ETH_hold is True and ADA_hold is True and TRX_hold is False and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 3

            elif CHZ_hold is True and ETH_hold is False and ADA_hold is False and TRX_hold is False and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 3

            elif CHZ_hold is True and ETH_hold is False and ADA_hold is False and TRX_hold is True and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 3

            elif CHZ_hold is True and ETH_hold is False and ADA_hold is True and TRX_hold is False and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 3

            elif CHZ_hold is True and ETH_hold is True and ADA_hold is False and TRX_hold is False and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 3

            elif CHZ_hold is False and ETH_hold is False and ADA_hold is True and TRX_hold is True and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 2

            elif CHZ_hold is False and ETH_hold is True and ADA_hold is False and TRX_hold is True and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 2

            elif CHZ_hold is False and ETH_hold is True and ADA_hold is True and TRX_hold is False and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 2

            elif CHZ_hold is False and ETH_hold is True and ADA_hold is True and TRX_hold is True and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 2

            elif CHZ_hold is True and ETH_hold is False and ADA_hold is False and TRX_hold is True and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 2

            elif CHZ_hold is True and ETH_hold is False and ADA_hold is True and TRX_hold is False and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 2

            elif CHZ_hold is True and ETH_hold is False and ADA_hold is True and TRX_hold is True and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 2

            elif CHZ_hold is True and ETH_hold is True and ADA_hold is False and TRX_hold is False and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 2

            elif CHZ_hold is True and ETH_hold is True and ADA_hold is False and TRX_hold is True and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 2

            elif CHZ_hold is True and ETH_hold is True and ADA_hold is True and TRX_hold is False and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 2

            else:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 1

            print(f"{now} KRW Balance Update & Divide ... OK")
            print(f"Hold Status: ETH {ETH_hold} / ADA {ADA_hold} / TRX {TRX_hold} / CHZ {CHZ_hold} / MANA {MANA_hold}")
            print(f"KRW_Balance: {KRW_balance:.1f} / KRW_balance_div: {KRW_balance_div:.1f}")
            print("-------------------------------------------------------------------------------------------------------")
            time.sleep(0.5)
            
            #  BTC > MT15 & Now Price > MT15 --> Market Price Buy
            if op_mode is True and ETH_price is not None and BTC_price is not None and ETH_hold is False and ETH_price > ETH_mt15 and BTC_price > BTC_mt15:
                upbit.buy_market_order("KRW-ETH", KRW_balance_div * 0.9994)
                print(f"{now} Today ETH Buy ... OK")
                print("-------------------------------------------------------------------------------------------------------")
                ETH_hold = True

            if op_mode is True and ADA_price is not None and BTC_price is not None and ADA_hold is False and ADA_price > ADA_mt15 and BTC_price > BTC_mt15:
                upbit.buy_market_order("KRW-ADA", KRW_balance_div * 0.9994)
                print(f"{now} Today ADA Buy ... OK")
                print("-------------------------------------------------------------------------------------------------------")
                ADA_hold = True

            if op_mode is True and TRX_price is not None and BTC_price is not None and TRX_hold is False and TRX_price > TRX_mt15 and BTC_price > BTC_mt15:
                upbit.buy_market_order("KRW-TRX", KRW_balance_div * 0.9994)
                print(f"{now} Today TRX Buy ... OK")
                print("-------------------------------------------------------------------------------------------------------")
                TRX_hold = True

            if op_mode is True and CHZ_price is not None and BTC_price is not None and CHZ_hold is False and CHZ_price > CHZ_mt15 and BTC_price > BTC_mt15:
                upbit.buy_market_order("KRW-CHZ", KRW_balance_div * 0.9994)
                print(f"{now} Today CHZ Buy ... OK")
                print("-------------------------------------------------------------------------------------------------------")
                CHZ_hold = True

            if op_mode is True and MANA_price is not None and BTC_price is not None and MANA_hold is False and MANA_price > MANA_mt15 and BTC_price > BTC_mt15:
                upbit.buy_market_order("KRW-MANA", KRW_balance_div * 0.9994)
                print(f"{now} Today MANA Buy ... OK")
                print("-------------------------------------------------------------------------------------------------------")
                MANA_hold = True

            time.sleep(8)

        # 2sec Delay
        time.sleep(2)


    except Exception as e:
        print(e)
        time.sleep(1)
