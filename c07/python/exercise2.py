
def in_range(num, lower, upper):
    if (num >= lower) and (num <= upper):
        return True
    else:
        return False


def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif (rating > 5) or (rating < 9):
        return "This one was fun."
    elif rating > 9:
        return "Outstanding!"


def twice_as_large(num1, num2):
    twice_as_large = num2*2
    if num1 > twice_as_large:
        return True
    else:
        return False


def large_power(base, exponent):
    if base**exponent > 5000:
        return True
    else:
        False


def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False


def max_num(num1, num2, num3):
    my_arr = [num1, num2, num3]
    return max(my_arr)


def max_num2(num1, num2, num3):
    if ((num1 == num2) and (num3 < num1)) or ((num1 == num3) and (num2 < num1)) or ((num2 == num3) and (num1 < num2)):
        print("Es un empate")
    elif (num1 > num2) and (num1 > num3):
        print(num1)
    elif (num2 > num1) and (num2 > num3):
        print(num2)
    else:
        print(num3)


def max_num3(num1, num2, num3):
    my_arr = [num1, num2, num3]
    if ((num1 == num2) and (num3 < num1)) or ((num1 == num3) and (num2 < num1)) or ((num2 == num3) and (num1 < num2)):
        print("Es un empate")
    else:
        return max(my_arr)


def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    if budget > (food_bill+electricity_bill+internet_bill+rent):
        return True
    else:
        return False
