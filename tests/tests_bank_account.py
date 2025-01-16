"""Test cases for class BankAccount"""

# P.S.: If you are placing your model directory in some other location
# (not in the same directory branch), you will have to modify the python path using sys.path.

import sys
import os
from unittest import TestCase

# $ pip install parameterized
from libs_downloaded.parameterized.parameterized import parameterized, parameterized_class

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Book_unit170.account import BankAccount, MyError



# this is if we want to use same test case wwith multiple values to check scenarios (exxample)
# other case is with the library parameterized but I could not install it ...

# from unittest import TestCase

# param_list = [('a', 'a'), ('a', 'b'), ('b', 'b')]

# class TestDemonstrateSubtest(TestCase):
#     def test_works_as_expected(self):
#         for p1, p2 in param_list:
#             with self.subTest(p1, p2):
#                 self.assertEqual(p1, p2)
# You can also specify a custom message and parameter values to subTest():

# with self.subTest(msg="Checking if p1 equals p2", p1=p1, p2=p2):

class TestBankAccount(TestCase):

    def setUp(self):
        """start up of test object"""
        self.my_account = BankAccount("123A", "2025-01-16", 2.32, 10000)

    @parameterized.expand([
        ('Iskren', 1),
        ('Test2', 2)
    ])
    def test_multiples(self, a,b):
        self.assertTrue(type(a), "String")
        self.assertTrue(type(b), "Int")

    # test initial deposit
    def test_initial_deposit(self):
        """test case 1"""
        self.assertEqual(self.my_account.balance, 10000)
        self.assertTrue(self.my_account.balance >= 0)

    # test deposit
    def test_deposit(self):
        """test case 2"""
        self.my_account.deposit(1000)
        self.assertEqual(self.my_account.balance, 11000)
        self.assertGreater(self.my_account.balance, 10000)

    # test withraw
    def test_withraw(self):
        """test case 3"""
        old_amount = self.my_account.balance
        self.my_account.withraw(1000)
        self.assertEqual(self.my_account.balance, 9000)
        self.assertNotEqual(self.my_account.balance, old_amount)

    # insifficient funds
    def test_incifficient_funds(self):
        """test case 4"""
        with self.assertRaises(MyError):
            self.my_account.withraw(100000)

    # test negative deposit
    def test_negative_deposit(self):
        """test case 5"""
        with self.assertRaises(MyError):
            self.my_account.deposit(-100)

    # test negative withraw
    def test_negative_withraw(self):
        """test case 6"""
        with self.assertRaises(MyError):
            self.my_account.withraw(-100)

    # balance change
    def test_balance_change(self):
        """test case 7"""
        old_balance = self.my_account.balance
        self.my_account.deposit(100)
        self.my_account.withraw(200)
        self.assertEqual(self.my_account.balance, 9900)
        self.assertTrue(old_balance > self.my_account.balance)

    def tearDown(self):
        """cleaning up"""
        self.my_account = None
