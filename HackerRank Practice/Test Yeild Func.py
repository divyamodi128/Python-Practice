def test_range(num):
    for n in range(0,num):
        print "Before yeild", n
        yield n
        print "After yeild", n


print "get_range(5) =", test_range(5)


print "List form:", [num for num in test_range(5)]


for num in test_range(5):
    print num