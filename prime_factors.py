def factors(number, denomenator):
    return number//denomenator

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




print(just_facts(8))
print(just_facts(24))
print(just_facts(78))
