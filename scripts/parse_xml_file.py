#parse xml file to get the protein name, hit_def, hit_acc, e-value
#!/usr/bin/env python3
import xml.etree.ElementTree as ET
my_file = open("/Users/barradd/Documents/BARRADD_Things/CO2FDH_22/files/blast_output.xml", "r")
## <Hit_id> tag for hit ID
## <Hit_accession> tag for hit accession
## <Hsp_qseq> tag for the query sequence
## <Hsp_hseq> tag for the hit sequence
## <Hsp_identity> tag for the identity
## <Hit_def> tag for the hit definition
## <Hsp_bit-score> tag for the bit score
## <Hsp_evalue> tag for the e-value

tree = ET.parse(my_file)
root = tree.getroot()


for child in root:
    for subchild in child:
        print(subchild.tag, subchild.attrib)


out_file = open("/Users/barradd/Documents/BARRADD_Things/CO2FDH_22/files/blast_output_seq.fsa","w")
for hit_id, hit_sequence in zip ( root.iter('Hit_id'), root.iter('Hsp_hseq')):
    out_file.write(">{hit_id.text}\n{hit_sequence.text}\n".format(**locals()))
    # print(hit_sequence.text)]
out_file.close()

desc_file = open("/Users/barradd/Documents/BARRADD_Things/CO2FDH_22/files/blast_output_desc.csv","w")
desc_file.write("Accesion,Length,Hit_identity,Hit_score,E-value,Definition,EC number\n")
for accession,hit_len,identity,bit_score,evalue,definition in zip ( root.iter('Hit_accession'), root.iter('Hit_len'),root.iter('Hsp_identity'), root.iter('Hsp_bit-score'), root.iter('Hsp_evalue'), root.iter('Hit_def')):
    desc_file.write("{accession.text},{hit_len.text},{identity.text},{bit_score.text},{evalue.text},{definition.text},1.17.1.9\n".format(**locals()))
    # print(hit_sequence.text)]
desc_file.close()