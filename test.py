# -*- coding: utf-8 -*-
"""
Test of simple_prime_checker.PrimeChecker.is_prime_1(n) for small-ish input.
"""
from simple_prime_checker import PrimeChecker


if __name__ == "__main__":

    prime_checker = PrimeChecker()

    print(prime_checker.is_prime_1(prime_checker.prime_inputs[4]))

    print(prime_checker.is_prime_1(25))

    print(prime_checker.is_prime_2(prime_checker.prime_inputs[4]))

    print(prime_checker.is_prime_2(25))
