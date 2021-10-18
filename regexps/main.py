from math import gcd


class RegExpError(Exception):
    pass


class WrongDivisionNumber(RegExpError):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class WrongSymbolError(RegExpError):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class WrongRegularExpression(RegExpError):
    def __init__(self, message):
        self.message = message


class WrongKleeneStarPositionExpression(RegExpError):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class WrongMainLetterExpression(RegExpError):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


def __letter_list(index, main_letter, division_number) -> list:
    new_letter_list = [0 for i in range(division_number)]
    if index == main_letter:
        new_letter_list[1 % division_number] = 1
    else:
        new_letter_list[0] = 1
    return new_letter_list


def __plus(first_list, second_list, size_of_lists) -> list:
    result_list = list()
    for j in range(size_of_lists):
        result_list.append(max(first_list[j], second_list[j]))
    return result_list


def __multiply(first_list, second_list, size_of_lists) -> list:
    result_list = [0 for i in range(size_of_lists)]
    for j in range(size_of_lists):
        for k in range(size_of_lists):
            if first_list[j] == 1 and second_list[k] == 1:
                result_list[(j + k) % size_of_lists] = 1
    return result_list


def __kleene_star(first_list, division_number) -> list:
    result_list = [0 for j in range(division_number)]
    general_gsd = division_number
    for j in range(division_number):
        if first_list[j] == 1:
            general_gsd = gcd(general_gsd, j)
    for j in range(division_number):
        if j % general_gsd == 0:
            result_list[j] = 1
    return result_list


def solver(regular_expression: str, main_letter: str, division_number: int) -> bool:

    letters_number = 0
    operations_number = 0

    if main_letter != "a" and main_letter != "b" and main_letter != "c":
        raise WrongMainLetterExpression(main_letter, "Main letter for function must be a, b or c")

    if division_number <= 0:
        raise WrongDivisionNumber(division_number, "Division number must be positive")

    for i in regular_expression:
        if (operations_number == 1 and letters_number < 2) \
                or (operations_number > 1 and letters_number <= operations_number):
            raise WrongRegularExpression("Wrong regular expression")
        if i == "a" or i == "b" or i == "c":
            letters_number += 1
        elif i == "+" or i == ".":
            operations_number += 1
        elif i == "*" and letters_number == 0:
            raise WrongKleeneStarPositionExpression(i, "Wrong position for Kleene star")
        elif i == " " or i == "*":
            continue
        else:
            raise WrongSymbolError(i, "Wrong symbol")

    if letters_number != operations_number + 1:
        raise WrongRegularExpression("Wrong regular expression")

    main_stack = list()

    for i in regular_expression:
        if i == "a" or i == "b" or i == "c" or i == "1":
            main_stack.append(__letter_list(i, main_letter, division_number))
            continue
        elif i == "+":
            first_list = main_stack.pop()
            second_list = main_stack.pop()
            main_stack.append(__plus(first_list, second_list, division_number))
            continue
        elif i == ".":
            first_list = main_stack.pop()
            second_list = main_stack.pop()
            main_stack.append(__multiply(first_list, second_list, division_number))
            continue
        elif i == "*":
            first_list = main_stack.pop()
            main_stack.append(__kleene_star(first_list, division_number))

    if main_stack[0][0] == 1:
        return True
    else:
        return False
