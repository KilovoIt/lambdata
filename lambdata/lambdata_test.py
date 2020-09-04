"""Basic test for lambdata functionality"""

import unittest

from oop_examples import Firearms, Rifles

class FirearmsTests(unittest.TestCase):
    """Test of a firearm type behavior with a selector switch change"""
    def test_safety(self):
    """Test that a pistol on fire position is off the safety"""
        pistol = Firearms('1911', 0.45, 'USA')
        pistol.selector_fire()
        self.assertEqual(pistol.sel, 1)
        
    def test_full_auto(self):
    """Test that a rifle on safety is not on full auto"""
        rifle = Rifles('AK74', 5.45, 'Russia')
        rifle.selector_safety()
        self.assertNotEqual(rifle.sel, 2)

if __name__ == '__main__':
    unittest.main()
