import unittest
from tdd_buckets import *

class tdd_buckets_test(unittest.TestCase):
    def test_ranges(self):
        self.assertTrue(Obj_Group_Number_Range.iterate_numbers([1,2,3,4,5,6,8,9,10]) == {'1-6': 6, '8-10': 3})
        self.assertTrue(Obj_Group_Number_Range.iterate_numbers([1,2]) == {'1-2': 2})
        self.assertTrue(Obj_Group_Number_Range.iterate_numbers([-1,0,1,2,3,4,5,6,8,9,10]) == {'-1-6': 8, '8-10': 3})

    def test_empty_range(self):
        self.assertTrue(Obj_Group_Number_Range.iterate_numbers([]) == {})

    def test_printOnConsole(self):
        self.assertTrue(Obj_Group_Number_Range.print_last_range_details('Printing on Console') == True)

Obj_Group_Number_Range = Group_Number_Range()
unittest.main()
        
