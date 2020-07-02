---
title: 'Pyntheon: A Functional Analysis Framework for Protein Modifications and Mutations of 83 Model Organisms'
tags:
- python
- Posttranslational modifications (PTMs)
- cell
- computational biology
authors: 
- name: Ahmed Arslan
orcid: https://orcid.org/0000-0002-5325-6558
date: 01 July 2020
bibliography: paper.bib

---
# Summary

Posttranslational modifications (PTMs) modulate proteins activity depending on the dynamics of cellular conditions, in the highly regulated processes that control the reversible nature of these modifications and a cellular state. Due to the unique importance of PTMs, a number of resources are available to analyze the protein modification data for different organisms. These databases are quite informative on a limited number of popular organisms, mostly human and yeast. However there has not been a single database to date that makes it possible to analyze the modified protein residue data for up to 83 model organisms. Moreover, there are limited resources that rely on both protein mutations and modifications in evaluating a phenotype.
I am presenting a comprehensive python tool Pyntheon that enables users to analyze protein modifications and mutations data. This resource can be used in different ways to know: (i) if the proteins of interest have modifications and (ii) if the modified residues overlap with mutated sites. Additional functions include, analyzing if a PTM-site is present in a functional protein region, like domain and structural regions. In summary, Pyntheon makes it possible for a larger community of researchers to evaluate their curated proteomics data and interpret the impact of mutations on phenotypes. Pyntheon has multifold functions that can help analyzing the protein mutations impact on the modified residues for a large number of popular model organisms.

# Examples 

The two following examples show the utility and robustness of Pyntheon. In the first case, I retrieved protein mutation data on human cancers from COSMIC database (Forbes et al 2014). I selected 262,013 non-redundant pathogenic amino-acid alterations present in 7,574 proteins from different tumors (see supplementary information). With a simple one-line command (A) I mapped all the tumor-associated mutational data to human PTMs data and conveniently observed (i) how many proteins that are known in human tumors are modified and (ii) how many of these protein mutation positions overlap with the modified residues. 

$ python3 pyntheon.py -f file.txt -s hs -m TRUE ...... (A) 

Out of the tumor genes analyzed, 746 proteins have different types of modifications, with phosphorylation being the most abundant. That is not surprising, as compromised cellular signaling is a hallmark of cancer cells (Sever R. et al 2015). In addition, a total of 231 mutations fall in the protein domains of 137 tumor proteins. Overall, a large number of proteins are modified at multiple residues in this data set; also, many proteins suffer from the modified residue mutations. If further explored, this dataset can aid in distinguishing and interpreting a specific type of tumor with a specific repertoire of PTM-mutational load. 
In the second case, I performed Pyntheon analyses on proteins that are linked to plant Arabidopsis thaliana disease/stress resistance (Haung et al 2010). The use of a Pyntheon command (B) showed that proteins that are associated to the plant resistance are modified at different residues and that these modifications have a potential role to play in the resistance (see supplementary data). 

$ python3 pyntheon.py –f file.txt –s at -p TRUE...... (B) 

These examples show the potential of Pyntheon in evaluating the involvement of protein functional features in a phenotype, in addition to the robustness of it in performing such analyses for a large number of species. For an explanation of the commands used, the data, and the presented in these examples, see the Code-Availability. 

# Conclusion 

The development of such a comprehensive tool will generate interest in analysis of mutational overload impacting the PTMs present in a large number of species. The ease of use for the analyses of large experimental datasets will accelerate the understanding and interpretation of PTM functions-dependent biological systems. I believe, Pyntheon will help the larger scientific community study PTMs in different species. 
In future development, I am aiming to implement Pyntheon in R and in an HTML-based user interface, to further facilitate users. 
