lst = [0,1]
def fibonacci(n):
    i = len(lst)
    if i < n:
        lst.append(lst[i-1]+lst[i-2])
        fibonacci(n)
    return lst

if __name__ == '__main__':
    n = int(raw_input())
    print(fibonacci(n))