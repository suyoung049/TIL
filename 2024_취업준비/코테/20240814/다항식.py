polynomial = "3x + 7 + x"
def solution(polynomial):
    pol_list = [0, 0]
    split_list = polynomial.split(" ")
    for str in split_list:
        if "x" in str:
            if str == "x":
                pol_list[0] += 1
            else:
                if (len(str) == 2):
                  pol_list[0] += int(str[0])
                else:
                    pol_list[0] += int(str[0] + str[1])
        else:
            if str == "+":
                continue
            else:
                pol_list[1] += int(str)
    
    if pol_list[0] != 0 and pol_list[1] != 0:
        if pol_list[0] == 1:
            return f"x + {pol_list[1]}"
        else:
          return f"{pol_list[0]}x + {pol_list[1]}"
    elif pol_list[0] == 0:
        return f"{pol_list[1]}"
    elif pol_list[1] == 0:
        if pol_list[0] == 1:
            return "x"
        else:
            return f"{pol_list[0]}x"
        

solution(polynomial)