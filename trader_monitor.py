from test_case import *


# 可以在此基础上进行任意的设计和修改
class TradeMonitor:
    def __init__(self):
        pass

    def on_trade(self, trade):
        print(trade)
        pass

    @staticmethod
    def alarm(atime, name, atype='quantity'):
        alarm_msg = '累计成交量报警'
        if atype == 'delta':
            alarm_msg = '累计Delta报警'
        print(atime, name, alarm_msg)


if __name__ == "__main__":
    monitor = TradeMonitor()

    load_param_data1()
    load_trade_data1(monitor)

    load_param_data2()
    load_trade_data2(monitor)
