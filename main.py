class Array:
    def __init__(self, array = []):
        self.array = array
        self.len = len(array)

    def bubbleSort(self):
        for i in range(self.len):
            for j in range(0, self.len - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
        return self.array

    def pivot(numbers, low, high):
        pivot = numbers[high]
        item = low - 1

        for i in range(low, high):
            if numbers[i] <= pivot:
                item = item + 1
                numbers[item], numbers[i] = numbers[i], numbers[item]
        numbers[item + 1], numbers[high] = numbers[high], numbers[item + 1]

        return item + 1

    def quickSortAlg(array, low, high):
        if low < high:
            pivot = Array.pivot(array, low, high)
            Array.quickSortAlg(array, low, pivot - 1)
            Array.quickSortAlg(array, pivot + 1, high)

    def quickSort(self):
        Array.quickSortAlg(self.array, 0, self.len-1)
        return self.array
