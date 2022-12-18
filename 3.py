def answer_three():
    max_num = -1
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):

            # multiply each i and j pairs
            result = i * j

            # cast result to string for polindrome control
            str_nmbr = str(result)

            """
            make a polindrome control and if result is greater than current max polindrome multiplication result, 
            make an update 
            """
            if str_nmbr == str_nmbr[::-1] and max_num < result:
                max_num = result
                break

    return max_num


print(answer_three())
