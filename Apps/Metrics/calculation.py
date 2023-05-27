from decimal import Decimal

def calculate_very_small_value(max_value, cant_intervals):
    very_small_value = 0
    if cant_intervals != 0:
        resoult_div = str((max_value / cant_intervals))
        integer_values = resoult_div.find('.')
        if integer_values > -1:
            decimal_values = (len(resoult_div) - (integer_values))
        else:
            decimal_values = 2
        very_small_value = Decimal(1 / (10 ** decimal_values))
    return very_small_value


def calculate_intervals(min_value, max_value, cant_intervals):
    very_small_value = calculate_very_small_value(max_value, cant_intervals)
    iterator = 0
    intervals_list = []
    if min_value < max_value and cant_intervals > 2:
        initial_interval_value = Decimal(min_value)
        terminal_interval_value = initial_interval_value + \
            Decimal((max_value / cant_intervals))
        interval = [initial_interval_value, terminal_interval_value]
        intervals_list.append(interval)
        while(iterator != cant_intervals - 2):
            initial_interval_value = terminal_interval_value + very_small_value
            terminal_interval_value = Decimal(initial_interval_value) + \
                Decimal((max_value / cant_intervals))
            interval = [initial_interval_value, terminal_interval_value]
            intervals_list.append(interval)
            iterator += 1
        intervals_list.append([(terminal_interval_value + very_small_value), max_value])
        return intervals_list
    else:
        intervals_list.append("Valores Errónios")
    return intervals_list
