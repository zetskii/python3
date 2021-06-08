import time
from numpy import False_
import pyupbit
import datetime

access = "MpxoZr3htLZV2IIpCt6JIbDKwfxzEadosCGQ6bzt"
secret = "3hkxepxaNw7mxQe5IxS2TsYKUZMHIwS9YHJTmlyl"

# Login
upbit = pyupbit.Upbit(access, secret)

# Target Calculate Function Defined
def cal_target(ticker):
    df = pyupbit.get_ohlcv(ticker, "day", count=3)
    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    yesterday_range = yesterday['high'] - yesterday['low']
    target = today['open'] + yesterday_range * 0.43           # K = 0.43
    return target

# 3 day Moving Average Calculate Function Defined
def get_ma3(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=3)   #3, 5, 10, 15 change
    ma3 = df['close'].rolling(3).mean().iloc[-1]
    return ma3

# initialize
BTC_target = cal_target("KRW-BTC")
ETH_target = cal_target("KRW-ETH")
ADA_target = cal_target("KRW-ADA")
DOGE_target = cal_target("KRW-DOGE")
MANA_target = cal_target("KRW-MANA")

BTC_ma3 = get_ma3("KRW-BTC")
ETH_ma3 = get_ma3("KRW-ETH")
ADA_ma3 = get_ma3("KRW-ADA")
DOGE_ma3 = get_ma3("KRW-DOGE")
MANA_ma3 = get_ma3("KRW-MANA")

op_mode = False

BTC_hold = False
ETH_hold = False
ADA_hold = False
DOGE_hold = False
MANA_hold = False


# Auto Trade Start
while True:

    try:

        # Now Time
        now = datetime.datetime.now()

        # 09:00:20 ~ 09:00:30 target Update
        if now.hour == 9 and now.minute == 0 and (20 <= now.second <= 30):
            BTC_target = cal_target("KRW-BTC")
            ETH_target = cal_target("KRW-ETH")
            ADA_target = cal_target("KRW-ADA")
            DOGE_target = cal_target("KRW-DOGE")
            MANA_target = cal_target("KRW-MANA")
            op_mode = True
            time.sleep(10)
        
    
        # Now Price (every 1sec)
        BTC_price = pyupbit.get_current_price("KRW-BTC")
        ETH_price = pyupbit.get_current_price("KRW-ETH")
        ADA_price = pyupbit.get_current_price("KRW-ADA")
        DOGE_price = pyupbit.get_current_price("KRW-DOGE")
        MANA_price = pyupbit.get_current_price("KRW-MANA")



        # KRW balace -> Divide (every 1sec)

        if BTC_hold is False and ETH_hold is False and ADA_hold is False and DOGE_hold is False and MANA_hold is False:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 5

        elif BTC_hold is False and ETH_hold is False and ADA_hold is False and DOGE_hold is False and MANA_hold is True:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 4

        elif BTC_hold is False and ETH_hold is False and ADA_hold is False and DOGE_hold is True and MANA_hold is False:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 4

        elif BTC_hold is False and ETH_hold is False and ADA_hold is True and DOGE_hold is False and MANA_hold is False:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 4

        elif BTC_hold is False and ETH_hold is True and ADA_hold is False and DOGE_hold is False and MANA_hold is False:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 4

        elif BTC_hold is True and ETH_hold is False and ADA_hold is False and DOGE_hold is False and MANA_hold is False:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 4

        elif BTC_hold is False and ETH_hold is False and ADA_hold is False and DOGE_hold is True and MANA_hold is True:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 3

        elif BTC_hold is False and ETH_hold is False and ADA_hold is True and DOGE_hold is False and MANA_hold is True:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 3

        elif BTC_hold is False and ETH_hold is False and ADA_hold is True and DOGE_hold is True and MANA_hold is False:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 3

        elif BTC_hold is False and ETH_hold is True and ADA_hold is False and DOGE_hold is False and MANA_hold is True:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 3

        elif BTC_hold is False and ETH_hold is True and ADA_hold is False and DOGE_hold is True and MANA_hold is False:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 3

        elif BTC_hold is False and ETH_hold is True and ADA_hold is True and DOGE_hold is False and MANA_hold is False:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 3

        elif BTC_hold is True and ETH_hold is False and ADA_hold is False and DOGE_hold is False and MANA_hold is True:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 3

        elif BTC_hold is True and ETH_hold is False and ADA_hold is False and DOGE_hold is True and MANA_hold is False:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 3

        elif BTC_hold is True and ETH_hold is False and ADA_hold is True and DOGE_hold is False and MANA_hold is False:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 3

        elif BTC_hold is True and ETH_hold is True and ADA_hold is False and DOGE_hold is False and MANA_hold is False:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 3

        elif BTC_hold is False and ETH_hold is False and ADA_hold is True and DOGE_hold is True and MANA_hold is True:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 2

        elif BTC_hold is False and ETH_hold is True and ADA_hold is False and DOGE_hold is True and MANA_hold is True:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 2

        elif BTC_hold is False and ETH_hold is True and ADA_hold is True and DOGE_hold is False and MANA_hold is True:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 2

        elif BTC_hold is False and ETH_hold is True and ADA_hold is True and DOGE_hold is True and MANA_hold is False:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 2

        elif BTC_hold is True and ETH_hold is False and ADA_hold is False and DOGE_hold is True and MANA_hold is True:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 2

        elif BTC_hold is True and ETH_hold is False and ADA_hold is True and DOGE_hold is False and MANA_hold is True:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 2

        elif BTC_hold is True and ETH_hold is False and ADA_hold is True and DOGE_hold is True and MANA_hold is False:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 2

        elif BTC_hold is True and ETH_hold is True and ADA_hold is False and DOGE_hold is False and MANA_hold is True:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 2

        elif BTC_hold is True and ETH_hold is True and ADA_hold is False and DOGE_hold is True and MANA_hold is False:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 2

        elif BTC_hold is True and ETH_hold is True and ADA_hold is True and DOGE_hold is False and MANA_hold is False:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 2

        else:
            KRW_balance = upbit.get_balance("KRW")
            KRW_balance_div = KRW_balance / 1



    
        # BTC _ Market Price Buy (every 1sec)
        if op_mode is True and BTC_price is not None and BTC_price >= BTC_target and BTC_hold is False and BTC_price >= BTC_ma3:
            upbit.buy_market_order("KRW-BTC", KRW_balance_div)
            BTC_hold = True

        # ETH _ Market Price Buy (every 1sec)
        if op_mode is True and ETH_price is not None and ETH_price >= ETH_target and ETH_hold is False and ETH_price >= ETH_ma3:
           upbit.buy_market_order("KRW-ETH", KRW_balance_div)
           ETH_hold = True

        # ADA _ Market Price Buy (every 1sec)
        if op_mode is True and ADA_price is not None and ADA_price >= ADA_target and ADA_hold is False and ADA_price >= ADA_ma3:
            upbit.buy_market_order("KRW-ADA", KRW_balance_div)
            ADA_hold = True

        # DOGE _ Market Price Buy (every 1sec)
        if op_mode is True and DOGE_price is not None and DOGE_price >= DOGE_target and DOGE_hold is False and DOGE_price >= DOGE_ma3:
            upbit.buy_market_order("KRW-DOGE", KRW_balance_div)
            DOGE_hold = True

        # MANA _ Market Price Buy (every 1sec)
        if op_mode is True and MANA_price is not None and MANA_price >= MANA_target and MANA_hold is False and MANA_price >= MANA_ma3:
            upbit.buy_market_order("KRW-MANA", KRW_balance_div)
            MANA_hold = True




        # Next Day 08:59:30 ~ 08:59:40 ALL Sell (Market Price)
        if now.hour == 8 and now.minute == 59 and (30 <= now.second <=40):
            if op_mode is True and BTC_hold is True:
                btc_balance = upbit.get_balance("KRW-BTC")
                upbit.sell_market_order("KRW-BTC", btc_balance)
                BTC_hold = False

            if op_mode is True and ETH_hold is True:
                eth_balance = upbit.get_balance("KRW-ETH")
                upbit.sell_market_order("KRW-ETH", eth_balance)
                ETH_hold = False

            if op_mode is True and ADA_hold is True:
                ada_balance = upbit.get_balance("KRW-ADA")
                upbit.sell_market_order("KRW-ADA", ada_balance)
                ADA_hold = False

            if op_mode is True and DOGE_hold is True:
                doge_balance = upbit.get_balance("KRW-DOGE")
                upbit.sell_market_order("KRW-DOGE", doge_balance)
                DOGE_hold = False

            if op_mode is True and MANA_hold is True:
                mana_balance = upbit.get_balance("KRW-MANA")
                upbit.sell_market_order("KRW-MANA", mana_balance)
                MANA_hold = False

            op_mode = False
            time.sleep(10)



        # print message (every 1sec)
          
        #print(f"{now} B_P: {BTC_price} B_T: {BTC_target} E_P: {ETH_price} E_T: {ETH_target} A_P: {ADA_price} A_T: {ADA_target} D_P: {DOGE_price} D_T: {DOGE_target} M_P: {MANA_price} M_T: {MANA_target}")

        print(f"{now.second} BTC: {BTC_price} {BTC_target} {BTC_ma3} {BTC_hold} / ETH: {ETH_price} {ETH_target} {ETH_ma3} {ETH_hold} / ADA: {ADA_price} {ADA_target} {ADA_ma3} {ADA_hold} / DOGE: {DOGE_price} {DOGE_target} {DOGE_ma3} {DOGE_hold} / MANA: {MANA_price} {MANA_target} {MANA_ma3} {MANA_hold}")
        
        
        #print(f"Time: {now} BTC_ma3: {BTC_ma3} ETH_ma3: {ETH_ma3} ADA_ma3: {ADA_ma3} DOGE_ma3: {DOGE_ma3} MANA_ma3: {MANA_ma3}")        
        
        #print(f"KRW Balance: {KRW_balance} KRW DIV Balance: {KRW_balance_div}")

        # 1초 Delay
        time.sleep(1)



    except Exception as e:
        print(e)
        time.sleep(1)
