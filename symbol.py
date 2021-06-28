# 可以在此基础上进行任意的设计和修改


class Symbol:
    def __init__(self, name, exchange_name, group_name, quantity_limit, quantity_interval, delta_limit, delta_interval):
        self.name = name
        self.exchange_name = exchange_name
        self.group_name = group_name
        self.quantity_limit = quantity_limit
        self.quantity_interval = quantity_interval
        self.delta_limit = delta_limit
        self.delta_interval = delta_interval
