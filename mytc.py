# myTestCase

def Test(cases, fn): # Dict
    for (test, value) in cases.items():
        print("fn(" + str(test) + ")", "is", result := fn(test), "-- should be", value)
        assert result == value