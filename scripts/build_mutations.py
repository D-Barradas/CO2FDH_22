import os 
try:
    from pymol import cmd
except:
    os.system("module load pymol")



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

print("total residues_second_shells:%i" %( len ( second_shell_residues)))
count_ala , count_gly = 0 ,0 
for x,y,z in second_shell_residues:
    if x == "ALA":
        count_ala +=1 
    elif x == "GLY":
        count_gly += 1 
print (f"GLY :{count_gly}, ALA:{count_ala}")