#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
'''This moudle contains the test cases for base.py'''


class TestBaseInitialize(unittest.TestCase):
    '''This class contains all the tests for base.py'''
    def test_a_idIncrement(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_b_idNone(self):
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_c_idNotNone(self):
        b4 = Base(10)
        self.assertEqual(b4.id, 10)

    def test_d_idAfterNonNone(self):
        b5 = Base()
        self.assertEqual(b5.id, 4)


class TestRectangleInitialize(unittest.TestCase):
    '''This class contains all the test for rectangle.py'''
    """
    def test_a_noArg(self):
        r0 = Rectangle(0)

    def test_b_oneArg(self):
        r1 = Rectangle(1)
    """
    def test_c_twoArg(self):
        result = []
        r2 = Rectangle(1, 2)
        result.append(r2.width)
        result.append(r2.height)
        result.append(r2.x)
        result.append(r2.y)
        result.append(r2.id)
        self.assertListEqual(result, [1, 2, 0, 0, 5])

    def test_d_threeArg(self):
        result = []
        r3 = Rectangle(1, 2, 3)
        result.append(r3.width)
        result.append(r3.height)
        result.append(r3.x)
        result.append(r3.y)
        result.append(r3.id)
        self.assertListEqual(result, [1, 2, 3, 0, 6])

    def test_e_fourArg(self):
        result = []
        r4 = Rectangle(1, 2, 3, 4)
        result.append(r4.width)
        result.append(r4.height)
        result.append(r4.x)
        result.append(r4.y)
        result.append(r4.id)
        self.assertListEqual(result, [1, 2, 3, 4, 7])

    def test_f_fiveArg(self):
        result = []
        r5 = Rectangle(1, 2, 3, 4, 5)
        result.append(r5.width)
        result.append(r5.height)
        result.append(r5.x)
        result.append(r5.y)
        result.append(r5.id)
        self.assertListEqual(result, [1, 2, 3, 4, 5])


class TestRectangleValidator(unittest.TestCase):
    '''TestRectangleValidator class'''
    def test_g_valTypeError(self):
        setter_test = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            re1 = Rectangle("one", 2)

    def test_h_valTypeError(self):
        setter_test = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            re1 = Rectangle(1, "two")

    def test_i_valTypeError(self):
        setter_test = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            re1 = Rectangle(1, 2, "three")

    def test_j_valTypeError(self):
        setter_test = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            re1 = Rectangle(1, 2, 3, "four")

    def test_k_valTypeError(self):
        setter_test = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            setter_test.width = "one"

    def test_l_valTypeError(self):
        setter_test = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            setter_test.height = "one"

    def test_m_valTypeError(self):
        setter_test = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            setter_test.x = "one"

    def test_n_valTypeError(self):
        setter_test = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            setter_test.y = "one"

    def test_o_valValueError(self):
        setter_test = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            re1 = Rectangle(-1, 2)

    def test_p_valValueError(self):
        setter_test = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            re1 = Rectangle(1, -12)

    def test_q_valValueError(self):
        setter_test = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            re1 = Rectangle(1, 2, -1)

    def test_r_valValueError(self):
        setter_test = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            re1 = Rectangle(1, 2, 3, -1)

    def test_s_valValueError(self):
        setter_test = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            setter_test.width = -1

    def test_t_valValueError(self):
        setter_test = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            setter_test.height = -2

    def test_u_valValueError(self):
        setter_test = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            setter_test.x = -3

    def test_v_valValueError(self):
        setter_test = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            setter_test.y = -4
