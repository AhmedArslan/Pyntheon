#!/usr/bin/env python
#
# Pyntheon; A resource for common lab specimens from virus to human
# to analyze their proteins for the presence of Posttranslational modifications (PTMs)
# in a large set of proteins of interest, also analyze the presence of mutations 
# overlap with the modified residues. 
# Besides this, Pyntheon also provides with curated PTMs data mapped to the other functional 
# regions like protein domains and structural regions, this indirect provides another layer 
# of functionality to the mutations that occur during the course of an experiement.


def unimap(fname, species, ptm=None, mutation=None):
	
	""" The UniMap is a first attempt to make a universal PTMS reprository to help users to 
	map PTMs to protein list and/or mutations to PTMs sites."""

	with open ('pyntheon-data.txt', 'w') as ac:
		if species in ('arbacia', 'ap'):
			fname2 = 'Arbacia+punctulata-PTMs.txt'
		elif species in ('branchiostoma', 'bf'):
			fname2 = 'Branchiostoma+floridae-PTMs.txt'
		elif species in ('celegans', 'ce'):
			fname2 = 'Caenorhabditis+elegans-functional_data.txt'
		elif species in ('ciona', 'ci'):
			fname2 = 'Ciona+intestinalis-PTMs.txt'
		elif species in ('daphnia', 'dm'):
			fname2 = 'Daphnia+magna-PTMs.txt'
		elif species in ('euprymna', 'es'):
			fname2 = 'Euprymna+scolopes-PTMs.txt'
		elif species in ('galleria', 'gm'):
			fname2 = 'Galleria+mellonella-PTMs.txt'
		elif species in ('gryllus', 'gb'):
			fname2 = 'Gryllus+bimaculatus-PTMs.txt'
		elif species in ('hydra', 'hy'):
			fname2 = 'Hydra-PTMs.txt'
		elif species in ('loligo', 'lp'):
			fname2 = 'Loligo+pealei-PTMs.txt'
		elif species in ('nematostella', 'nv'):
			fname2 = "Nematostella+vectensis-PTMs.txt"
		elif species in ('oikopleura', 'od'):
			fname2 = "Oikopleura+dioica-PTMs.txtx"
		elif species in ('platynereis', 'pd'):
			fname2 = 'Platynereis+dumerilii-PTMs.txt'
		elif species in ('pristionchus', 'pp'):
			fname2 = "Pristionchus+pacificus-PTMs.txt"
		elif species in ('schmidtea', 'sm'):
			fname2 = "Schmidtea+mediterranea-PTMs.txt"
		elif species in ('symsagittifera', 'sr'):
			fname2 = "Symsagittifera+roscoffensis-PTMs.txt"
		elif species in ('tribolium', 'tc'):
			fname2 = "Tribolium+castaneum-PTMs.txt"
		elif species in ('amphimedon', 'aq'):
			fname2 = "Amphimedon+queenslandica-PTMs.txt"
		elif species in ('aplysia', 'acc'):
			fname2 = "Aplysia-PTMs.txt"
		elif species in ('ecoli', 'ec'):
			fname2 = "Escherichia+coli-functional_data.txt"
		elif species in ('mycobacterium', 'mb'):
			fname2 = "Mycobacterium+tuberculosis-functional_data.txt"
		elif species in ('ashbya', 'ag'):
			fname2 = "Ashbya+gossypii.gff-PTMs.txt"
		elif species in ('Aspergillus+nidulans.gff-PTMs.txt', 'an'):
			fname2 = "Aspergillus+nidulans.gff-PTMs.txt"
		elif species in ('coprinus', 'cc'):
			fname2 = "Coprinus+cinereus-functional_data.txt"
		elif species in ("cryptococcus", 'cn'):
			fname2 = "Cryptococcus+neoformans.gff-PTMs.txt"
		elif species in ('neurospora', 'nc'):
			fname2 = "Neurospora+crassa-PTMs.txt"
		elif species in ('schizophyllum', 'sc'):
			fname2 = "Schizophyllum+commune.gff-PTMs.txt"
		elif species in ('schizosaccharomyces','sp'):
			fname2 = "Schizosaccharomyces+pombe.gff-PTMs.txt"
		elif species in ('ustilago', 'um'):
			fname2 = "Ustilago+maydis-PTMs.txt"
		elif species in ('scerevisiae', 'sce'):
			fname2 = "yeast-functional_data.txt"
		elif species in ('herpes', 'hsv'):
			fname2 = "Herpes+simplex+virus-PTMs.txt"
		elif species in ('plambda', 'pl'):
			fname2 = "Phage+lambda-PTMs.txt"
		elif species in ('Phi_X_174', 'px'):
			fname2 = "Phi+X+174-PTMs.txt"
		elif species in ('sv40', 'sv'):
			fname2 = "SV40-PTMs.txt"
		elif species in ('T4phage', 't4'):
			fname2 = "T4+phage-PTMs.txt"
		elif species in ('tmvirus', 'tmv'):
			fname2 = 'Tobacco+mosaic+virus-PTMs.txt'
		elif species in ('chlamydomonas', 'cr'):
			fname2 = "Chlamydomonas+reinhardtii.gff-PTMs.txt"
		elif species in ('dictyostelium', 'dd'):
			fname2 = "Dictyostelium+discoideum.gff-PTMs.txt"
		elif species in ('emiliania', 'eh'):
			fname2 = "Emiliania+huxleyi.gff-PTMs.txt"
		elif species in ('tetrahymena', 'tt'):
			fname2 = "Tetrahymena+thermophila.gff-PTMs.txt"
		elif species in ('thalassiosira', 'tp'):
			fname2 = "Thalassiosira+pseudonana.gff-PTMs.txt"
		elif species in ('aliivibrio', 'af'):
			fname2 = "uniprot-Aliivibrio+fischeri.gff-PTMs.txt"
		elif species in ('bacillus', 'bs'):
			fname2 = "uniprot-Bacillus+subtilis.gff-PTMs.txt"
		elif species in ('caulobacter', 'cac'):
			fname2 = "uniprot-Caulobacter+crescentus.gff-PTMs.txt"
		elif species in ('pseudomonas', 'pf'):
			fname2 = "uniprot-Pseudomonas+fluorescens.gff-PTMs.txt"
		elif species in ('synechocystis', 'sy'):
			fname2 = "uniprot-Synechocystis.gff-PTMs.txt"
		elif species in ('mycoplasma', 'mg'):
			fname2 = "uniprot-Mycoplasma+genitalium.gff-PTMs.txt"
		elif species in ('arabidopsis', 'at'):
			fname2 = "arabidopsis+thaliana-functional_data.txt"
		elif species in ('brachypodium', 'bd'):
			fname2 = "Brachypodium+distachyon.gff-PTMs.txt"
		elif species in ('lemna', 'lg'):
			fname2 = "Lemna+gibba.gff-PTMs.txt"
		elif species in ('lotus', 'lj'):
			fname2 = "Lotus+japonicus.gff-PTMs.txt"
		elif species in ('medicago', 'mt'):
			fname2 = "Medicago+truncatula.gff-PTMs.txt"
		elif species in ('mimulus', 'mig'):
			fname2 = "Mimulus+guttatus.gff-PTMs.txt"
		elif species in ('nicotiana', 'nb'):
			fname2 = "Nicotiana+benthamiana.gff-PTMs.txt"
		elif species in ('oryza', 'os'):
			fname2 = "Oryza+sativa.gffPTMs.txt"
		elif species in ('physcomitrella', 'php'):
			fname2 = "Physcomitrella+patens.gff-PTMs.txt"
		elif species in ('populus', 'pt'):
			fname2 = "Populus+trichocarpa.gff-PTMs.txt"
		elif species in ('selaginella', 'sem'):
			fname2 = "Selaginella+moellendorffii.gff-PTMs.txt"
		elif species in ('setaria', 'sev'):
			fname2 = "Setaria+viridis.gff-PTMs.txt"
		elif species in ('tobacco', 'tb'):
			fname2 = "Tobacco+BY-2+cells.gff-PTMs.txt"
		elif species in ('zea', 'zm'):
			fname2 = "Zea+mays.gff-PTMs.txt"
		elif species in ('anolis', 'ac'):
			fname2 = "Anolis+carolinensis.gffPTMs.txt"
		elif species in ('bombina', 'bm'):
			fname2 = "Bombina+maxima.gff-PTMs.txt"
		elif species in ('bombina', 'bo'):
			fname2 = "Bombina+orientalis.gff-PTMs.txt"
		elif species in ('canis', 'cl'):
			fname2 = "Canis+lupus.gff-PTMs.txt"
		elif species in ('cavia', 'cp'):
			fname2 = "Cavia+porcellus.gff-PTMs.txt"
		elif species in ('columba', 'cld'):
			fname2 = "Columba+livia+domestica.gff-PTMs.txt"
		elif species in ("drosophila", 'do'):
			fname2 = "drosophila-functional_data.txt"
		elif species in ('felis', 'fc'):
			fname2 = "Felis+catus.gff-PTMs.txt"
		elif species in ('gallus', 'gg'):
			fname2 = "Gallus+gallus.gff-PTMs.txt"
		elif species in ('gasterosteus', 'ga'):
			fname2 = "Gasterosteus+aculeatus.gff-PTMs.txt"
		elif species in ('heterocephalus', 'hg'):
			fname2 = "Heterocephalus+glaber.gff-PTMs.txt"
		elif species in ('hsapiens', 'hs'):
			fname2 = "human-functional_data.txt"
		elif species in ('mesocricetus', 'ma'):
			fname2 = "Mesocricetus+auratus.gff-PTMs.txt"
		elif species in ('mus', 'mus'):
			fname2 = "Mus+musculus.gff-PTMs.txt"
		elif species in ('myotis', 'ml'):
			fname2 = "Myotis+lucifugus.gff-PTMs.txt"
		elif species in ('oryzias', 'ol'):
			fname2 = "Oryzias+latipes.gff-PTMs.txt"
		elif species in ('petromyzon', 'pem'):
			fname2 = "Petromyzon+marinus.gff-PTMs.txt"
		elif species in ("poecilia", "pr"):
			fname2 = "Poecilia+reticulata-PTMs.txt"
		elif species in ('rattus', 'rn'):
			fname2 = "Rattus+norvegicus.gff-PTMs.txt"
		elif species in ('rhesus', 'rm'):
			fname2 = "Rhesus+macaque.gff-PTMs.txt"
		elif species in ('sigmodon', 'sh'):
			fname2 = "Sigmodon+hispidus.gff-PTMs.txt"
		elif species in ('takifugu', 'tr'):
			fname2 = "Takifugu+rubripes.gff-PTMs.txt"
		elif species in ('xenopus', 'xl'):
			fname2 = "Xenopus+laevis.gff-PTMs.txt"
		elif species in ('xenopust', 'xt'):
			fname2 = "Xenopus+tropicalis.gff-PTMs.txt"
		elif species in ('zebra', 'zf'):
			fname2 = "Zebra+finch.gff-PTMs.txt"
		else:
			raise ValueError("species name does not exits")
		with  open(fname2,'rU') as pm:
			for line in pm:
				line = line.split()
				with open(fname, 'rU') as user:
					for e in user:
						e = e.split()
						if ptm:
							if e[0] == line[0]:
								with open ('pyntheon-data.txt', 'a') as ac:
									ac.write("\t".join(line)+'\n')
						elif mutation:
							if e[0] == line[0] and e[1] == line[1]:
								with open ('pyntheon-mutation-data.txt', 'a') as ac:
									ac.write("\t".join(line)+'\n')
									pass
							elif e[0] == line[0] and e[1] == line[2]:
								with open ('pyntheon-mutation-data.txt', 'a+') as ac:
									ac.write("\t".join(line)+'\n')
						else:
							return "data not found"

def pyn():
	unimap(input("fname"), input("species"), input("ptm"), input ("mutaton"))
		
if __name__ == "__main__":

	import argparse

	parser = argparse.ArgumentParser()

	parser.add_argument("-f", "--fname", help= 'A text file needed for proper mapping of protein PTMS')
	parser.add_argument("-s", "--species", help= 'A proper species name needed, mapping of protein PTMS; see README')
	parser.add_argument("-m", "--mutation", help= 'mutation=True if PTMs sites also desired to be mapped on mutation sites; see README')
	parser.add_argument("-p", "--ptm", help='ptm=True if proteins PTMs sites present in functional regions desired to be mapped on mutation sites')

	args = parser.parse_args()
	
	try:
		unimap(args.fname, args.species, args.ptm, args.mutation)
	except IOError:
		print(parser.usage)
		exit(0)

