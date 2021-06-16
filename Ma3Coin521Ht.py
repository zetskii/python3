import time
from numpy import False_
import pyupbit
import datetime

access = "MpxoZr3htLZV2IIpCt6JIbDKwfxzEadosCGQ6bzt"
secret = "3hkxepxaNw7mxQe5IxS2TsYKUZMHIwS9YHJTmlyl"

# Now Time
now = datetime.datetime.now()

# Login
upbit = pyupbit.Upbit(access, secret)

print("----------------------------------------------------------------------------------------------------------------------")
print(f"{now} Login ... OK")
print("----------------------------------------------------------------------------------------------------------------------")


# Daily 21:00 --> 3 day Moving Average Calculate Function Defined
def get_ma3(ticker):
    df = pyupbit.get_daily_ohlcv_from_base(ticker, base=21)  
    
    D_0day = df.iloc[-1]
    D_1day = df.iloc[-2]
    D_2day = df.iloc[-3]

    ma3 = (D_0day['open'] + D_1day['open'] + D_2day['open']) / 3

    return ma3


# initialize
BTC_price = pyupbit.get_current_price("KRW-BTC")
ETH_price = pyupbit.get_current_price("KRW-ETH")
ADA_price = pyupbit.get_current_price("KRW-ADA")
TRX_price = pyupbit.get_current_price("KRW-TRX")
MANA_price = pyupbit.get_current_price("KRW-MANA")

print(f"Now Price Initialized ... OK")
print(f"BTC_Price: {BTC_price:.1f} / ETH_Price: {ETH_price:.1f} / ADA_Price: {ADA_price:.1f} / TRX_Price: {TRX_price:.1f} / MANA_Price: {MANA_price:.1f}")
print("----------------------------------------------------------------------------------------------------------------------")
time.sleep(1)

BTC_ma3 = get_ma3("KRW-BTC")
ETH_ma3 = get_ma3("KRW-ETH")
ADA_ma3 = get_ma3("KRW-ADA")
TRX_ma3 = get_ma3("KRW-TRX")
MANA_ma3 = get_ma3("KRW-MANA")

print(f"MA3 Initialized ... OK")
print(f"BTC_ma3: {BTC_ma3:.1f} / ETH_ma3: {ETH_ma3:.1f} / ADA_ma3: {ADA_ma3:.1f} / TRX_ma3: {TRX_ma3:.1f} / MANA_ma3: {MANA_ma3:.1f}")
print("----------------------------------------------------------------------------------------------------------------------")
time.sleep(1)

KRW_balance = upbit.get_balance("KRW")
KRW_balance_div = KRW_balance / 5

print(f"KRW Balance Initialized ... OK")
print(f"KRW_Balance: {KRW_balance:.1f} / KRW_balance_div: {KRW_balance_div:.1f}")
print("----------------------------------------------------------------------------------------------------------------------")
time.sleep(1)

print(f"Auto Trade Mode Start ... OK")
print("----------------------------------------------------------------------------------------------------------------------")

op_mode = False

BTC_hold = False
ETH_hold = False
ADA_hold = False
TRX_hold = False
MANA_hold = False


# Auto Trade Mode Start
while True:

    try:


        # Now Time (every 1sec)
        now = datetime.datetime.now()


        # Now Price (every 1sec)
        BTC_price = pyupbit.get_current_price("KRW-BTC")
        ETH_price = pyupbit.get_current_price("KRW-ETH")
        ADA_price = pyupbit.get_current_price("KRW-ADA")
        TRX_price = pyupbit.get_current_price("KRW-TRX")
        MANA_price = pyupbit.get_current_price("KRW-MANA")


        # 21:00:45 ~ 21:00:55 MA3 Update
        if now.hour == 21 and now.minute == 0 and (45 <= now.second <= 55):

            BTC_ma3 = get_ma3("KRW-BTC")
            ETH_ma3 = get_ma3("KRW-ETH")
            ADA_ma3 = get_ma3("KRW-ADA")
            TRX_ma3 = get_ma3("KRW-TRX")
            MANA_ma3 = get_ma3("KRW-MANA")

            op_mode = True

            print(f"{now} Today MA3 Update ... OK")
            print(f"BTC_ma3: {BTC_ma3:.1f} / ETH_ma3: {ETH_ma3:.1f} / ADA_ma3: {ADA_ma3:.1f} / TRX_ma3: {TRX_ma3:.1f} / MANA_ma3: {MANA_ma3:.1f}")
            print("----------------------------------------------------------------------------------------------------------------------")
            time.sleep(10)


        # 21:01:05 ~ 21:01:15 Now Price <= MA3 --> Each Ticker Market Price ALL Sell
        if now.hour == 21 and now.minute == 1 and (5 <= now.second <= 15):

            BTC_price = pyupbit.get_current_price("KRW-BTC")
            ETH_price = pyupbit.get_current_price("KRW-ETH")
            ADA_price = pyupbit.get_current_price("KRW-ADA")
            TRX_price = pyupbit.get_current_price("KRW-TRX")
            MANA_price = pyupbit.get_current_price("KRW-MANA")

            time.sleep(1)

            if op_mode is True and BTC_hold is True and BTC_price <= BTC_ma3:
                btc_balance = upbit.get_balance("KRW-BTC")
                upbit.sell_market_order("KRW-BTC", btc_balance)
                print(f"{now} Today BTC Sell ... OK")
                print("----------------------------------------------------------------------------------------------------------------------")
                BTC_hold = False

            if op_mode is True and ETH_hold is True and ETH_price <= ETH_ma3:
                eth_balance = upbit.get_balance("KRW-ETH")
                upbit.sell_market_order("KRW-ETH", eth_balance)
                print(f"{now} Today ETH Sell ... OK")
                print("----------------------------------------------------------------------------------------------------------------------")
                ETH_hold = False

            if op_mode is True and ADA_hold is True and ADA_price <= ADA_ma3:
                ada_balance = upbit.get_balance("KRW-ADA")
                upbit.sell_market_order("KRW-ADA", ada_balance)
                print(f"{now} Today ADA Sell ... OK")
                print("----------------------------------------------------------------------------------------------------------------------")
                ADA_hold = False

            if op_mode is True and TRX_hold is True and TRX_price <= TRX_ma3:
                trx_balance = upbit.get_balance("KRW-TRX")
                upbit.sell_market_order("KRW-TRX", trx_balance)
                print(f"{now} Today TRX Sell ... OK")
                print("----------------------------------------------------------------------------------------------------------------------")
                BTC_hold = False

            if op_mode is True and MANA_hold is True and MANA_price <= MANA_ma3:
                mana_balance = upbit.get_balance("KRW-MANA")
                upbit.sell_market_order("KRW-MANA", mana_balance)
                print(f"{now} Today MANA Sell ... OK")
                print("----------------------------------------------------------------------------------------------------------------------")
                MANA_hold = False

            time.sleep(9)


        # 21:01:20 ~ 21:01:30 KRW Balance Update --> Divide
        if now.hour == 21 and now.minute == 1 and (20 <= now.second <= 30):

            if BTC_hold is False and ETH_hold is False and ADA_hold is False and TRX_hold is False and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 5

            elif BTC_hold is False and ETH_hold is False and ADA_hold is False and TRX_hold is False and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 4

            elif BTC_hold is False and ETH_hold is False and ADA_hold is False and TRX_hold is True and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 4

            elif BTC_hold is False and ETH_hold is False and ADA_hold is True and TRX_hold is False and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 4

            elif BTC_hold is False and ETH_hold is True and ADA_hold is False and TRX_hold is False and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 4

            elif BTC_hold is True and ETH_hold is False and ADA_hold is False and TRX_hold is False and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 4

            elif BTC_hold is False and ETH_hold is False and ADA_hold is False and TRX_hold is True and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 3

            elif BTC_hold is False and ETH_hold is False and ADA_hold is True and TRX_hold is False and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 3

            elif BTC_hold is False and ETH_hold is False and ADA_hold is True and TRX_hold is True and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 3

            elif BTC_hold is False and ETH_hold is True and ADA_hold is False and TRX_hold is False and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 3

            elif BTC_hold is False and ETH_hold is True and ADA_hold is False and TRX_hold is True and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 3

            elif BTC_hold is False and ETH_hold is True and ADA_hold is True and TRX_hold is False and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 3

            elif BTC_hold is True and ETH_hold is False and ADA_hold is False and TRX_hold is False and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 3

            elif BTC_hold is True and ETH_hold is False and ADA_hold is False and TRX_hold is True and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 3

            elif BTC_hold is True and ETH_hold is False and ADA_hold is True and TRX_hold is False and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 3

            elif BTC_hold is True and ETH_hold is True and ADA_hold is False and TRX_hold is False and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 3

            elif BTC_hold is False and ETH_hold is False and ADA_hold is True and TRX_hold is True and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 2

            elif BTC_hold is False and ETH_hold is True and ADA_hold is False and TRX_hold is True and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 2

            elif BTC_hold is False and ETH_hold is True and ADA_hold is True and TRX_hold is False and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 2

            elif BTC_hold is False and ETH_hold is True and ADA_hold is True and TRX_hold is True and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 2

            elif BTC_hold is True and ETH_hold is False and ADA_hold is False and TRX_hold is True and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 2

            elif BTC_hold is True and ETH_hold is False and ADA_hold is True and TRX_hold is False and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 2

            elif BTC_hold is True and ETH_hold is False and ADA_hold is True and TRX_hold is True and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 2

            elif BTC_hold is True and ETH_hold is True and ADA_hold is False and TRX_hold is False and MANA_hold is True:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 2

            elif BTC_hold is True and ETH_hold is True and ADA_hold is False and TRX_hold is True and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 2

            elif BTC_hold is True and ETH_hold is True and ADA_hold is True and TRX_hold is False and MANA_hold is False:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 2

            else:
                KRW_balance = upbit.get_balance("KRW")
                KRW_balance_div = KRW_balance / 1

            print(f"{now} Today KRW Balance Update ... OK")
            print(f"KRW_Balance: {KRW_balance:.1f} / KRW_balance_div: {KRW_balance_div:.1f}")
            print("----------------------------------------------------------------------------------------------------------------------")

            time.sleep(10)


        # 21:01:35 ~ 21:01:45 Now Price > MA3 --> Each Ticker Market Price Buy (KRW Divided * 0.9994)
        if now.hour == 21 and now.minute == 1 and (35 <= now.second <= 45):

            BTC_price = pyupbit.get_current_price("KRW-BTC")
            ETH_price = pyupbit.get_current_price("KRW-ETH")
            ADA_price = pyupbit.get_current_price("KRW-ADA")
            TRX_price = pyupbit.get_current_price("KRW-TRX")
            MANA_price = pyupbit.get_current_price("KRW-MANA")

            time.sleep(1)

            # BTC _ Market Price Buy
            if op_mode is True and BTC_price is not None and BTC_hold is False and BTC_price > BTC_ma3:
                upbit.buy_market_order("KRW-BTC", KRW_balance_div * 0.9994)
                print(f"{now} Today BTC Buy ... OK")
                print("----------------------------------------------------------------------------------------------------------------------")
                BTC_hold = True

            # ETH _ Market Price Buy
            if op_mode is True and ETH_price is not None and ETH_hold is False and ETH_price > ETH_ma3:
                upbit.buy_market_order("KRW-ETH", KRW_balance_div * 0.9994)
                print(f"{now} Today ETH Buy ... OK")
                print("----------------------------------------------------------------------------------------------------------------------")
                ETH_hold = True

            # ADA _ Market Price Buy
            if op_mode is True and ADA_price is not None and ADA_hold is False and ADA_price > ADA_ma3:
                upbit.buy_market_order("KRW-ADA", KRW_balance_div * 0.9994)
                print(f"{now} Today ADA Buy ... OK")
                print("----------------------------------------------------------------------------------------------------------------------")
                ADA_hold = True

            # TRX _ Market Price Buy
            if op_mode is True and TRX_price is not None and TRX_hold is False and TRX_price > TRX_ma3:
                upbit.buy_market_order("KRW-TRX", KRW_balance_div * 0.9994)
                print(f"{now} Today TRX Buy ... OK")
                print("----------------------------------------------------------------------------------------------------------------------")
                TRX_hold = True

            # MANA _ Market Price Buy
            if op_mode is True and MANA_price is not None and MANA_hold is False and MANA_price > MANA_ma3:
                upbit.buy_market_order("KRW-MANA", KRW_balance_div * 0.9994)
                print(f"{now} Today MANA Buy ... OK")
                print("----------------------------------------------------------------------------------------------------------------------")
                MANA_hold = True

            time.sleep(9)

        # 1sec Delay
        time.sleep(1)


    except Exception as e:
        print(e)
        time.sleep(1)
