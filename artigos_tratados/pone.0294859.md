<!-- image -->

<!-- image -->

## OPENACCESS

Citation: McGill CJ, Ewald CY, Benayoun BA (2023) Sex-dimorphic expression of extracellular matrix genes in mouse bone marrow neutrophils. PLoS ONE 18(11): e0294859. https://doi.org/ 10.1371/journal.pone.0294859

Editor: Syed M. Faisal, University of Michigan Medical School, UNITED STATES

Received: May 31, 2023

Accepted:

November 8, 2023

Published: November 30, 2023

Peer Review History: PLOS recognizes the benefits of transparency in the peer review process; therefore, we enable the publication of all of the content of peer review and author responses alongside final, published articles. The editorial history of this article is available here: https://doi.org/10.1371/journal.pone.0294859

Copyright: © 2023 McGill et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Data Availability Statement: The bulk RNA-seq data was previously described in Lu et al., 2021 [11], and sequencing data is accessible through BioProject PRJNA630663 (https://www.ncbi.nlm. nih.gov/sra?LinkName=bioproject\_sra\_all&amp;from\_

## RESEARCHARTICLE

## Sex-dimorphic expression of extracellular matrix genes in mouse bone marrow neutrophils

Cassandra J. McGillID , Collin Y. EwaldID 1 2 * , Bere ' nice A. BenayounID ' 1,3,4,5,6 *

1 Leonard Davis School of Gerontology, University of Southern California, Los Angeles, California, United States of America, 2 Laboratory of Extracellular Matrix Regeneration, Department of Health Sciences and Technology, Institute of Translational Medicine, Swiss Federal Institute of Technology (ETH Zurich), Schwerzenbach, Switzerland, 3 Molecular and Computational Biology Department, USC Dornsife College of Letters, Arts and Sciences, Los Angeles, California, United States of America, 4 Biochemistry and Molecular Medicine Department, USC Keck School of Medicine, Los Angeles, California, United States of America, 5 USCNorris Comprehensive Cancer Center, Epigenetics and Gene Regulation, Los Angeles, California, United States of America, 6 USCStemCell Initiative, Los Angeles, California, United States of America

- * berenice.benayoun@usc.edu (BAB); collin-ewald@ethz.ch (CYE)

## Abstract

The mammalian innate immune system is sex-dimorphic. Neutrophils are the most abundant leukocyte in humans and represent innate immunity's first line of defense. We previously found that primary mouse bone marrow neutrophils show widespread sex-dimorphism throughout life, including at the transcriptional level. Extracellular matrix [ECM]-related terms were observed among the top sex-dimorphic genes. Since the ECM is emerging as an important regulator of innate immune responses, we sought to further investigate the transcriptomic profile of primary mouse bone marrow neutrophils at both the bulk and single-cell level to understand how biological sex may influence ECM component expression in neutrophils throughout life. Here, using curated gene lists of ECM components and unbiased weighted gene co-expression network analysis [WGCNA], we find that multiple ECMrelated gene sets show widespread female-bias in expression in primary mouse neutrophils. Since many immune-related diseases ( e g . ., rheumatoid arthritis) are more prevalent in females, our work may provide insights into the pathogenesis of sex-dimorphic inflammatory diseases.

## Introduction

Accumulating evidence shows that, even outside of reproductive organs, mammalian biology is very sex-dimorphic [1]. Indeed, the mammalian immune system shows broad differences between males vs. females, including aspects of innate and adaptive immune responses [2-4]. Generally, a more robust immune response is observed in females, which may underlie a higher auto-immunity risk, whereas an increased susceptibility to infection and a worse response to sepsis is found in males [2].

Neutrophils are the most abundant white blood cell type in human blood, representing 5070% of leukocytes in humans throughout life [5]. They are a type of 'granulocytes', produced

uid=630663). The processed normalized count table and DEseq2 result tables were obtained from Github (https://github.com/BenayounLaboratory/ Neutrophil\_Omics\_2020). The single-cell RNA-seq data was previously described in Kim et al., 2022 [12], and raw sequencing data is accessible through BioProject PRJNA796634 (https://www. ncbi.nlm.nih.gov/sra?LinkName=bioproject\_sra\_ all&amp;from\_uid=796634). The processed annotated Seurat file was obtained from Figshare (https://doi. org/10.6084/m9.figshare.19623978). The serum proteomics dataset was previously described in Aumailley et al, 2021 [22], and the processed protein expression matrix was obtained from the online Table S2 for the article (https://pubs.acs.org/ doi/suppl/10.1021/acs.jproteome.1c00542/suppl\_ file/pr1c00542\_si\_006.xlsx).

Funding: This work was supported by National Institute of Aging [https://www.nia.nih.gov/] T32 AG052374 predoctoral fellowship to C.J.M., by the Swiss National Science Foundation [https://www. snf.ch/en] from the SNF P3 Project 190072 to CYE, National Institute of Aging [https://www.nia.nih. gov/] R01 AG076433 to B.A.B. and Pew Biomedical Scholar award #00034120 from the Pew Charitable Trust [https://www.pewtrusts.org/] to B.A.B. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

Competing interests: The authors have declared that no competing interests exist.

in the bone marrow and released into circulation for immune surveillance, representing a first line-of-defense against infections [6, 7]. Neutrophils perform key immune functions, including the production/release of antimicrobial granules and of 'Neutrophil Extracellular Traps' (NETs) [6, 8], composed of extruded chromatin, proteases, and antimicrobial peptides. While neutrophils defend against infections, their aberrant activation aggravates pathological inflammation [6, 7, 9]. They can also drive inflammatory disease, leading to tissue damage [8, 10].

Recent work by our group revealed widespread sex-dimorphism in the transcriptome of primary murine bone marrow neutrophils throughout life (4 to 20 months of age) [11]. Consistently, transcriptomic data by the ImmGen Consortium showed clear differences between the neutrophils of young prepubertal female vs . male mice (6 weeks of age) [4]. Importantly, we also recently reported that sex-differences in primary bone marrow neutrophils are found at every stage of underlying heterogeneity using single-cell RNA-seq [12]. In our previous analyses of primary neutrophil transcriptomes, Gene Ontology [GO] terms related to collagen synthesis and extracellular matrix (ECM) biology were observed in the top listed GO terms with significant sex-dimorphic gene expression at the bulk RNA-seq level [11]. Furthermore, beyond the transcriptional level, accumulating evidence supports the idea that the functional landscape of neutrophils differs between sexes throughout life, with male-bias in the production of primary granule protein neutrophil elastase (ELANE) [11], a serine protease that can break down elastin and collagens [13], potentially remodels the ECM.

Intriguingly, ECM components are emerging as potent regulatory mediators of innate immune responses [14]. The importance of the extracellular matrix in neutrophil recruitment and function is becoming more evident based on recent studies [15]. Indeed, recent work suggests that neutrophils can transport ECM components to wound sites to help promote healing [16]. Although the production of ECM components by neutrophils themselves has not been explored in depth, emerging evidence suggests that the synthesis of 'emergency' ECM containing fibronectins by neutrophils plays an important role in promoting fracture healing [17]. However, sex-differences in the regulation of ECM biology by neutrophils remain poorly understood.

To follow-up on this observation of sex-dimorphism in ECM gene expression, we reanalyze transcriptomic data from primary mouse bone marrow neutrophils to help understand how biological sex may influence ECM component gene expression. Using expert-curated ECM gene sets, we confirm broad female-bias in the expression of genes related to ECM components and remodeling in young and old female neutrophils in our bulk RNA-seq dataset. To gain a more granular view and determine any underlying heterogeneity of ECM expression of young mice's neutrophils, we recently generated a single cell RNA-seq data and find again a female-specific enrichment for ECM. In addition, using unbiased weighted gene co-expression network analysis (WGCNA), we identify significant sex-biased gene expression modules in primary neutrophils. Importantly, the top female-biased WGCNA module in neutrophils was significantly enriched for ECM-related genes. Thus, our analyses suggest that female neutrophils may uniquely contribute to tissue repair and ECM remodeling, in addition to their core function in the immune response.

## Results

## Gene set enrichment analysis confirms female-biased expression of ECMrelated genes expression in primary mouse neutrophils

In our previous study using a multi-omic approach to assess changes in neutrophils based on age and sex, we observed a significant female bias (regardless of age) for expression of genes related to GO terms 'Collagen chain trimerization', 'Assembly of collagen fibrils and other

multimeric structures', and 'Non-integrin membrane-ECM interactions' [11]. Because of the emerging role of neutrophils in ECM-remodeling [15], we decided to investigate further the potential differential expression of extracellular matrix related processes, as a function of organismal aging or biological sex.

To determine whether ECM-related genes are differentially regulated as a function of organismal age or biological sex, we took advantage of 2 datasets that we previously generated: (i) a bulk transcriptomic dataset of primary bone marrow neutrophils derived from young and old, female and male C57BL/6Nia mice [11], and (ii) a single cell transcriptomic dataset of primary bone marrow neutrophils derived from young female and male C57BL/6J mice [12] ( Fig 1A ). In addition, to maximize our understanding of the differential expression of ECM-related genes in neutrophils, we leveraged expert-curated gene sets related to ECM biology (hereafter matrisome; S1 Table ). The matrisome encompasses all proteins that form the extracellular matrix ( . i e ., collagens, ECM glycoproteins, proteoglycans), also referred to as the core matrisome, encompassing 274 genes in mice [18]. Furthermore, the matrisome also includes proteins that either remodel the ECM ( . ., matrix metalloproteases or ECM regulators) or localize i e into the ECM ( . ., secreted factors, ECM-affiliated genes), collectively referred to as matrii e some-associated genes, which are 836 genes in mice [18]. Thus, examining the changes in the composition of these 1,110 matrisome genes might help us reveal some new underlying biology.

First, we leveraged these gene sets to perform Gene Set Enrichment Analysis (GSEA) on bulk transcriptomic neutrophil data to detect potential changes as a function of aging or sex ( Fig 1B; S2A and S2B Table ). We observed no significant changes in the expression of ECMrelated genes based on organismal age, suggesting that ECM biology is not broadly disrupted in aging mouse neutrophils ( S2A Table ). By contrast, we did find robust female bias in the expression of most ECM-related gene sets in neutrophils ( Fig 1B S2B Table ; ). In addition to a female-biased enrichment in collagen-encoding genes ( Fig 1B , FDR = 4.26x10 -9 ), we also observed significant female-biased expression for genes related to the core matrisome, ECM affiliated genes, ECM glycoproteins, matrisome-associated genes, and secreted factors, but not for proteoglycan-related genes ( Fig 1B S2B Table ; ). Using Fisher's exact test for the significance of overlap, we confirmed that genes from ECM-related gene sets tended to be overrepresented among genes with significant female-biased neutrophil expression by bulk RNAsequencing (Genes biased for female expression according to DESeq2 at FDR &lt; 5%; S1A Fig; S2C Table ). Interestingly, genes expressed at significantly higher levels in female neutrophils show 1.7- to 7.9-fold enrichment for ECM-related genes compared to chance ( S2C Table ).

Wewere also curious whether the female ECM-related gene expression bias would also be observed at the single-cell level. For this purpose, we took advantage of a recent single-cell RNA-seq dataset from female vs . male mouse bone marrow neutrophils [12]. To minimize the impact of 'dropouts' in single-cell RNA-seq datasets [19], we used a gene set scoring approach, UCell [20], to determine the overall expression of the ECM-related gene set in each individual cell. This approach computes a single numeric value per cell based on the expression of genes in a gene set of interest without the need for expression thresholding, thus increasing statistical power [20]. We show the summarized UCell scoring values for each ECM-related gene set per biological sample, and the significance of the difference in score distributions in female vs . male neutrophils ( Fig 1C ). Importantly, this analysis revealed a robust female-bias expression for most of the ECM-related gene sets ( Fig 1C ). Interestingly, based on neutrophil subset definitions from Xie et al. (2020) [21], ECM-related genes may be highest in more mature neutrophils, suggesting that this phenotype is acquired during the maturation process ( S1B Fig ).

Fig 1. Female neutrophils exhibit higher transcriptional expression of extra-cellular matrix related genes. ( A ) Experimental design of primary neutrophil transcriptomic datasets reanalyzed in this study [11, 12]. Panel created with BioRender.com. ( B ) Bubble plot showing GSEA enrichment results for ECM-related genes based on sex expression from neutrophil bulk RNA-seq (all terms are female-biased). See full analysis results in S2B Table . ( C ) Dotplot of 'Ucell' scores of ECM-related genesets aggregated by sample of origin in single cell neutrophil RNA-seq dataset from [12]. For each geneset, statistical significance in a non-parametric Wilcoxon rank sum test between the distribution of UCell scores between female and male

<!-- image -->

- B GSEA of ECM-related genes as a function of sex (bulk)

<!-- image -->

- D GSEA plot of collagen genes as a function of sex (bulk)

E Heatmap of collagen gene expression (bulk)

<!-- image -->

<!-- image -->

2

Ucell analysis of ECM-related genes as a function of sex (single cell)

<!-- image -->

neutrophils is reported. ( D ) GSEA plot of collagen genes from neutrophil bulk RNA-seq (FDR &lt; 1e-8, indicative of female neutrophil expression bias). ( E ) Heatmap displaying the expression of collagen genes (gene set identical as in C) from the bulk neutrophil RNA-seq.

https://doi.org/10.1371/journal.pone.0294859.g001

Interestingly, although collagens were not robustly detected in single-cell RNA-seq due to relatively low expression and sensitivity of the assay ( &lt; 10% of cells showed detectable collagen transcript levels in single-cell RNA-seq regardless of sex, which makes single-cell level analysis not robust for this class of genes; Fig 1C ), collagen genes showed robust female-bias in their expression at the bulk transcriptome level ( Fig 1D and 1E ).

Although we could not find a publicly available mouse neutrophil quantitative proteomics dataset with female and male animals, we identified a high-quality serum proteomics dataset derived from young C57BL/6NHsd female and male mice [22]. Since neutrophils represent a large proportion of circulating blood leukocytes [5], we reasoned that differences in the production of ECM-related proteins by neutrophils should be at least partially reflected in the serum proteome. Thus, we identified significantly sex-biased serum proteins using Limma [23], with respectively 73 female-biased and 42 male-biased serum proteins at FDR &lt; 5% ( S1C and S1D Fig S2D Table ; ). Consistent with our transcriptomics observations, ECM-related gene sets tend to be enriched among serum female-biased proteins (Limma FDR &lt; 5%; S1E Fig; S2E Table ). While neutrophils are likely contributing to this sex-bias in serum ECM proteomics signatures, this observation may also indicate a more general sex bias in ECM expression among immune/circulating cells.

Overall, our analysis determined that genes that both encode structural components of the ECMand remodel the ECM tend to be expressed at higher levels in female neutrophils throughout life (and found at higher protein levels in the serum), suggesting that the emerging interactions between neutrophil activity and ECM biology may be sex-dimorphic throughout life.

## Weighted gene co-expression network analysis reveals that the top femalebiased module in neutrophil transcriptomes is enriched for collagens

Wenext asked which gene modules were coregulated together with ECM-related genes in a female-biased fashion by leveraging WGCNA ( S2A Fig ). Since WCGNA is optimized to be used on bulk datasets, we focused this analysis on the bulk transcriptomic neutrophil data. After network construction, we identified 13 significant transcriptional modules ( S3 Table ). Wenext used the WGCNA module-trait relationship feature to identify which modules were significantly associated with organismal age and/or sex ( Fig 2A ).

Most notably, the most significant sex-associated module, the Salmon module, which contains 318 genes, showed clear female-bias regardless of age ( Fig 2B, S2B Fig ). To note, there was no significant enrichment for X-linked genes in the Salmon module (p = 0.9153 in Fisher's exact test), although some X-linked genes were found in this module ( . ., i e Xist , Tsix , Nyx , Kdm6a Kdm5c Zxdb) , , . Manual inspection also revealed that this module contains many collagen genes ( S3 Table ). By contrast, the module with the second most significant sex-association, the Magenta module, which contains 544 genes, showed male-bias, as well as decreases with aging ( Fig 2B ). To unbiasedly determine which functions were associated with the Salmon and Magenta module, we used hypergeometric enrichment with Gene Ontology and Reactome categories ( Fig 2C and 2D S3 Table ; ). Consistent with the presence of collagenrelated genes, the Salmon module was strongly associated with collagen- and ECM-related terms ( Fig 2C and 2D S3 Table ; ). By contrast, the Magenta module was strongly associated with chromatin and cell cycle-related terms ( S3 Table ), consistent with our previous

## Module-trait relationships from WGCNA (bulk)

<!-- image -->

<!-- image -->

- Csalmon cluster hypergeometric enrichments (Gene Ontology)
- D Salmon cluster gene-concept network (Gene Ontology)

<!-- image -->

Fig 2. WGCNA reveals that the top female-biased expression module is enriched for collagen and ECM-related genes. (A) Module-trait relationships from neutrophil bulk RNA-seq WGCNA. Note that the Salmon module (bold) is the most biased for female neutrophils. Also see S1 Fig and S3 Table. (B) Heatmap of sample-wise module eigengenes from bulk neutrophil RNA-seq WGCNA analysis. (C) Dotplot of significantly enriched gene sets associated to the Salmon module, using hypergeometric enrichment analysis with Gene Ontology [GO] terms (FDR &lt; 0.05). Also see full results in S3 Table . (D) Gene Concept network for GO enrichment analysis related to the Salmon cluster, derived from the same analysis as (C).

<!-- image -->

https://doi.org/10.1371/journal.pone.0294859.g002

observations that these terms were male-biased and regulated with aging [11]. Together, our analysis of the topmost sex-associated WGCNA modules revealed that ECM gene expression is a sex-dimorphic transcriptional feature of neutrophils.

- B Heatmap of module eigengenes by sample WGCNA (bulk) from

## Discussion

While neutrophils, upon activation, are known to secrete elastase and MMPs to remodel ECM [13, 15], activate fibroblasts [24, 25], or even transport ECM to wound sites [16], little is known about the intrinsic expression of ECM genes of neutrophils in their bone marrow niche. Here, we show that the most significant gene cluster correlating with biological sex (Salmon cluster) is enriched with a distinct set of ECM genes that are biased to be expressed at higher levels in female neutrophils. With our analysis, we were not able to detect an impact of aging on the regulation of ECM-related gene expression (regardless of sex). Nevertheless, it is possible that changes related to aging as a function of sex may emerge in datasets with larger numbers of animals, which should be investigated in future studies. In addition, future single cell RNA-seq studies of neutrophils including female and male mice across the lifespan may provide important new insights into the impact of aging and sex on neutrophil heterogeneity, including relating to ECM biology.

Weidentified potential gene sets in the Salmon cluster that might prime female neutrophils for improved wound healing ( S3 Table ). This gene network consists of collagens interacting with platelet-derived growth factor binding ( Fig 2 ), known to initiate neutrophil activation and inflammatory responses at sites of injury [26]. Interestingly, integrin a5 (Itga5) was uniquely expressed in the Salmon cluster. Neutrophils that express α β 5 1 integrin bind fibronectin [27]. Fibronectin is important for wound healing and is required to be placed first in order to add collagen to build a new functional ECM [28]. In human bone fracture hematomas, neutrophils localize to fibronectin shortly after injury, and hematoma-localized neutrophils are uniquely stained for cellular fibronectin [17]. This suggests that activated neutrophils in the hematoma may produce a first 'emergency ECM' [17], consistent with our observation of fibrillar collagen gene expression of neutrophils. Furthermore, upon adhering to fibronectin, neutrophils secrete branched-chain (valine, isoleucine, leucine), aromatic (tyrosine, phenylalanine), and positively charged free amino acids (arginine, ornithine, lysine, hydroxylysine, histidine) [17]. Although the reason for this is unclear, the release of, for instance, hydroxylysine, crucial for Lysol oxidase-mediated collagen crosslinking, is either increased by stimulating neutrophils with insulin or reduced by blocking the PI3K/Akt pathway [17]. Based on this and the composition of the female-enriched Salmon module, we speculate on a connection among this metabolic axis via serum/glucocorticoid regulated kinase 1 (Sgk1), integrin a5, and fibrillar collagens (Col1a1/2, Col2a1), integrated stress response activating transcription factor 4 (Atf4), also implicated in amino acid metabolism for collagen biosynthesis [29], and potentially modulating immune responses via Pdgfa and interleukin 6 receptor alpha (Il6ra) and further collagen synthesis fibroblast growth factor receptor 1 (Fgfr1) ( S3 Table ). This hypothesis might be interesting to test in the future and might provide a mechanistic explanation for why female mice show enhanced wound-healing compared to males [30, 31].

Understanding neutrophil biology has broad implications for therapeutic interventions. Additionally, investigating sex-dimorphic mechanisms affecting neutrophil responses is vital for developing interventions beneficial to both males and females. For example, there is a clear female bias when it comes to rheumatoid arthritis, whereby 75% of patients are women [32]. Inducing arthritis in mice by anti-type II collagen antibodies and lipopolysaccharide, leads to massive neutrophil infiltration into the joint space [33]. Fascinatingly, depleting neutrophils either by the onset of arthritis or during arthritis completely ameliorates the disease [33], suggesting that neutrophils not only initiate but are also involved in maintaining arthritis disease progression. Thus, investigating female-biased processes in neutrophils, including the contribution of the ECM to promote pathology, might be an important next step in managing

rheumatoid arthritis. These female-biased signatures suggest that targeting sex hormone signaling could be a potential therapeutic translation of these findings.

This analysis offers new insights into the potential molecular underpinning of sex-differences in ECM biology. Our analysis, which focuses on differential expression of ECM-related gene sets, reveals a potential source for female-biased ECM production, which has not been previously explored and provides new insights for the scientific community to pursue. While our research primarily hinges on transcriptomic data, it does not offer direct insights into protein levels or functional outcomes. Future studies using targeted CRISPR or shRNA screens in neutrophil cell lines (e.g. MPRO) or use of transgenic mouse lines carrying mutations in ECM-related genes will be useful to understand the role of the clusters found in our data in setting sex-dimorphic physiological responses of neutrophils. Additionally, the intricate regulation of post-transcriptional and post-translational mechanisms may contribute substantial influence over the ECM, thus necessitating further investigation. Our study focuses on neutrophils, which are one part of the complex immune system, and our analyses do not encompass their interactions with other cells, thereby limiting the overall understanding of these intricate relationships. Ultimately, future studies investigating the mechanisms by which the ECM influences neutrophil activity and its interaction with other immune cells are essential, as well as examining how these features are conserved or differ from human neutrophils.

In summary, we examined the sex-specific gene expression differences of neutrophils. We established that a major difference between male and female neutrophils is the expression of ECMgenes. We identified a gene network that might prime ECM gene expression in female neutrophils to potentially accelerate wound healing. Dissecting sex-specific and intrinsic gene expression of neutrophils may significantly impact our understanding to tailor sex-specific therapeutic interventions for wound healing, immune responses, and arthritis.

## Methods

## Data acquisition and preprocessing

Weobtained published processed bulk RNA-seq differential expression results from young (4 months) and aged (20 months), male and female primary bone marrow neutrophils derived from C57BL/6JNia mice (PRJNA630663; Fig 1A upper; n = 4/group) [11]. For all analyses below, we used the SVA-normalized count table and DEseq2 analyses results generated in that study, for which the processed files were available online from https://github.com/ BenayounLaboratory/Neutrophil\_Omics\_2020 [11].

Wealso obtained a processed and annotated Seurat object containing data from a 10xGenomics single-cell RNA-seq dataset of young (3 months) male and female primary bone marrow neutrophils derived from C57BL/6J mice (PRJNA796634; Fig 1A lower; n = 2/group) [12]. This file was obtained from Figshare (https://doi.org/10.6084/m9.figshare.19623978) [12]. R package 'Seurat' 4.2.0 was used to load and interact with the annotated single-cell RNA-seq expression dataset.

Finally, we obtained a processed serum proteomics dataset from C57BL/6NHsd female and male mice (4-5 months of age) [22]. The processed proteomics expression file was obtained from S2 Table from the publisher's site (see below data availability statement). For our analysis, we only considered label-free quantitation [LFQ] intensity data derived from wild-type animals. We performed Multidimensional Scaling (MDS) analysis on protein expression levels in serum using a distance metric between samples based on the Spearman's rank correlation value (1-Rho), then provided to the core R command 'cmdscale'. Limma 3.50.3 [23] was used to perform differential expression analysis, with sex as the variable of interest and ascorbate treatment as a modeling covariate. Proteins with Limma False Discovery Rate [FDR] &lt; 0.05 were considered significantly sex-biased and are reported in S2D Table .

## Curated lists of extracellular matrix-related terms

Weobtained a manually curated list of gene sets relevant to extracellular matrix biology [18]. The curated gene sets are also provided in S1 Table.

Gene Set Enrichment Analysis of extracellular matrix-related terms. Weused the GSEA paradigm to determine whether ECM-related gene sets were differentially regulated as a function of sex or age in bulk RNA-seq of primary neutrophils [34]. For this purpose, we used R package 'phenotest' 1.42.0 in R version 4.1.2. The DEseq2 t-statistic for each gene calculated for age- or sex-expression was used to create the ranked gene list for functional enrichment analysis for both sex and aging [11]. The table output of this analysis is reported in S2A and S2B Table and graphically represented in Fig 1B .

## Overrepresentation analysis using Fisher's exact test

To determine the significance of the overlap between significantly female-biased genes in neutrophils by RNA-seq (DEseq2 FDR &lt; 0.05) or serum proteomics (limma FDR &lt; 0.05) and ECM-related gene lists, we used Fisher's exact test. The background used was all genes detected by RNA-seq or proteins detected by proteomics, respectively. P-value correction for multiple hypothesis testing was performed using the Benjamini-Hochberg method. The table output of this analysis is reported in S2C and S2E Table and graphically represented in S1A and S1E Fig . To determine the significance of the overlap between X-linked genes and genes from the Salmon module, we obtained a list of X-encoded genes from ENSEMBL BioMart version 108 (database access 2023/02/02), restricting output based on gene position on chromosome X. This list was further restricted to genes expressed in our bulk neutrophil RNA-seq according to our previous study [11]. The Fisher's exact test was used to determine the significance of the overlap between genes of the Salmon module and expressed X-linked genes, using the list of expressed genes from the bulk RNA-seq as the universe.

## Ucell scoring analysis of extracellular matrix-related terms

To determine whether ECM-related terms were differentially regulated as a function of neutrophil biological sex at the single-cell level, we leveraged the UCell robust single-cell gene signature scoring metric implemented through R package 'UCell' 1.3.1 [20]. Cell-wise UCell scores were computed for each ECM-related gene list and are graphically reported as aggregates by sample of origin in Fig 1C . Note that Collagen-related genes were not robustly detected at the single cell level, likely a limitation of the platform, and have an extremely low percentage of cells with detected expression ( Fig 1C ). For analysis of statistical significance, a non-parametric Wilcoxon rank sum test was used to compare the distribution of UCell scores between female and male neutrophils and is reported for each gene set in Fig 1C .

## Weighted gene co-expression network analysis [WGCNA]

To investigate what other genes are being co-expressed with the collagens and other ECMrelated genes, we used the WGCNA paradigm [35, 36]. We used R package 'WGCNA' 1.71 [36] and the above-mentioned normalized SVA count table as the inputs. The data was preprocessed by removing any genes with inconsistent expression, as recommended by the user manual. A power of 10 was chosen to create the scale-free topology based on the power and scale independence equilibration. The produced topological overlap matrix [TOM] reveals the mean network connectivity of each gene, and genes with similar expression profiles were then classified into different modules. We set the minimum module size to 100. The analyses yield

13 significant modules. We then performed module-trait analysis using age and sex as the traits to correlate to the modules.

## Functional enrichment analysis of WGCNA gene modules

Weperformed functional enrichment analysis for genes associated with the top sex-biased module, the 'Salmon' module (p = 2x10 -10 ; Fig 2A and 2B ), to unbiasedly determine the top functions differentially regulated in primary neutrophils as a function of sex. We used a hypergeometric test to determine overrepresented Gene Ontology [GO] terms and REACTOME Genesets in the Salmon module compared to expressed genes in the bulk neutrophil transcriptome dataset. For this purpose, we took advantage of R package 'ClusterProfiler' 4.2.2 [37], with GO annotations derived from Bioconductor annotation package 'org.Mm.eg.db' 3.14.0, and with Reactome annotations derived from the 'Reactome-PA' 1.38.0 package [38]. Both dotplot and gene concept network results were derived from ClusterProfiler plotting functions.

## Supporting information

S1 Fig. Analysis of ECM-related gene expression in bulk neutrophil RNA-seq, single-cell neutrophil RNA-seq and serum proteomics. (A) Bubble plot showing Fisher's exact test enrichment results for overlap of significantly female-biased genes in neutrophil bulk transcriptomes (DESeq2 FDR &lt; 5%) and ECM-related genes. See full results in S2C Table . (B) Dotplot of 'Ucell' scores of ECM-related genesets aggregated by neutrophil maturation subset (as defined by [21]) in single-cell neutrophil RNA-seq dataset from [12]. (C) Multidimensional scaling analysis for mouse serum proteomics. MDS: Multidimensional Scaling. (D) Heatmap of significant (Limma FDR &lt; 5%) sex-dimorphic proteins in mouse serum. Also see S2D Table . (E) Bubble plot showing Fisher's exact test enrichment results for overlap of significantly female-biased proteins in serum proteomics (Limma FDR &lt; 5%) and ECM-related proteins. See full results in S2E Table . (TIF)

S2 Fig. WGCNA module cluster dendrogram and salmon module expression profile. (A) WGCNAmodule cluster dendrogram from bulk neutrophil RNA-seq. (B) Heatmap of WGCNASalmon module gene expression from bulk neutrophil RNA-seq. S1 Table : Curated Gene Lists for ECM-related genes.

(TIF)

S1 Table. Curated Gene Lists for ECM-related genes. (XLSX)

S2 Table. Enrichment analysis results for ECM-related gene lists. (A) GSEA results for ECM-related gene lists on bulk neutrophil RNA-seq, as a function of age (sex as covariate). Note that no ECM gene set passed significance thresholds for age-related expression. (B) GSEA results for ECM-related gene lists on bulk neutrophil RNA-seq in female vs. male neutrophils (age as covariate). (C) Analysis of significance of overlap for female-biased neutrophil genes by RNA-seq (DEseq2 FDR &lt; 0.05) for ECM related gene list. (D) Limma differential expression analysis of sex-biased proteins in C57BL/6 serum proteomics from [22] (FDR &lt; 0.05). (E) Analysis of significance of overlap for female-biased serum proteins by proteomics (Limma FDR &lt; 0.05) for ECM-related gene list. (XLSX)

S3 Table. WGCNA related analysis with module membership, and Gene Ontology and Reactome hypergeometric enrichment analysis of Salmon and magenta modules. (XLSX)

## Acknowledgments

Some panels created with BioRender.com.

## Author Contributions

Conceptualization: Collin Y. Ewald, Berenice A. Benayoun. ' '

Data curation: Be 'renice A. Benayoun. '

Formal analysis: Cassandra J. McGill, Berenice A. Benayoun. ' '

Funding acquisition: Collin Y. Ewald, Berenice A. Benayoun. ' '

Investigation: Cassandra J. McGill, Berenice A. Benayoun. ' '

Supervision: Be 'renice A. Benayoun. '

Writing - original draft: Cassandra J. McGill, Collin Y. Ewald, Berenice A. Benayoun. ' '

Writing - review &amp; editing: Cassandra J. McGill, Collin Y. Ewald, Berenice A. Benayoun. ' '

## References

- 1. Sampathkumar NK, Bravo JI, Chen Y, Danthi PS, Donahue EK, Lai RW, et al. Widespread sex dimorphism in aging and age-related diseases. Hum Genet. 2020; 139(3):333-56. Epub 2019/11/05. https:// doi.org/10.1007/s00439-019-02082-w PMID: 31677133; PubMed Central PMCID: PMC7031050.
- 2. Klein SL, Flanagan KL. Sex differences in immune responses. Nat Rev Immunol. 2016; 16(10):626-38. Epub 2016/08/23. https://doi.org/10.1038/nri.2016.90 PMID: 27546235.
- 3. Marquez EJ, Chung CH, Marches R, Rossi RJ, Nehar-Belaid D, Eroglu A, et al. Sexual-dimorphism in human immune system aging. Nat Commun. 2020; 11(1):751. Epub 2020/02/08. https://doi.org/10. 1038/s41467-020-14396-9 PMID: 32029736; PubMed Central PMCID: PMC7005316.
- 4. Gal-Oz ST, Maier B, Yoshida H, Seddu K, Elbaz N, Czysz C, et al. ImmGen report: sexual dimorphism in the immune system transcriptome. Nat Commun. 2019; 10(1):4295. Epub 2019/09/22. https://doi. org/10.1038/s41467-019-12348-6 PMID: 31541153; PubMed Central PMCID: PMC6754408.
- 5. Nah EH, Kim S, Cho S, Cho HI. Complete Blood Count Reference Intervals and Patterns of Changes Across Pediatric, Adult, and Geriatric Ages in Korea. Ann Lab Med. 2018; 38(6):503-11. https://doi.org/ 10.3343/alm.2018.38.6.503 PMID: 30027692.
- 6. Shah B, Burg N, Pillinger MH. Chapter 11-Neutrophils. In: Firestein GS, Budd RC, Gabriel SE, McInnes IB, O'Dell JR, editors. Kelley and Firestein's Textbook of Rheumatology (Tenth Edition): Elsevier; 2017. p. 169-88.e3.
- 7. Furze RC, Rankin SM. Neutrophil mobilization and clearance in the bone marrow. Immunology. 2008; 125(3):281-8. https://doi.org/10.1111/j.1365-2567.2008.02950.x PMID: 19128361.
- 8. Sollberger G, Tilley DO, Zychlinsky A. Neutrophil Extracellular Traps: The Biology of Chromatin Externalization. Developmental cell. 2018; 44(5):542-53. Epub 2018/03/14. https://doi.org/10.1016/j.devcel. 2018.01.019 PMID: 29533770.
- 9. Soehnlein O, Steffens S, Hidalgo A, Weber C. Neutrophils as protagonists and targets in chronic inflammation. Nat Rev Immunol. 2017; 17(4):248-61. Epub 2017/03/14. https://doi.org/10.1038/nri.2017.10 PMID: 28287106.
- 10. Papayannopoulos V. Neutrophil extracellular traps in immunity and disease. Nat Rev Immunol. 2018; 18(2):134-47. Epub 2017/10/11. https://doi.org/10.1038/nri.2017.105 PMID: 28990587.
- 11. Lu RJ, Taylor S, Contrepois K, Kim M, Bravo JI, Ellenberger M, et al. Multi-omic profiling of primary mouse neutrophils predicts a pattern of sex and age-related functional regulation. Nat Aging. 2021; 1 (8):715-33. Epub 2021/09/14. https://doi.org/10.1038/s43587-021-00086-8 PMID: 34514433; PubMed Central PMCID: PMC8425468.

- 12. Kim M, Lu RJ, Benayoun BA. Single-cell RNA-seq of primary bone marrow neutrophils from female and male adult mice. Sci Data. 2022; 9(1):442. Epub 2022/07/24. https://doi.org/10.1038/s41597-02201544-7 PMID: 35871169; PubMed Central PMCID: PMC9308797.
- 13. McGowanSE, Stone PJ, Snider GL, Franzblau C. Alveolar macrophage modulation of proteolysis by neutrophil elastase in extracellular matrix. Am Rev Respir Dis. 1984; 130(5):734-9. Epub 1984/11/01. https://doi.org/10.1164/arrd.1984.130.5.734 PMID: 6568097.
- 14. Garcia-Garcia A, Martin I. Extracellular Matrices to Modulate the Innate Immune Response and Enhance Bone Healing. Front Immunol. 2019; 10:2256. Epub 2019/10/17. https://doi.org/10.3389/ fimmu.2019.02256 PMID: 31616429; PubMed Central PMCID: PMC6764079.
- 15. Zhu Y, Huang Y, Ji Q, Fu S, Gu J, Tai N, et al. Interplay between Extracellular Matrix and Neutrophils in Diseases. J Immunol Res. 2021; 2021:8243378. Epub 2021/07/31. https://doi.org/10.1155/2021/ 8243378 PMID: 34327245; PubMed Central PMCID: PMC8302397.
- 16. Fischer A, Wannemacher J, Christ S, Koopmans T, Kadri S, Zhao J, et al. Neutrophils direct preexisting matrix to initiate repair in damaged tissues. Nat Immunol. 2022; 23(4):518-31. Epub 2022/04/01. https://doi.org/10.1038/s41590-022-01166-6 PMID: 35354953; PubMed Central PMCID: PMC8986538.
- 17. Bastian OW, Koenderman L, Alblas J, Leenen LP, Blokhuis TJ. Neutrophils contribute to fracture healing by synthesizing fibronectin+ extracellular matrix rapidly after injury. Clin Immunol. 2016; 164:78-84. Epub 2016/02/09. https://doi.org/10.1016/j.clim.2016.02.001 PMID: 26854617.
- 18. Naba A, Clauser KR, Ding H, Whittaker CA, Carr SA, Hynes RO. The extracellular matrix: Tools and insights for the "omics" era. Matrix Biol. 2016; 49:10-24. Epub 2015/07/15. https://doi.org/10.1016/j. matbio.2015.06.003 PMID: 26163349; PubMed Central PMCID: PMC5013529.
- 19. Qiu P. Embracing the dropouts in single-cell RNA-seq analysis. Nat Commun. 2020; 11(1):1169. Epub 2020/03/05. https://doi.org/10.1038/s41467-020-14976-9 PMID: 32127540; PubMed Central PMCID: PMC7054558.
- 20. Andreatta M, Carmona SJ. UCell: Robust and scalable single-cell gene signature scoring. Comput Struct Biotechnol J. 2021; 19:3796-8. Epub 2021/07/22. https://doi.org/10.1016/j.csbj.2021.06.043 PMID: 34285779; PubMed Central PMCID: PMC8271111.
- 21. Xie X, Shi Q, Wu P, Zhang X, Kambara H, Su J, et al. Single-cell transcriptome profiling reveals neutrophil heterogeneity in homeostasis and infection. Nat Immunol. 2020; 21(9):1119-33. Epub 2020/07/29. https://doi.org/10.1038/s41590-020-0736-z PMID: 32719519; PubMed Central PMCID: PMC7442692.
- 22. Aumailley L, Bourassa S, Gotti C, Droit A, Lebel M. Vitamin C Differentially Impacts the Serum ProteomeProfile in Female and Male Mice. J Proteome Res. 2021; 20(11):5036-53. Epub 2021/10/14. https://doi.org/10.1021/acs.jproteome.1c00542 PMID: 34643398.
- 23. Ritchie ME, Phipson B, Wu D, Hu Y, Law CW, Shi W, et al. limma powers differential expression analyses for RNA-sequencing and microarray studies. Nucleic Acids Res. 2015; 43(7):e47. Epub 2015/01/ 22. https://doi.org/10.1093/nar/gkv007 PMID: 25605792; PubMed Central PMCID: PMC4402510.
- 24. Chrysanthopoulou A, Mitroulis I, Apostolidou E, Arelaki S, Mikroulis D, Konstantinidis T, et al. Neutrophil extracellular traps promote differentiation and function of fibroblasts. J Pathol. 2014; 233(3):294-307. Epub 2014/04/18. https://doi.org/10.1002/path.4359 PMID: 24740698.
- 25. Curaj A, Schumacher D, Rusu M, Staudt M, Li X, Simsekyilmaz S, et al. Neutrophils Modulate Fibroblast Function and Promote Healing and Scar Formation after Murine Myocardial Infarction. Int J Mol Sci. 2020; 21(10). Epub 2020/05/28. https://doi.org/10.3390/ijms21103685 PMID: 32456225; PubMed Central PMCID: PMC7279328.
- 26. Tzeng DY, Deuel TF, Huang JS, Senior RM, Boxer LA, Baehner RL. Platelet-derived growth factor promotes polymorphonuclear leukocyte activation. Blood. 1984; 64(5):1123-8. Epub 1984/11/01. PMID: 6091815.
- 27. Pierini LM, Lawson MA, Eddy RJ, Hendey B, Maxfield FR. Oriented endocytic recycling of alpha5beta1 in motile neutrophils. Blood. 2000; 95(8):2471-80. Epub 2001/02/07. PMID: 10753823.
- 28. Patten J, Wang K. Fibronectin in development and wound healing. Adv Drug Deliv Rev. 2021; 170:35368. Epub 2020/09/23. https://doi.org/10.1016/j.addr.2020.09.005 PMID: 32961203.
- 29. Selvarajah B, Azuelos I, Plate M, Guillotin D, Forty EJ, Contento G, et al. mTORC1 amplifies the ATF4dependent de novo serine-glycine pathway to supply glycine during TGF-beta(1)-induced collagen biosynthesis. Sci Signal. 2019; 12(582). Epub 2019/05/23. https://doi.org/10.1126/scisignal.aav3048 PMID: 31113850; PubMed Central PMCID: PMC6584619.
- 30. Ashcroft GS. Sex differences in wound healing. Advances in Molecular and Cell Biology. 34: Elsevier; 2004. p. 321-8.
- 31. R n ø ø B, Engelholm LH, Lund LR, Hald A. Gender Affects Skin Wound Healing in Plasminogen Deficient Mice. PLOS ONE. 2013; 8(3):e59942. https://doi.org/10.1371/journal.pone.0059942 PMID: 23527289

- 32. Sokka T, Toloza S, Cutolo M, Kautiainen H, Makinen H, Gogus F, et al. Women, men, and rheumatoid arthritis: analyses of disease activity, disease characteristics, and treatments in the QUEST-RA study. Arthritis Res Ther. 2009; 11(1):R7. Epub 2009/01/16. https://doi.org/10.1186/ar2591 PMID: 19144159; PubMedCentral PMCID: PMC2688237.
- 33. Tanaka D, Kagari T, Doi H, Shimozato T. Essential role of neutrophils in anti-type II collagen antibody and lipopolysaccharide-induced arthritis. Immunology. 2006; 119(2):195-202. Epub 2006/07/14. https://doi.org/10.1111/j.1365-2567.2006.02424.x PMID: 16836650; PubMed Central PMCID: PMC1782359.
- 34. Subramanian A, Tamayo P, Mootha VK, Mukherjee S, Ebert BL, Gillette MA, et al. Gene set enrichment analysis: a knowledge-based approach for interpreting genome-wide expression profiles. Proc Natl Acad Sci U S A. 2005; 102(43):15545-50. Epub 2005/10/04. https://doi.org/10.1073/pnas.0506580102 PMID: 16199517; PubMed Central PMCID: PMC1239896.
- 35. Fuller TF, Ghazalpour A, Aten JE, Drake TA, Lusis AJ, Horvath S. Weighted gene coexpression network analysis strategies applied to mouse weight. Mamm Genome. 2007; 18(6-7):463-72. Epub 2007/ 08/02. https://doi.org/10.1007/s00335-007-9043-3 PMID: 17668265; PubMed Central PMCID: PMC1998880.
- 36. Langfelder P, Horvath S. WGCNA: an R package for weighted correlation network analysis. BMC Bioinformatics. 2008; 9:559. Epub 2008/12/31. https://doi.org/10.1186/1471-2105-9-559 PMID: 19114008; PubMedCentral PMCID: PMC2631488.
- 37. Yu G, Wang LG, Han Y, He QY. clusterProfiler: an R package for comparing biological themes among gene clusters. OMICS. 2012; 16(5):284-7. Epub 2012/03/30. https://doi.org/10.1089/omi.2011.0118 PMID: 22455463; PubMed Central PMCID: PMC3339379.
- 38. Yu G, He QY. ReactomePA: an R/Bioconductor package for reactome pathway analysis and visualization. Mol Biosyst. 2016; 12(2):477-9. Epub 2015/12/15. https://doi.org/10.1039/c5mb00663e PMID: 26661513.