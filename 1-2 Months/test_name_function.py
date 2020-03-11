import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for name_function.py"""

    def test_first_last_name(self):
        """DO names like Mike OxLong work?"""
        formatted_name = get_formatted_name('Chris', 'Snapshot')
        self.assertEqual(formatted_name, 'Chris Snapshot')

    def test_first_middle_last_names(self):
        """Do names like ' hard ' work?"""
        formatted_name = get_formatted_name('Chris', 'Snapshot', 'God')
        self.assertEqual(formatted_name, 'Chris God Snapshot')
if __name__ == '__main__':
    unittest.main()