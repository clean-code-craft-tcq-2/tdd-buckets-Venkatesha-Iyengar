import unittest
from tdd_buckets import *
from A2D_converter import *

class tdd_buckets_test(unittest.TestCase):
    #Tests for Continuous Range Evaluator -> Legacy Code
    def test_ranges(self):
        self.assertTrue(Obj_Group_Number_Range.iterate_numbers([1,2,3,4,5,6,8,9,10]) == {'1-6': 6, '8-10': 3})
        self.assertTrue(Obj_Group_Number_Range.iterate_numbers([1,2]) == {'1-2': 2})
        self.assertTrue(Obj_Group_Number_Range.iterate_numbers([-1,0,1,2,3,4,5,6,8,9,10]) == {'-1-6': 8, '8-10': 3})

    def test_empty_range(self):
        self.assertTrue(Obj_Group_Number_Range.iterate_numbers([]) == {})

    def test_printOnConsole(self):
        self.assertTrue(Obj_Group_Number_Range.print_last_range_details('Printing on Console') == True)

    #Tests For Extension -> Digital to Analog Convertor
    def test_maximum_possible_value(self):
        self.assertEqual(adc_object1.get_maximum_value(),4095)
        self.assertEqual(adc_object2.get_maximum_value(),1023)

    def test_valid_range(self):
        self.assertEqual(adc_object1.get_valid_range([0,10,20,4095,5000,-50,1000,2000,3000,4000]),[0,10,20,1000,2000,3000,4000])
        self.assertEqual(adc_object2.get_valid_range([0,10,20,4095,5000,-50,1000,2000,3000,4000]),[0,10,20,1000])

    def test_absolute_current_values_range(self):
        self.assertEqual(adc_object1.get_absolute_range([],max_current_in_amps=10),[])
        self.assertEqual(adc_object2.get_absolute_range([],max_current_in_amps=10),[])
        self.assertEqual(adc_object1.get_absolute_range([0,1024,2048,4095],max_current_in_amps=10),[0,3,5])
        self.assertEqual(adc_object2.get_absolute_range([0,1024,2048,4095],max_current_in_amps=15),[15])
        self.assertEqual(adc_object2.get_absolute_range([0,10,204,511,4095],max_current_in_amps=15),[15, 15, 9, 0])

    #Tests for Extension Combined with Legacy Code
    def test_absolute_current_ranges(self):
        self.assertEqual(Obj_Group_Number_Range.iterate_numbers(adc_object1.get_absolute_range([],max_current_in_amps=10)),{})
        self.assertEqual(Obj_Group_Number_Range.iterate_numbers(adc_object2.get_absolute_range([],max_current_in_amps=10)),{})
        self.assertEqual(Obj_Group_Number_Range.iterate_numbers(adc_object1.get_absolute_range([0,1024,2048,4095],max_current_in_amps=10)),{})
        self.assertEqual(Obj_Group_Number_Range.iterate_numbers(adc_object1.get_absolute_range([0,10,20,30,100,1024,2048,4095],max_current_in_amps=10)),{'0-0':4})
        self.assertEqual(Obj_Group_Number_Range.iterate_numbers(adc_object2.get_absolute_range([0,1024,2048,4095],max_current_in_amps=15)),{})
        self.assertEqual(Obj_Group_Number_Range.iterate_numbers(adc_object2.get_absolute_range([0,10,204,511,4095],max_current_in_amps=15)),{'15-15':2})
        

Obj_Group_Number_Range = Group_Number_Range()
adc_object1 = A2D_Conerter(no_bits=12)
adc_object2 = A2D_Conerter(no_bits=10,flag_signed=True)


unittest.main()
