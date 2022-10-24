from fizzbuzz import fizz_buzz_iter_2, fizz_buzz_iter_3, fizzbuzz, super_fizz_buzz


class TestFizzBuzz:
    def test_should_return_fizz_when_number_is_multiple_of_3(self):
        numbers = [3, 6, 9, 12]
        expected = (fizzbuzz(n) for n in numbers)
        for e in expected:
            assert e == "fizz"

    def test_should_return_buzz_when_number_is_multiple_of_5(self):
        numbers = [5, 10, 20]
        expected = (fizzbuzz(n) for n in numbers)
        for e in expected:
            assert e == "buzz"

    def test_should_return_fizzbuzz_when_number_is_multiple_of_5_and_3(self):
        numbers = [15, 30, 45]
        expected = (fizzbuzz(n) for n in numbers)
        for e in expected:
            assert e == "fizzbuzz"

    def test_should_return_same_number_when_number_is_not_a_multiple_of_3_or_5(self):
        numbers = [1, 2, 7, 11, 17]
        expected = map(fizzbuzz, numbers)
        for i, e in enumerate(expected):
            assert e == str(numbers[i])


class TestFizzBuzzIter2:
    def test_should_return_fizz_when_number_is_multiple_of_7(self):
        numbers = [7, 14, 21, 28, 35]
        expected = (fizz_buzz_iter_2(n) for n in numbers)
        for e in expected:
            assert e == "fizz"

    def test_should_return_buzz_when_number_is_multiple_of_11(self):
        numbers = [11, 22, 33, 44, 55]
        expected = (fizz_buzz_iter_2(n) for n in numbers)
        for e in expected:
            assert e == "buzz"

    def test_should_return_fizzbuzz_when_number_is_multiple_of_7_and_11(self):
        numbers = [77, 154, 308, 616]
        expected = (fizz_buzz_iter_2(n) for n in numbers)
        for e in expected:
            assert e == "fizzbuzz"

    def test_should_return_same_number_when_number_is_not_a_multiple_of_7_or_11(self):
        numbers = [1, 2, 17, 23, 25, 4]
        expected = (fizz_buzz_iter_2(n) for n in numbers)
        for i, e in enumerate(expected):
            assert e == str(numbers[i])


class TestFizzBuzzIter3:
    def test_should_return_fizz_when_number_is_13(self):
        expected = fizz_buzz_iter_3(number=13)
        assert expected == "fizz"

    def test_should_return_buzz_when_number_is_multiple_of_17(self):
        numbers = [17, 34, 51, 68]
        expected = map(fizz_buzz_iter_3, numbers)
        for e in expected:
            assert e == "buzz"

    def test_should_return_fuzz_when_number_is_multiple_of_19(self):
        numbers = [19, 38, 57, 76]
        expected = map(fizz_buzz_iter_3, numbers)
        for e in expected:
            assert e == "fuzz"

    def test_should_return_bizz_when_number_is_multiple_of_23(self):
        numbers = [23, 46, 69, 92]
        expected = map(fizz_buzz_iter_3, numbers)
        for e in expected:
            assert e == "bizz"

    def test_should_return_fizzbuzz_when_number_is_multiple_of_13_and_17(self):
        numbers = [221, 442, 13 * 17 * 3]
        expected = map(fizz_buzz_iter_3, numbers)
        for e in expected:
            assert e == "fizzbuzz"

    def test_should_return_fizzfuzz_when_number_is_multiple_of_13_and_19(self):
        numbers = [247, 494, 13 * 19 * 3]
        expected = map(fizz_buzz_iter_3, numbers)
        for e in expected:
            assert e == "fizzfuzz"

    def test_should_return_fizzbuzzfuzz_when_number_is_multiple_of_13_and_17_and_19(
        self,
    ):
        numbers = [13 * 17 * 19, 13 * 17 * 19 * 2, 13 * 17 * 19 * 3]
        expected = map(fizz_buzz_iter_3, numbers)
        for e in expected:
            assert e == "fizzbuzzfuzz"

    def test_should_return_fizzbizz_when_number_is_multiple_of_13_and_23(self):
        numbers = [13 * 23, 13 * 23 * 2, 13 * 23 * 3]
        expected = map(fizz_buzz_iter_3, numbers)
        for e in expected:
            assert e == "fizzbizz"

    def test_should_return_input_when_number_is_matching_no_rule(self):
        numbers = [1, 2, 3, 4, 48]
        expected = map(fizz_buzz_iter_3, numbers)
        for i, e in enumerate(expected):
            assert e == str(numbers[i])


class TestSuperFizzBuzz:
    def test_should_return_fizz_when_number_is_not_divisible_by_3(self):
        numbers = [14, 20]
        expected = map(super_fizz_buzz, numbers)
        for e in expected:
            assert e == "fizz"

    def test_should_return_buzz_when_number_is_odd(self):
        numbers = [3, 15]
        expected = map(super_fizz_buzz, numbers)
        for e in expected:
            assert e == "buzz"

    def test_should_return_fuzz_when_number_is_perfect_square(self):
        numbers = [36, 12 * 12]
        expected = map(super_fizz_buzz, numbers)
        for e in expected:
            assert e == "fuzz"

    def test_should_return_fizzfuzz_when_number_is_perfect_square_and_not_a_multiple_of_3(
        self,
    ):
        numbers = [16, 8 * 8, 100]
        expected = map(super_fizz_buzz, numbers)
        for e in expected:
            assert e == "fizzfuzz"

    def test_should_return_fizzbuzz_when_number_is_not_a_multiple_of_3_and_is_odd(self):
        numbers = [7, 11, 13]
        expected = map(super_fizz_buzz, numbers)
        for e in expected:
            assert e == "fizzbuzz"

    def test_should_return_fizzbuzzfuzz_when_number_is_not_multiple_of_3_and_is_odd_and_a_perfect_square(
        self,
    ):
        numbers = [49, 25, 11 * 11]
        expected = map(super_fizz_buzz, numbers)
        for e in expected:
            assert e == "fizzbuzzfuzz"

    def test_should_return_input_when_number_matching_no_rules(self):
        numbers = [6, 18, 24]
        expected = map(super_fizz_buzz, numbers)
        for i, e in enumerate(expected):
            assert e == str(numbers[i])
