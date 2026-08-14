import math


def calculate_entropy(password):
    """Calculate estimated password entropy in bits."""

    if not password:
        return 0

    character_set_size = 0

    if any(char.islower() for char in password):
        character_set_size += 26

    if any(char.isupper() for char in password):
        character_set_size += 26

    if any(char.isdigit() for char in password):
        character_set_size += 10

    if any(not char.isalnum() for char in password):
        character_set_size += 32

    if character_set_size == 0:
        return 0

    entropy = len(password) * math.log2(character_set_size)

    return round(entropy, 2)


def password_strength(password):
    """
    Return:
        score
        strength level
        display color
        entropy
    """

    if not password:
        return 0, "Very Weak", "#F44336", 0

    score = 0

    length = len(password)

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    categories = sum([
        has_upper,
        has_lower,
        has_number,
        has_symbol
    ])

    # Length score
    if length >= 8:
        score += 20

    if length >= 12:
        score += 20

    if length >= 16:
        score += 20

    # Character variety
    score += categories * 10

    # Extra bonus
    if length >= 20 and categories == 4:
        score += 20

    score = min(score, 100)

    entropy = calculate_entropy(password)

    if score < 40:
        return score, "Weak", "#F44336", entropy

    elif score < 70:
        return score, "Medium", "#FF9800", entropy

    elif score < 90:
        return score, "Strong", "#2196F3", entropy

    else:
        return score, "Very Strong", "#4CAF50", entropy