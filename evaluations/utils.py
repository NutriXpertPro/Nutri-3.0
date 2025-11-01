import math


def calculate_body_fat_navy(gender, waist, neck, height, hip=None):
    """
    Calculates body fat percentage using the U.S. Navy method.
    All measurements should be in centimeters.
    """
    if gender == "M":
        try:
            body_fat = (
                86.010 * math.log10(waist - neck) - 70.041 * math.log10(height) + 36.76
            )
        except ValueError:
            return None
    elif gender == "F":
        if not hip:
            return None
        try:
            body_fat = (
                163.205 * math.log10(waist + hip - neck)
                - 97.684 * math.log10(height)
                - 78.387
            )
        except ValueError:
            return None
    else:
        return None

    return round(body_fat, 2)
