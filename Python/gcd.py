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
    gcd = 1
    factor_list = []

    first_facts = just_facts(first_num)
    second_facts = just_facts(second_num)

    print(first_facts)
    print(second_facts)


    test_index = min(len(first_facts), len(second_facts))
#    print(test_index)

    if (len(first_facts) < len(second_facts)):
        test_list = first_facts
        other_list = second_facts
    else:
        test_list = second_facts
        other_list = first_facts

    for i in range(test_index):
        if test_list[i] in other_list:
            factor_list.append(test_list[i])

#    print(factor_list)

    for j in factor_list:
        gcd = gcd * j

    print(gcd)

