##https://stackoverflow.com/questions/31265282/how-to-randomly-extract-fasta-sequences-using-python
from Bio import SeqIO
from random import sample
with open("../files/results.fsa") as f:
    seqs = SeqIO.parse(f, "fasta")
    samps = ((seq.name, seq.seq) for seq in sample(list(seqs),5000))
    for samp in samps:
        print(">{}\n{}".format(*samp))
