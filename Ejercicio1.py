def select_numbers(hash):
    for char in hash:
        if char.isdigit():
            return int(char)

def validate_inputs(n, s):
    return 0 <= s <= 9 and n <= 100

def exercise1(array, s):
    result = []
    if validate_inputs(len(array), s):
        for index in range(len(array)-1, -1, -1):
            numberResult = ''.join([digit for digit in str(array[index]) if int(digit) < s])
            if numberResult:
                result.append(int(numberResult))
        return result
    else:
        return "Invalid input"
    
inputs = [[1, 2, 3, 4, 5, 6],
          [10, 20, 30, 40],
          [6],
          [66],
          [6, 2, 1],
          [60, 6, 5, 4, 3, 2, 7, 7, 29, 1],
          [1, 2, 3, 4, 562]
          ]
    
if __name__ == "__main__":
    hash = "d4621655bd94041050b1c81a9f9c7b3b"
    S = select_numbers(hash)
    print("S: ", S)
    for input in inputs:
        result = exercise1(input, S)
        print(result)
