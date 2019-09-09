# -*- coding: utf-8 -*-
"""
Test of simple_prime_checker.PrimeChecker.is_prime_1(n) for small-ish input.
"""
import time

from simple_prime_checker import PrimeChecker


if __name__ == "__main__":

    prime_checker = PrimeChecker()

    start = time.perf_counter()
    prime_n = 25
    result = prime_checker.is_prime_1(prime_n)
    duration = time.perf_counter() - start
    print(
        "is_prime_1({0}) - duration: {1:.3f}(s)".\
            format(prime_n, duration)
    )

    start = time.perf_counter()
    prime_n = 25
    result = prime_checker.is_prime_2(prime_n)
    duration = time.perf_counter() - start
    print(
        "is_prime_2({0}) - duration: {1:.3f}(s)".\
            format(prime_n, duration)
    )

    print('\n')

    start = time.perf_counter()
    prime_n = prime_checker.prime_inputs[4]
    result = prime_checker.is_prime_1(prime_n)
    duration = time.perf_counter() - start
    print(
        "is_prime_1({0}) - duration: {1:.3f}(s)".\
            format(prime_n, duration)
    )

    start = time.perf_counter()
    prime_n = prime_checker.prime_inputs[4]
    result = prime_checker.is_prime_2(prime_n)
    duration = time.perf_counter() - start
    print(
        "is_prime_2({0}) - duration: {1:.3f}(s)".\
            format(prime_n, duration)
    )
