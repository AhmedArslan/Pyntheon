# Pyntheon

we are presenting, Universal Functional PTMs Mapping Tool (Pyntheon) which maps post translational modifications (PTMs) present in the functional regions of proteins of almost all lab specimens that are popular among research community. From viruses to human, this tool includes 87 species (see below) can help mapping the mutations to PTMS sites or just to give information about the PTMs present for a list of proteins of interest. 

# Usage

# install via pip

sudo install pyntheon -d /dir/where/to/install

cd /dir/pyntheon

sudo python setup.py install

cd /dir/pyntheon/pyntheon

$pyntheon

fname “/gives/name/of/file/“

species “species-id”

ptm True/False

mutaton False/True

# Usage (source-code)

cd /dir/pyntheon

$python pyntheon.py -f test1.txt -s hs -p TRUE

$python pyntheon.py -f test1.txt -s hs -m TRUE

# Parameter description

-f 				A user input text file, with proteins list (parameter = ptm)or tab separated proteins lists with mutation sites (parameter = mutation)

-s			specify the species of interest for which a user has a proteins lists (see species_id.txt)

-p 				This parameter take in the proteins lists file and gives all the PTMs present in different functional regions for a particular protein present in the list.

-m			This parameter take in the proteins lists file with mutations in a tab separated format and  gives all the PTMs positions which overlaps with mutations along side with information about the functional regions where these mapped PTMs are present.
