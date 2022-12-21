def arithmetic_arranger(problems, answer=False):
    operators = list()
    operands1 = list()
    operands2 = list()
    dash_line = list()

    # Checking amount of problems
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems

    # Checking operators
    for arrange in problems:
        operator = arrange.split(" ")[1]
        operators.append(operator)
        if operator != "+" and operator != "-":
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems

    # Check digits and length
    for arrange in problems:
        operand1 = arrange.split(" ")[0]
        operand2 = arrange.split(" ")[2]
        operands1.append(operand1)
        operands2.append(operand2)
        if operand1.isdigit() is False or operand2.isdigit() is False:
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems
        if len(operand1) > 4 or len(operand2) > 4:
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems

    # Formatting results
    operands1_line = list()
    for i in range(len(problems)):
        if len(operands1[i]) >= len(operands2[i]):
            operands1_line.append("  " + operands1[i])
        else:
            operands1_line.append(" "*(len(operands2[i]) - len(operands1[i]) + 2) + operands1[i])
    operands2_line = list()
    for i in range(len(problems)):
        if len(operands1[i]) < len(operands2[i]):
            operands2_line.append(operators[i] + " " + operands2[i])
        else:
            operands2_line.append(operators[i] + " "*(len(operands1[i]) - len(operands2[i]) + 1) + operands2[i])

    for i in range(len(problems)):
        dash_line.append("-" * (max(len(operands1[i]), len(operands2[i]))+2))

    # Answer
    answers_line = list()
    if answer:
        for i in range(len(problems)):
            if operators[i] == "+":
                solution = str(int(operands1[i]) + int(operands2[i]))
            else:
                solution = str(int(operands1[i]) - int(operands2[i]))

            if len(solution) > max(len(operands1[i]), len(operands2[i])):
                answers_line.append(" " + solution)
            else:
                answers_line.append(" " * (max(len(operands1[i]), len(operands2[i])) - len(solution) + 2) + solution)
        arranged_problems = "    ".join(operands1_line) + "\n" + "    ".join(operands2_line) + "\n" + "    ".join(
            dash_line) + "\n" + "    ".join(answers_line)
    else:
        arranged_problems = "    ".join(operands1_line) + "\n" + "    ".join(operands2_line) + "\n" + "    ".join(
            dash_line)
    return arranged_problems


arithmetic_arranger(['3801 - 2', '123 + 49'])
