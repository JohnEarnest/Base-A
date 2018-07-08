# -*- coding: utf-8 -*-
from decimal import Decimal
from unittest import TestCase
from basea import basea

base_max = 4095
length = 64


class BaseATest(TestCase):
    """
    Testing BaseA
    """

    def setUp(self):
        pass

    def test_correct_dimensions(self):
        """
        This validates the assumed max and lengths
        """
        self.assertEqual(basea.max, base_max)
        self.assertEqual(len(basea.a), length)
        self.assertEqual(len(basea.b), length)

    def test_bad_decoding(self):
        """
        Validate that decoding fails in the ways we expect
        """
        for val in [-1, 82324, 'seven', {}]:
            with self.assertRaises(ValueError) as e:
                basea.decode(val)

            self.assertEqual(e.exception.args[0], 'Invalid name value')

    def test_bad_encoding(self):
        """
        Validate that encoding fails in the ways we expect
        """
        for val in [-1, 82324, 'seven', {}]:
            with self.assertRaises(ValueError) as e:
                basea.encode(val)

            self.assertEqual(e.exception.args[0], 'Invalid integer value')

    def test_valid(self):
        """
        Validate that the valid function returns valid on correct names
        """
        test_sets = [
            ('Goatse Danger', False),
            ('Gipsy Danger', True),
            ('Gipsy Doofus', False),
            ('Challenger Redeemer', True),
        ]
        for val, result in test_sets:
            self.assertEqual(basea.valid(val), result)

    def test_happy_decode(self):
        """
        Test a valid decoding path
        """
        test_name = 'Challenger Redeemer'
        val = basea.decode(test_name)
        self.assertEqual(val, 4)

    def test_happy_encode(self):
        """
        Test a valid encoding path
        """
        test_ints = [4, 4.0, Decimal('4.0')]
        for test_int in test_ints:
            val = basea.encode(test_int)
            self.assertEqual(val, 'Challenger Redeemer')
