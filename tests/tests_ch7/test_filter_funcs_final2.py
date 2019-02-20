#!/usr/bin/python


from unittest import TestCase

from nose.tools import assert_list_equal

from ch7.filter_funcs import filter_ints


class FilterIntsTestCase(TestCase):
      
     def test_filter_ints(self):

         v=[0,-7,8,9,5]

      

         assert_list_equal([8,9,5],filter_ints(v))
