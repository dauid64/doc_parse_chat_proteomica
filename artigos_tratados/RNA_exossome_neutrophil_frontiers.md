<!-- image -->

## Edited by:

Maria Efthymiou, University College London, United Kingdom

## Reviewed by:

Juan Du, Capital Medical University, China Hui Li, Guangxi University, China

## *Correspondence:

Honglin Zhu honglinzhu@csu.edu.cn

## Specialty section:

This article was submitted to In /uniFB02 ammation Pharmacology, a section of the journal Frontiers in Pharmacology

Received: 20 June 2021 Accepted: 20 August 2021 Published: 17 September 2021

## Citation:

Li L, Zuo X, Liu D, Luo H and Zhu H (2021) The Functional Roles of RNAs Cargoes Released by NeutrophilDerived Exosomes in Dermatomyositis. Front. Pharmacol. 12:727901. doi: 10.3389/fphar.2021.727901

<!-- image -->

## TheFunctional Roles of RNAs Cargoes Released by Neutrophil-Derived Exosomes in Dermatomyositis

Liya Li 1,2 , Xiaoxia Zuo 1,3,4 , Di Liu 1 , Hui Luo 1,3,4 and Honglin Zhu 1,3,4 *

1 The Department of Rheumatology and Immunology, Xiangya Hospital of Central South University, Changsha, China, 2 The Department of Rheumatology and Immunology, The Third Xiangya Hospital, Central South University, Changsha, China, 3 Provincial Clinical Research Center for Rheumatic and Immunologic Diseases, Xiangya Hospital, Changsha, China, 4 National Clinical Research Center for Geriatric Disorders, Xiangya Hospital, Changsha, China

Dermatomyositis (DM) is an idiopathic in /uniFB02 ammatory myopathy characterized by cutaneous manifestations. We /uniFB01 rst identi /uniFB01 ed the pro /uniFB01 les of noncoding RNAs (lncRNAs and miRNAs) in peripheral neutrophil exosomes (EXOs) of DM patients and explored their potential functional roles. Bioinformatics analyses were performed with R packages. Real-time quantitative PCR was used to validate the altered RNAs in DM neutrophil EXO-stimulated human dermal microvascular endothelial cells (HDMECs) and human skeletal muscle myoblasts (HSkMCs). In DM neutrophil EXOs, 124 upregulated lncRNAs (with 1,392 target genes), 255 downregulated lncRNAs (with 1867 target genes), 17 upregulated miRNAs (with 2,908 target genes), and 15 downregulated miRNAs (with 2,176 target genes) were identi /uniFB01 ed. GO analysis showed that the differentially expressed (DE) lncRNAs and DE miRNAs participated in interleukin-6 and interferon-beta production, skeletal muscle cell proliferation and development, and endothelial cell development and differentiation. KEGG analysis suggested that DE lncRNAs and DE miRNAs were enriched in the PI3K -Akt, MAPK, AMPK and FoxO signalling pathways. Many novel and valuable DE lncRNAs and DE miRNAs interacted and cotargeted in the PI3K -Akt, MAPK, AMPK and FoxO signalling pathways. Our study suggests that neutrophil EXOs participate in DM pathogenesis through lncRNAs and miRNAs in the PI3K Akt, -MAPK, AMPK and FoxO signalling pathways.

Keywords: dermatomyositis, neutrophil-derived exosome, lncRNA, miRNA, PI3K-Akt, MAPK, AMPK, FoxO

Abbreviations: DM, dermatomyositis; IFN, interferon; PI3K, phosphoinositol-3-kinase; Akt, v-akt murine thymoma viral oncogene homologue; MAPK, mitogen-activated protein kinase; AMPK, adenosine monophosphate-activated protein kinase; FoxO, Forkhead box O; EXOs, exosomes; EVs, extracellular vesicles; HDMECs, human dermal microvascular endothelial cells; miRNAs, microRNAs; lncRNAs, long noncoding RNAs; JDM, juvenile DM; NCs, normal controls; DE, differentially expressed; GO, Gene Ontology; KEGG, Kyoto Encyclopedia of Genes and Genomes; HSkMCs, human skeletal muscle myoblasts; IGF, insulin-like growth factor.

September 2021 | Volume 12 | Article 727901

## INTRODUCTION

Dermatomyositis (DM) is an idiopathic in /uniFB02 ammatory myopathy with characteristic cutaneous manifestations and symmetrical progressive proximal weakness (Bohan and Peter, 1975a; Bohan and Peter, 1975b; Callen, 2000). The hallmark histopathological features of DM include perifascicular atrophy and in /uniFB02 ammatory in /uniFB01 ltration (by macrophages/neutrophils, CD20 + B cells, CD4 + T cells and plasmacytoid dendritic cells) in muscle (Dalakas, 2015; DeWane et al., 2019). Although the mechanism of DM is largely unknown, some factors are thought to contribute to DM pathogenesis, such as MHC polymorphisms, epigenetic modi cations, type I interferon (IFN) signalling, myositis-speci /uniFB01 /uniFB01 c antibodies and many other pathways, such as the phosphoinositol3-kinase (PI3K) -v-akt murine thymoma viral oncogene homologue (Akt), mitogen-activated protein kinase (MAPK), adenosine monophosphate-activated protein kinase (AMPK) and Forkhead box O (FoxO) signalling pathways (Lahoria et al., 2016; Gao et al., 2017; Tartar et al., 2018; Gao et al., 2019).

In recent years, neutrophils have been recognized as participants in imbalances among autoimmune responses directed at tissue-speci /uniFB01 c antigens with the ability to inhibit and control these responses (Wahren-Herlenius and Dörner, 2013) and as intermediates between effectors and regulatory mechanisms (Navegantes et al., 2017). Neutrophils play pathogenic roles by releasing various molecules, such as proteases, cytokines, reactive oxygen species and exosomes (EXOs), extracellularly after triggering the immune complex (Glennon-Alty et al., 2018). Neutrophils also interact with macrophages, dendritic cells, B and T cells, and natural killer cells that produce IFN- , γ regulating the immune response (Jaillon et al., 2013). In DM patients, an increased baseline peripheral blood neutrophil-tolymphocyte ratio is associated with pulmonary involvement, disease activity and worse overall survival (Yang et al., 2017; Gao et al., 2018a; Ha et al., 2018). In our previous study, proteinases and proteins in the neutrophil cytoplasm were found to play important roles in muscle in /uniFB02 ammatory cell in /uniFB01 ltration and vascular damage in DM patients (Gao et al., 2018b; Xiao et al., 2019). All of the above results suggest that neutrophils play important roles in the pathogenesis of DM; however, the detailed mechanisms need further research.

EXOs are extracellular vesicles (EVs) that are 30 -150 nm in diameter and are secreted by most cells. EXOs express speci /uniFB01 c surface markers, including tumour susceptibility gene 101, integrins and tetraspanins (CD63, CD9, and CD81/82) (Yáñez-Mó et al., 2015). EXOs contain selective cargoes of RNAs, DNAs and proteins, which are valuable sources of intercellular signalling molecules, biomarkers and treatment targets (Li et al., 2018; Li et al., 2019). For example, serum EXOs can restore cellular function in vitro and can be employed for the treatment and noninvasive diagnosis of dysferlinopathy (Dong et al., 2018). In addition, EXOs released from in /uniFB02 amed myotubes induce myoblast in /uniFB02 ammation and inhibit myogenic mechanisms while stimulating atrophic signals (Kim et al., 2018). Neutrophil-derived EXOs (neutrophil EXOs) also play important roles in immune responses (Rossaint et al., 2016). In generalized pustular

psoriasis, proteomic analysis of neutrophil EXO contents has identi /uniFB01 ed olfactomedin 4 as the critical differentially expressed (DE) protein that mediates autoimmune in /uniFB02 ammatory responses (Shao et al., 2019). In the progression of asthma, neutrophil EXOs can modulate immune responses, enhance the proliferation of airway smooth muscle cells, and promote airway remodelling (Vargas et al., 2016). In chronic obstructive pulmonary disease (COPD), activated neutrophil EXOs predominate in lung /uniFB02 uids. These EXOs can degrade extracellular matrix by protecting surface neutrophil elastase from alpha-1 antitrypsin inhibition. Transferring activated neutrophil EXOs causes a COPD-like phenotype in murine lungs in which alveoli are destroyed via neutrophil elastase (Genschmer et al., 2019). In our previous study, neutrophil EXOs from systemic sclerosis patients were found to inhibit the proliferation and migration of human dermal microvascular endothelial cells (HDMECs) (Li et al., 2020a; Li et al., 2020b). Therefore, we hypothesized that neutrophil EXOs might lead to muscle damage in DM patients.

Recently, noncoding RNA regulatory mechanisms involving microRNAs (miRNAs, &lt; 50 nucleotides) and long noncoding RNAs (lncRNAs, &gt; 200 nucleotides) have been widely studied in the context of DM (Peng et al., 2016; Gao et al., 2019; Mazzone et al., 2019). Many miRNAs and lncRNAs are associated with disease activity and participate in the pathogenesis of DM (Satoh et al., 2005; Misunova et al., 2016; Peng et al., 2016). In juvenile DM (JDM) patients, the miRNAs of plasma EXOs are capable of altering transcriptional programmes within endothelial cells (Jiang et al., 2019). Here, we analysed the noncoding RNAs (lncRNAs and miRNAs) pro /uniFB01 les of neutrophil EXOs from DM patients and sought insights into their predicted functional roles, such as their roles in pathogenetic mechanisms, and their potential utility as new biomarkers and therapeutic targets.

## MATERIALS AND METHODS

## Patients and Controls

We collected blood from 20 DM patients and 22 normal controls (NCs) who were all Han Chinese. Among these participants, 5 patients with DM as primary diagnosis and 5 ageand sexmatched NCs were selected for lncRNA and miRNA sequencing analyses. The clinical characteristics of 5 DM patients for neutrophil EXOs RNAseq are shown in Supplementary Table S1 . All patients ful /uniFB01 lled the 1975 Bohan and Peter diagnostic criteria for DM and were enrolled at the Department of Rheumatology and Immunology at the Xiangya Hospital of Central South University (Bohan and Peter, 1975a; Bohan and Peter, 1975b). The clinical characteristics of the participants, including their demographic characteristics, serological characteristics, organ involvement and medications, are shown in Supplementary Table S2 .

## Isolation and Culture of Neutrophils

Peripheral whole blood samples (10 ml) were collected in EDTA anticoagulant-coated tubes and processed within 2 h. Neutrophils were isolated by density gradient equilibrium centrifugation using Histopaque-1077 and Histopaque-1119 (Sigma-Aldrich,

St. Louis, United States) according to the manufacturer s ' instructions. The neutrophil pellets were used for culture or stored at -80 ° C until analysis. For neutrophil culture, the cell pellets (cell viability &gt; 90%) were resuspended in the appropriate volume (2 -5 × 10 6 cell/ml) of 1,640 medium (Gibco, Carlsbad, United States) supplemented with 10% EXO-free foetal bovine serum (FBS, Gibco), which was prepared by collecting the supernatant after ultracentrifugation of FBS at 150,000 × g for 3 h at 4 ° C (the same procedure was used for the EXO-free FBS described below). The neutrophils were incubated for 2 h at 37 ° C in a humidi /uniFB01 ed atmosphere containing 5% CO2. The cell pellets and supernatants were collected separately for further analysis.

## Isolation and Identi /uniFB01 cation of Exosomes and EXO RNAs

We isolated EXOs from cultured neutrophil supernatants using an exoEasy Maxi Kit (Qiagen, Frederick, United States) according to the manufacturer s instructions. The neutrophil EXOs were dissolved in ' 600 μ l of eluting buffer and stored at -80 ° C until analysis. Neutrophil EXOs were identi /uniFB01 ed as cup-shaped double-membrane structures by transmission electron microscopy (FEI Tecnai G2 Spirit Twin, Hillsboro, United States) via negative staining ( Supplementary Figure S1A ), were con /uniFB01 rmed to express CD63 with a FACSCalibur /uniFB02 ow cytometer (BD Biosciences, San Jose, United States) using EXOome-Human CD63 Isolation/Detection Dynabeads (Invitrogen, Thermo Fisher Scienti /uniFB01 c, Lithuania) and anti-human CD63-PE antibodies (12 -0,639, eBioscience, United States) according to the manufacturer s ' protocol ( Supplementary Figure S1B ) and were veri /uniFB01 ed to meet the expected EXO size by dynamic light scattering with a Zetasizer Nano ZS instrument (Malvern Instrument, Marvin, United Kingdom) ( Supplementary Figure S1C ).

Total RNA was extracted from the neutrophil EXOs with TRIzol (Invitrogen Life Technologies, California, United States) according to the manufacturer s ' protocol. An Agilent 2,200 TapeStation (Agilent Technologies, California, United States) and a Qubit ® 2.0 Fluorometer (Life Technologies) were used to assess the quantity and integrity of the total RNA and the puri /uniFB01 ed library products described below.

## RNA Library Construction, Sequencing and Data Analysis

RNAs libraries were created with an NEBNext ® Multiplex Small RNALibrary Prep Set for Illumina (NEB, Ipswich, United States) for small RNA and an NEBNext ® Ultra ™ RNA Library Prep Kit for Illumina for lncRNA, according to the manufacturer s ' instructions. Paired-end sequencing (PE150) with the Illumina 3,000 platform was performed (RiboBio Co.,Guangzhou, China). The number of lncRNAs and miRNAs detected in neutrophil EXOs are shown in Supplementary Table S3 . The sequencing reads were preprocessed with fastQC software and Trimmomatic tools (v 0.36) to assess the read quality and to /uniFB01 lter out poorquantity reads, HISAT2 was used to map the reads to the human reference genome hg19; uniquely mapped reads were assigned to annotated genes with HTSeq (for lncRNAs) and the BurrowsWheeler Aligner (for miRNAs). The miRDeep2 database was

used to identify known mature miRNAs based on miRBase (v21) (www.miRBase.org) and to predict novel miRNAs. DESeq2 was used to identify the signi /uniFB01 cantly DE lncRNAs (adjusted p &lt; 0.05 and |log2(fold change)| &gt; 1.5), while the R package edgeR was used to identify the signi /uniFB01 cantly DE miRNAs (adjusted p &lt; 0.05 and |log2(fold change)| &gt; 1).

## Bioinformatics Analysis for Differentially Expressed lncRNAs and Differentially Expressed miRNAs

LncRNAs regulate potential target genes through two major mechanisms: cis regulation and trans regulation. Target genes in cis were obtained by integrating the DE lncRNAs and their adjacent (within 10 kb) DE mRNAs. After extracting the sequences of the DE lncRNAs and DE mRNAs, both BLAST software (for initial screening) and RNAplex software (for rescreening) were used to identify potential target genes of the lncRNAs in trans. The target genes for selected miRNAs were predicted with the targetScan, miRDB, miRTarBase and miRWalk software programs. Moreover, the miRanda, PITA and RNAhybrid software programs were used to identify common elements between the lncRNAs and miRNAs and to predict the miRNAs associated with lncRNAs of interest.

The target genes of the DE lncRNAs and DE miRNAs were subjected to pathway analysis with the Gene Ontology (GO) (http://geneontology.org/) and Kyoto Encyclopedia of Genes and Genomes (KEGG) (https://www.genome.jp/kegg) databases. GO and KEGG enrichment analyses were performed with the R package clusterPro /uniFB01 ler (Yu et al., 2012). Interaction and coexpression networks for lncRNAs, miRNAs and mRNAs were constructed with Cytoscape software (http://apps.cytoscape.org/).

## Cell Culture

HDMECs were obtained from Cell Biolabs (# CBR130858, San Diego, United States) and cultured in DMEM (Gibco) with 10% EXO-free FBS. Human skeletal muscle myoblasts (HSkMCs) were purchased from ScienCell and cultured in Skeletal Muscle Cell Medium (ScienCell, San Diego, United States) with 5% EXO-free FBS. All cells were cultured at 37 ° C in a 5% CO2 humidi /uniFB01 ed incubator. Both HDMECs and HSkMCs were used when they reached 60 -70% con uence /uniFB02 and were then stimulated with 20% neutrophil EXOs (volume concentration, 160 µl of neutrophil EXO eluting buffer and 640 µl of medium) per well for 48 h in 24-well plates. Each experiment was repeated three times with three samples per group.

## Validation Using Real-Time Quantitative PCR

Total RNA from neutrophils, HDMECs and HSkMCs was extracted using TRIzol according to the manufacturer s ' instructions. For lncRNAs, cDNA was prepared using a PrimeScript ™ RT Reagent Kit (Perfect Real Time, Takara, Japan). Real-time quantitative PCR was performed using TB Green PCR Master Mix (Takara, Japan) on a 7,500 Real-Time PCR System (Applied Biosystems, California, United States).

TABLE 1 | DE lncRNAs in the neutrophil exosomes of DM patients (Top 30).

| lncRNAs           | log2(FC)   |   p value | lncRNAs           | log2(FC)   |   p value |
|-------------------|------------|-----------|-------------------|------------|-----------|
| ENST00000600489.1 | 5.432      |     0     | NR\_123718.1       | - 2.136    |     0     |
| NR\_136569.1       | 5.423      |     0     | NR\_135530.1       | - 2.337    |     0     |
| ENST00000594492.1 | 3.713      |     0     | NR\_040001.2       | - 2.368    |     0     |
| NR\_003013.1       | 3.216      |     0     | ENST00000444796.1 | - 2.434    |     0.001 |
| ENST00000592523.1 | 3.207      |     0     | ENST00000453561.2 | - 2.609    |     0     |
| ENST00000607284.1 | 2.839      |     0     | ENST00000593824.1 | - 3.242    |     0     |
| NR\_024393.1       | 2.633      |     0.001 | ENST00000503403.1 | - 3.375    |     0     |
| ENST00000526936.1 | 2.163      |     0.001 | ENST00000572850.1 | - 3.755    |     0     |
| ENST00000428280.1 | 1.970      |     0.001 | NR\_110815.1       | - 4.137    |     0.001 |
| ENST00000419196.1 | 1.737      |     0.001 | ENST00000519840.1 | - 4.254    |     0     |
| ENST00000503469.2 | 1.577      |     0.001 | ENST00000587907.1 | - 4.275    |     0     |
| NR\_135626.1       | - 1.764    |     0.001 | NR\_104232.1       | - 4.649    |     0     |
| ENST00000438753.1 | - 1.899    |     0     | ENST00000581910.1 | - 4.667    |     0.001 |
| ENST00000450365.1 | - 1.929    |     0.001 | ENST00000592296.1 | - 5.274    |     0     |
| NR\_038194.1       | - 2.013    |     0.001 | ENST00000577199.1 | - 5.982    |     0     |

DE: differentially expressed; DM: dermatomyositis; FC: fold change.

GAPDH expression was used as the endogenous control. The gene-speci /uniFB01 c primers are shown in Supplementary Table S4 . The relative expression of miRNAs was measured with a miDETECT A Track ™ miRNA qRT-PCR Starter Kit (RiboBio.Co., Guangzhou, China) on the 7,500 Real-Time PCR System. The miRNA-speci /uniFB01 c primers and the Uni-Reverse Primer were purchased from RiboBio Co. (Guangzhou, China). The miRNA primers product information is shown in Supplementary Table S5 . U6B small nuclear RNA was used as the endogenous control to normalize the sample data. Each group had more than six samples.

## Statistical Analysis

All data except for the RNA sequencing data were analysed with GraphPad Prism 5 software, and statistical signi /uniFB01 cance was set as a two-sided p &lt; 0.05. Numerical variables with a normal distribution are presented as the mean ± SEM and were analysed by unpaired t-test. Data with a nonnormal distribution are shown as the median and were assessed with the Wilcoxon rank sum test.

## RESULTS

## Differentially Expressed lncRNAs in Dermatomyositis Neutrophil Exosomes

We identi /uniFB01 ed 379 DE lncRNAs in neutrophil EXOs in DM patients compared with NCs, including 124 upregulated and 255 downregulated lncRNAs [ Supplementary Data S1 ]. The top 30 DE lncRNAs are shown in Table 1 and Supplementary Table S6 . Bioinformatics analysis identi /uniFB01 ed 1,392 target genes for the upregulated lncRNAs and 1867 target genes for the downregulated lncRNAs [ Supplementary Data S2 ]. GO analysis of these target genes revealed that the regulation of interleukin-6 production, IFNβ production and skeletal muscle cell proliferation terms were enriched; KEGG analysis indicated that the FoxO signalling pathway, endocytosis and JAK-STAT signalling pathway were involved ( Table 3 and Supplementary Tables S7, S8 ).

## Differentially Expressed miRNAs in Dermatomyositis Neutrophil Exosomes

We identi /uniFB01 ed a total of 32 DE miRNAs between DM patients and NCs from the miRNA pro /uniFB01 les of neutrophil EXOs, including 17 upregulated and 15 downregulated miRNAs ( Table 2 and Supplementary Table S9 ). Bioinformatics analysis predicted 2,908 target genes for the upregulated miRNAs and 2,176 target genes for the downregulated miRNAs [Supplementary Data S3 ]. GO enrichment analysis suggested that both of these miRNA target genes were involved in actin /uniFB01 lament organization, muscle tissue development, endothelial cell development and differentiation and activation of MAPK activity; KEGG analysis indicated that the PI3K -Akt, MAPK, AMPK, and FoxO signalling pathways, among others, were enriched ( Table 3 and Supplementary Tables S10, S11 ).

## Interaction Relationships of Differentially Expressed lncRNAs and Differentially Expressed miRNAs in the Phosphoinositol-3-Kinase Akt, -Mitogen-Activated Protein Kinase, Adenosine Monophosphate-Activated Protein Kinase and FoxO Signalling Pathways

LncRNAs can regulate miRNAs in some cellular processes. Here, we analysed the relationships between the DE lncRNAs and DE miRNAs in DM neutrophil EXOs and found that 91 lncRNAs (58 downregulated and 33 upregulated lncRNAs) and 23 miRNAs (11 downregulated and 12 upregulated miRNAs) might interact with each other [ Supplementary Figure S2 ]. From the GO and KEGG analyses above, we found that the PI3K Akt, -MAPK, AMPK and FoxO signalling pathways were enriched for the predicted target genes of both DE lncRNAs and DE miRNAs. Thus, we analysed the lncRNAs, miRNAs and target genes involved in these four pathways. We found

TABLE 2 | DE miRNAs in the neutrophil exosomes of DM patients ( n /equals 32).

| miRNAs           |   log2(FC) |   p value | miRNAs           | log2(FC)   |   p value |
|------------------|------------|-----------|------------------|------------|-----------|
| hsa-miR-3614-5p  |      4.262 |     0     | hsa-miR-1273h-3p | 3.138      |     0.049 |
| hsa-miR-1180-3p  |      4.25  |     0.007 | hsa-miR-4792     | - 2.993    |     0.002 |
| hsa-miR-451a     |      1.705 |     0.014 | hsa-miR-1323     | - 2.938    |     0.005 |
| hsa-miR-23a-5p   |      2.905 |     0.014 | hsa-miR-516a-5p  | - 3.424    |     0.005 |
| hsa-miR-183-5p   |      1.296 |     0.015 | hsa-miR-512-3p   | - 3.163    |     0.008 |
| hsa-miR-486-3p   |      2.303 |     0.016 | hsa-miR-372-3p   | - 12.485   |     0.01  |
| hsa-miR-223-5p   |      1.286 |     0.02  | hsa-miR-4488     | - 3.933    |     0.022 |
| hsa-miR-1268a    |     12.006 |     0.022 | hsa-let-7f-1-3p  | - 12.101   |     0.027 |
| hsa-miR-424-3p   |      1.291 |     0.03  | hsa-miR-520a-3p  | - 2.520    |     0.03  |
| hsa-miR-16-2-3p  |      1.031 |     0.031 | hsa-miR-424-5p   | - 1.967    |     0.033 |
| hsa-miR-363-3p   |      1.394 |     0.033 | hsa-miR-542-3p   | - 2.116    |     0.039 |
| hsa-miR-122-5p   |      1.251 |     0.036 | hsa-miR-4433b-5p | - 12.189   |     0.039 |
| hsa-miR-1278     |     11.949 |     0.039 | hsa-miR-1307-5p  | - 3.503    |     0.043 |
| hsa-miR-548ad-5p |      3.3   |     0.044 | hsa-miR-195-5p   | - 1.511    |     0.046 |
| hsa-miR-548ae-5p |      3.3   |     0.044 | hsa-miR-27b-3p   | - 1.632    |     0.047 |
| hsa-miR-182-5p   |      1.099 |     0.045 | hsa-miR-518e-3p  | - 3.719    |     0.047 |

TABLE3| GOandKEGGenrichment analysis for target genes of DE lncRNAs and DE miRNAs in DM neutrophil exosomes.

| GO enrichment for target genes of DE lncRNAs               | p value (up/down a )   |
|------------------------------------------------------------|------------------------|
| regulation of interleukin-6 production                     | 0.013/0.015            |
| regulation of interferon-beta production                   | 0.011/0.002            |
| regulation of skeletal muscle satellite cell proliferation | 0.045/0.019            |
| KEGG enrichment for target genes of DE lncRNAs             | p value (up/down a )   |
| FoxO signaling pathways                                    | 0.037/0.247            |
| Endocytosis                                                | 0.049/0.214            |
| JAK-STAT signaling pathway                                 | 0.153/0.013            |
| GO enrichment for target genes of DE miRNAs                | p value (up/down a )   |
| actin /uniFB01 lament organization                         | 0.000/0.001            |
| muscle tissue development                                  | 0.000/0.000            |
| endothelial cell development and differentiation           | 0.000/0.000            |
| activation of MAPK activity                                | 0.000/0.001            |
| KEGG enrichment for target genes of DE miRNAs              | p value (up/down a )   |
| MAPK signaling pathways                                    | 0.000/0.000            |
| AMPK signaling pathways                                    | 0.000/0.000            |
| FoxO signaling pathways                                    | 0.000/0.000            |
| Endocytosis                                                | 0.002/0.017            |
| Regulation of actin cytoskeleton                           | 0.001/0.000            |
| Wnt signaling pathway                                      | 0.002/0.002            |
| mTOR signaling pathway                                     | 0.009/0.002            |
| TNF signaling pathway                                      | 0.012/0.001            |
| Th17 cell differentiation                                  | 0.013/0.009            |
| VEGF signaling pathway                                     | 0.048/0.032            |

that 43 predicted target genes were able to be regulated by both lncRNAs and miRNAs. Finally, we obtained an interaction network that included 50 lncRNAs, 18 miRNAs and their 43 cotarget mRNAs ( Table 4 ). Among the relationships, 3 of the lncRNA-miRNA pairs (in

which the miRNAs were regulated by lncRNAs) were NR\_046101.1 -hsa-miR-3614-5p, ENST00000444868.2 -hsa-miR195-5p and ENST00000433036 -hsa-miR-512-3p.

Analysis of Differentially Expressed lncRNAs and Differentially Expressed miRNAs in the Phosphoinositol-3-Kinase Akt, -Mitogen-Activated Protein Kinase, Adenosine Monophosphate-Activated Protein Kinase and FoxO Signalling Pathways in Neutrophils and Neutrophil EXO Stimulated Human Dermal -Microvascular Endothelial Cells and Human Skeletal Muscle Myoblasts

Skeletal muscle cells and endothelial cells are target cells in the pathogenesis of DM (Yáñez-Mó et al., 2015; Gao et al., 2018b; Gao et al., 2019). To further analyze the functions of neutrophil EXOs, we validated the expression of DE lncRNAs and DE miRNAs in neutrophils and in neutrophil EXO-stimulated HDMECs and HSkMCs. As shown in Figure 1 and Supplementary Figure S3 , 10 DE lncRNAs (6 upregulated and 4 downregulated lncRNAs) and 10 DE miRNAs (5 upregulated and 5 downregulated miRNAs) involved in the PI3K -Akt, MAPK, AMPK and FoxO signalling pathways were chosen for validation analysis.

Nine of the 10 DE lncRNAs (ENST00000510274.1, ENST00000609726.1, NR\_110761.1, NR\_125423.1, ENST00000592296.1, ENST00000584643.1, ENST00000428280.1, ENST00000591854.1 and NR\_039978.1) were signi /uniFB01 cantly DE in HDMECs-stimulated by neutrophil EXOs, ENST00000433036.1 was not. Eight of the lncRNAs were signi /uniFB01 cantly DE in HSkMCs-stimulated by neutrophil EXOs, and /uniFB01 ve of them were DE in neutrophils. The results for most of them were consistent with the results of the lncRNA pro /uniFB01 le analysis ( Figure 1A ).

TABLE 4 | Co-target genes for DE lncRNAs and DE miRNAs in the PI3K-Akt, MAPK, AMPK, FoxO signaling pathways.

| Co-target    | DE lncRNAs ( n = 50)                                                                                                                             | DE miRNAs ( n = 18)                                                                               |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| ANGPT2       | ENST00000581633.1, NR\_125914.1, NR\_125915.1                                                                                                      | hsa-miR-542-3p                                                                                    |
| ATG12        | ENST00000584643.1                                                                                                                                | hsa-miR-183-5p                                                                                    |
| BCL2         | ENST00000588307.1                                                                                                                                | hsa-miR-486-3p, hsa-miR-182-5p                                                                    |
| CACNG3       | ENST00000567624.1                                                                                                                                | hsa-miR-486-3p                                                                                    |
| CACNG8       | NR\_046101.1 a , ENST00000565495.1, ENST00000539313.1, ENST00000600508.1, ENST00000584643.1                                                       | hsa-miR-3614-5p a                                                                                 |
| CPT1A        | ENST00000582536.1, NR\_038219.1, ENST00000591918.2, ENST00000504658.1, ENST00000592296.1, ENST00000508878.1, ENST00000526936.1, ENST00000511517.1 | hsa-miR-512-3p, hsa-miR-372-3p, hsa-miR-520a-3p                                                   |
| CREB1        | ENST00000448256.1, ENST00000609726.1                                                                                                             | hsa-let-7f-1-3p, hsa-miR-512-3p, hsa-miR-3614-5p, hsa-miR-182- 5p, hsa-miR-122-5p, hsa-miR-27b-3p |
| CREB3L1      | ENST00000527239.1                                                                                                                                | hsa-miR-182-5p                                                                                    |
| CRK          | NR\_104232.1, NR\_039978.1, ENST00000519451.1, ENST00000609726.1, ENST00000544086.1, ENST00000539313.1                                             | hsa-miR-372-3p, hsa-miR-195-5p, hsa-miR-424-5p                                                    |
| EEF2K        | ENST00000510274.1, ENST00000504658.1, ENST00000428280.1, ENST00000584643.1, ENST00000591918.2                                                    | hsa-miR-1323                                                                                      |
| ELK4         | ENST00000582269.1                                                                                                                                | hsa-miR-3614-5p, hsa-miR-520a-3p, hsa-miR-195-5p, hsa-miR-                                        |
| ERBB3        | NR\_125423.1, ENST00000581633.1                                                                                                                   | 424-5p, hsa-miR-372-3p hsa-miR-512-3p                                                             |
| FGF5         | ENST00000582269.1                                                                                                                                | hsa-miR-542-3p                                                                                    |
| FGFR1        | NR\_125423.1, ENST00000544086.1                                                                                                                   | hsa-miR-424-5p, hsa-miR-486-3p                                                                    |
| FGFR2        | ENST00000444868.2, ENST00000585761.1                                                                                                             | hsa-miR-1323                                                                                      |
| FLT1         | ENST00000609726.1, ENST00000539313.1, ENST00000581633.1                                                                                          | hsa-miR-372-3p                                                                                    |
| FOXO3        | ENST00000444868.2                                                                                                                                | hsa-miR-182-5p                                                                                    |
| GHR          | ENST00000606096.1                                                                                                                                | hsa-miR-195-5p                                                                                    |
| GRB2         | NR\_134920.1, ENST00000585921.1, ENST00000609726.1                                                                                                | hsa-miR-1323                                                                                      |
| IL1R1        | ENST00000544086.1                                                                                                                                | hsa-miR-1323                                                                                      |
| IL2RA        | NR\_038219.1                                                                                                                                      | hsa-miR-122-5p                                                                                    |
| IL6R         | ENST00000592296.1, ENST00000584643.1                                                                                                             | hsa-miR-3614-5p, hsa-miR-451a                                                                     |
| IRAK4        | NR\_039978.1, NR\_125915.1, NR\_125914.1                                                                                                            | hsa-miR-372-3p, hsa-miR-520a-3p, hsa-miR-512-3p                                                   |
| ITGA2        | ENST00000565495.1                                                                                                                                | hsa-miR-424-5p, hsa-miR-372-3p, hsa-miR-195-5p                                                    |
| ITGB8        | NR\_110119.1, ENST00000584643.1                                                                                                                   | hsa-miR-183-5p, hsa-miR-182-5p, hsa-miR-372-3p                                                    |
| MAP3K13      | NR\_110761.1, ENST00000399866.3, ENST00000584643.1,                                                                                               | hsa-miR-183-5p, hsa-miR-542-3p                                                                    |
| MDM2         | ENST00000436249.3                                                                                                                                |                                                                                                   |
| MEF2C        | ENST00000366360.2, ENST00000533008.1                                                                                                             | hsa-miR-542-3p, hsa-miR-3614-5p, hsa-miR-1278                                                     |
| MRAS         | NR\_109940.1, ENST00000510274.1 NR\_023922.2                                                                                                       | hsa-miR-182-5p, hsa-miR-183-5p hsa-miR-424-5p                                                     |
| NFATC3       | ENST00000569088.1                                                                                                                                | hsa-miR-512-3p                                                                                    |
| NR4A1        | NR\_037177.1, ENST00000462717.1, ENST00000568362.1, ENST00000433036.1                                                                             | hsa-miR-542-3p                                                                                    |
| OSMR         | NR\_110,761.1, ENST00000425192.1, ENST00000428280.1, ENST00000558478.1, ENST00000584643.1                                                         | hsa-miR-1323                                                                                      |
| PIK3CD       | ENST00000591918.2 ENST00000585921.1                                                                                                              | hsa-miR-4792 hsa-miR-486-3p                                                                       |
| PIK3R2       | ENST00000585761.1                                                                                                                                | hsa-miR-1323, hsa-miR-182-5p                                                                      |
| PPM1B        |                                                                                                                                                  |                                                                                                   |
| RAP1A        | NR\_023922.2                                                                                                                                      | hsa-miR-512-3p                                                                                    |
| RPS6KA3      | NR\_125423.1, NR\_134920.1, NR\_039978.1, NR\_125914.1, NR\_125915.1, ENST00000591854.1, ENST00000581633.1, ENST00000582536.1, ENST00000444868.2 b    | hsa-miR-183-5p, hsa-miR-372-3p, hsa-miR-195-5p b                                                  |
| SLC2A4 SMAD2 | ENST00000433036.1 c ENST00000582269.1, ENST00000606096.1, ENST00000462717.1,                                                                     | hsa-miR-520a-3p, hsa-miR-512-3p c hsa-miR-1278                                                    |
| SMAD4        | NR\_023922.2, ENST00000510274.1, ENST00000568362.1                                                                                                | hsa-miR-27b-3p, hsa-miR-183-5p, hsa-miR-182-5p                                                    |
| STAT3        | ENST00000526936.1, ENST00000444868.2                                                                                                             | hsa-miR-486-3p                                                                                    |
| STMN1        |                                                                                                                                                  |                                                                                                   |
| THEM4        | ENST00000582269.1, ENST00000366360.2, ENST00000462717.1                                                                                          | hsa-miR-1268a                                                                                     |
|              | NR\_046101.1, NR\_038219.1                                                                                                                         | hsa-miR-512-3p, hsa-miR-183-5p, hsa-miR-372-3p                                                    |

a, b, c The lncRNA-miRNA pairs of interaction relationship.

DE: differentially expressed.

Among the 10 DE miRNAs, all of them (hsa-miR-3614-5p, hsamiR-451a, hsa-miR-1268a, hsa-miR-486-3p, hsa-miR-424-5p, hsamiR-122-5p, hsa-let-7f-1-3p, hsa-miR-1323, hsa-miR-195-5p, and

hsa-miR-27b-3p) were expressed at substantially higher levels in the DM group than in the NC group for both neutrophils and HDMECs-stimulated by neutrophil EXOs. Among them, hsa-miR-

FIGURE 1 | Expression levels of DE lncRNAs (A) and DE miRNAs (B) in the PI3K -Akt, MAPK, AMPK and FoxO signalling pathways validated by real-time quantitative PCR in neutrophils of DM patients and in HDMECs and HSkMCs after stimulation with DM neutrophil EXOs (*DM vs. NC).

<!-- image -->

3614-5p, hsa-miR-451a, hsa-miR-1268a, hsa-miR-486-3p, and hsamiR-122-5p were signi /uniFB01 cantly DE consistent with the results of the miRNA pro le analysis. Among HSkMCs-stimulated by neutrophil /uniFB01 EXOs, the expression levels of hsa-miR-451a and hsa-miR-486-3p were higher in the DM group than in the NC group, while those of hsa-miR-3614-5p, hsa-miR-1268a, hsa-let-7f-1-3p, hsa-miR-195-5p and hsa-miR-27b-3p, were lower ( Figure 1B ).

## DISCUSSION

Increasing amounts of data have recently highlighted the potential contributions of EXOs to vascular injury and muscle damage in DM pathogenesis. In the current study, 10 DE miRNAs in plasma EXOs were identi /uniFB01 ed JDM patients compared with NCs. JDM-derived plasma EXOs can be taken up by human aortic endothelial cells, and induce alteration in multiple genes (59 genes) in these cells, which suggests potential mechanisms by which plasmas EXOs can ultimately target vascular tissue in JDM (Jiang et al., 2019). In addition, DM plasma-derived EVs have been found to trigger proin /uniFB02 ammatory cytokine (IFN β , TNF α and IL-6) release and STING signalling pathway activation in circulating immune cells. The activated STING pathway is preferentially mediated by EV-dsDNA (Li et al., 2021). DE proteins have also been found in DM serum EVs. The number of serum Plexin D1+ EVs is positively associated with muscle

pain or weakness in DM patients, and correlates with the levels of aldolase, white blood cells, neutrophils and platelets. In DM patients after treatment (in clinical remission), the serum levels of Plexin D1+ EVs are signi /uniFB01 cantly decreased (Uto et al., 2021). As EXOs contain multiple RNAs, DNAs, lipids, and proteins, EXOs can be selectively taken up by any neighbouring or distant cells, and reprogram the recipient cells. Thus, they have extremely strong potential to be diagnostic biomarkers and therapeutic nanocarriers, and might also participate in multiple processes of DM pathogenesis.

In this study, the noncoding RNAs pro /uniFB01 les were also changed in DM neutrophil EXOs. Functional analysis suggested that the DE lncRNAs and DE miRNAs might participate in interleukin-6 and IFNβ production, skeletal muscle cell proliferation and development, and endothelial cell development and differentiation, which are associated with DM histopathology. Our validation results and interaction analyses revealed that, many novel and valuable DE lncRNAs and DE miRNAs were cotargeted and altered in the PI3K Akt, MAPK, AMPK and FoxO signalling pathways in the -neutrophil EXO stimulated -HDMECs and HSkMCs. In the pathogenesis of DM, immune activation resulted in capillary destruction and leaded to ischemia and microinfarction, hypoperfusion, and perifascicular atrophy. Vascular endothelial cells injury was the initiating factor of DM pathogenesis, and then caused skeletal muscle damage. The functions and transcriptome levels of endothelial cells and skeletal muscle cells are different. So the

reactions to neutrophil EXOs stimulation were not the same, leading to the expression of DE lncRNAs and miRNAs were not accordant. Several studies have demonstrated that many miRNAs of the PI3K Akt FoxO --pathway participate in the posttranscriptional regulation of skeletal muscle genes, including miR-19b-3p, miR99a-5p, miR-100-5p, miR-222-3p, miR-324-3p, and miR-486-5p (Urbánek and Klotz, 2017; Brown and Webb, 2018).

PI3K Akt, -MAPK and AMPK are major effectors of insulin metabolic action and are essential for glucose homeostasis (Schultze et al., 2012). Once the insulin/insulin-like growth factor (IGF) signalling pathway is stimulated, insulin and IGF receptors are autophosphorylated and recruit downstream PI3K -Akt, MAPK and AMPK signalling pathway members. PI3K is a lipid kinase that generates phosphatidylinositol triphosphate and subsequently activates Akt, a serine/threonine kinase that converts extracellular stimuli into a wide range of cellular responses. The MAPK family is also a protein serine/threonine kinase family that includes c-Jun N-terminal kinase (JNK), p38 MAPK and extracellular-regulated protein kinases. AMPK is mainly known as a conserved and ubiquitously expressed energy sensor (that senses increases in AMP:ATP and ADP:ATP ratios) in eukaryotic cells. In addition to their diverse functions in cellular metabolism, the PI3K -Akt, MAPK and AMPK pathways have also been widely involved throughout evolution in regulating physiological processes such as gene expression, mitosis, motility, proliferation, survival, apoptosis and differentiation, and they might be attractive therapeutic targets for diabetes, cancers and autoimmune diseases (Cargnello and Roux, 2011; Mayer and Arteaga, 2016; Olivier et al., 2018).

FoxO transcription factors are conserved regulators of a variety of cellular processes, including cell cycle regulation, redox balance, proteostasis, apoptosis, metabolism and DNA damage repair. In all species, FoxO transcription factors are subject to extensive posttranslational modi cation, /uniFB01 including phosphorylation, acetylation, ubiquitination and methylation (Link, 2019). Such modi cation of FoxO activity can be regulated by the PI3K /uniFB01 -Akt, MAPK and AMPK signalling pathways upon stimulation by growth factor signalling, oxidative and genotoxic stress, and nutrient deprivation (Brown and Webb, 2018). The complex PI3K Akt, -MAPK, AMPK and FoxO signalling networks play decisive roles in the maintenance of skeletal muscle homeostasis and regulate the differentiation, proliferation and regeneration of muscle cells (Wu et al., 2017; Tia et al., 2018), either together or separately.

According to studies on DM pathogenesis, skeletal muscle in /uniFB02 ammation induces muscle atrophy by inhibiting PI3K Akt --mediated myogenic signals, which are activated by AMPK, p38 MAPK, JNK, mTOR, and IGF-1 (Stitt et al., 2004; Li et al., 2005; Kim et al., 2017; Kim et al., 2018). In a mouse model of autoimmune myositis and in differentiated C2C12 myotubes, cellular immune stimulation and intracellular β -amyloid (A i) β have been found to potentially independently drive muscle atrophy through the PI3K Akt FoxO --pathways (Lee et al., 2012). Furthermore, EXOs released from in /uniFB02 ammatory C2C12 myotubes likely contribute to in /uniFB02 ammation-induced muscle atrophy (Kim et al., 2018). These /uniFB01 ndings suggest that the PI3K Akt, MAPK, AMPK -and FoxO signalling pathways play remarkable roles in muscle in /uniFB02 ammation and damage in DM, possibly even through EXOs.

At present, inhibitors of PI3K Akt (mTOR and ETP-45658), -AMPK (doxorubicin hydrochloride and dorsomorphin dihydrochloride) and MAPK (PD98059, PD184352 and PD0325901) are already being successfully used in the clinic for the treatment of diverse cancer types and in /uniFB02 ammatory diseases; in contrast, the AMPK activator metformin is the only drug targeting protein kinase activity that is widely used today, demonstrating the dual roles of AMPK activation (Arana-Argáez et al., 2010; Farhan et al., 2017). The /uniFB01 ndings of the current study might provide important insights to aid in the search for new DM therapeutics.

## CONCLUSION

This study identi /uniFB01 ed the noncoding RNAs pro /uniFB01 les of neutrophil EXOs. Bioinformatics analysis showed that the predicted target genes of DE lncRNAs and DE miRNAs were enriched in the PI3K -Akt, MAPK, AMPK and FoxO signalling pathways, which suggests their roles in the pathogenesis of DM. These molecules may be useful diagnostic and prognostic biomarkers in the future.

## DATA AVAILABILITY STATEMENT

The bioinformatics analysis datasets presented in this study can be found in the article/ Supplementary Material . The raw data for RNAs sequencing are provided in the repository, the accession number is GSE155281.

## ETHICS STATEMENT

All blood samples were approved by the Ethical Committee of Xiangya Hospital of Central South University (No. 201303293, 201404360, 201212074) in accordance with the 1964 Helsinki Declaration and its later amendments or comparable ethical standards. The patients/ participants provided their written informed consent to participate in this study.

## AUTHOR CONTRIBUTIONS

LL and HZ performed the research and wrote the manuscript; DL and HL collected and managed the clinical samples and data; HZ and XZ devised the research study and revised the manuscript. All authors read and approved the /uniFB01 nal manuscript.

## FUNDING

This study was funded by grants from the National Key Research and Development Program of China (2016YFC0903900), National Natural Science Foundation of China (81671622, 81771765, 81701621), and Hunan Provincial Natural Science Foundation (2018JJ3823, 2019JJ40503).

## ACKNOWLEDGMENTS

The authors thank all the members of the Department of Rheumatology and Immunology, Xiangya Hospital, Central South University for their clinical support.

## REFERENCES

- Arana-Argáez, V. E., Delgado-Rizo, V., Pizano-Martínez, O. E., Martínez-Garcia, E. A., Martín-Márquez, B. T., Muñoz-Gómez, A., et al. (2010). Inhibitors of MAPKPathway ERK1/2 or P38 Prevent the IL-1{beta}-induced Up-Regulation of SRP72 Autoantigen in Jurkat Cells. J. Biol. Chem. 285 (43), 32824 -32833. doi:10.1074/jbc.M110.121087

Bohan, A., and Peter, J. B. (1975). Polymyositis and Dermatomyositis (First of Two Parts). N. Engl. J. Med. 292 (7), 344 -347. doi:10.1056/NEJM197502132920706 Bohan, A., and Peter, J. B. (1975). Polymyositis and Dermatomyositis (Second of Two Parts). N. Engl. J. Med. 292 (8), 403 -407. doi:10.1056/ NEJM197502202920807

- Brown, A. K., and Webb, A. E. (2018). Regulation of FOXO Factors in Mammalian Cells. Curr. Top. Dev. Biol. 127, 165 -192. doi:10.1016/bs.ctdb.2017.10.006
- Callen, J. P. (2000). Dermatomyositis. The Lancet 355 (9197), 53 -57. doi:10.1016/ s0140-6736(99)05157-0
- Cargnello, M., and Roux, P. P. (2011). Activation and Function of the MAPKs and Their Substrates, the MAPK-Activated Protein Kinases. Microbiol. Mol. Biol. Rev. 75 (1), 50 -83. doi:10.1128/MMBR.00031-10
- Dalakas, M. C. (2015). In /uniFB02 ammatory Muscle Diseases. N. Engl. J. Med. 372 (18), 1734 -1747. doi:10.1056/NEJMra1402225
- DeWane, M. E., Waldman, R., and Lu, J. (2019). Dermatomyositis Part I: Clinical Features and Pathogenesis. J. Am. Acad. Dermatol. 82, 267. doi:10.1016/ j.jaad.2019.06.1309
- Dong, X., Gao, X., Dai, Y., Ran, N., and Yin, H. (2018). Serum Exosomes Can Restore Cellular Function In Vitro and Be Used for Diagnosis in Dysferlinopathy. Theranostics 8 (5), 1243 -1255. doi:10.7150/thno.22856
- Farhan, M., Wang, H., Gaur, U., Little, P. J., Xu, J., and Zheng, W. (2017). FOXO Signaling Pathways as Therapeutic Targets in Cancer. Int. J. Biol. Sci. 13 (7), 815 -827. doi:10.7150/ijbs.20052
- Gao, M. Z., Huang, Y. L., Wu, X. D., Xu, Q. W., Ji, R., Gu, B., et al. (2018). Red Blood Cell Distribution Width and Neutrophil to Lymphocyte Ratio Are Correlated with Disease Activity of Dermatomyositis and Polymyositis. J. Clin. Lab. Anal. 32 (1), e22209. doi:10.1002/jcla.22209
- Gao, S., Luo, H., Zhang, H., Zuo, X., Wang, L., and Zhu, H. (2017). Using MultiOmics Methods to Understand Dermatomyositis/polymyositis. Autoimmun. Rev. 16 (10), 1044 -1048. doi:10.1016/j.autrev.2017.07.021
- Gao, S., Zhang, H., Zuo, X., Xiao, Y., Liu, D., Zhu, H., et al. (2019). Integrated Comparison of the miRNAome and mRNAome in Muscles of Dermatomyositis and Polymyositis Reveals Common and Speci /uniFB01 c miRNAmRNAs. Epigenomics 11 (1), 23 -33. doi:10.2217/epi-2018-0064
- Gao, S., Zuo, X., Liu, D., Xiao, Y., Zhu, H., Zhang, H., et al. (2018). The Roles of Neutrophil Serine Proteinases in Idiopathic In /uniFB02 ammatory Myopathies. Arthritis Res. Ther. 20 (1), 134. doi:10.1186/s13075-018-1632-x
- Genschmer, K. R., Russell, D. W., Lal, C., Szul, T., Bratcher, P. E., Noerager, B. D., et al. (2019). Activated PMN Exosomes: Pathogenic Entities Causing Matrix Destruction and Disease in the Lung. Cell 176 (1-2), 113 -e15. doi:10.1016/j.cell.2018.12.002
- Glennon-Alty, L., Hackett, A. P., Chapman, E. A., and Wright, H. L. (2018). Neutrophils and Redox Stress in the Pathogenesis of Autoimmune Disease. Free Radic. Biol. Med. 125, 25 -35. doi:10.1016/j.freeradbiomed.2018.03.049
- Ha, Y. J., Hur, J., Go, D. J., Kang, E. H., Park, J. K., Lee, E. Y., et al. (2018). Baseline Peripheral Blood Neutrophil-To-Lymphocyte Ratio Could Predict Survival in Patients with Adult Polymyositis and Dermatomyositis: A Retrospective Observational Study. PLoS One 13 (1), e0190411. doi:10.1371/journal.pone.0190411 Jaillon, S., Galdiero, M. R., Del Prete, D., Cassatella, M. A., Garlanda, C., and Mantovani, A. (2013). Neutrophils in Innate and Adaptive Immunity. Semin. Immunopathol 35 (4), 377 -394. doi:10.1007/s00281-013-0374-8
- Jiang, K., Karasawa, R., Hu, Z., Chen, Y., Holmes, L., O Neil, K. M., et al. (2019). ' Plasma Exosomes from Children with Juvenile Dermatomyositis Are Taken up

## SUPPLEMENTARY MATERIAL

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fphar.2021.727901/ full#supplementary-material

by Human Aortic Endothelial Cells and Are Associated with Altered Gene Expression in Those Cells. Pediatr. Rheumatol. Online J. 17 (1), 41. doi:10.1186/ s12969-019-0347-0

- Kim, J. S., Lee, Y. H., Chang, Y. U., and Yi, H. K. (2017). PPAR γ Regulates In /uniFB02 ammatory Reaction by Inhibiting the MAPK/NFκ B Pathway in C2C12 Skeletal Muscle Cells. J. Physiol. Biochem. 73 (1), 49 -57. doi:10.1007/s13105016-0523-3
- Kim, S., Lee, M. J., Choi, J. Y., Park, D. H., Kwak, H. B., Moon, S., et al. (2018). Roles of Exosome-like Vesicles Released from In /uniFB02 ammatory C2C12 Myotubes: Regulation of Myocyte Differentiation and Myokine Expression. Cell Physiol Biochem 48 (5), 1829 -1842. doi:10.1159/000492505
- Lahoria, R., Selcen, D., and Engel, A. G. (2016). Microvascular Alterations and the Role of Complement in Dermatomyositis. Brain 139 (Pt 7), 1891 -1903. doi:10.1093/brain/aww122
- Lee, H. K., Rocnik, E., Fu, Q., Kwon, B., Zeng, L., Walsh, K., et al. (2012). Foxo/ atrogin Induction in Human and Experimental Myositis. Neurobiol. Dis. 46 (2), 463 -475. doi:10.1016/j.nbd.2012.02.011
- Li, B. G., Hasselgren, P. O., and Fang, C. H. (2005). Insulin-like Growth Factor-I Inhibits Dexamethasone-Induced Proteolysis in Cultured L6 Myotubes through PI3K/Akt/GSK-3beta and PI3K/Akt/mTOR-dependent Mechanisms. Int. J. Biochem. Cel Biol 37 (10), 2207 -2216. doi:10.1016/j.biocel.2005.04.008
- Li, L., Zuo, X., Liu, D., Luo, H., and Zhu, H. (2020). The Pro /uniFB01 les of miRNAs and lncRNAs in Peripheral Blood Neutrophils Exosomes of Diffuse Cutaneous Systemic Sclerosis. J. Dermatol. Sci. 98 (2), 88 -97. doi:10.1016/ j.jdermsci.2020.02.009
- Li, L., Zuo, X., Xiao, Y., Liu, D., Luo, H., and Zhu, H. (2020). Neutrophil-derived Exosome from Systemic Sclerosis Inhibits the Proliferation and Migration of Endothelial Cells. Biochem. Biophys. Res. Commun. 526 (2), 334 -340. doi:10.1016/j.bbrc.2020.03.088
- Li, S., Li, Y., Chen, B., Zhao, J., Yu, S., Tang, Y., et al. (2018). exoRBase: a Database of circRNA, lncRNA and mRNA in Human Blood Exosomes. Nucleic Acids Res. 46 (D1), D106 -D12. doi:10.1093/nar/gkx891
- Li, Y., Bax, C., Patel, J., Vazquez, T., Ravishankar, A., Bashir, M. M., et al. (2021). Plasma-derived DNA Containing-Extracellular Vesicles Induce STINGMediated Proin /uniFB02 ammatory Responses in Dermatomyositis. Theranostics 11 (15), 7144 -7158. doi:10.7150/thno.59152
- Li, Y., Zhao, J., Yu, S., Wang, Z., He, X., Su, Y., et al. (2019). Extracellular Vesicles Long RNA Sequencing Reveals Abundant mRNA, circRNA, and lncRNA in Human Blood as Potential Biomarkers for Cancer Diagnosis. Clin. Chem. 65 (6), 798 -808. doi:10.1373/clinchem.2018.301291
- Link, W. (2019). Introduction to FOXO Biology. Methods Mol. Biol. 1890, 1 -9. doi:10.1007/978-1-4939-8900-3\_1
- Mayer, I. A., and Arteaga, C. L. (2016). The PI3K/AKT Pathway as a Target for Cancer Treatment. Annu. Rev. Med. 67, 11 -28. doi:10.1146/annurev-med062913-051343
- Mazzone, R., Zwergel, C., Artico, M., Taurone, S., Ralli, M., Greco, A., et al. (2019). The Emerging Role of Epigenetics in Human Autoimmune Disorders. Clin. Epigenetics 11 (1), 34. doi:10.1186/s13148-019-0632-2
- Misunova, M., Salinas-Riester, G., Luthin, S., Pommerenke, C., Husakova, M., Zavada, J., et al. (2016). Microarray Analysis of Circulating Micro RNAs in the Serum of Patients with Polymyositis and Dermatomyositis Reveals a Distinct Disease Expression Pro /uniFB01 le and Is Associated with Disease Activity. Clin. Exp. Rheumatol. 34 (1), 17 -24.
- Navegantes, K. C., de Souza Gomes, R., Pereira, P. A. T., Czaikoski, P. G., Azevedo, C. H. M., and Monteiro, M. C. (2017). Immune Modulation of Some Autoimmune Diseases: the Critical Role of Macrophages and Neutrophils in the Innate and Adaptive Immunity. J. Transl Med. 15 (1), 36. doi:10.1186/s12967-017-1141-8
- Olivier, S., Foretz, M., and Viollet, B. (2018). Promise and Challenges for Direct Small Molecule AMPK Activators. Biochem. Pharmacol. 153, 147 -158. doi:10.1016/j.bcp.2018.01.049

- Peng, Q. L., Zhang, Y. M., Yang, H. B., Shu, X. M., Lu, X., and Wang, G. C. (2016). Transcriptomic Pro /uniFB01 ling of Long Non-coding RNAs in Dermatomyositis by Microarray Analysis. Sci. Rep. 6, 32818. doi:10.1038/srep32818
- Rossaint, J., Kühne, K., Skupski, J., Van Aken, H., Looney, M. R., Hidalgo, A., et al. (2016). Directed Transport of Neutrophil-Derived Extracellular Vesicles Enables Platelet-Mediated Innate Immune Response. Nat. Commun. 7, 13464. doi:10.1038/ncomms13464
- Satoh, T., Okano, T., Matsui, T., Watabe, H., Ogasawara, T., Kubo, K., et al. (2005). Novel Autoantibodies against 7SL RNA in Patients with Polymyositis/ dermatomyositis. J. Rheumatol. 32 (9), 1727 -1733.
- Schultze, S. M., Hemmings, B. A., Niessen, M., and Tschopp, O. (2012). PI3K/AKT, MAPK and AMPK Signalling: Protein Kinases in Glucose Homeostasis. Expert Rev. Mol. Med. 14, e1. doi:10.1017/S1462399411002109
- Shao, S., Fang, H., Zhang, J., Jiang, M., Xue, K., Ma, J., et al. (2019). Neutrophil Exosomes Enhance the Skin Autoin /uniFB02 ammation in Generalized Pustular Psoriasis via Activating Keratinocytes. FASEB J. 33 (6), 6813 -6828. doi:10.1096/fj.201802090RR
- Stitt, T. N., Drujan, D., Clarke, B. A., Panaro, F., Timofeyva, Y., Kline, W. O., et al. (2004). The IGF-1/PI3K/Akt Pathway Prevents Expression of Muscle AtrophyInduced Ubiquitin Ligases by Inhibiting FOXO Transcription Factors. Mol. Cel 14 (3), 395 -403. doi:10.1016/s1097-2765(04)00211-4
- Tartar, D. M., Chung, L., and Fiorentino, D. F. (2018). Clinical Signi /uniFB01 cance of Autoantibodies in Dermatomyositis and Systemic Sclerosis. Clin. Dermatol. 36 (4), 508 -524. doi:10.1016/j.clindermatol.2018.04.008
- Tia, N., Singh, A. K., Pandey, P., Azad, C. S., Chaudhary, P., and Gambhir, I. S. (2018). Role of Forkhead Box O (FOXO) Transcription Factor in Aging and Diseases. Gene 648, 97 -105. doi:10.1016/j.gene.2018.01.051
- Urbánek, P., and Klotz, L. O. (2017). Posttranscriptional Regulation of FOXO Expression: microRNAs and beyond. Br. J. Pharmacol. 174 (12), 1514 -1532. doi:10.1111/bph.13471
- Uto, K., Ueda, K., Okano, T., Akashi, K., Takahashi, S., Nakamachi, Y., et al. (2021). Identi /uniFB01 cation of Plexin D1 on Circulating Extracellular Vesicles as a Potential Biomarker of Polymyositis and Dermatomyositis. Rheumatology (Oxford) , keab588. doi:10.1093/rheumatology/keab588
- Vargas, A., Roux-Dalvai, F., Droit, A., and Lavoie, J. P. (2016). Neutrophil-Derived Exosomes: A New Mechanism Contributing to Airway Smooth Muscle Remodeling. Am. J. Respir. Cel Mol Biol 55 (3), 450 -461. doi:10.1165/ rcmb.2016-0033OC

- Wahren-Herlenius, M., and Dörner, T. (2013). Immunopathogenic Mechanisms of Systemic Autoimmune Disease. Lancet 382 (9894), 819 -831. doi:10.1016/ S0140-6736(13)60954-X
- Wu, C. L., Satomi, Y., and Walsh, K. (2017). RNA-seq and Metabolomic Analyses of Akt1Mediated Muscle Growth Reveals Regulation of Regenerative Pathways and Changes in the Muscle Secretome. BMC Genomics 18 (1), 181. doi:10.1186/s12864-017-3548-2
- Xiao, Y., Zhu, H., Li, L., Gao, S., Liu, D., Dai, B., et al. (2019). Global Analysis of Protein Expression in Muscle Tissues of Dermatomyositis/polymyosisits Patients Demonstrated an Association between Dysferlin and Human Leucocyte Antigen A. Rheumatology 58, 1474. doi:10.1093/rheumatology/kez085
- Yáñez-Mó, M., Siljander, P. R., Andreu, Z., Zavec, A. B., Borràs, F. E., Buzas, E. I., et al. (2015). Biological Properties of Extracellular Vesicles and Their Physiological Functions. J. Extracell Vesicles 4, 27066. doi:10.3402/jev.v4.27066
- Yang, W., Wang, X., Zhang, W., Ying, H., Xu, Y., Zhang, J., et al. (2017). Neutrophillymphocyte Ratio and Platelet-Lymphocyte Ratio Are 2 New In /uniFB02 ammatory Markers Associated with Pulmonary Involvement and Disease Activity in Patients with Dermatomyositis. Clin. Chim. Acta 465, 11 -16. doi:10.1016/j.cca.2016.12.007
- Yu, G., Wang, L. G., Han, Y., and He, Q. Y. (2012). clusterPro /uniFB01 ler: an R Package for Comparing Biological Themes Among Gene Clusters. OMICS 16 (5), 284 -287. doi:10.1089/omi.2011.0118

Con ict of Interest: /uniFB02 The authors declare that the research was conducted in the absence of any commercial or /uniFB01 nancial relationships that could be construed as a potential con /uniFB02 ict of interest.

Publisher s Note: ' All claims expressed in this article are solely those of the authors and do not necessarily represent those of their af /uniFB01 liated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

Copyright © 2021 Li, Zuo, Liu, Luo and Zhu. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.