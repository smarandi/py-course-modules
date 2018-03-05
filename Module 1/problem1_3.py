def problem1_3(n):
    my_sum = 0
    if isinstance(n, int):
        ct = 1
        while ct <= n:
            my_sum = my_sum + ct
            ct =  ct + 1
        print(my_sum)
    else:
        print("Enter a valid number")
