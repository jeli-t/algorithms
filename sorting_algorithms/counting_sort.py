# counting sort implementation
# author: D1N3SHh
# https://github.com/D1N3SHh/algorithms


def counting_sort(A, B, k):
    C = []
    for i in range(0, k + 1):
        C.append(0)
    for j in range(0, len(A)):
        C[A[j]] += 1
    for i  in range(1, k):
        C[i] = C[i] + C[i-1]
    for j in reversed(range(0, len(A))):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    return B


def example_usage():
    A = [3, 7, 1, 8, 4, 6, 9, 2, 5]
    print('Unsorted:\t', A)
    print('Sorted:\t\t', counting_sort(A, [0] * len(A), max(A) + 1))


if __name__ == "__main__":
    example_usage() # run an example on start