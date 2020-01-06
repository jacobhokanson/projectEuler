# myTestCase

def Test(cases, fn): # Dict
    results = [] # List[Tuple] # (Input, Output, Expected)
    for (test, value) in cases.items():
        results.append((fn.__name__ + "(" + str(test) + ")", fn(test), value))
        # print("fn(" + str(test) + ") is", result := fn(test), "-- should be", value)
        # assert result == value
    print("\n" + "-" * 30, "MYTC RESULTS", "-" * 30)
    for case in results:
        print(" -", case[0], "returned", case[1], "expected", case[2])
        