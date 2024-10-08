from pathlib import Path


def generate_profile(theme, **kwargs):
    """Generate profile readme from theme and kwargs"""
    # Read theme profile
    with open(f"src/themes/{theme}/profile.txt") as f:
        profile = f.read()

    # Replace placeholders with items
    for item, value in kwargs.items():
        # Skip empty values
        if not value:
            profile = profile.replace(f"{{ {item} }}", '')
            continue

        # Skip items that don't exist in theme
        item_path = Path(f"src/themes/{theme}/{item}.txt")
        if not item_path.exists():
            continue

        # Replace placeholder with item
        with open(item_path) as f:
            profile_item = f.read().strip()
        profile_item = profile_item.replace("{ value }", value)
        profile = profile.replace(f"{{ {item} }}", profile_item)

    return profile


if __name__ == '__main__':
    # Personal Info
    name = "John Doe"
    email = "johndoe@gmail.com"
    phone = "+1 123 456 7890"
    homepage = "https://johndoe.com"
    location = "New York, USA"

    # Social Media
    github = "johndoe"
    linkedin = "johndoe"
    twitter = "johndoe"
    facebook = "johndoe"
    instagram = "johndoe"
    youtube = "johndoe"
    medium = "johndoe"

    # Select Theme
    theme = "default"

    # Generate Readme
    profile = generate_profile(theme, name=name, email=email)
    print(profile)