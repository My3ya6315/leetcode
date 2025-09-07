def add_digits(num):
    if num < 10:
        return num

    while num > 10:
        summ = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            summ += digit
            temp = temp // 10
            # print(summ, temp)
        num = summ
    return num

def add_digits2(num):
    if num < 10:
        return num
    summ = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        summ += digit
        temp = temp // 10

    return add_digits2(summ) if summ > 10 else summ

def main():
    print(add_digits(78))
    print(add_digits2(78))

if __name__ == '__main__':
    main()

