class Solution:
    def kClosest(self, points, K):

        def quickselect(arr, low, high):
            if low < high:
                p = partition(arr, low, high)
                if p > K:
                    return quickselect(arr, low, p - 1)
                elif p < K:
                    return quickselect(arr, p + 1, high)
                else:
                    return arr[:K]

        def partition(arr, low, high):
            pivotdistance = calculatedistance(arr[high][0], arr[high][1])
            arr[low], arr[high] = arr[high], arr[low]
            i = low
            for j in range(low + 1, high + 1):
                if calculatedistance(arr[j][0], arr[j][1]) <= pivotdistance:
                    i += 1
                    (arr[j], arr[i]) = (arr[i], arr[j])
            (arr[i], arr[low]) = (arr[low], arr[i])
            return i

        def calculatedistance(x, y):
            return (x ** 2 + y ** 2) ** (1 / 2)

        quickselect(points, 0, len(points) - 1)
        return points[:K]