import sys

def find_day_stats(input_file, output_file):
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    result = {}

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            base, date, active_vehicles, trips = line.strip().split(',')
            day = date.split('/')[1]
            day_code = days[int(day) % 7]
            if base not in result:
                result[base] = []
            result[base].append((day_code, active_vehicles, trips))

    with open(output_file, 'w', encoding='utf-8') as output:
        for base, data in result.items():
            for entry in data:
                output.write(f"{base},{entry[0]} {entry[1]},{entry[2]}\n")

if __name__ == '__main__':
    input_file = "uber_exp.txt"
    output_file = "uberoutput.txt"
    find_day_stats(input_file, output_file)
