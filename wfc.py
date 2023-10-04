import random

class Model():
    def __init__(
        self,
        input_path: str = "./images/dungeon.png",
        output_dimensions: (int, int) = (512, 512),
        N: int = 16,
        input_periodic: bool = False,
        output_periodic: bool = False,
        symmetry: int = 1,
        ground: int = 0,
    ):
        """
        Args:
            input_path - input path to the sample image to generate WFC output from
            output_dimensions - how large in (x,y) the output image should be
            N - represents the width & height of the patterns that the overlap model breaks the input into
            input_periodic - represents whether the input pattern is tiling.
            output_periodic - determines if the output solutions are tilable
            symmetry - represents which additional symmetries of the input pattern are digested. 
                1 is just the original input, 2-8 adds mirrored and rotated variations.
            ground - when not 0, this assigns a pattern for the bottom row of the output.
        """
        self.input_path = input_path
        self.output_dimensions = output_dimensions
        self.N = N
        self.input_periodic = input_periodic
        self.output_periodic = output_periodic
        self.symmetry = symmetry
        self.ground = ground

    def generate(
        self,
        seed: int = 0,
        limit: int = 0,
    ):
        if (seed == 0):
            seed = random.randrange(0,1000000)
        print("Seed:", seed)
        # canvas = np.zeros()

wfc = Model()
wfc.generate()