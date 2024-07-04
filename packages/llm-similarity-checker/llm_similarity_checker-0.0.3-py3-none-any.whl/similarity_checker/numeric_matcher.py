import re

class NumericMatcher:
    def __init__(self, target):
        self.target = target

    @staticmethod
    def normalize_numeric(input_str):
        try:
            # Extract numeric part from the input string
            numeric_part = re.search(r'[\d\.,]+', input_str).group(0)
            
            # Replace commas and convert to float
            numeric_value = float(numeric_part.replace(',', ''))
            return numeric_value
        except (AttributeError, ValueError):
            # If extraction or conversion fails, return None
            return None

    def match(self, input_str):
        # Normalize the numeric value from the input string
        numeric_value = self.normalize_numeric(input_str)
        
        # Check if numeric_value is None (conversion failed)
        if numeric_value is None:
            return False
        
        # Determine rounding and comparison logic based on the value of numeric_value
        if numeric_value < 1:
            # For numbers less than 1, match up to 2 decimal places
            return round(numeric_value, 2) == round(self.target, 2)
        else:
            # For numbers greater than or equal to 1, round and check if match
            return round(numeric_value) == round(self.target)

# Example usage
if __name__ == "__main__":
    # Create an instance of NumericMatcher with target value
    matcher = NumericMatcher(0.12)

    # Test cases
    test_cases = [
        "The average of object is RM15,222.333", 
        "The total is RM1.00", 
        "The value is RM15.12", 
        "The value is RM0.124", 
        "The value is RM0.00", 
    ]

    # Test each input string against the target value
    for case in test_cases:
        if matcher.match(case):
            print(f"'{case}' matches with {matcher.target}")
        else:
            print(f"'{case}' does not match with {matcher.target}")