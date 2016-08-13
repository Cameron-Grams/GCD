def factors(number, denominator):
    return number//denominator

def just_facts(number):
    pfact_list = [1]
    test_num = number
    i = 2

    while test_num > 1:
        while (test_num % i == 0):
            test_num = factors(test_num, i)   
            pfact_list.append(i)          
        i += 1

    return pfact_list


def gcd(first_num, second_num):
    factor_list = []

    first_facts = just_facts(first_num)
    second_facts = just_facts(second_num)

    print(first_facts)
    print(second_facts)


    test_index = min(len(first_facts), len(second_facts))
    print(test_index)




gcd(8, 25)
