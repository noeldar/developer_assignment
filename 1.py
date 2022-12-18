def answer_one():
    # iterate for 100 steps save numbers that can be divide by 3 or 5 to a list
    selected_numbers = [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]

    # sum resulted list and return
    list_sum = sum(selected_numbers)
    return list_sum


print(answer_one())
