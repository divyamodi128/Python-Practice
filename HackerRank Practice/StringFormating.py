n = int(raw_input())
w = bin(n).__len__()
print w
for i in range(1, n + 1, 1):
    print str(int(i)).rjust(w), "\t", oct(i).replace('0', '', 1).rjust(w), "\t", hex(i).replace('0x', '').upper().rjust(w), "\t", bin(i).replace('0b', '').rjust(w)