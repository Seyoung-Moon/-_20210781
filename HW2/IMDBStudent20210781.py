import sys

def count_movies_by_genre(input_file, output_file):
    genre_count = {}

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            _, _, genres = line.strip().split('::')
            genres = genres.split('|')
            for genre in genres:
                genre_count[genre] = genre_count.get(genre, 0) + 1

    with open(output_file, 'w', encoding='utf-8') as output:
        for genre, count in genre_count.items():
            output.write(f"{genre} {count}\n")

if __name__ == '__main__':
    if len(sys.argv) != 1:
        input_file = input("Enter the input file name: ")
        output_file = input("Enter the output file name: ")
        count_movies_by_genre(input_file, output_file)
    else:
        print("Usage: python3 IMDBStudent20210781.py")
