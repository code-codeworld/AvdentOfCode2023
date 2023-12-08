def identify_snow_terms(line):
    snow_terms = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    identified_terms = []

    for term in snow_terms:
        # Find all occurrences of the term in the line
        start_index = 0
        while start_index < len(line):
            if line.startswith(term, start_index):
                identified_terms.append((term, start_index))
                start_index += len(term)
            else:
                start_index += 1

    # Sort the identified terms based on the start index
    identified_terms.sort(key=lambda x: x[1])

    # Extract the sorted terms from the tuples
    sorted_terms = [term for term, _ in identified_terms]

    return sorted_terms

def process_file():
    input_file = 'input.txt'
    output_file = 'output2.txt'

    # Create the snow dictionary
    snow = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

    # Process the input file and create the output file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as out_file:
        for line in lines:
            # Identify snow terms in the line
            identified_terms = identify_snow_terms(line)

            # Output the identified terms to the output file
            out_file.write(', '.join(identified_terms) + '\n')

# Use the function to process the files
process_file()
