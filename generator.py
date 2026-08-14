import secrets
import string


def generate_password(
    length,
    use_upper,
    use_lower,
    use_numbers,
    use_symbols,
    exclude_similar=False
):
    """Generate a secure random password."""

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation

    similar_characters = "O0oIl1|"

    character_pool = ""
    password = []

    # Uppercase
    if use_upper:
        characters = uppercase

        if exclude_similar:
            characters = "".join(
                char for char in characters
                if char not in similar_characters
            )

        character_pool += characters
        password.append(secrets.choice(characters))

    # Lowercase
    if use_lower:
        characters = lowercase

        if exclude_similar:
            characters = "".join(
                char for char in characters
                if char not in similar_characters
            )

        character_pool += characters
        password.append(secrets.choice(characters))

    # Numbers
    if use_numbers:
        characters = numbers

        if exclude_similar:
            characters = "".join(
                char for char in characters
                if char not in similar_characters
            )

        character_pool += characters
        password.append(secrets.choice(characters))

    # Symbols
    if use_symbols:
        character_pool += symbols
        password.append(secrets.choice(symbols))

    # No character type selected
    if not character_pool:
        return None

    # Password must be long enough
    if length < len(password):
        return None

    # Fill remaining characters
    while len(password) < length:
        password.append(
            secrets.choice(character_pool)
        )

    # Securely shuffle
    secrets.SystemRandom().shuffle(password)

    return "".join(password)