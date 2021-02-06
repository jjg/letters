import sys

# Get command line arguments
# TODO: Add more arguments (output dir, font, etc.)
if len(sys.argv) < 2:
    print("Usage: lettergen.py <footprint in mm> <handle length in mm>")
else:

    footprint = sys.argv[1]
    handle = sys.argv[2]

    # Iterate over all letters in the alphabet
    for letter_int in range(65,91):
        letter_char = str(chr(letter_int))
        print(f"Generating: {letter_char}")

        # Render OpenSCAD code
        letter_openscad = f"""
cube([{footprint}, {footprint}, {handle}]);
translate([0.5, 0.5, {handle}]){{
    linear_extrude(5){{
        text("{letter_char}", size={footprint});
    }}
}}
"""

        # Write letter file
        with open(f"{letter_char}_{footprint}_mm.scad", "w") as f:
            f.write(letter_openscad)

        # TODO: Use openscad command line to render and export STL
