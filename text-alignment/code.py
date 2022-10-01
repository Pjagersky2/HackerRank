"""Module containing LETTER alignment examples best for the letter H."""

LETTER = "H"


def top_cone(thickness):
    """Function that builds the top cone."""

    substring_length = thickness - 1

    layers = []
    for index in range(thickness):
        substring = LETTER * index
        prefix = substring.rjust(substring_length)
        suffix = substring.ljust(substring_length)

        layer = prefix + LETTER + suffix
        layers.append(layer)

    body = "\n".join(layers)

    return body


def top_pillars(string, width, height, total_width):
    """Function that builds the top pillars."""

    layers = []
    for _ in range(height):
        left = string.center(width)
        right = string.center(total_width)

        layer = left + right
        layers.append(layer)

    body = "\n".join(layers)

    return body


def middle_belt(string, height, total_width):
    """Function that builds the middle belt."""

    layers = []
    for _ in range(height // 2):
        string_width = string * 5

        layer = string_width.center(total_width)
        layers.append(layer)

    body = "\n".join(layers)

    return body


def bottom_pillars(string, width, height, total_width):
    """Function that builds the bottom pillars."""

    layers = []
    for _ in range(height):
        left = string.center(width)
        right = string.center(total_width)

        layer = left + right
        layers.append(layer)

    body = "\n".join(layers)

    return body


def bottom_cone(thickness, total_length):
    """Build the bottom cone."""

    layers = []
    for index in range(thickness):
        length = thickness - index - 1
        substring = LETTER * length

        prefix = substring.rjust(thickness)
        suffix = substring.ljust(thickness)
        string = prefix + LETTER + suffix

        layer = string.rjust(total_length)
        layers.append(layer)

    body = "\n".join(layers)

    return body


def build(thickness):
    """Draw the letter."""

    pillar_height = thickness + 1
    pillar_length = thickness * 2
    total_length = thickness * 6
    string = LETTER * thickness

    body = "\n".join([
        top_cone(thickness),
        top_pillars(string, pillar_length, pillar_height, total_length),
        middle_belt(string, pillar_height, total_length),
        bottom_pillars(string, pillar_length, pillar_height, total_length),
        bottom_cone(thickness, total_length)
    ])

    return body


def main():
    """Run the main function."""

    thickness = int(input())


    result = build(thickness)

    print(result)


if __name__ == "__main__":
    main()
