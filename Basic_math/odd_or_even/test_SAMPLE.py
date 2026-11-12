from odd_or_even import Solution

# STEP 1: Create an object
obj = Solution()

# STEP 2: Track test results
passed = 0
failed = 0


# STEP 3: Normal test cases
def test_normal_numbers():

    test_cases = [
        (2, True),
        (4, True),
        (6, True),
        (1, False),
        (3, False),
        (7, False),
    ]

    for n, expected in test_cases:

        actual = obj.isEven(n)

        assert actual == expected, f"Input: {n}"

        print(f"PASS: Normal number {n}")
        

# STEP 4: Boundary test cases
def test_boundary_numbers():

    test_cases = [
        (0, True),
        (1, False),
        (-1, False),
        (-2, True),
    ]

    for n, expected in test_cases:

        actual = obj.isEven(n)

        assert actual == expected, f"Input: {n}"

        print(f"PASS: Boundary number {n}")


# STEP 5: Negative number test cases
def test_negative_numbers():

    test_cases = [
        (-4, True),
        (-5, False),
        (-100, True),
        (-101, False),
    ]

    for n, expected in test_cases:

        actual = obj.isEven(n)

        assert actual == expected, f"Input: {n}"

        print(f"PASS: Negative number {n}")


# STEP 6: Large integer test cases
def test_large_numbers():

    test_cases = [
        (10**100, True),
        (10**100 + 1, False),
        (-(10**100), True),
        (-(10**100 + 1), False),
    ]

    for n, expected in test_cases:

        actual = obj.isEven(n)

        assert actual == expected, f"Input: {n}"

        print("PASS: Large integer")


# STEP 7: Invalid input test cases
def test_invalid_inputs():

    test_cases = [
        "2",
        "hello",
        2.0,
        3.5,
        None,
        [],
        {},
        (2,),
        True,
        False,
    ]

    for n in test_cases:

        try:
            obj.isEven(n)

            # If no TypeError occurs, test fails.
            raise AssertionError(
                f"Expected TypeError for input: {n!r}"
            )

        except TypeError:
            print(f"PASS: Invalid input {n!r}")


# STEP 8: Execute all test functions
def run_all_tests():

    global passed, failed

    test_functions = [
        test_normal_numbers,
        test_boundary_numbers,
        test_negative_numbers,
        test_large_numbers,
        test_invalid_inputs,
    ]

    for test_function in test_functions:

        try:
            test_function()
            passed += 1

        except Exception as error:
            failed += 1
            print(f"FAILED: {test_function.__name__}")
            print(f"Reason: {error}")

    print("\n========== TEST SUMMARY ==========")
    print(f"Test groups passed: {passed}")
    print(f"Test groups failed: {failed}")
    print("=================================")


if __name__ == "__main__":
    run_all_tests()

#Can also use pytest framework to run the test cases, which is more efficient and provides better reporting.

# # ============================================================
# # PYTEST BASICS
# # Topic: Testing an Odd or Even Number
# # ============================================================

# # STEP 1: IMPORTS
# # ------------------------------------------------------------

# # Import pytest testing framework.
# # pytest provides fixtures, parametrization, assertions,
# # exception handling and test discovery.

# import pytest

# # Import the Solution class from our implementation file.
# # odd_or_even.py contains the actual business logic.
# from odd_or_even import Solution


# # STEP 2: FIXTURE
# # ------------------------------------------------------------

# # @pytest.fixture tells pytest that this function is a fixture.
# #
# # A fixture is used to prepare reusable resources for test cases.
# #
# # Here, we create an object of the Solution class.
# #
# # When a test function declares 'obj' as an argument,
# # pytest automatically executes this fixture and injects
# # the returned object into that test function.
# #
# # Default scope = "function".
# # So, a fresh Solution object is created for each test invocation.

# @pytest.fixture
# def obj():
#     return Solution()


# # STEP 3: NORMAL TEST CASES
# # ------------------------------------------------------------

# # @pytest.mark.parametrize allows us to execute the same
# # test function with multiple sets of inputs.
# #
# # "n, expected" defines two parameter names.
# #
# # Each tuple represents one test case:
# # (input_number, expected_output)
# #
# # For example:
# # (2, True) means:
# # Input = 2
# # Expected output = True
# #
# # Instead of writing six separate test functions,
# # pytest automatically generates six test invocations.

# @pytest.mark.parametrize("n, expected", [
#     (2, True),
#     (4, True),
#     (6, True),
#     (1, False),
#     (3, False),
#     (7, False),
# ])

# # Pytest discovers functions whose names start with test_.
# #
# # Arguments:
# # obj      -> Injected through the fixture.
# # n        -> Input supplied by parametrize.
# # expected -> Expected output supplied by parametrize.

# def test_normal_numbers(obj, n, expected):

#     # ASSERTION:
#     # 1. Call the actual implementation: obj.isEven(n)
#     # 2. Compare the returned result with expected.
#     #
#     # If both are equal -> Test PASSES.
#     # If they are different -> Test FAILS.

#     assert obj.isEven(n) == expected


# # STEP 4: BOUNDARY TEST CASES
# # ------------------------------------------------------------

# # Boundary testing checks values at important limits.
# #
# # Here, zero and numbers immediately around zero are tested.
# #
# # 0  -> Even
# # 1  -> Odd
# # -1 -> Odd
# # -2 -> Even

# @pytest.mark.parametrize("n, expected", [
#     (0, True),
#     (1, False),
#     (-1, False),
#     (-2, True),
# ])

# def test_boundary_numbers(obj, n, expected):

#     # Verify whether the implementation handles
#     # boundary values correctly.

#     assert obj.isEven(n) == expected


# # STEP 5: NEGATIVE NUMBER TEST CASES
# # ------------------------------------------------------------

# # Test whether the algorithm works for negative integers.
# #
# # Important:
# # Python modulo behaviour:
# # -4 % 2 = 0
# # -5 % 2 = 1
# #
# # Therefore, negative even numbers should return True
# # and negative odd numbers should return False.

# @pytest.mark.parametrize("n, expected", [
#     (-4, True),
#     (-5, False),
#     (-100, True),
#     (-101, False),
# ])

# def test_negative_numbers(obj, n, expected):

#     # Compare actual output against expected output.

#     assert obj.isEven(n) == expected


# # STEP 6: VERY LARGE INTEGER TEST CASES
# # ------------------------------------------------------------

# # Python integers support arbitrary precision.
# #
# # Unlike fixed-width integer types in languages such as C,
# # Python integers can grow beyond 32-bit or 64-bit limits.
# #
# # 10**100 means 10 raised to the power of 100.
# #
# # We test whether the implementation handles very large
# # positive and negative integers correctly.

# @pytest.mark.parametrize("n, expected", [
#     (10**100, True),
#     (10**100 + 1, False),
#     (-(10**100), True),
#     (-(10**100 + 1), False),
# ])

# def test_large_numbers(obj, n, expected):

#     # Verify correctness for extremely large integers.

#     assert obj.isEven(n) == expected


# # STEP 7: INVALID INPUT TEST CASES
# # ------------------------------------------------------------

# # So far, we tested valid integer inputs.
# #
# # Now we test invalid input types.
# #
# # Expected behaviour:
# # The implementation should raise TypeError.
# #
# # Invalid inputs include:
# # String, float, None, list, dictionary, tuple and Boolean.
# #
# # Note:
# # Python considers bool a subclass of int.
# # Therefore, the implementation must explicitly reject bool.

# @pytest.mark.parametrize("n", [
#     "2",
#     "hello",
#     2.0,
#     3.5,
#     None,
#     [],
#     {},
#     (2,),
#     True,
#     False,
# ])

# def test_invalid_inputs(obj, n):

#     # pytest.raises(TypeError) is used to verify exceptions.
#     #
#     # It means:
#     # Execute the code inside this block.
#     # If TypeError occurs -> Test PASSES.
#     # If TypeError does not occur -> Test FAILS.
#     # If another exception occurs -> Test FAILS.

#     with pytest.raises(TypeError):

#         # Call the actual implementation using invalid input.
#         obj.isEven(n)


# # ============================================================
# # END OF TEST CASES
# # ============================================================
