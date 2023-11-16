def calculate_intervals(min_value, max_value, cant_intervals):
    iterator = 0
    intervals_list = []
    if min_value < max_value and cant_intervals > 2:
        initial_interval_value = float(min_value)
        terminal_interval_value = initial_interval_value + \
            float((max_value / cant_intervals))
        interval = [initial_interval_value, terminal_interval_value]
        intervals_list.append(interval)
        while(iterator != cant_intervals - 2):
            initial_interval_value = terminal_interval_value + 0.0001
            terminal_interval_value = float(initial_interval_value) + \
                float((max_value / cant_intervals))
            interval = [initial_interval_value, terminal_interval_value]
            intervals_list.append(interval)
            iterator += 1
        intervals_list.append([(terminal_interval_value + 0.0001), max_value])
        return intervals_list
    else:
        intervals_list.append("Valores Errónios")
    return intervals_list

