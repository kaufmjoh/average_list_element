import unittest
import average

class TestAverage(unittest.TestCase):
	def test_average(self):
		self.assertEqual(average.average([1,2,3]), 2)
		self.assertEqual(average.average([2,4,5]), 3.66667)
		self.assertEqual(average.average([-1,-2,-3]), -2)
		self.assertEqual(average.average([-1,0,1]), 0)
		self.assertEqual(average.average([0,0,1]), 0.33333)
		self.assertEqual(average.average([0.5,0.6,0.7]), 0.6)

	def test_empty_list(self):
		self.assertEqual(average.average([]), "You entered an empty list.")

	
	def test_bad_input(self):
		self.assertEqual(average.average(["Fail", 3, 4]), "At least one of the list elements was invalid.")
		self.assertEqual(average.average([2 , "Fail", 4]), "At least one of the list elements was invalid.")
		self.assertEqual(average.average([2 , 3, "Fail"]), "At least one of the list elements was invalid.")
		self.assertEqual(average.average([1 , 3, '4a']), "At least one of the list elements was invalid.")


if __name__ == '__main__':
	unittest.main()
