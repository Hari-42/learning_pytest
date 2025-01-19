def positive_or_negative(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def simple_counter():
    count = []
    i = 1
    while i <= 5:
        count.append(i)
        i += 1
    return count

def number_comparison(a, b):
    if a > b:
        return "a is greater than b"
    elif a < b:
        return "a is less than b"
    else:
        return "a and b are equal"

def countdown():
    count = []
    i = 5
    while i > 0:
        count.append(i)
        i -= 1
    count.append("Done!")
    return count

if __name__ == '__main__':
    positive_or_negative()
    simple_counter()
    number_comparison()
    countdown()
