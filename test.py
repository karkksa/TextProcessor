import unittest
from main import TextProcessor

class TestTextProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = TextProcessor()
        
    def test_validate_string_length_basic(self):
        self.assertTrue(self.processor.validate_string_length("Hello"))
        self.assertFalse(self.processor.validate_string_length(""))
        
    def test_validate_string_length_edge_cases(self):
        # Test with None
        self.assertFalse(self.processor.validate_string_length(None))
        
        # Test with non-string input
        self.assertFalse(self.processor.validate_string_length(123))
        
        # Test with very long string
        long_string = "a" * 1001
        self.assertFalse(self.processor.validate_string_length(long_string))
        
    def test_validate_string_length_unicode(self):
        # Test with Chinese characters
        self.assertTrue(self.processor.validate_string_length("你好世界"))
        
        # Test with Arabic characters
        self.assertTrue(self.processor.validate_string_length("مرحبا"))
        
        # Test with emoji
        self.assertTrue(self.processor.validate_string_length("👋🌍"))
        
    def test_count_unique_characters_basic(self):
        result = self.processor.count_unique_characters("hello")
        self.assertEqual(result, {'h': 1, 'e': 1, 'l': 2, 'o': 1})
        
    def test_count_unique_characters_unicode(self):
        # Test with mixed Unicode characters
        result = self.processor.count_unique_characters("你好你世界")
        self.assertEqual(result['你'], 2)
        self.assertEqual(result['好'], 1)
        
    def test_count_unique_characters_invalid_input(self):
        with self.assertRaises(ValueError):
            self.processor.count_unique_characters(None)
        with self.assertRaises(ValueError):
            self.processor.count_unique_characters(123)
            
    def test_extract_numbers_basic(self):
        result = self.processor.extract_numbers("The price is 23.50 and quantity is 5")
        self.assertEqual(result, [23.50, 5.0])
        
    def test_extract_numbers_edge_cases(self):
        # Test negative numbers
        result = self.processor.extract_numbers("Temperature is -15.5°C")
        self.assertEqual(result, [-15.5])
        
        # Test very large numbers
        result = self.processor.extract_numbers("Distance is 1234567.89 light years")
        self.assertEqual(result, [1234567.89])
        
    def test_extract_numbers_invalid_input(self):
        with self.assertRaises(ValueError):
            self.processor.extract_numbers(None)
            
    def test_sanitize_text_basic(self):
        result = self.processor.sanitize_text("Hello123!")
        self.assertEqual(result, "Hello123")
        
    def test_sanitize_text_unicode(self):
        # Test with mixed characters
        result = self.processor.sanitize_text("你好123 World!", 
                                            allow_numbers=True,
                                            allow_spaces=True,
                                            allowed_special_chars="!")
        self.assertEqual(result, "你好123 World!")
        
    def test_sanitize_text_long_input(self):
        # Test with very long input
        long_input = "A" * 10000 + "123" + "!" * 100
        result = self.processor.sanitize_text(long_input)
        self.assertEqual(result, "A" * 10000 + "123")
        
    def test_sanitize_text_special_chars(self):
        # Test with various special characters
        result = self.processor.sanitize_text("Hello@#$%^&*()", 
                                            allowed_special_chars="@#$")
        self.assertEqual(result, "Hello@#$")

if __name__ == '__main__':
    unittest.main()
