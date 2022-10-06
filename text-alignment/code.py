"""Module containing letter graphic representations."""
import graphics.letters


def main():
    """Run the main function."""

    thickness = int(input())
    letters = (
        graphics.letters.LetterE(thickness),
        graphics.letters.LetterH(thickness),
        graphics.letters.LetterL(thickness),
        graphics.letters.LetterI(thickness)
    )
    print("\n\n".join([str(letter) for letter in letters]))


if __name__ == "__main__":
    main()
