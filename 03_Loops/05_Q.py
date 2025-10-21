input_str = "turrrrrrrt"

for char in input_str:
    if input_str.count(char)==1:
        print(f"The char which is not repeated is :- {char}")
        break
