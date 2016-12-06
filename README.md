# Pyntheon

The post-translational modifications are the centre of functional gravity when it comes to protein structure and functional outcomes. With the exponential advancement of high through put data generating machine, Terabytes of data being generated on daily bases. Where data generation is getting easy and precise day by day where data analysis and interpretation reached new levels of complexity. In addition, functional annotation of PTMs is not a separate topic. around 400 PTMs have been discovered and very few have been analysed for their functional importance in the cell. The online tools like PTMCode and PTMfunc are contributing their share for reducing the work labor as these resources have complied PTMs data into functional and structural regions. But the need if to have recourse that can facilitates the bigger community of researchers. The researchers from all life sciences research fields wants to take advantage of PTMs can take advantage of the resource/tool. 
we are presenting here a tool, Universal Functional PTMs Mapping Tool (Pyntheon) which maps PTMs present in the functional regions of proteins of almost lab specimens that are very popular among research community conducting research in lab. From viruses to human, this tool includes 85 species (see below) can help mapping the mutations to PTMS sites or just to give information about the PTMs present in the genelist. 

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

-s			specify the species of interest for which a user has a proteins lists (see below)

-p 				This parameter take in the proteins lists file and gives all the PTMs present in different functional regions for a particular protein present in the list.

-m			This parameter take in the proteins lists file with mutations in a tab separated format and  gives all the PTMs positions which overlaps with mutations along side with information about the functional regions where these mapped PTMs are present.


# Species ID

Species name 						           -species

Amphimedon queenslandica 				   aq

Anolis carolinensis 					       ac
 
Aplysia californica					        acc

Arabidopsis thaliana 					at

Arbacia punctulata					ap

Ashbya gossypii						ag

Aspergillus nidulans					an

Bombina maxima						bm 

Bombina orientalis					bo

Brachypodium distachyon				bd 

Branchiostoma floridae  				bf

Caenorhabditis elegans 				ce

Canis lupus						cl
   
Cavia porcellus  					cp
   
Chlamydomonas reinhardtii  				cr
   
Ciona intestinalis  					ci
   
Columba livia domestica 				cld  
   		
Coprinus cinereus  					cc 
   
Cryptococcus neoformans  				cn
   
Daphnia magna  						dm 
   
Dictyostelium discoideum  				dd 
   
Drosophila melanogaster				do 
   
Emiliania huxleyi  					eh 
   
Escherichia coli 					ec  
   
Euprymna scolopes  					es 
   
Felis catus						fc   
   
Galleria mellonella 					gm
   
Gallus gallus  						gg
   
Gasterosteus aculeatus  				ga
   
Gryllus bimaculatus 					gb 
   
Herpes simplex virus  					hsv
  
Heterocephalus glaber  				hg 
   
homo sapien						hs  
   
Hydra  							hy 
   
Lemna gibba 						lg  
   
Loligo pealei  						lp 
   
Lotus japonicus  					lj 
   
Medicago truncatula  					mt 
   
Mesocricetus auratus  					ma 
   
Mimulus guttatus  					mij 
   
Mus musculus  						mus 
   
Mycobacterium tuberculosis 				mb 
   
Myotis lucifugus  					ml 
   
Nematostella vectensis 				nv  
   
Neurospora crassa  					nc 
   
Nicotiana benthamiana  				nb 
   
Oikopleura dioica 					od  
  
Oryza sativa						os 
   
Oryzias latipes 					ol  
   
Petromyzon marinus  					pem 
   
Phage lambda 						pl  
   
Phi X 174						px   
   
Physcomitrella patens 					php  
   
Platynereis dumerilii 					pd  
   
Poecilia reticulata 					pr 

Populus trichocarpa 					pt
   
Pristionchus pacificus  				pp 
   
Rattus norvegicus  					rn 
   
Rhesus macaque  					rm 
   
Schizophyllum commune  				sc 
   
Schizosaccharomyces pombe 				sp  
   
Schmidtea mediterranea  				sm 
   
Selaginella moellendorffii  				sem 
   
Setaria viridis  					sev 
   
Sigmodon hispidus 					sh  
   
SV40 							sv  
   
Symsagittifera roscoffensis  				sr 

T4 phage 						t4  
   
Takifugu rubripes  					tr 
   
Tetrahymena thermophila  				tt 
   
Thalassiosira pseudonana 				tp  
   
Tobacco BY-2 cells 					tb  
(Nicotiana tabacum)  
Tobacco mosaic virus 					tmv  
   
Tribolium castaneum 					tc  

Aliivibrio fischeri 					af   
   
Bacillus subtilis  					bs 
   
Caulobacter crescentus  				cac 
   
Mycoplasma genitalium 					mg  
   
Pseudomonas fluorescens 				pf  
   
Synechocystis  						sy 
   
Ustilago maydis  					um 
   
Xenopus laevis  					xl 
   
Xenopus tropicalis 					xt  
   
saccharomyces cerevisiae				sce 
   
Zea mays 						zm 
   
Zebra finch  						zf
