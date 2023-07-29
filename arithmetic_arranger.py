import operator
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}

def arithmetic_arranger(problems, show_result=False):
    # Check if the number of problems exceeds the limit (5)
    if len(problems) > 5:
        return "Error: Too many problems."
    
    top_line = ""
    bottom_line = ""
    separator_line = ""
    result_line = ""

    for problem in problems:
        first_number, operator, second_number = problem.split()

        # Handle errors for input:
        if operator not in ops:
            return "Error: Operator must be '+' or '-'."
        if not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits"

        # Calculate the result for the current problem
        result = ops[operator](int(first_number), int(second_number))

        # Determine the width for the current problem
        line_width = max(len(first_number), len(second_number)) + 2

        # Build the lines
        top_line += f"{first_number.rjust(line_width)}    "
        bottom_line += f"{operator}{second_number.rjust(line_width - 1)}    "
        separator_line += "-" * line_width + "    "
        result_line += f"{result}".rjust(line_width) + "    "

    if show_result:
        print(top_line)
        print(bottom_line)
        print(separator_line)
        print(result_line)

# Example usage:
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_result=True)

