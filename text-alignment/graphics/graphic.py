"""Module containing the base Graphic functionality."""


class Graphic:

    HEIGHT = 5

    def __init__(self, thickness, letter):
        self.thickness = thickness
        self.letter = letter

        self.pillar_height = thickness + 1
        self.pillar_length = thickness * 2
        self.total_length = thickness * 6
        self.string = self.letter * thickness

        self.half_pillar_height = self.pillar_height // 2
        self.pillar_thickness = self.string * self.HEIGHT

    def __str__(self):
        return "\n".join(self)

    def __len__(self):
        return len(self.parts)

    def __iter__(self):
        for part in self.parts.values():
            yield self.build_layers(*part)

    def build_layers(self, loop_length, layer) -> str:
        """Function that builds the part layers."""

        layers = []
        for _ in range(loop_length):
            layers.append(layer)

        body = "\n".join(layers)
        return body
