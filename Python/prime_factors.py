def factors(number, denominator):
    return number//denominator

def just_facts(number):
    pfact_list = [1]
    test_num = number
    i = 2

    while test_num > 1:
        while (test_num % i == 0):
            test_num = factors(test_num, i)   
            print(test_num)
            pfact_list.append(i)          
        i += 1

    return pfact_list



