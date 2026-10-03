def unpack_profile(profile):
    name, age, hobbies = profile
    first, second = hobbies
    return f"{name} ({age}) likes {first} and {second}"
