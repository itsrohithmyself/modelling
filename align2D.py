from modeller import *
from modeller.automodel import *

env = environ()
aln = alignment(env)
mdl = model(env, file='7szs', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='7szs', atom_files='7szs.pdb')
aln.append(file='TARGET.ali', align_codes='TARGET')
aln.align2d()
aln.write(file='TARGET-7szs.ali', alignment_format='PIR')
aln.write(file='TARGET-7szs.pap', alignment_format='PAP')
