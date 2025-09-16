def sort(width, height, length, mass):
    volume = width * height * length
    bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    heavy = mass >= 20

    return "REJECTED" if bulky and heavy else "SPECIAL" if bulky or heavy else "STANDARD"


if __name__ == "__main__":
    tests = [
        ((100, 100, 100, 10), "STANDARD"),

        ((200, 100, 50, 10), "SPECIAL"),

        ((100, 100, 100, 25), "SPECIAL"),

        ((200, 200, 200, 30), "REJECTED"),

        ((100, 100, 100, 19.9), "SPECIAL"),

        ((150, 50, 50, 10), "SPECIAL"),

        ((50, 50, 50, 20), "SPECIAL"),
    ]

    for args, expected in tests:
        result = sort(*args)
        print(f"sort{args} = {result} (expected {expected})")
