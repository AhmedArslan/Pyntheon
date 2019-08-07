# Pyntheon

we are presenting, Universal Functional PTMs Mapping Tool (Pyntheon) which maps post translational modifications (PTMs) present in the functional regions of proteins of almost all lab specimens that are popular among research community. From viruses to human, this tool includes 87 species (see species_id.txt) can help mapping the mutations to PTMs sites or give information about the PTMs present for a list of proteins (UniProt ID) of interest. 

# Usage

# install

via pip3 

$ pip3 install -t /path/to/dir/ pyntheon

$ cd /dir/pyntheon

$ sudo python setup.py install

OR via git

$ git clone https://github.com/AhmedArslan/Pyntheon 

$ cd /dir/pyntheon/pyntheon

# run via commendline

$ pyntheon

fname “/gives/name/of/file/“

species “species-id” (see file: species_id.txt)

ptm True/False

mutation False/True

# run via source-code

$python /path/to/pyntheon.py -f uniprot-ids.txt -s hs -p TRUE

$python /path/to/pyntheon.py -f uniprot-id&mutation-aa-positions.txt -s hs -m TRUE

# Parameter description

-f 				A user input tab-separated-text file, with proteins list (parameter = ptm)or tab separated proteins lists with mutation sites (parameter = mutation)

-s			specify the species of interest for which a user has a proteins lists (see species_id.txt)

-p 				This parameter take in the proteins lists file and gives all the PTMs present in different functional regions for a particular protein present in the list.

-m			This parameter take in the proteins lists file with mutations in a tab separated format and  gives all the PTMs positions which overlaps with mutations along side with information about the functional regions where these mapped PTMs are present.

# output

pyntheon-data.txt / pyntheon-mutation-data.txt (depending on the commend)

# Cite
if you like this tool please cite:
