inputs = [[5, 7, 1, 1, 2, 3, 22],
          [1, 1, 1, 1, 1],
          [1, 5, 1, 1, 1, 10, 15, 20, 100],
          ]

def exercise3(array):
    array.sort()
    accumulated = 0
    for index in range(len(array)):
        if array[index] > accumulated + 1:
            return accumulated + 1
        accumulated += array[index]
    return accumulated + 1
        
if __name__ == "__main__":
    for input in inputs:
        result = exercise3(input)
        print(result)