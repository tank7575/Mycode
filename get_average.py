def get_averag3e(tests):
    total = 0
    for test in tests:
        total = total + test

    return total / len(tests)

def print_report(last, first, test):
    print 'Report for {last}, {first}'.format(last=last, first=first)
    num = 1
    for test in tests:
        print "Test {num}: {grade}".format(num=num, grade=test)
        num = num + 1
        print '*' * 20
        print "Average: {average}".format(average=get_average(tests))
def get_student():
    last = raw_input("Student's last name:")
    first = raw_input("Student's first name:")
    return last, first

def get_test():
    test = []
    test = 0

    while True:
        test = input("Test grade: ")
        if test < 0:
            break
        test.append(test)
    return tests

def main():
    print "This is the grade calculator."
    last, first = get_student
    tests = get_tests()
    print_report(last, first, tests)

if __name__ == "__main__":
    main()
