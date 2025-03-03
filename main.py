import re
from typing import List, Optional

class TextProcessor:
    """A utility class for text processing and validation operations."""
    
    def __init__(self):
        self.last_processed = None
    
    def validate_string_length(self, text: str, min_length: int = 1, max_length: int = 1000) -> bool:
        """
        Validates if a string's length is within specified bounds.
        
        Args:
            text (str): Input text to validate
            min_length (int): Minimum allowed length (default: 1)
            max_length (int): Maximum allowed length (default: 1000)
            
        Returns:
            bool: True if length is valid, False otherwise
        """
        if not isinstance(text, str):
            return False
        text_length = len(text)
        return min_length <= text_length <= max_length

    def count_unique_characters(self, text: str) -> dict:
        """
        Counts occurrence of each unique character in the text.
        
        Args:
            text (str): Input text to analyze
            
        Returns:
            dict: Dictionary with characters as keys and their counts as values
        """
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        
        char_count = {}
        for char in text:
            char_count[char] = char_count.get(char, 0) + 1
        
        self.last_processed = text
        return char_count

    def extract_numbers(self, text: str) -> List[float]:
        """
        Extracts all numbers (including decimals) from text.
        
        Args:
            text (str): Input text to process
            
        Returns:
            List[float]: List of numbers found in text
        """
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
            
        number_pattern = r'-?\d*\.?\d+'
        numbers = re.findall(number_pattern, text)
        return [float(num) for num in numbers]

    def sanitize_text(self, text: str, 
                     allow_numbers: bool = True,
                     allow_spaces: bool = True,
                     allowed_special_chars: Optional[str] = None) -> str:
        """
        Sanitizes text by removing or keeping specific character types.
        
        Args:
            text (str): Input text to sanitize
            allow_numbers (bool): Whether to keep numbers
            allow_spaces (bool): Whether to keep spaces
            allowed_special_chars (str, optional): String of allowed special characters
            
        Returns:
            str: Sanitized text
        """
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
            
        # Convert to list for manipulation
        chars = list(text)
        result = []
        
        for char in chars:
            # Always allow letters
            if char.isalpha():
                result.append(char)
                continue
                
            # Handle numbers
            if char.isdigit() and allow_numbers:
                result.append(char)
                continue
                
            # Handle spaces
            if char.isspace() and allow_spaces:
                result.append(char)
                continue
                
            # Handle special characters
            if allowed_special_chars and char in allowed_special_chars:
                result.append(char)
                
        return ''.join(result)
