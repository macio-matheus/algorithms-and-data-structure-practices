"""
Regex validate PIN code

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or
exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
"""


def validate_pin(pin: str): return len(pin) in [4, 6] and pin.isdigit()
