numbers = "onetwothreefourfivesixseveneightnine"

def solution(numbers):
    numbers.append("a")
    num_dict ={
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    result = ""
    number = ""
    for str in numbers:
        if num_dict.__contains__(number):
            result += num_dict[number]
            number = str
        else:
            number += str
    
    return int(result)

solution(numbers)


