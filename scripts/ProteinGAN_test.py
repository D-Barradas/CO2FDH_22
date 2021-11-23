# Helper methods
import shutil

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

import numpy as np
import pandas as pd

import tensorflow as tf

# A mapping between amino acids ids and their corresponding letters
ID_TO_AMINO_ACID = {0: '0', 1: 'A', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'K', 10: 'L', 11: 'M', 12: 'N', 13: 'P', 14: 'Q', 15: 'R', 16: 'S', 17: 'T', 18: 'V', 19: 'W', 20: 'Y'}

def to_seqs(model_output):
  """Takes ProteinGAN output and returns list of generated protein sequences"""
  human_readable_seqs = []
  seqs = model_output["prediction"]
  for i in range(len(seqs)):
    human_readable_seq ="".join([ID_TO_AMINO_ACID[a] for a in seqs[i].numpy()])
    human_readable_seq = human_readable_seq.replace("0", "")
    human_readable_seqs.append(human_readable_seq)
  return human_readable_seqs

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

def append_to_fasta(path, seqs, prefix):
  """Appends new sequences to existing file in FASTA format."""
  fasta = ""
  for i, seq in enumerate(seqs):
    fasta += f">{prefix}_{i}\n{seq}\n"
  print(fasta, file=open(path, 'a'))

def interpolate(starting, ending, steps):
  """
  Interpolates between starting and end points. Steps parameter determines 
  how many interpolated points will be returned.
  """
  points = [starting]
  step = (ending-starting)/steps
  for i in range(steps):
    starting = starting + step
    points.append(starting)
  return np.asanyarray(points)


tf.random.set_seed(42)
from absl import logging
logging.set_verbosity("ERROR")
tf.get_logger().setLevel("ERROR")

# Loading pre-trained model.
model = tf.saved_model.load("../models/pre_trained_protein_gan/").signatures["serving_default"]

# Choosing random points from latent space.
noise = tf.random.truncated_normal([64, 128], stddev=0.5, dtype=tf.float32)

# Feeding noise to generator to get an output.
model_output = model(noise)

# Model returns indices of amino acids. Here we convert them to actual letters.
seqs = to_seqs(model_output)
print ( seqs[0] ) 

print (get_blast_results(seqs[0]))