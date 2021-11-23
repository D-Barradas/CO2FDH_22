import pandas as pd 
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

def get_blast_results(seq):
  """Takes a protein sequence, calls BLAST server and returns parsed results"""
  print("Calling BLAST server. This might take a while")
  r = NCBIWWW.qblast("blastp", "nr", seq, hitlist_size = 5, expect=0.5, 
                     word_size=6, matrix_name="BLOSUM62")
  blast_record = NCBIXML.read(r)

  to_df = []

  for a in blast_record.alignments:
    to_df.append({"name": a.hit_def,"identity": a.hsps[0].identities,
                  "subject": a.hsps[0].sbjct})

  return pd.DataFrame(to_df)

seq = [x for x in open("../files/6tg9_A.fasta","r")] 
print ("".join(seq))
seq2 = "".join(seq)
my_blast_results = get_blast_results(seq2)
print (my_blast_results.head())