
def factorial(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


def combination(n,r):
    combination = factorial(n) / (factorial(r)*factorial((n-r)))
    return combination

def permutations(n,r):
    premutation = factorial(n) / factorial((n-r))
    return premutation

num = int(input('How many times do you want to run this test? : '))
if num > 10:
    sure = input('Are you sure?[y/n] : ')
    if sure.lower() == 'yes' or sure.lower() == 'y':
        permutOrComb = input('What do you want to perform?(permutation[p]/combination[c]/factorial[f] : ')
        for number in range(num):

            if permutOrComb.lower() == 'p' or permutOrComb.lower() == 'permutation':
                n = int(input('Please provider the upper index: '))
                r = int(input('Please provide the lower index: '))
                print(permutations(n, r))
            elif permutOrComb.lower() == 'c' or permutOrComb.lower() == 'combination' :
                n = int(input('Please provider the upper index: '))
                r = int(input('Please provide the lower index: '))
                print(combination(n, r))
            elif permutOrComb.lower() == 'f' or permutOrComb.lower() == 'factorial':
                n = int(input('Please provide the number for which you desire to find the factorial: '))
                print(factorial(n))
            else:
                print('Invalid Format!')

    else:
        num = int(input('How many times do you want to run this test? : '))
        if num > 10:
            sure = input('Are you sure?[y/n] : ')
            if sure.lower() == 'yes' or sure.lower() == 'y':
                permutOrComb = input('What do you want to perform?(permutation[p]/combination[c]/factorial[f) : ')
                for number in range(num):

                    if permutOrComb.lower() == 'p' or permutOrComb.lower() == 'permutation':
                        n = int(input('Please provider the upper index: '))
                        r = int(input('Please provide the lower index: '))
                        print(permutations(n, r))
                    elif permutOrComb.lower() == 'c' or permutOrComb.lower() == 'combination':
                        n = int(input('Please provider the upper index: '))
                        r = int(input('Please provide the lower index: '))
                        print(combination(n, r))
                    elif permutOrComb.lower() == 'f' or permutOrComb.lower() == 'factorial':
                        n = int(input('Please provide the number for which you desire to find the factorial: '))
                        print(factorial(n))
                    else:
                        print('Invalid Format!')


else:

    permutOrComb = input('What do you want to perform?(permutation[p]/combination[c]/factorial[f) : ')
    for number in range(num):

        if permutOrComb.lower() == 'p' or permutOrComb.lower() == 'permutation':
            n = int(input('Please provider the upper index: '))
            r = int(input('Please provide the lower index: '))
            print(permutations(n, r))
        elif permutOrComb.lower() == 'c' or permutOrComb.lower() == 'combination':
            n = int(input('Please provider the upper index: '))
            r = int(input('Please provide the lower index: '))
            print(combination(n, r))
        elif permutOrComb.lower() == 'f' or permutOrComb.lower() == 'factorial':
            n = int(input('Please provide the number for which you desire to find the factorial: '))
            print(factorial(n))
        else:
            print('Invalid Format!')
