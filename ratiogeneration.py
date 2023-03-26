import random

def generate_4_speed_ratios():
    ratios = {}
    ratios['R'] = round(random.uniform(3.5, 4.5), 2)
    ratios['N'] = 0
    ratios['1'] = round(random.uniform(3.0, 3.5), 2)
    ratios['2'] = round(random.uniform(1.8, 2.3), 2)
    ratios['3'] = round(random.uniform(1.3, 1.6), 2)
    ratios['4'] = round(random.uniform(1.0, 1.2), 2)
    return ratios

def generate_5_speed_ratios():
    ratios = {}
    ratios['R'] = round(random.uniform(3.5, 4.5), 2)
    ratios['N'] = 0
    ratios['1'] = round(random.uniform(3.0, 3.5), 2)
    ratios['2'] = round(random.uniform(1.8, 2.3), 2)
    ratios['3'] = round(random.uniform(1.3, 1.6), 2)
    ratios['4'] = round(random.uniform(1.0, 1.2), 2)
    ratios['5'] = round(random.uniform(0.8, 1.0), 2)
    return ratios

def generate_6_speed_ratios():
    ratios = {}
    ratios['R'] = round(random.uniform(3.5, 4.5), 2)
    ratios['N'] = 0
    ratios['1'] = round(random.uniform(3.0, 3.5), 2)
    ratios['2'] = round(random.uniform(1.8, 2.3), 2)
    ratios['3'] = round(random.uniform(1.3, 1.6), 2)
    ratios['4'] = round(random.uniform(1.0, 1.2), 2)
    ratios['5'] = round(random.uniform(0.8, 1.0), 2)
    ratios['6'] = round(random.uniform(0.6, 0.8), 2)
    return ratios

def print_ratios(ratios):
    ratio_values = list(ratios.values())
    ratio_values[0] *= -1
    ratios_str = [str(ratio) for ratio in ratio_values]
    print(', '.join(ratios_str))

def main():
    while True:
        num_gears = int(input("Enter the number of gears (4, 5, or 6): "))
        if num_gears == 4:
            ratios = generate_4_speed_ratios()
        elif num_gears == 5:
            ratios = generate_5_speed_ratios()
        elif num_gears == 6:
            ratios = generate_6_speed_ratios()
        else:
            print("Invalid number of gears")
            continue
        
        print_ratios(ratios)
        
        choice = input("Do you want to regenerate the ratios (Y/N) or select another number of gears (G)? ")
        if choice.lower() == 'y':
            continue
        elif choice.lower() == 'g':
            continue
        else:
            print("Invalid choice, exiting")
            break

if __name__ == '__main__':
    main()
