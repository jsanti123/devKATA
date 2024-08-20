def select_numbers(hash):
    for char in hash:
        if char.isdigit():
            return int(char)

def validate_inputs(array, s):
    return 0 <= s <= 9 and len(array) > 0

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]
    sorted_arr = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        sorted_arr[count[num] - 1] = num
        count[num] -= 1
    return sorted_arr

def exercise2(array, s):
    if not validate_inputs(array, s):
        return "Invalid input"
    limit = (s * 10) + s
    result = []
    for number in array:
        pow_number = number**2
        if pow_number < limit:
            result.append(pow_number)
    return counting_sort(result) if result else []

inputs = [[1, 2, 3, 5, 6, 8, 9],
          [-2, -1],
          [-6, -5, 0, 5, 6],
          [-10, 10]
        ]

if __name__ == "__main__":
    hash = "d4621655bd94041050b1c81a9f9c7b3b"
    S = select_numbers(hash)
    for input in inputs:
        result = exercise2(input, 6)
        print(result)