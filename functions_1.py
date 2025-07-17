def find_total(expenses):
    """

    :param expenses: input list expense
    :return: total number of the expenses
    """
    total = 0
    for expense in expenses:
        total += expense
    return total
expenses_surgey = [30,45,54,67,89,90]
expenses_sundar = [23,43,46,67,76,99]
total_expenses_surgey = find_total(expenses_surgey)
print("total_expenses_surgey's:",total_expenses_surgey)
total_expenses_sundar = find_total(expenses_sundar)
print("total_expenses_sundar's:",total_expenses_sundar)
print(help(find_total))