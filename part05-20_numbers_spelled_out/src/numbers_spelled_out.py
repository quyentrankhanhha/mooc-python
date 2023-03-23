# Write your solution here
def dict_of_numbers():
    numbers={}
    ones_dict={
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }
    tens_dict = {
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
        14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
        18: 'eighteen', 19: 'nineteen'
    }
    tens_multiple_dict = {
        20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
        60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
    }

    for i in range(100):
        if i in ones_dict:
            numbers[i] = ones_dict[i]
        elif i in tens_dict:
            numbers[i] = tens_dict[i]
        elif i in tens_multiple_dict:
            numbers[i] = tens_multiple_dict[i]
        else:
            tens = i // 10
            ones = i % 10
            if ones == 0:
                numbers[i] = tens_multiple_dict[tens * 10]
            else:
                numbers[i] = tens_multiple_dict[tens * 10] + '-' + ones_dict[ones]
    return numbers
if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])