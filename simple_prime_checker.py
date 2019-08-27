# -*- coding: utf-8 -*-
"""
Simple function to check whether a given integer is a prime or composite.

is_prime(n)

Example:
    > prime_checker = PrimeChecker()
    > prime_checker.is_prime_1(prime_checker.prime_inputs[0])
    >> True
    > prime_checker.is_prime_1(25)
    >> False
"""
import math


class PrimeChecker:

    def __init__(self):
        """
        Class to encapsulate a few prime inputs and a
        primality checker method.
        """
        self.prime_inputs = (2147483647,
            17180131327,
            200560490131,
            4398050705407,
            10963707205259,
            792606555396977,
            9999999900000001,
            10657331232548839,
            909090909090909091 # is_prime_1 performance is very slow on this
        )


    def is_prime_1(self, n):
        """
        Simple method to check whether integer is prime.

        Args:
            n (int): integer to check whether prime.

        Returns:
            bool: True if n is prime, False otherwise.
        """
        if n <= 3:
            return n > 1
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True


    def is_prime_2(self, n):
        """
        A bit faster method to check whether integer is prime.

        Args:
            n (int): integer to check whether prime.

        Returns:
            bool: True if n is prime, False otherwise.

        Adapted from https://stackoverflow.com/questions/1801391
        """

        if n <= 1:          # 0 or 1
            return False
        if n <= 3:          # 2 or 3
            return True
        if n % 2 == 0 or n % 3 == 0: # divisble by 2 or 3
            return False
        #
        for i in range(5, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False

        return True


if __name__ == "__main__":

    prime_checker = PrimeChecker()

    print(prime_checker.is_prime_1(prime_checker.prime_inputs[4]))

    print(prime_checker.is_prime_1(25))

    print(prime_checker.is_prime_2(prime_checker.prime_inputs[4]))

    print(prime_checker.is_prime_2(25))
