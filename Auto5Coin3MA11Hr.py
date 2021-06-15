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

# Target1 Calculate Function Defined
def cal_target1(ticker):
    df = pyupbit.get_daily_ohlcv_from_base(ticker, base=11)
    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    yesterday_range = yesterday['high'] - yesterday['low']
    target = today['open'] + yesterday_range * 0.43           # K = 0.43
    return target

# Target2 Calculate Function Defined
def cal_target2(ticker):
    df = pyupbit.get_daily_ohlcv_from_base(ticker, base=11)
    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    yesterday_range = yesterday['high'] - yesterday['low']
    target = today['open'] + yesterday_range * 0.5           # K = 0.5
    return target   

# 3 day Moving Average Calculate Function Defined
def get_ma3(ticker):
    df = pyupbit.get_daily_ohlcv_from_base(ticker, base=11)   #3, 5, 10, 15 change
    ma3 = df['close'].rolling(3).mean().iloc[-1]
    return ma3

# initialize
BTC_target1 = cal_target1("KRW-BTC")
ETH_target1 = cal_target1("KRW-ETH")
ADA_target1 = cal_target1("KRW-ADA")
TRX_target1 = cal_target1("KRW-TRX")
MANA_target1 = cal_target1("KRW-MANA")

print(f"Target1 Initialized ... OK")
print(f"BTC_Target1: {BTC_target1:.1f} / ETH_Target1: {ETH_target1:.1f} / ADA_Target1: {ADA_target1:.1f} / TRX_Target1: {TRX_target1:.1f} / MANA_Target1: {MANA_target1:.1f}")
print("----------------------------------------------------------------------------------------------------------------------")
time.sleep(1)

BTC_target2 = cal_target2("KRW-BTC")
ETH_target2 = cal_target2("KRW-ETH")
ADA_target2 = cal_target2("KRW-ADA")
TRX_target2 = cal_target2("KRW-TRX")
MANA_target2 = cal_target2("KRW-MANA")

print(f"Target2 Initialized ... OK")
print(f"BTC_Target2: {BTC_target2:.1f} / ETH_Target2: {ETH_target2:.1f} / ADA_Target2: {ADA_target2:.1f} / TRX_Target2: {TRX_target2:.1f} / MANA_Target2: {MANA_target2:.1f}")
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

        # Now Time
        now = datetime.datetime.now()

        # 11:01:05 ~ 11:01:15 target, ma3 Update
        if now.hour == 11 and now.minute == 1 and (5 <= now.second <= 15):
            BTC_target1 = cal_target1("KRW-BTC")
            ETH_target1 = cal_target1("KRW-ETH")
            ADA_target1 = cal_target1("KRW-ADA")
            TRX_target1 = cal_target1("KRW-TRX")
            MANA_target1 = cal_target1("KRW-MANA")

            print(f"{now} Today Target1 Update ... OK")
            print(f"BTC_Target1: {BTC_target1:.1f} / ETH_Target1: {ETH_target1:.1f} / ADA_Target1: {ADA_target1:.1f} / TRX_Target1: {TRX_target1:.1f} / MANA_Target1: {MANA_target1:.1f}")
            print("----------------------------------------------------------------------------------------------------------------------")
            time.sleep(1)

            BTC_target2 = cal_target2("KRW-BTC")
            ETH_target2 = cal_target2("KRW-ETH")
            ADA_target2 = cal_target2("KRW-ADA")
            TRX_target2 = cal_target2("KRW-TRX")
            MANA_target2 = cal_target2("KRW-MANA")

            print(f"{now} Today Target2 Update ... OK")
            print(f"BTC_Target2: {BTC_target2:.1f} / ETH_Target2: {ETH_target2:.1f} / ADA_Target2: {ADA_target2:.1f} / TRX_Target2: {TRX_target2:.1f} / MANA_Target2: {MANA_target2:.1f}")
            print("----------------------------------------------------------------------------------------------------------------------")
            time.sleep(1)

            BTC_ma3 = get_ma3("KRW-BTC")
            ETH_ma3 = get_ma3("KRW-ETH")
            ADA_ma3 = get_ma3("KRW-ADA")
            TRX_ma3 = get_ma3("KRW-TRX")
            MANA_ma3 = get_ma3("KRW-MANA")

            print(f"{now} Today MA3 Update ... OK")
            print(f"BTC_ma3: {BTC_ma3:.1f} / ETH_ma3: {ETH_ma3:.1f} / ADA_ma3: {ADA_ma3:.1f} / TRX_ma3: {TRX_ma3:.1f} / MANA_ma3: {MANA_ma3:.1f}")
            print("----------------------------------------------------------------------------------------------------------------------")
            time.sleep(1)

            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 5

            print(f"{now} Today KRW Balance Update ... OK")
            print(f"KRW_Balance: {KRW_balance:.1f} / KRW_balance_div: {KRW_balance_div:.1f}")
            print("----------------------------------------------------------------------------------------------------------------------")

            op_mode = True
            time.sleep(7)      


        # Now Price (every 1sec)
        BTC_price = pyupbit.get_current_price("KRW-BTC")
        ETH_price = pyupbit.get_current_price("KRW-ETH")
        ADA_price = pyupbit.get_current_price("KRW-ADA")
        TRX_price = pyupbit.get_current_price("KRW-TRX")
        MANA_price = pyupbit.get_current_price("KRW-MANA")



        # BTC _ Market Price Buy (every 1sec)
        if op_mode is True and BTC_price is not None and (BTC_target1 <= BTC_price <= BTC_target2) and BTC_hold is False and BTC_price >= BTC_ma3:
            upbit.buy_market_order("KRW-BTC", KRW_balance_div * 0.9994)
            print(f"{now} Today BTC Buy ... OK")
            print("----------------------------------------------------------------------------------------------------------------------")
            BTC_hold = True


        # ETH _ Market Price Buy (every 1sec)
        if op_mode is True and ETH_price is not None and (ETH_target1 <= ETH_price <= ETH_target2) and ETH_hold is False and ETH_price >= ETH_ma3:
           upbit.buy_market_order("KRW-ETH", KRW_balance_div * 0.9994)
           print(f"{now} Today ETH Buy ... OK")
           print("----------------------------------------------------------------------------------------------------------------------")
           ETH_hold = True

        # ADA _ Market Price Buy (every 1sec)
        if op_mode is True and ADA_price is not None and (ADA_target1 <= ADA_price <= ADA_target2) and ADA_hold is False and ADA_price >= ADA_ma3:
            upbit.buy_market_order("KRW-ADA", KRW_balance_div * 0.9994)
            print(f"{now} Today ADA Buy ... OK")
            print("----------------------------------------------------------------------------------------------------------------------")
            ADA_hold = True

        # TRX _ Market Price Buy (every 1sec)
        if op_mode is True and TRX_price is not None and (TRX_target1 <= TRX_price <= TRX_target2) and TRX_hold is False and TRX_price >= TRX_ma3:
            upbit.buy_market_order("KRW-TRX", KRW_balance_div * 0.9994)
            print(f"{now} Today TRX Buy ... OK")
            print("----------------------------------------------------------------------------------------------------------------------")
            TRX_hold = True

        # MANA _ Market Price Buy (every 1sec)
        if op_mode is True and MANA_price is not None and (MANA_target1 <= MANA_price <= MANA_target2) and MANA_hold is False and MANA_price >= MANA_ma3:
            upbit.buy_market_order("KRW-MANA", KRW_balance_div * 0.9994)
            print(f"{now} Today MANA Buy ... OK")
            print("----------------------------------------------------------------------------------------------------------------------")
            MANA_hold = True




        # Next Day 10:59:30 ~ 10:59:40 ALL Sell (Market Price)
        if now.hour == 10 and now.minute == 59 and (30 <= now.second <=40):
            if op_mode is True and BTC_hold is True:
                btc_balance = upbit.get_balance("KRW-BTC")
                upbit.sell_market_order("KRW-BTC", btc_balance)  # * 0.9995 fee deltete
                print(f"{now} Today BTC Sell ... OK")
                print("----------------------------------------------------------------------------------------------------------------------")
                BTC_hold = False

            if op_mode is True and ETH_hold is True:
                eth_balance = upbit.get_balance("KRW-ETH")
                upbit.sell_market_order("KRW-ETH", eth_balance)
                print(f"{now} Today ETH Sell ... OK")
                print("----------------------------------------------------------------------------------------------------------------------")
                ETH_hold = False

            if op_mode is True and ADA_hold is True:
                ada_balance = upbit.get_balance("KRW-ADA")
                upbit.sell_market_order("KRW-ADA", ada_balance)
                print(f"{now} Today ADA Sell ... OK")
                print("----------------------------------------------------------------------------------------------------------------------")
                ADA_hold = False

            if op_mode is True and TRX_hold is True:
                trx_balance = upbit.get_balance("KRW-TRX")
                upbit.sell_market_order("KRW-TRX", trx_balance)
                print(f"{now} Today TRX Sell ... OK")
                print("----------------------------------------------------------------------------------------------------------------------")
                TRX_hold = False

            if op_mode is True and MANA_hold is True:
                mana_balance = upbit.get_balance("KRW-MANA")
                upbit.sell_market_order("KRW-MANA", mana_balance)
                print(f"{now} Today MANA Sell ... OK")
                print("----------------------------------------------------------------------------------------------------------------------")
                MANA_hold = False

            op_mode = False
            time.sleep(10)


        # print message (every 1sec)
        #print(f"{now} B_P: {BTC_price} B_T: {BTC_target1} E_P: {ETH_price} E_T: {ETH_target1} A_P: {ADA_price} A_T: {ADA_target1} D_P: {TRX_price} D_T: {TRX_target1} M_P: {MANA_price} M_T: {MANA_target1}")
        #print(f"{now.second} BTC: {BTC_price} {BTC_target1} {BTC_ma3} {BTC_hold} / ETH: {ETH_price} {ETH_target1} {ETH_ma3} {ETH_hold} / ADA: {ADA_price} {ADA_target1} {ADA_ma3} {ADA_hold} / TRX: {TRX_price} {TRX_target1} {TRX_ma3} {TRX_hold} / MANA: {MANA_price} {MANA_target1} {MANA_ma3} {MANA_hold}")
        #print(f"Time: {now} BTC_ma3: {BTC_ma3} ETH_ma3: {ETH_ma3} ADA_ma3: {ADA_ma3} TRX_ma3: {TRX_ma3} MANA_ma3: {MANA_ma3}")        
        #print(f"KRW Balance: {KRW_balance} KRW DIV Balance: {KRW_balance_div}")

        # 1sec Delay
        time.sleep(1)

    except Exception as e:
        print(e)
        time.sleep(1)
