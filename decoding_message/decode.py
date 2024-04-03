# This function builds a number pyramid up to a certain maximum number and returns the last number on each row.
def build_number_pyramid(max_number):
    counter = 1
    row = 1
    last_numbers = []
    while counter <= max_number:
        for _ in range(row):
            if counter > max_number:
                break
            counter += 1
        last_numbers.append(counter - 1)
        row += 1
    return last_numbers

# This function finds the maximum number in a file.
def find_max_number(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.split()[0]) for line in file]
    return max(numbers)
print(find_max_number('coding_qual_input.txt'))

max_number = find_max_number('coding_qual_input.txt')
last_numbers = build_number_pyramid(max_number)
print("Last numbers on each row of number pyramid:", last_numbers)

# This function finds the words that correspond to a given list of numbers in a file.
def find_corresponding_words(filename, numbers):
    with open(filename, 'r') as file:
        number_word_dict = {}
        for line in file:
            number, word = line.split()
            number = int(number)
            if number in numbers:
                number_word_dict[number] = word
    sorted_dict = dict(sorted(number_word_dict.items()))
    return sorted_dict

number_word_dict = find_corresponding_words('coding_qual_input.txt', last_numbers)
print("Corresponding words for each number:", ' '.join(number_word_dict.values()))