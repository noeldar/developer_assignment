def answer_two():
    # initialized first two fibonacci numbers and answer
    a, b = 0, 1
    answer = 0

    # iterate until one of the fibonacci number hits 4 000 000
    while a + b < 4000000:

        # update answer if it is even
        if (a + b) % 2 == 0:
            answer += a + b

        # update two fibonacci numbers
        a, b = b, a + b

    return answer


print(answer_two())
