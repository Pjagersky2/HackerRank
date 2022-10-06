"""Module containing LETTER alignment examples best for the letter H."""
from graphics.graphic import Graphic


class LetterH(Graphic):
    """Represent the letter H graphic."""

    LETTER = "H"

    def __init__(self, thickness):
        """Initialize Graphic type object."""

        super().__init__(thickness, self.LETTER)

        adjusted_height = self.half_pillar_height + 1
        left = self.string.center(self.pillar_length)
        right = self.string.center(self.total_length)
        outer_layer = left + right
        middle_layer = self.pillar_thickness.center(self.total_length)

        outer_part = adjusted_height, outer_layer
        middle_part = self.half_pillar_height, middle_layer

        self.parts = {
            "upper_top": outer_part,
            "upper_mid": outer_part,
            "middle": middle_part,
            "lower_mid": outer_part,
            "lower_bot": outer_part
        }


class LetterE(Graphic):
    """Represent the letter E graphic."""

    LETTER = "E"

    def __init__(self, thickness):
        """Initialize Graphic type object."""

        super().__init__(thickness, self.LETTER)

        four_fifths = ((self.HEIGHT * 4) // 5)
        middle_string = self.string * four_fifths
        outer_layer = self.pillar_thickness.center(self.total_length)
        inner_layer = self.string.center(self.pillar_length)

        total_width = len(self.pillar_thickness)
        string_width = middle_string.ljust(total_width)
        middle_layer = string_width.center(self.total_length)

        outer_parts = self.half_pillar_height, outer_layer
        inner_parts = self.pillar_height, inner_layer
        middle_part = self.half_pillar_height, middle_layer

        self.parts = {
            "upper_top": outer_parts,
            "upper_mid": inner_parts,
            "middle": middle_part,
            "lower_mid": inner_parts,
            "lower_bot": outer_parts
        }


class LetterI(Graphic):
    """Represent the letter I graphic."""

    LETTER = "I"

    def __init__(self, thickness):
        """Initialize Graphic type object."""

        super().__init__(thickness, self.LETTER)

        outer_layer = self.pillar_thickness.center(self.total_length)
        middle_layer = self.string.center(self.total_length)

        outer_part = self.half_pillar_height, outer_layer
        middle_part = self.half_pillar_height, middle_layer

        self.parts = {
            "upper_top": outer_part,
            "upper_mid": middle_part,
            "middle": middle_part,
            "lower_mid": middle_part,
            "lower_bot": outer_part
        }


class LetterL(Graphic):
    """Represent the letter L graphic."""

    LETTER = "L"

    def __init__(self, thickness):
        """Initialize Graphic type object."""

        super().__init__(thickness, self.LETTER)

        left_layer = self.string.center(self.pillar_length)
        bottom_layer = self.pillar_thickness.center(self.total_length)

        outer_part = self.half_pillar_height, left_layer
        bottom_part = self.half_pillar_height, bottom_layer

        self.parts = {
            "upper_top": outer_part,
            "upper_mid": outer_part,
            "middle": outer_part,
            "lower_mid": outer_part,
            "lower_bot": bottom_part
        }
