import sys

def find_day_stats(input_file, output_file):
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    result = {}

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            base, date, active_vehicles, trips = line.strip().split(',')
            day = date.split('/')[1]
            day_code = days[int(day) % 7]
            key = (base, day_code)

            if key not in result:
                result[key] = {'active_vehicles': 0, 'trips': 0}

            result[key]['active_vehicles'] += int(active_vehicles)
            result[key]['trips'] += int(trips)

    with open(output_file, 'w', encoding='utf-8') as output:
        for (base, day_code), data in result.items():
            output.write(f"{base},{day_code} {data['active_vehicles']},{data['trips']}\n")

if __name__ == '__main__':
    input_file = "uber_exp.txt"
    output_file = "uberoutput.txt"
    find_day_stats(input_file, output_file)
