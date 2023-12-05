def process_file():
    input_file = 'input.txt'
    output_file = 'output.txt'
    sum_file = 'sum.txt'

    # Process the input file and create output file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as out_file:
        for line in lines:
            # Extract the first and last digits
            first_digit = next(char for char in line if char.isdigit())
            last_digit = next(char for char in line[::-1] if char.isdigit())

            # Combine to form a two-digit number
            value = int(first_digit + last_digit)

            # Write the result to the output file
            out_file.write(str(value) + '\n')

    # Calculate and write the sum to a separate file
    with open(output_file, 'r') as file:
        values = [int(line.strip()) for line in file]

    with open(sum_file, 'w') as file:
        file.write(str(sum(values)))


# Use the function to process the files
process_file()
