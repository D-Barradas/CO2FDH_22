#
# Rozaimi Razali <rozaimirazali@gmail.com>
#
# Modified by PhD. Student Mario Sergio Valdes Tresanco
# June 26 2018
#
# Modified by PhD Didier Barradas Bautista
# October 5 2021

from pymol import cmd

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
prot_list = [['6tg9', 'A']] # example [['1nzp', 'A'], ['4oxn', 'B']] # how many proteins do you want
# prot_list = [['1shr', 'B']] # example [['1nzp', 'A'], ['4oxn', 'B']] # how many proteins do you want
residues_list = [int(z) for x,y,z in second_shell_residues]
aminoacid = ['ALA','GLY' ] # only two


def mutate_this(prot, res ,num ):
    cmd.get_wizard().do_select("/obj_%s//%s/%d" % (num,prot[1], res))
    cmd.frame(1)
    cmd.get_wizard().apply()
    cmd.save(f"../files/mutant_{res}_{prot[1]}.pdb","obj_%s"%(num))

def mutate_all(prot, res ,num ):
    if res != "ALA":
        cmd.get_wizard().set_mode(aminoacid[0])
        cmd.get_wizard().do_select("/obj_%s//%s/%d" % (num,prot[1], res))
        cmd.frame(1)
        cmd.get_wizard().apply()
        cmd.save("../files/mutant_all_residues.pdb","obj_%s"%(num))
    else:
        cmd.get_wizard().set_mode(aminoacid[1])
        cmd.get_wizard().do_select("/obj_%s//%s/%d" % (num,prot[1], res))
        cmd.frame(1)
        cmd.get_wizard().apply()
        cmd.save("../files/mutant_all_residues.pdb","obj_%s"%(num)) 

for prot in prot_list:
    #Initialize
    # fetch protein by PDB code
    cmd.fetch(prot[0], async_=0)
    # mutagenesis mode
    cmd.wizard("mutagenesis")
    cmd.do("refresh_wizard")
    
    # create 7 object 
    for obj in range(len(second_shell_residues)):
        cmd.create('obj_%s' % obj, prot[0])
    # Mutate
    # cmd.get_wizard().set_mode(aminoacid)

    #for obj_1 (mutation in all residues) 
    for res in residues_list:  
        mutate_all(prot, res, num=1)
    # cmd.get_wizard().do_select("/obj_1//%s/%d" % (prot[1], residues_list[1]))
    # cmd.frame(1)
    # cmd.get_wizard().apply()
    # cmd.get_wizard().do_select("/obj_1//%s/%d" % (prot[1], residues_list[2]))
    # cmd.frame(1)
    # cmd.get_wizard().apply()
    # cmd.save("%s_%s_%s_%s_%s_x_%s.pdb" % (prot[0], prot[1], residues_list[0], residues_list[1], residues_list[2], aminoacid),'obj_1')
    
#    #for obj_2 (mutation in residue # 1 and 2)
#    cmd.get_wizard().do_select("/obj_2//%s/%d" % (prot[1], residues_list[0]))
#    cmd.frame(1)
#    cmd.get_wizard().apply()
#    cmd.get_wizard().do_select("/obj_2//%s/%d" % (prot[1], residues_list[1]))
#    cmd.frame(1)
#    cmd.get_wizard().apply()
#    cmd.save("%s_%s_%s_%s_x_%s.pdb" % (prot[0], prot[1], residues_list[0], residues_list[2], aminoacid),'obj_2')
#    
#    #for obj_3 (mutation in residue # 1 and 3)
#    cmd.get_wizard().do_select("/obj_3//%s/%d" % (prot[1], residues_list[0]))
#    cmd.frame(1)
#    cmd.get_wizard().apply()
#    cmd.get_wizard().do_select("/obj_3//%s/%d" % (prot[1], residues_list[2]))
#    cmd.frame(1)
#    cmd.get_wizard().apply()
#    cmd.save("%s_%s_%s_%s_x_%s.pdb" % (prot[0], prot[1], residues_list[0], residues_list[2], aminoacid),'obj_3')
#    
#    #for obj_4 (mutation in residue # 2 and 3)
#    cmd.get_wizard().do_select("/obj_4//%s/%d" % (prot[1], residues_list[1]))
#    cmd.frame(1)
#    cmd.get_wizard().apply()
#    cmd.get_wizard().do_select("/obj_4//%s/%d" % (prot[1], residues_list[2]))
#    cmd.frame(1)
#    cmd.get_wizard().apply()
#    cmd.save("%s_%s_%s_%s_x_%s.pdb" % (prot[0], prot[1], residues_list[1], residues_list[2], aminoacid),'obj_4')
#    
#    #for obj_5 (mutation in residue # 1)
#    cmd.get_wizard().do_select("/obj_5//%s/%d" % (prot[1], residues_list[0]))
#    cmd.frame(1)
#    cmd.get_wizard().apply()
#    cmd.save("%s_%s_%s_x_%s.pdb" % (prot[0], prot[1], residues_list[0], aminoacid),'obj_5')
#    #for obj_6 (mutation in residue # 2)
#    cmd.get_wizard().do_select("/obj_6//%s/%d" % (prot[1], residues_list[1]))
#    cmd.frame(1)
#    cmd.get_wizard().apply()
#    cmd.save("%s_%s_%s_x_%s.pdb" % (prot[0], prot[1], residues_list[1], aminoacid),'obj_6')
#    #for obj_7 (mutation in residue # 3)
#    cmd.get_wizard().do_select("/obj_7//%s/%d" % (prot[1], residues_list[2]))
#    cmd.frame(1)
#    cmd.get_wizard().apply()
#    cmd.save("%s_%s_%s_x_%s.pdb" % (prot[0], prot[1], residues_list[2], aminoacid),'obj_7')
#
#    # Done
#    cmd.set_wizard()
#    if len(prot_list) == 1:
#        continue
#    else:
#        cmd.reinitialize()  
#   
#