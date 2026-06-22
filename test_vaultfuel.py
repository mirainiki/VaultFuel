# test_vaultfuel.py
"""
Tests for VaultFuel module.
"""

import unittest
from vaultfuel import VaultFuel

class TestVaultFuel(unittest.TestCase):
    """Test cases for VaultFuel class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VaultFuel()
        self.assertIsInstance(instance, VaultFuel)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VaultFuel()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
