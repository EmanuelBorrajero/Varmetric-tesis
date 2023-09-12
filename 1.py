
suma = [1,201,3,400,12]

result = sum(suma)

a = 3
b = 10

print(b/a)




def calculate_very_small_value(max_value, cant_intervals):
    very_small_value = float(0.0)
    if cant_intervals != float(0.0):
        resoult_div = str((max_value / cant_intervals))
        integer_values = resoult_div.find('.')
        if integer_values > -1:
            float_values = (len(resoult_div) - (integer_values))
        else:
            float_values = 2
        very_small_value = float(1 / (10 ** float_values))
    return very_small_value, 99
    



def calculate_intervals(min_value, max_value, cant_intervals):
    very_small_value = calculate_very_small_value(max_value, cant_intervals)
    iterator = 0
    intervals_list = []
    if min_value < max_value and cant_intervals > 2:
        initial_interval_value = float(min_value)
        terminal_interval_value = initial_interval_value + \
            float((max_value / cant_intervals))
        interval = [initial_interval_value, terminal_interval_value]
        intervals_list.append(interval)
        while(iterator != cant_intervals - 2):
            initial_interval_value = terminal_interval_value + very_small_value
            terminal_interval_value = float(initial_interval_value) + \
                float((max_value / cant_intervals))
            interval = [initial_interval_value, terminal_interval_value]
            intervals_list.append(interval)
            iterator += 1
        intervals_list.append([(terminal_interval_value + very_small_value), max_value])
        return intervals_list
    else:
        intervals_list.append("Valores Errónios")
    return [round(i,2) for i in intervals_list]



print(calculate_intervals(3,16,3))

print("El mayor resultado posible es: "+str(result))