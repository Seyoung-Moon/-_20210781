import sys

def count_movies_by_genre(input_file, output_file):
    genre_count = {}

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip().split('::')
            if len(data) >= 3:
                _, _, genres = data
                genres = genres.split('|')
                for genre in genres:
                    genre_count[genre] = genre_count.get(genre, 0) + 1
            else:
                print(f"Issue with line: {line}")

    with open(output_file, 'w', encoding='utf-8') as output:
        for genre, count in genre_count.items():
            output.write(f"{genre} {count}\n")

if __name__ == '__main__':
    input_file = "movies_exp.txt"
    output_file = "movieoutput.txt"
    count_movies_by_genre(input_file, output_file)
