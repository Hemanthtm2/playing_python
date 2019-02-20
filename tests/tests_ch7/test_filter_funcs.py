#!/usr/bin/python

from unittest import TestCase
from unittest.mock import patch,call
from nose.tools import assert_equal
from nose.tools import assert_list_equal 
from ch7.filter_funcs import filter_ints


class FilterIntsTestCase(TestCase):

      @patch('ch7.filter_funcs.is_positive')
      
      def test_filter_ints(self,is_positive_mock):
          
          v=[0,2,-7,5,8]
          
          filter_ints(v)

          assert_equal([call(0),call(2),call(-7),call(5),call(8)],is_positive_mock.call_args_list)

      def test_filter_ints_return_values(self):
          
          v=[3,-4,0,-2,5,0,8,-1]

          result=filter_ints(v)

          assert_list_equal([3,5,8],result)
