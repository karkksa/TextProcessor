# TextProcessor

A Python utility class for text processing and validation operations.

## Features

- String length validation
- Character counting
- Number extraction
- Text sanitization

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/TextProcessor.git
cd TextProcessor
```

## Usage

```python
from main import TextProcessor

processor = TextProcessor()

# Validate string length
result = processor.validate_string_length("Hello", min_length=1, max_length=10)

# Count unique characters
char_count = processor.count_unique_characters("Hello World")

# Extract numbers
numbers = processor.extract_numbers("The price is 23.50")

# Sanitize text
clean_text = processor.sanitize_text("Hello123!", allow_numbers=True)
```

## Running Tests

```bash
python -m unittest test.py -v
```