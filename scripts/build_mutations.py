from pymol import cmd
from pymol.selecting import select

def get_unique_residues_numbers():
    """
    A quick pdb file parser to obtain 
    unique sequence of residues in a list mode

    Returns:
        final_list: a list wit unique values, separated by the split
    """
    my_list_residues = [] 
    for x in open(file="../files/6tg9_second_shell.pdb"):
        residue , chain, number = x[17:20],x[21:22],x[22:26]
        if chain == "A":
            dummy = f"{residue}_{chain}_{number}"
            if dummy not in my_list_residues:
                my_list_residues.append(dummy)
            # print (residue , chain, number)
    final_list = [y.split("_") for y in my_list_residues]
    return final_list

second_shell_residues = get_unique_residues_numbers()

print (second_shell_residues)
## load the file and select the chain to change
cmd.load(filename="../files/6tg9.cif")
cmd.select(name="ChainA",selection="c. A")

## enable mutagenesis
cmd.wizard("mutagenesis")
cmd.do("refresh_wizard")
