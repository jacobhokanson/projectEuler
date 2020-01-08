# myTestCase

def Test(cases, fn): # Dict
    results = [] # List[Tuple] # (Input, Output, Expected)
    for (test, value) in cases.items():
        results.append((fn.__name__ + "(" + str(test) + ")", fn(test), value))
        # print("fn(" + str(test) + ") is", result := fn(test), "-- should be", value)
        # assert result == value
    print(f'{" MYTC RESULTS ":-^74}')

    # print("\n" + "-" * 30, "MYTC RESULTS", "-" * 30)
    for case in results:
        print(f'{f" - {case[0]} = {case[1]} expected {case[2]} ":.<69}', "PASS" if case[1] == case[2] else "FAIL")

        # WOW learning this was a pain
        # print(" -", case[0], "returned", case[1], "expected", case[2], "--", "PASS" if case[1] == case[2] else "FAIL")
        # print(f' - {case[0]} returned {case[1]} expected {case[2]} --', f'{"PASS" if case[1] == case[2] else "FAIL"}')
        # print(f'{" - {case[0]} returned {case[1]} expected {case[2]} -- {'PASS' if case[1] == case[2] else 'FAIL'}":<12}')
        # print(f'{f" - {case[0]} returned {case[1]} expected {case[2]} -- {m[0] if case[1] == case[2] else m[1]}":>50}') m = ("PASS", "FAIL")