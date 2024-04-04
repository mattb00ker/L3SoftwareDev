def generate_target_numbers(max_number):
    """
    Generates target triangular numbers up to a specified max number.
    """
    targets = []
    n = 1
    while True:
        triangular_number = n * (n + 1) // 2
        if triangular_number > max_number:
            break
        targets.append(triangular_number)
        n += 1
    return targets

def decode_message_from_file(file_path):

    # Read the file and extract each line's number and word, converting the number to an integer
    with open(file_path, 'r') as file:
        lines = file.readlines()
    entries = [(int(line.split()[0]), line.split()[1]) for line in lines]

    # Sort the entries based on the number
    sorted_entries = sorted(entries, key=lambda x: x[0])

    # Find the maximum number to know until which triangular number to generate
    max_number = max(sorted_entries, key=lambda x: x[0])[0]

    # Generate target triangular numbers up to the maximum number found
    target_numbers = generate_target_numbers(max_number)

    # Filter the entries to only include those with numbers that are in our list of target numbers
    target_entries = [word for number, word in sorted_entries if number in target_numbers]

    # Print the decoded message
    for word in target_entries:
        print(word)

decode_message_from_file('code.txt')
