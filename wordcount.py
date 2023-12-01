import sys

# read file data if the file exists.
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File {filename} was not found.")
        sys.exit(2)
    except IOError:
        print(f"Error: An IO error occurred while reading the {filename} file.")
        sys.exit(3)

# count the words in the file and store them in a dictionary.
def count_words(text):
    text_as_list = text.split()
    count_dict = {}
    for word in text_as_list:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return count_dict
# sort the dictionary values using lambda.
def sort_dict_by_value(count_dict, N):
    sorted_keys = sorted(count_dict, key=lambda k: count_dict[k], reverse=True)
    return sorted_keys[:N]

def main():
    if len(sys.argv) != 3:
        print("Usage: python wordcount.py <N> <filename>")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("Error: N must be an integer.")
        sys.exit(4)

    filename = sys.argv[2]

    file_data = read_file(filename)
    count_dict = count_words(file_data)
    sorted_array = sort_dict_by_value(count_dict , N)

# print elements in sorted array
    for element in sorted_array:
        print(element)

if __name__ == '__main__':
    main()