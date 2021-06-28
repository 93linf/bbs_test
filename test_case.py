from group import Group
from exchange import Exchange
from symbol import Symbol
from trader_monitor import TradeMonitor


# 请不要修改本文件!!!
Global_Data = {}


def load_param_data1():
    Global_Data['groups'] = [
        Group('Group1', 200, 20, 3000.0, 20),
        Group('Group2', 200, 20, 3000.0, 20),
        Group('Group3', 200, 20, 3000.0, 20)
    ]

    Global_Data['exchanges'] = [
        Exchange('Binance', 150, 10, 2500.0, 10),
        Exchange('Huobi', 150, 10, 2500.0, 10),
        Exchange('Okex', 150, 10, 2500.0, 10),
        Exchange('Bitfinex', 150, 10, 2500.0, 10),
    ]

    Global_Data['symbols'] = [
        Symbol('BTCUSDT', 'Binance', 'Group1', 100, 10, 2000.0, 10),
        Symbol('ETHUSDT', 'Binance', 'Group2', 100, 10, 2000.0, 10),
        Symbol('XRPUSDT', 'Huobi', 'Group3', 100, 10, 2000.0, 10),
        Symbol('LTCUSDT', 'Huobi', 'Group1', 100, 10, 2000.0, 10),
        Symbol('EOSUSDT', 'Okex', 'Group2', 100, 10, 2000.0, 10),
        Symbol('OKBUSDT', 'Okex', 'Group3', 100, 10, 2000.0, 10),
        Symbol('XMRUSDT', 'Bitfinex', 'Group1', 100, 10, 2000.0, 10),
        Symbol('BCHUSDT', 'Bitfinex', 'Group2', 100, 10, 2000.0, 10)
    ]


def load_trade_data1(monitor: TradeMonitor):
    # no alerts
    monitor.on_trade({'name': 'BTCUSDT', 'time':  0, 'side': 'BUY', 'quantity': 10, 'price': 25.0})
    monitor.on_trade({'name': 'ETHUSDT', 'time':  1, 'side': 'SELL', 'quantity': 10, 'price': 25.0})
    monitor.on_trade({'name': 'XRPUSDT', 'time':  1, 'side': 'BUY', 'quantity': 10, 'price': 25.0})
    monitor.on_trade({'name': 'LTCUSDT', 'time':  2, 'side': 'SELL', 'quantity': 10, 'price': 25.0})
    monitor.on_trade({'name': 'EOSUSDT', 'time':  9, 'side': 'BUY', 'quantity': 10, 'price': 25.0})
    monitor.on_trade({'name': 'OKBUSDT', 'time': 10, 'side': 'SELL', 'quantity': 10, 'price': 25.0})
    monitor.on_trade({'name': 'XMRUSDT', 'time': 20, 'side': 'BUY', 'quantity': 10, 'price': 25.0})
    monitor.on_trade({'name': 'BCHUSDT', 'time': 21, 'side': 'SELL', 'quantity': 10, 'price': 25.0})
    # alert XMRUSDT (quantity)
    monitor.on_trade({'name': 'XMRUSDT', 'time': 30, 'side': 'SELL', 'quantity': 10, 'price': 15.0})
    monitor.on_trade({'name': 'XMRUSDT', 'time': 40, 'side': 'BUY', 'quantity': 90, 'price': 15.0})
    monitor.on_trade({'name': 'XMRUSDT', 'time': 41, 'side': 'SELL', 'quantity':  9, 'price': 15.0})
    monitor.on_trade({'name': 'XMRUSDT', 'time': 41, 'side': 'SELL', 'quantity':  2, 'price': 15.0})
    # alert all Bitfinex symbols ( quantity )
    monitor.on_trade({'name': 'BCHUSDT', 'time': 100, 'side': 'BUY', 'quantity': 30, 'price': 25.0})
    monitor.on_trade({'name': 'XMRUSDT', 'time': 102, 'side': 'BUY', 'quantity': 30, 'price': 25.0})
    monitor.on_trade({'name': 'BCHUSDT', 'time': 104, 'side': 'SELL', 'quantity': 30, 'price': 25.0})
    monitor.on_trade({'name': 'BCHUSDT', 'time': 106, 'side': 'SELL', 'quantity': 30, 'price': 25.0})
    monitor.on_trade({'name': 'XMRUSDT', 'time': 108, 'side': 'SELL', 'quantity': 31, 'price': 25.0})
    # alert all Group2 symbols ( quantity )
    monitor.on_trade({'name': 'ETHUSDT', 'time': 200, 'side': 'BUY', 'quantity': 50, 'price': 25.0})
    monitor.on_trade({'name': 'EOSUSDT', 'time': 204, 'side': 'BUY', 'quantity': 50, 'price': 25.0})
    monitor.on_trade({'name': 'BCHUSDT', 'time': 208, 'side': 'SELL', 'quantity': 50, 'price': 25.0})
    monitor.on_trade({'name': 'EOSUSDT', 'time': 216, 'side': 'SELL', 'quantity': 51, 'price': 25.0})
    # alert all Group1 symbols ( positive delta )
    monitor.on_trade({'name': 'BTCUSDT', 'time': 300, 'side': 'BUY', 'quantity': 10, 'price': 75.0})
    monitor.on_trade({'name': 'XMRUSDT', 'time': 304, 'side': 'BUY', 'quantity': 10, 'price': 75.0})
    monitor.on_trade({'name': 'LTCUSDT', 'time': 308, 'side': 'BUY', 'quantity': 10, 'price': 75.0})
    monitor.on_trade({'name': 'BTCUSDT', 'time': 312, 'side': 'BUY', 'quantity': 11, 'price': 75.0})
    # alert all Huobi symbols ( negative delta )
    monitor.on_trade({'name': 'XRPUSDT', 'time': 400, 'side': 'SELL', 'quantity': 10, 'price': 100.0})
    monitor.on_trade({'name': 'LTCUSDT', 'time': 404, 'side': 'SELL', 'quantity': 10, 'price': 100.0})
    monitor.on_trade({'name': 'XRPUSDT', 'time': 408, 'side': 'SELL', 'quantity': 10, 'price': 100.0})


def load_param_data2():
    # moving BTCUSDT from group1 to group2
    Global_Data['symbols'][0].group_name = 'Group2'
    # moving BCHUSDT from group2 to group1
    Global_Data['symbols'][-1].group_name = 'Group1'


def load_trade_data2(monitor: TradeMonitor):
    # alert all Group2 symbols ( quantity )
    monitor.on_trade({'name': 'ETHUSDT', 'time': 500, 'side': 'BUY', 'quantity': 50, 'price': 25.0})
    monitor.on_trade({'name': 'EOSUSDT', 'time': 504, 'side': 'BUY', 'quantity': 50, 'price': 25.0})
    monitor.on_trade({'name': 'BTCUSDT', 'time': 508, 'side': 'SELL', 'quantity': 50, 'price': 25.0})
    monitor.on_trade({'name': 'EOSUSDT', 'time': 516, 'side': 'SELL', 'quantity': 51, 'price': 25.0})
    # alert all Group1 symbols ( positive delta )
    monitor.on_trade({'name': 'BCHUSDT', 'time': 600, 'side': 'BUY', 'quantity': 10, 'price': 75.0})
    monitor.on_trade({'name': 'XMRUSDT', 'time': 604, 'side': 'BUY', 'quantity': 10, 'price': 75.0})
    monitor.on_trade({'name': 'LTCUSDT', 'time': 608, 'side': 'BUY', 'quantity': 10, 'price': 75.0})
    monitor.on_trade({'name': 'BCHUSDT', 'time': 612, 'side': 'BUY', 'quantity': 11, 'price': 75.0})
