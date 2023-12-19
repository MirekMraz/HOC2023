def calculate_calibration_value(text):
    """
    This function calculates the calibration value from the given text.
    It assumes that each line in the text represents a separate calibration,
    with the first and last digits on each line forming a two-digit number.
    The function then sums these values.
    """
    # Splitting the text into lines
    lines = text.split("\n")
    
    # Initializing the total sum
    total_sum = 0

    # Iterating over each line
    for line in lines:
        # Finding the first digit
        first_digit = None
        for char in line:
            if char.isdigit():
                first_digit = char
                break

        # Finding the last digit
        last_digit = None
        for char in reversed(line):
            if char.isdigit():
                last_digit = char
                break

        # If both digits are found, add to the total sum
        if first_digit is not None and last_digit is not None:
            total_sum += int(first_digit + last_digit)

    return total_sum

# Reading the file and calculating the calibration value
with open('/Users/mirekmraz/Documents/HOC/2023/day1/input.txt', 'r') as file:
    text = file.read()
    calibration_value = calculate_calibration_value(text)

print(calibration_value)
