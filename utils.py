def check_if_float(amount):
    """checks if a string for bank amounts is really a float"""
    
    try:
        float(amount)
        return True
    except ValueError:
        return False
