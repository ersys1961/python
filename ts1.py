from sys import argv


def conv_to_float(s):
    try:
        return float(s)
    except ValueError:
        return -1


if len(argv) != 4:
    print('Parameters: Hours Tariff Bonus !')
    exit()
hours, tariff, bonus = conv_to_float(argv[1]), conv_to_float(argv[2]), conv_to_float(argv[3])
if (hours < 0) or (tariff < 0) or (bonus < 0):
    print('Parameters: input errors !')
    exit()
else:
    print('Staff=', round(hours*tariff, 2) + bonus)
