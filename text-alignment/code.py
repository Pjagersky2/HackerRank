"""Module containing LETTER alignment examples best for the letter H."""


class Graphic:

    LETTER = "H"

    def __init__(self, thickness):
        self.thickness = thickness

        self.pillar_height = thickness + 1
        self.pillar_length = thickness * 2
        self.total_length = thickness * 6
        self.string = self.LETTER * thickness

        self.parts = (
            self.top_cone(),
            self.top_pillars(),
            self.middle_belt(),
            self.bottom_pillars(),
            self.bottom_cone()
        )

    def __str__(self):
        return "\n".join(self)

    def __len__(self):
        return len(self.parts)

    def __iter__(self):
        for part in self.parts:
            yield part

    def top_cone(self):
        """Function that builds the top cone."""

        substring_length = self.thickness - 1

        layers = []
        for index in range(self.thickness):
            substring = self.LETTER * index
            prefix = substring.rjust(substring_length)
            suffix = substring.ljust(substring_length)

            layer = prefix + self.LETTER + suffix
            layers.append(layer)

        body = "\n".join(layers)

        return body

    def top_pillars(self):
        """Function that builds the top pillars."""

        layers = []
        for _ in range(self.pillar_height):
            left = self.string.center(self.pillar_length)
            right = self.string.center(self.total_length)

            layer = left + right
            layers.append(layer)

        body = "\n".join(layers)

        return body

    def middle_belt(self):
        """Function that builds the middle belt."""

        layers = []
        for _ in range(self.pillar_height // 2):
            string_width = self.string * 5

            layer = string_width.center(self.total_length)
            layers.append(layer)

        body = "\n".join(layers)

        return body

    def bottom_pillars(self):
        """Function that builds the bottom pillars."""

        layers = []
        for _ in range(self.pillar_height):
            left = self.string.center(self.pillar_length)
            right = self.string.center(self.total_length)

            layer = left + right
            layers.append(layer)

        body = "\n".join(layers)

        return body

    def bottom_cone(self):
        """Build the bottom cone."""

        layers = []
        for index in range(self.thickness):
            length = self.thickness - index - 1
            substring = self.LETTER * length

            prefix = substring.rjust(self.thickness)
            suffix = substring.ljust(self.thickness)
            string = prefix + self.LETTER + suffix

            layer = string.rjust(self.total_length)
            layers.append(layer)

        body = "\n".join(layers)

        return body


def main():
    """Run the main function."""

    thickness = int(input())
    graphic = Graphic(thickness)
    print(graphic)


if __name__ == "__main__":
    main()
