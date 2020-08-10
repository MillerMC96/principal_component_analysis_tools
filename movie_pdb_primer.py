import numpy as np
import sys
import os
from pymol import cmd
from modes import get_xvg_stats
from generate_probability import generate_color_profile

if __name__ == "__main__":
    # xvg file that has the trajectory information
    xvgfile = sys.argv[1]
    # probability mode
    mode = int(sys.argv[2])
    # input pdb name
    input_pdb = sys.argv[3]
    # pdb name without the pdb extension
    input_pdb_name = os.path.splitext(input_pdb)[0]
    # output pdb name
    movie_primer_pdb = sys.argv[4]

    # load pdb into pymol
    cmd.load(input_pdb)

    color_profile = generate_color_profile(xvgfile, mode)
    for i in range(len(color_profile)):
        color = color_profile[i]
        # change the b factors of input pdb here
        cmd.alter("%s and index %s and n. CA"%(input_pdb_name, i), "b=%s"%color)

    # save the primer pdb here
    cmd.save(movie_primer_pdb)