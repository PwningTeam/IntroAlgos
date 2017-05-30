"""

- INFO: 
    + Insertion sort implement based on Introduction to Algorithms Book
        https://en.wikipedia.org/wiki/Introduction_to_Algorithms
    + Author: Anh Quan
    + Contacts: anhquan.itc500@gmail.com

- INSERTION SORT:
    + Input: A[1..n]
    + Output: A[1..n] (a[1] <= a[2] <= ... <= a[n-1] <= a[n])
    + Complexity: O(n^2)

- PSEUDO CODE:
    INSERTION-SORT(A)
        for j = 2 to A.length
            key = A[j]
            // Insert A[j] into the sorted sequence A[1..j-1]
            i = j - 1
            while i > 0 and A[i] > key
                A[i + 1] = A[i]
                i = i - 1
            A[i + 1] = key

"""

import time


class Sort:
    def __init__(self, a):
        self.a = a

    @staticmethod
    def insertion_sort(a):
        for j in range(1, len(a)):
            key = a[j]
            i = j - 1
            while i >= 0 and a[i] > key:
                a[i + 1] = a[i]
                i = i - 1
            a[i + 1] = key


def main():
    start_time = time.time()

    # Mock array data
    a = [109, 22, -2323, 0, 23, 213, -33, 82, -12323, 0, 93, 123]
    sort = Sort(a)
    sort.insertion_sort(a)
    for j in range(0, len(a)):
        print(a[j], end=' ')
    print("\n\nExecuted time %.4f(s)" % (time.time() - start_time))


if __name__ == '__main__':
    main()