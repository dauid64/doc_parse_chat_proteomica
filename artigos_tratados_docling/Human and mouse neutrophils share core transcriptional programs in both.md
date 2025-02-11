1234567890():,;

1234567890():,;

## Human and mouse neutrophils share core transcriptional programs in both homeostatic and in /uniFB02 amed contexts

Received: 14 December 2022

Accepted: 14 November 2023

Check for updates

Nicolaj S. Hackert 1,2,3,4,12 , Felix A. Radtke 1,2,5,6,7,12 , Tarik Exner 1,2,12 , Hanns-Martin Lorenz 1 , Carsten Müller-Tidow 8,9 , Peter A. Nigrovic 3,5 , Guido Wabnitz 2 &amp; Ricardo Grieshaber-Bouyer 1,2,9,10,11

Neutrophils are frequently studied in mouse models, but the extent to which /uniFB01 ndings translate to humans remains poorly de /uniFB01 ned. In an integrative analysis of 11 mouse and 13 human datasets, we /uniFB01 nd a strong correlation of neutrophil gene expression across species. In in /uniFB02 ammation, neutrophils display substantial transcriptional diversity but share a core in /uniFB02 ammation program. This programincludesgenesencodingIL-1familymembers,CD14,IL-4R,CD69,and PD-L1. Chromatin accessibility of core in /uniFB02 ammation genes increases in blood compared to bone marrow and further in tissue. Transcription factor enrichment analysis implicates members of the NFκ B family and AP-1 complex as important drivers, and HoxB8 neutrophils with JunB knockout show a reduced expression of core in /uniFB02 ammation genes in resting and activated cells. In independent single-cell validation data, neutrophil activation by type I or type II interferon, G-CSF, and E. coli leads to upregulation in core in /uniFB02 ammationgenes. In COVID-19 patients, higher expression of core in /uniFB02 ammation genes in neutrophils is associated with more severe disease. In vitro treatment with GMCSF, LPS, and type II interferon induces surface protein upregulation of core in /uniFB02 ammation members. Together, we demonstrate transcriptional conservation in neutrophils in homeostasis and identify a core in /uniFB02 ammation program shared across heterogeneous in /uniFB02 ammatory conditions.

<!-- image -->

Neutrophils mediate homeostatic and in /uniFB02 ammatory processes and display substantial phenotypic and functional heterogeneity. While animal models fuel fundamental discoveries in immunology, differences between humans and mice can impair the translation of /uniFB01 ndings 1 . To maximize impact on human health, life sciences increasingly bene /uniFB01 t from seamless transitions between the mouse and human system. However, due to structural and functional differences in genomes, it is often unclear which aspects re /uniFB02 ect conserved biology. Therefore, integrative analyses of cellular systems across species are important for the success of translational research.

Structurally, the mouse and human genomes are closely related. They harbor ~16,000 protein-coding genes considered to be one-to-

one orthologs with high con /uniFB01 dence 2 . However, structural orthology does not equal functional similarity since expression patterns of orthologous genes can deviate substantially across organs and development 3 . In leukocytes, expression of most orthologous genes and lineage-speci /uniFB01 c genes, in particular, is well-conserved between humans and mice 4 . Despite this overall similarity, different species can display substantial differences in ortholog expression between tissues . 5 For example, human neutrophils are highly abundant in defensins, yet their mouse orthologs are expressed in gut epithelial cells, not in neutrophils. Furthermore, neutrophils display high phenotypic and functional heterogeneity as a function of organ, maturation, and in /uniFB02 ammatory condition 6 9 -, but whether a core in /uniFB02 ammation

program consisting of genes that become induced across a range of in /uniFB02 ammatory conditions exists is not known. It is thus unclear how similarities and differences between human and mouse transcriptomes should be interpreted, particularly in the context of different in /uniFB02 ammatory conditions.

To address these gaps in knowledge, we perform an integrative analysis of resting and in /uniFB02 amed leukocytes from humans and mice and assess the degree of conservation of gene expression. We /uniFB01 nd that human and mouse transcriptomes can be analyzed together and that lineage-speci /uniFB01 c gene expression was closely related between humans and mice. We further study how the neutrophil transcriptome changes in in /uniFB02 ammation,using a wide range of studies covering in vitro and in vivo in /uniFB02 ammation as well as resting conditions in human 10 -21 and mouse 12,22 31 -. While transcriptional responses to different activating stimuli are heterogeneous, we identify a core in /uniFB02 ammation program in neutrophils conserved across species and conditions. We predict upstream regulators and /uniFB01 nd increasing accessibility of core in /uniFB02 ammation program members in ATAC-seq. JunB - -/ HoxB8cells display a lower upregulation of core in /uniFB02 ammation genes when stimulated with zymosan compared to wild-type cells. In single-cell RNA-seq data from resting and activated neutrophils, stimulation with type I and II interferon, G-CSF, E. coli is associated with higher expression of core in /uniFB02 ammation genes. Further, neutrophils from COVID-19 patients with more severe disease display higher expression of core in /uniFB02 ammation genes. Finally, we validated members of the core in /uniFB02 ammation program using /uniFB02 ow cytometry of stimulated human and mouse neutrophils and identi /uniFB01 ed an interplay between tissue of origin and stimulation in driving the phenotype of the neutrophil in /uniFB02 ammatory response. Our approach illustrates that multiple datasets of mouse and human gene expression data can be effectively combined to identify patterns shared across conditions and conserved across species. This approach can be transferred to other cell types and organisms to facilitate studies comparing gene expression across species.

## Results

## Integrative analysis of leukocyte gene expression across species

To assess gene expression similarities and differences between human and mouse immune cells, we obtained bulk RNA-seq data from six sorted leukocyte lineages from the Haemopedia atlas 12,32 (Supplementary Fig. 1). This dataset consisted of a total of 76 samples of T cells, B cells, dendritic cells, monocytes, NK cells, and neutrophils (Supplementary Fig. 1). Sequencing depths for samples across all lineages are shown in Supplementary Fig. 2a, b, and detailed quality control metrics are summarized in Supplementary Data 1. We then integrated gene expression matrices by mapping protein-coding, one-to-one orthologous genes with high con /uniFB01 dence, according to ENSEMBL 33 .

To evaluate the robustness of this approach, we performed a principal component analysis on the integrated expression matrix. For each lineage, up to 200 lineage-associated genes were selected. Here, sample distribution was driven predominantly by lineage, followed by species (Fig. 1a). As envisioned, lineage-associated gene expression was highest in each respective lineage and occurred across species in all lineages (Fig. 1b). Similarly, clustering of sample-wise Pearson correlation coef /uniFB01 cients based on these genes was driven predominantly by lineage, con /uniFB01 rming that in our analytical approach, lineage identity dominates species differences (Fig. 1c).

Correspondingly, expression of key lineage-associated genes was highly conserved between humans and mice (Fig. 1d), such as CSF3R and CHI3L1 in neutrophils, CD19 and CD22 in B cells, CD3 molecules and CD28 in T cells, NKG7 and GZMA in NK cells, MSR1 and SERPINB2 in monocytes and FLT3 and MYCL in dendritic cells. The highest correlation between human and mouse gene expression was observed in neutrophils ( r =0.79), followed by T cells (0.65), B cells (0.65),

Monocytes (0.56), and a weaker correlation in NK cells (0.24) and dendritic cells (0.22) (Fig. 1d).

This analysis demonstrates that mapping one-to-one orthologs allows an integrated analysis of leukocyte transcriptomes across species to identify conserved and divergent expression patterns of structurally related genes. Of note, although these data indicate a higher correlation in neutrophils compared to other lineages, this effect may have been in /uniFB02 uenced by smaller library complexities in neutrophils.

## Transcriptional conservation in resting neutrophils

To systematically analyze which genes display similar and divergent expression across species, we integrated transcriptional pro /uniFB01 les of resting (not activated) neutrophils available through the Sequence ReadArchive(SRA).Inthis context, resting neutrophils werede /uniFB01 nedas those isolated from blood or tissue in the absence of disease or experimental manipulation. In a total of 84 human and 39 mouse samples, we observed a high correlation in overall gene expression, transcription factor expression, and lineage-associated gene expression across humans and mice (Pearson s ' r between 0.78 -0.87, P &lt;2.2× 10 -16 ) (Fig. 2a). These results were remarkably similar to those obtained from the more homogenous Haemopedia dataset, further illustrating the robustness of this approach even when integrating multiple datasets from different sources.

We next focused on neutrophil lineage-associated genes and de ned /uniFB01 /uniFB01 ve GENE: Gene ( HUMAN: Mouse ) pairs based on their expression patterns. In addition to one-to-one orthologs, we considered highcon dence one-to-many and many-to-many orthologs. /uniFB01

Orthologs with high expression in both humans and mice included the key neutrophil genes CSF3R (encoding the G-CSF receptor), CXCR2 NCF4 , (neutrophil cytosolic factor 4), the transcription factors MCL1 SPI1 , (encoding PU.1, an essential transcription factor for terminal granulopoiesis 34,35 ) and JUNB , a transcription factor prominently expressed in late neutrotime which plays a vital role in the in /uniFB02 ammatory response of neutrophils 9,36 (Fig. 2b). As CSF3R , CXCR2 and JUNB expression changes along neutrophil development, their concordance in expression might suggest that the analyzed neutrophils from humans and mice were of comparable developmental stage.

Orthologs with higher expression in human neutrophils included FCGR3A and FCGR3B (encoding CD16A and CD16B, respectively), whichboth areone-to-many orthologs of mouse Fcgr4 . This group also included the receptor for activated complement ( C5AR1 ) and CXCR1 , the receptor for CXCL8 (human)/KC (mouse). Genes with higher expression in mouse neutrophils included the protease Mmp9 Camp , (encoding Cathelicidin Antimicrobial Peptide), Il1b , and Retnlg (encoding Resistin-like gamma) (Fig. 2b).

Of note, most genes in categories 1 -3 were one-to-one orthologs, although 13/133 (9.8 %) were one-to-many orthologs. However, wellknown neutrophil genes without one-to-one orthologs were also identi /uniFB01 ed (categories 4 and 5) and included CXCL8 in humans, a cytokine abundantly expressed in blood neutrophils, and Ccl6 , one of the most abundant chemokines in mouse neutrophils (Fig. 2b). Enrichment for neutrophil-related GO terms was found across all /uniFB01 ve groups of genes (Supplementary Fig. 3).

Thus, while resting human and mouse neutrophils display conserved expression of many key neutrophil genes and transcription factors, gene expression can deviate substantially in the same lineage between species, even for structurally highly related genes.

## A core in /uniFB02 ammation program is shared across conditions and conserved across species

We next assessed how the expression of one-to-one structural orthologs changes in different in /uniFB02 ammatory contexts. Neutrophils display varied phenotypes in homeostasis and in /uniFB02 ammation 6,7,9,37 , but it is unknown if a proportion of the transcriptional characteristics of

<!-- image -->

<!-- image -->

<!-- image -->

different neutrophil states is shared across different in /uniFB02 ammatory conditions . 9 Here, resting neutrophils were de /uniFB01 ned as above and compared with their respective in /uniFB02 ammatory condition.

To identify changes in in /uniFB02 ammation, we analyzed 11 studies encompassing a total of 46 resting and 66 activated neutrophil samples across different conditions (Fig. 3a, Supplementary Data 2). We

<!-- image -->

tested for differential expression of genes with high-con /uniFB01 dence oneto-one orthologs according to ENSEMBL separately within each study, comparing all reported conditions against their own resting controls to reduce the effect of technical variation between studies.

Compared to controls, in /uniFB02 amed neutrophils displayed 975 (median) differentially expressed genes (adjusted P &lt; 0.05, absolute

## Fig. 1 | Integrative analysis of leukocyte gene expression across species.

a Principal component analysis based on per-species mean-centered log2(CPM) of lineage-speci /uniFB01 c genes shows a distribution driven predominantly by lineage. b Concordant expression of the top lineage-speci /uniFB01 c genes for each lineage in each species. Shown is the average of log2(CPM) centered expression values in each lineage. The number of lineage-speci /uniFB01 c genes shown is indicated on the left, up to 200 genes are shown per lineage. For each lineage, 8 genes with the highest expression in the respective cell line are labeled. c Lineage-speci /uniFB01 c gene expression dominates the species effect. Shown is the clustering of Pearson s ' R based on the

centered expression of top lineage-speci /uniFB01 c genes. d Neutrophils display the strongest correlation of lineage-speci /uniFB01 c gene expression across humans and mice compared to other leukocyte lineages. Gene expression (mean-centered log2(CPM)) of lineage-speci /uniFB01 c genes was de /uniFB01 ned as above. Pearson correlation coef /uniFB01 cient and P -value (two-sided) between human (x) and mouse (y) gene expression are shown on the top left (B cells: r =0.65, P &lt;2.2e-16; Dendritic cells: r =0.22, P =0.3; Monocytes: r =0.56, P &lt;2.2e-16; Neutrophils: r =0.79, P &lt;2.2e-16; NK cells: r =0.24, P =0.005; T cells: r =0.65, P &lt;2.2e-16). The top 10 most abundantly expressed genes are labeled. Source data are provided as a Source Data /uniFB01 le.

log2 fold change ≥ 0.5). These comprised 621 (median) signi /uniFB01 cantly increased and 205 (median) signi /uniFB01 cantly decreased genes (Supplementary Fig. 4a). Both the number of differentially expressed genes and the genes themselves were heterogeneous -concordant with the diverse transcriptional responses neutrophils can undergo in in /uniFB02 ammation.

We next searched for potential overlap in the in /uniFB02 ammatory response shared across conditions. Such an overlap may represent a ' core in /uniFB02 ammation program , from which neutrophils preferentially ' upregulate genes across a broad range of activating conditions.

WeusedFisher s combined test to obtain a combined test statistic ' for each gene, summarizing individual comparisons from all datasets (Supplementary Data 3). Based on the elbow of the P -value-rank plot, weselected from the top 500 genes with the lowest P -value those with absolute log2 fold change ≥ 0.5 (Fig. 3b).

A total of 221 genes displayed consistent changes in in /uniFB02 ammation across studies: 179 genes were upregulated across comparisons (the ' core in /uniFB02 ammation program ), ' and 42 genes were downregulated (Fig. 3c). Effect sizes of those 221 up- and downregulated genes agreed well across all tested comparisons and across species (Fig. 3c, Supplementary Fig. 4b).

Core in /uniFB02 ammationgenesincluded the IL-1 molecules IL1A and IL1B , the LPS co-receptor CD14 , the adhesion molecule ICAM1 , the lectin receptor CD69 , CD40 , IL4R and CD274 (encoding PD-L1) (Fig. 3c, d). Downregulated genes in in /uniFB02 ammation included the cyclin-dependent kinase CDK5R1 , TLR5 (encoding Toll Like Receptor 5, an essential pathogen recognition receptor 38 ), CXCR4 , CD101 , and the member of the mitogen-activated protein kinase family MAP3K15 (Fig. 3c, d).

As expression of CD101 and CXCR4 changes throughout neutrophil maturation and aging, we compared the fold change of these markers between neutrophils activated in vitro and those activated in vivo to rule out the effects of differential release from the bone marrow under stress. No differences were observed in either marker (Supplementary Fig. 4c), suggesting that the transcriptional downregulation of CXCR4 and CD101 observed during neutrophil activation are cell-intrinsic and do not re /uniFB02 ect a different maturation stage of neutrophils captured in the in vivo studies.

On the level of individual samples, we could con /uniFB01 rm that the group of 179 core in /uniFB02 ammation genes had either weak or absent expression in healthy neutrophils and were induced in in /uniFB02 amed neutrophils (Fig. 3d).

Gene set enrichment analysis identi /uniFB01 ed a conserved enrichment of pathways related to apoptosis, in /uniFB02 ammatory response, IL-2 and IL-6 signaling, IFNγ response, and TNF signaling via NFKB and KRAS signaling (Fig. 3e).

Taken together, this integrative analysis of resting and activated neutrophils nominated a core in /uniFB02 ammation program in neutrophils which is shared across in /uniFB02 ammatory conditions and across species.

## The core in /uniFB02 ammation program is detectable using different analytical strategies and in single-cell data

To further test the robustness of the core in /uniFB02 ammation program, we performed two independent analyses. Using a linear mixed model, we observed high replicability of our results, with differentially expressed genes (absolute β ≥ 1, P adj &lt;0.05) identi /uniFB01 ed by the linear mixed model

showing a strong skewing toward low Fisher P -values and a π 1 -statistic of 0.71 (Supplementary Fig. 5).

We additionally assessed the replicability of differentially expressed genes between all tested comparisons. Median values of the π 1 -statistic ranged from 0.06 to 0.60, depending on the study, and, importantly, did not show systematic species-driven differences (Supplementary Fig. 6a). Normalized enrichment scores for differentially expressed gene sets were in concordance with up-/downregulation of the tested sets across all studies, supporting the existence of a shared core in /uniFB02 ammation program. Of note, the downregulation of speci /uniFB01 c genes in in /uniFB02 ammation was more variable across studies and hence less informative (Supplementary Fig. 6b). Pearson correlation coef /uniFB01 cients of log2 fold change values showed strong positive skewing, again pointing toward a core in /uniFB02 ammatory response across conditions and species (Supplementary Fig. 6c).

As an additional analytical approach, we performed a weighted correlation network analysis (WGCNA) 39 . WGCNAconstructs correlation networks and can help to identify clusters of genes ( modules ) that are ' ' co-expressed across different conditions. It identi /uniFB01 ed four modules (19, 5, 8, and 4) with signi /uniFB01 cant enrichment for core in /uniFB02 ammatory response genes(Fisher s exact test, ' Padj &lt;0.05). Gene expression within those four modules increased in in /uniFB02 ammation and contained several members of the core in /uniFB02 ammation program (Supplementary Fig. 7).

For validation purposes, we analyzed four recent single-cell RNAsequencing datasets that had not been used to derive the core in /uniFB02 ammation program. These included neutrophils from healthy control individuals and those with mild to moderate or severe COVID19 (Combes et al., dataset 1) 40 , human neutrophils stimulated with G-CSF, IFNβ or IFNγ (Montaldo et al., datasets 2+3) 41 and mouse neutrophils infected with E. coli (Xie et al., dataset 4) . 7

Expression of most of the 179 core in /uniFB02 ammation genes increased in in /uniFB02 amed neutrophils (Fig. 4a). A gene set was created based on the 179 core in /uniFB02 ammation genes, and changes in expression were tested compared to random background genes with the same expression abundance. A signi /uniFB01 cant increase in the core in /uniFB02 ammation genes was detected in all conditions and was higher in patients with severe compared to mild to moderate COVID-19 (Fig. 4b). However, examination of the expression of the core in /uniFB02 ammation program on a single cell level indicated heterogeneity within the population of neutrophils, which was characterized by the presence of groups of cells with exceptionally high or low expression of the de /uniFB01 ned gene set in in /uniFB02 amed states (Fig. 4c).

## The core in /uniFB02 ammation program shows conserved transcriptional regulation across species

To identify putative regulators of neutrophil activation in in /uniFB02 ammation, we applied transcription factor (TF) enrichment analysis individually to up- and downregulated genes in each study. TF enrichment across mouse and human in /uniFB02 amed neutrophils was highly consistent in TFs with decreasing (Supplementary Fig. 8a) and increasing (Supplementary Fig. 8b) activity.

Transcription factors that we found to be enriched in genes expressed in resting neutrophils include AKNA, PU.1 (encoded by SPI1 ), FOXO3, FOXO1, TFEB, RARA, and STAT5B (Supplementary Fig. 8a). Transcription factors that we found to be enriched in genes associated

<!-- image -->

a

b

with in /uniFB02 amed neutrophils included CSRNP1, PLSCR1, FOS, FOSB, the NF- B κ components NFKB1/NFKB2, the emergency granulopoiesis transcription factor CEBPB and JUNB (Supplementary Fig. 8b).

To reduce this selection of transcription factors to those with the highest changes in in /uniFB02 ammation, we compared the predicted regulatory activity of transcription factors and their respective gene

expression in in /uniFB02 ammation. This analysis highlighted that the genes encoding for CSRNP1, JUNB, CEBPB, XBP1, and ETS2 were strongly upregulated in in /uniFB02 amed neutrophils while also displaying strongly increased regulatory activity (Fig. 5a).

On the level of individual studies, we also found high consistency in the transcription factors predicted to be enriched in genes

Fig. 2 | Conservation of neutrophil gene expression in homeostasis. a Strong correlation of gene expression between resting human (x) and mouse (y) blood neutrophils. Left: all genes ( r =0.84, P &lt;2.2e-16). Middle: transcription factors, highlighted in green ( r =0.87, P &lt;2.2e-16). Transcription factors were retrieved from a curated set of transcription factors in ChEA3. The top 5 TFs (based on the sum of the average expression in human and mouse) were labeled and highlighted in red. Additionally, we manually labeled and highlighted the genes JUND, KLF2, ATF3, CEBPA, CEBPB , and CEBPE . Right: lineage-speci /uniFB01 c genes as depicted and de ned in Fig. 1, highlighted in green ( /uniFB01 r =0.78, P &lt;2.2e-16). Neutrophil genes were labeled as in Fig. 1c and highlighted in red. Shown are (log2(TPM+1)) expression values. Pearson correlation coef /uniFB01 cients between human and mouse gene expression for the three groups as well as P -values (two-sided) are shown in the upper left of each panel. b Neutrophil lineage-associated genes with orthologs can show

concordant or discordant expression across species. Gene expression heatmap (log2(TPM+1)) of neutrophil lineage-associated genes that were assigned to /uniFB01 ve different expression pro /uniFB01 le groups: high expression in both species, high expression in human/mouse and low in the other species, high in human/mouse and no high-con /uniFB01 dence ortholog; see ' Methods . Gene-gene pairs of particular impor-' tance in neutrophils are highlighted (HUMAN SYMBOL: Mouse Symbol). Annotated are Orthology relationships between the respective genes as well as species in which the gene was detected as lineage-associated. Right, violin plots of selected gene-gene-pairs show their expression in individual samples for each species. Benjamini-Hochberg adjusted P -values derived from a gene-wise likelihood ratio test between two linear mixed models with and without species as /uniFB01 xed effect are shown for each highlighted gene-gene pair; see ' Methods . Source data are pro-' vided as a Source Data /uniFB01 le.

upregulated and downregulated in activated neutrophils (Supplementary Fig. 8c). These results were consistent with an independent enrichment analysis performed separately for each species (Supplementary Fig. 8d, e).

## Migration into tissue and activation signi /uniFB01 cantly enhance chromatin accessibility and expression of core in /uniFB02 ammation genes

If genes in the core in /uniFB02 ammation program are predisposed to be upregulated, then chromatin accessibility for these genes should increase upon neutrophil maturation, migration into tissues, and exposure to in /uniFB02 ammatory stimuli.

To test this hypothesis, we analyzed chromatin accessibility data derived from bone marrow, blood, and an air pouch model of acute in /uniFB02 ammation. These data were generated using Assay for Transposase-Accessible Chromatin using sequencing (ATAC-Seq), a method that tests genome-wide chromatin accessibility. Brie /uniFB02 y, ATAC-seq allows the analysis of chromatin accessibility by sequencing DNA fragments that are bound by a hyperactive Tn5 transposase, which preferentially inserts sequencing adapters into open chromatin regions 42 . In the air pouch model (executed on C57BL/6J mice), blood neutrophils /uniFB01 rst migrate into a sterile membrane in the skin before being activated by zymosan in the air pouch 36 . Of the 179 core in /uniFB02 ammation program genes, 29 displayed increasing accessibility in blood vs. bone marrow, compared to only 10 genes with decreased accessibility (Fig. 5b). Neutrophils that had transmigrated from the blood into the membrane displayed enhanced accessibility of 78 genes. This increase was signi /uniFB01 cantly ( P = 5.1 × 10 -9 ) higher than the increase of 29 genes for neutrophils in blood compared to bone marrow.

Similar skewing toward enhanced accessibility of core in /uniFB02 ammation genes was observed when membrane vs. bone marrow (89 up, P =1.2 × 10 -13 ), in /uniFB02 amed air pouch vs. blood (85 up, P =1.5 × 10 -11 ), and in /uniFB02 amed air pouch vs. bone marrow (100 up, P =2.1 × 10 -17 ) were compared to blood vs. bone marrow. (Fig. 5b). The number of genes with increased accessibility was signi /uniFB01 cantly higher than expected by chance, as compared to the accessibility of randomly selected background genes. Importantly, the genes with increased and decreased accessibility were highly consistent across the comparisons (Fig. 5c).

After /uniFB01 nding that core in /uniFB02 ammation genes have increased chromatin accessibility even before the onset of in /uniFB02 ammation, we searched for potential driver transcription factors displaying increasing expression and regulatory activity in in /uniFB02 ammation. Comparing motif enrichment (HOMER) with actual expression change in air pouch vs. blood, we observed an increase in both measures for a remarkably restricted set of transcription factors, namely ATF3, BATF, FOSL1, JUNB, and JUN (Fig. 5d).

We next investigated whether the core in /uniFB02 ammation program represents a group of genes from which neutrophils preferentially draw upon exposure to in /uniFB02 ammatory stimuli. If this were the case, then it would be more likely for core in /uniFB02 ammation genes to be

upregulated in in /uniFB02 ammation compared to all other genes. We analyzed RNA-seq data from differentiated HoxB8 neutrophils stimulated with or without zymosan for 2 h 36 . We observed that in activated neutrophils, a signi /uniFB01 cantly higher proportion of core in /uniFB02 ammation genes (107/179 ≈ 60 %) was upregulated than expected by chance (36 -74 genes in 1000 simulations using expression-matched background genes; Poverrepresentation =6.5×10 -41 ) (Fig. 5e).

When evaluating predicted conserved regulatory activity and change in chromatin accessibility together, JUNB emerged as a prominently affected transcription factor and has previously been shown to control neutrophil activation 36 and to be highly expressed upon neutrophil activation 43 . On the other hand, CEBPB has previously been shown to be a key transcription factor mediating emergency granulopoiesis 44 and showed a high predicted regulatory activity in our analysis with limited changes in chromatin accessibility. To assess the impact of two transcription factors identi /uniFB01 ed in our enrichment analysis on the expression of core in /uniFB02 ammation program genes, we repeated the same analysis in differentiated HoxB8 neutrophils carrying a genetic knockout of either JunB or Cebp β . CEBPB showed upregulation in in /uniFB02 amed neutrophils as well as increased regulatory activity. In addition, JUNB, which plays an important role in the in /uniFB02 ammatory response of neutrophils 9,36 , also had increased motif enrichment in the air pouch vs. blood comparison.

Based on these analyses, we expected a modest reduction in the expression of core in /uniFB02 ammation genes in Cebp β - -/ cells and a stronger reduction in JunB - -/ cells. Indeed, this was the case: In a direct comparison of resting knockout ( JunB - -/ and Cebp β - -/ ) versus wild-type cells, we observed a signi /uniFB01 cantly stronger downregulation of the core in /uniFB02 ammation program in JunB - -/ cells (69 genes; P =1.5 × 10 -9 ) than in Cebp β - -/ cells (43 genes; P =0.0011) (Fig. 5e and Supplementary Fig. 9).

Comparing zymosan-stimulated knockout cells versus wild-type cells, we again saw a signi /uniFB01 cant downregulation of core in /uniFB02 ammation genes in the JunB - -/ condition (51 genes; P = 0.0025) but not in the Cebp β - -/ condition (25 genes; P = 0.79) (Fig. 5e and Supplementary Fig. 9).

Together, these results indicate that maturation and migration into an in /uniFB02 amedtissuesite predisposeneutrophilsto upregulate genes of the core in /uniFB02 ammation program and that knockout of Cebp β and especially JunB leads to a weaker induction of core in /uniFB02 ammation genes compared to WT cells.

## Membersofthe core in /uniFB02 ammation program can be validated on the protein level in activated human and mouse neutrophils

To validate members of the core in /uniFB02 ammation program experimentally, we /uniFB01 ltered the list of genes by surface proteins, yielding 36 markers (Fig. 6a) 45 . Based on antibody availability, we developed a /uniFB02 ow cytometry panel including canonical lineage markers (human: CD15, mouse: Ly6G) and /uniFB01 ve proteins predicted to be part of the core in /uniFB02 ammation program: CD14, CD69, CD40, CD274 (PD-L1) and IL-4R (Supplementary Tables 1 and 2).

<!-- image -->

Weisolated human neutrophils from peripheral blood and mouse neutrophils from bone marrow and cultured them over 48 h with or without the addition of GM-CSF + LPS and GM-CSF + IFNγ (Fig. 6b).

Prolonged cell culture without activation led to an increase in CXCR4andlossof CD62L and CD101 in human cells, while mouse cells showed a reversed phenotype with upregulation of CD62L and CD101

as well as a downregulation of CXCR4, suggesting continued maturation of bone marrow neutrophils in vitro and not classical neutrophil aging (Supplementary Fig. 10). Compared to unstimulated cells, activated mouse neutrophils signi /uniFB01 cantly upregulated the predicted core in /uniFB02 ammationprogram markers CD14, CD40, CD69, PD-L1, and IL-4R in the condition containing LPS and all but CD69 in the condition

Fig. 3 | A core in /uniFB02 ammation program is conserved across mouse and human neutrophils. a Overview of the 11 studies integrated for analysis. Differential expression testing was performed independently for each study, resting neutrophils within each study were used as control. b A combined analysis of the neutrophil response to activation/in /uniFB02 ammation identi /uniFB01 es 179 consistently upregulated (core in /uniFB02 ammation program) and 42 downregulated genes in in /uniFB02 ammation. Shown are all ( N =9697) tested genes ranked by their -log10 BenjaminiHochberg adjusted Fisher P -value (adjusted Fisher s combined test on two-sided ' P -values from individual differential expression analyses for each comparison). The 500 genes with the lowest P -values were subjected to an additional /uniFB01 ltering step based on a log2 fold change cutoff ≥ 0.5 and ≤-0.5 for upregulated and downregulated genes. Highlighted ( IL4R , CD14 CD69 CD274 CD40 , , , ) upregulated genes were validated experimentally (Figs. 6 and 7). c 42 genes downregulated in in /uniFB02 ammation and 179 core in /uniFB02 ammation genes are shared across studies. Shown are the log2 fold changes across comparisons of genes up- and downregulated in

in /uniFB02 ammation. Rows represent a comparison, columns represent genes that passed our meta-analysis thresholds. Columns are arranged by the mean log2 fold change across all comparisons. For each direction, the 15 genes with the highest absolute log2 fold change are labeled, as well as genes encoding for proteins validated in Figs. 6 and 7. d Core in /uniFB02 ammationgenes are not expressed in resting neutrophils in both species and are induced upon activation. Shown is a heatmap with relative expression values ( -score for each gene across samples) of the core in z /uniFB02 ammation genes. Each column represents a gene, and each row a sample. P -values: Results of a Benjamini-Hochberg adjusted Fisher s combined test. We labeled the top 20 genes ' with the lowest P -values, genes that were also labeled in ( c ), and manually labeled TRAF1 and JUNB . e Conserved Gene Set Enrichment Analysis based on rankings derived from each comparison s log2 ' fold changes. Heatmap showing normalized enrichment scores. Only pathways that have been signi /uniFB01 cant in more than 50% of comparisons are depicted. Gray /uniFB01 elds indicate nonsigni /uniFB01 cant NES values. Source data are provided as a Source Data /uniFB01 le.

containing IFNγ (Fig. 6c). Human neutrophils displayed a highly concordant increase in those markers. CD69 and PD-L1 increased with similar magnitude, while upregulation of CD14 was stronger in mouse neutrophils compared to human neutrophils. In human neutrophils, upregulation of CD40 was restricted to a small (~2%) population of neutrophils (in line with previous /uniFB01 ndings 46 ) but reached signi /uniFB01 cance on the bulk level for both stimulations (Fig. 6c).

Differences were also noticeable between in /uniFB02 ammatory conditions. In mouse neutrophils, the combination of GM-CSF and LPS led to a stronger increase in the expression of CD14, CD69, IL-4R, and CD40 compared to GM-CSF and IFN- . The reverse was true for PD-L1, which γ is driven substantially by IFNγ signaling . Further, IFN8 γ stimulation reduced CD69 expression, while LPS increased it. In human neutrophils, the combination of GM-CSF and IFNγ leads to stronger increases in CD14, CD69, IL-4R, and PD-L1 than the combination of GMCSF and LPS.

A combined diffusion map analysis revealed a high degree of overlap between mouse and human neutrophils, while cell distribution was driven predominantly by experimental conditions (Fig. 6d). Correspondingly, activated neutrophils of both species displayed a continuous upregulation of the in /uniFB02 ammatory response markers (Fig. 6e).

These /uniFB01 ndings con /uniFB01 rm the predicted activation markers, further substantiating the conservation of in /uniFB02 ammatoryresponseprogramsin neutrophils while also revealing differences between species and in /uniFB02 ammatory conditions.

## Neutrophil origin and in /uniFB02 ammatory condition in /uniFB02 uence the expression of the core in /uniFB02 ammation program

Neutrophil heterogeneity is in /uniFB02 uenced by the tissue microenvironment 6,9 . To evaluate the impact of tissue origin on the phenotype of neutrophils in in /uniFB02 ammation, we performed stimulation experiments with paired leukocyte preparations from blood, bone marrow, and spleen of wild-type BL6 mice. In a principal component analysis of /uniFB02 ow cytometry data, resting neutrophils clustered closely together, but each tissue remained distinguishable based on subtle baseline expression differences in IL-4R, CD69, and CD40 (Fig. 7a). In /uniFB02 amed neutrophils deviated markedly from their resting counterparts and reached distinct states as a function of tissue and in /uniFB02 ammatory condition (Fig. 7a).

Neutrophils from all tissues upregulated CD69 and IL-4R, suggesting that these markers can be utilized as neutrophil activation markers across a variety of conditions (Fig. 7a). In contrast, expression of CD40, CD14, and PD-L1 showed greater tissue dependence. CD40 (evident most prominently in mouse neutrophils) was robustly upregulated in splenic neutrophils and less prominently in blood neutrophils. Conversely, CD14 and PD-L1 expression was inducible to a greater extent in blood neutrophils and bone marrow neutrophils but less in splenic neutrophils.

We also noted differences related to activating stimuli, for example, through more prominent PD-L1 induction by IFNγ compared to LPS. The single-cell analysis highlighted a continuum of states in all organs (Fig. 7b), driven by increasing expression of the core in /uniFB02 ammation markers (Fig. 7c). Importantly, the core program was already inducible in bone marrow neutrophils, suggesting that in vitro and adoptive transfer experiments performed with bone marrow neutrophils can recapitulate important features of neutrophil biology in in /uniFB02 ammation.

## Discussion

Neutrophils are important mediators of immune defense and protagonists in immune-mediated diseases. Mouse and human neutrophils differ in morphology, frequency in blood (humans ~50 -70%, mice ~10 -25%), and expression of marker proteins. For example, mouse neutrophils are de /uniFB01 ned by surface expression of Ly6G, not present in the human genome, whereas mouse neutrophils lack expression of defensins 47 .

Both in humans and mice, neutrophils are phenotypically heterogeneous acrossdifferent tissues and in /uniFB02 ammatoryconditions 37,48,49 . Recentstudies suggest that neutrophil heterogeneity in homeostasis is driven by a chronological sequence of maturation and activation termed neutrotime, whereas the combination of aging, tissue factors, environmental features, and in /uniFB02 ammatory signals promote their polarization toward distinct states 6,7,9 .

While the neutrotime signature can be detected in both species and this overarching principle of neutrophil ontogeny is likely conserved across humans and mice, it is poorly understood which features of the neutrophil in /uniFB02 ammatory response are shared across species. Furthermore, it is unclear which aspects of the neutrophil in /uniFB02 ammatory response re /uniFB02 ect a general in /uniFB02 ammatoryresponseprogramshared across multiple in /uniFB02 ammatory conditions and which features are highly speci /uniFB01 c to certain triggers or sites of in /uniFB02 ammation.

To address these gaps in knowledge, we performed an integrative analysis of resting and in /uniFB02 amed RNA-seq samples from humans and mice. We validated our computational approach by comparing gene expression conservation across six immune cell lineages: T cells, B cells, monocytes, dendritic cells, NK cells, and neutrophils. Expression of lineage-speci /uniFB01 c genes was generally well-conserved across humans and mice. Intriguingly, neutrophils displayed both the greatest number of lineage-speci /uniFB01 c genes and the highest correlation of gene expression between mice and humans, suggesting a higher degree of conservation in this phagocytic cell compared to other lineages.

While different in /uniFB02 ammatory conditions induced highly heterogeneousresponsesinneutrophils,ourcombinedanalysisallowedusto predict a core in /uniFB02 ammation program conserved across mice and humans. The robustness of this program was underscored by the high concordance between the gene set derived from Fisher s combined ' test and complementary approaches based on a linear mixed model as

<!-- image -->

UMAP 2

well as weighted correlation network analysis (WGCNA 39,50,51 ). It is important to note that different analytical strategies may be used to derive this core in /uniFB02 ammation program, each detecting a varying number of genes. The situation is similar for differential gene expression in general, which depends on the chosen method, as has been reviewed extensively 52 . Nevertheless, our analysis indicates that a

groupofgenesexists from whichneutrophils preferentially drawwhen they become activated across humans and mice and across a large range of conditions and disease states. The conservation of a small set of transcription factors predicted to regulate a broad variety of conditions across humans and mice highlights the conserved nature of gene expression in neutrophils.

Fig. 4 | Validation of the enrichment of core in /uniFB02 ammation genes in single-cell RNA sequencing. The /uniFB01 rst dataset (Combes) includes neutrophils of patients without (control), mild (M/M), and severe cases (severe) of COVID-19. The second dataset (Montaldo I) was derived from in vivo neutrophils from healthy controls (control) and patients treated with G-CSF (G-CSF). The third dataset (Montaldo II) used in vitro stimulation of umbilical cord blood neutrophils with G-CSF, interferonβ , or interferonγ . The fourth dataset (Xie) consisted of neutrophils isolated from different organs of mice challenged with E. coli . a Core in /uniFB02 ammation genes show a higher expression in in /uniFB02 amed samples compared to controls. Shown is a heatmapwithmeanscaledexpressionvaluesofthecorein /uniFB02 ammationgenesacross all cells per condition and sample. Rows represent genes, columns samples. b In /uniFB02 amed cells show a higher gene module score for the core in /uniFB02 ammation program. Each cell has been scored for the enrichment of the core in /uniFB02 ammation program genes compared to a random reference gene set of similar expression. Shownarecontrol samplesin gray alongside in /uniFB02 amedcellsin orange. P -values were

derived from a maximum likelihood ratio test of linear mixed models. Box plots: Median between the 25th and 75th percentile, whiskers extend to 10% and 90%. Outliers are shown as dots. Top plot: Statistics are derived from a total of 10,782 cells (Control: 1026, M/M: 5732, Severe: 4024) cells from N =56 independent samples ( P Control:M/M =0.0109, P Control:Severe =0.000013). Top mid: The experiment included a total of 48,875 cells (healthy: 12,338, G-CSF: 36,537) from N =6 independent samples ( P Control:G-CSF =0.01416). Bottom mid: A total of 26,312 cells (Control: 4296, G-CSF: 5049, IFN-beta: 8472, IFN-gamma: 8495) from N =4 independent samples were analyzed ( P Control:G-CSF =9.42×10 -5 , P Control:IFNbeta =2.67 × 10 -5 , P Control:IFN-gamma =2.71 × 10 -5 ) Bottom plot: Calculation was performed on 26,239 cells (Control: 8990, E. coli : 17,249) from N =10 independent samples ( P Control: E. coli =0.0376). c UMAP embedding. Coloring by gene set score (top panel) and the cell s in ' /uniFB02 ammatory state (bottom panel) shows an increase in the core in /uniFB02 ammation program expression in in /uniFB02 amed samples compared to their control. Source data are provided as a Source Data /uniFB01 le.

To validate the predicted core in /uniFB02 ammation program in different models, we analyzed differential gene accessibility in ATACsequencing data from a mouse air pouch model of in /uniFB02 ammation. We found a signi /uniFB01 cant proportion of core in /uniFB02 ammation program genes to be more accessible with maturation and in pro-in /uniFB02 ammatory conditions. While this model is very speci /uniFB01 c, it covered neutrophils from different maturation stages and presented the opportunity to study transmigrated and activated neutrophils separately. Further, analysis of the transcriptome on a single cell level in both in vivo and in vitro in /uniFB02 amed neutrophils of both species allowed us to validate the core in /uniFB02 ammation program. While the overall enrichment of the proposed gene set on a pseudo-bulk level was clearly evident, our analyses also suggested signi /uniFB01 cant heterogeneity within the population of in /uniFB02 amed neutrophils, consistent with recent analyses 7,9,40,41 . These analyses further highlight the predictive value of the program in a method not used in its generation.

HoxB8-derived neutrophils are a powerful tool to model neutrophil function. We assessed the differential expression of zymosanactivated HoxB8-derived neutrophils versus control, showing a signi /uniFB01 cant overrepresentation of core in /uniFB02 ammation genes in activated neutrophils. Zymosan-activated myeloid cells through TLR2 and is a commonly used pro-in ammatory trigger. /uniFB02 The core in /uniFB02 ammation program was reduced in resting cells carrying a knockout of key regulators of this program ( JunB - -/ and Cebp β - -/ ). Core in /uniFB02 ammationgenes were also signi /uniFB01 cantly less upregulated in zymosan-stimulated JunB - -/ cells, indicating an impaired neutrophil in /uniFB02 ammatory response in these cell lines. Concordant with previous reports of a more limited impact of the Cebp β knockout on in /uniFB02 ammatory neutrophil functions compared to the JunB knockout 36 , the underrepresentation of core in /uniFB02 ammation genes was nonsigni /uniFB01 cant in our analysis.

Finally, we validated key components of the predicted core in /uniFB02 ammation program experimentally. Using primary human and mouse neutrophils, we showed that the surface proteins CD14, CD69, IL-4R, CD40, and PD-L1 are induced by in vitro cytokine stimulation, and this upregulation is observable in both species, although CD40 was restricted to a small subset of neutrophils in humans, as expected 46 .

This /uniFB01 nding further underlines the conserved character of the in /uniFB02 ammation program as presented in this study. Interestingly, while neutrophils from different mouse tissues upregulated the in /uniFB02 ammatory response markers, the magnitude of upregulation differed across bone marrow, spleen, and blood, suggesting that the tissue origin of neutrophils is an important consideration in experimental studies.

Recently, Jin et al. identi /uniFB01 ed a distinct neutrophil population termed ' antigen-presenting aged neutrophils (APANs) ' 53 . In humans, this population was characterized as CD66b + CXCR4 + CD62L lo CD40 + CD86 + , while in mice, they were identi /uniFB01 ed as Ly6G + CXCR4 + CD62L -/lo MHCII + CD40 + CD86 + . APANs were capable of inducing CD4 T cell proliferation via IL-12 and exhibited a hyper-NETosis phenotype. The

presence of these neutrophils in patients with sepsis was associated with increased mortality. While we also observed the upregulation of key marker genes like CD40 in our study s core in ' /uniFB02 ammationprogram, APANsdisplayeddistinctfeatures, such aselevated levelsof CXCR4 and coexpression with CD74 , suggesting a unique neutrophil polarization state discriminable from both neutrophil aging and canonical activation. The phenotype observed by the authors suggests the importance of further studying APANs, their features and their role in antigen presentation in humans and mice.

The upregulation of IL-4R we observed is concordant with reports of IL-4R upregulation during sterile information in mice, with implications for diseases that are IL-4 mediated 54 . CD14 has recently been shown to be an important, highly cell-speci /uniFB01 c mediator of TNF response in a mouse sepsis model 55 . Interestingly, CD14 + macrophages and neutrophils were found to be key players leading to lethality in response to TNF (with improved survival in CD14-de /uniFB01 cient mice), which provides a model for the cytokine storm seen in severe sepsis and provides evidence for the complexity of CD14-mediated in /uniFB02 ammatory response beyond TLR-signaling. These examples highlight the importance of core in /uniFB02 ammation program members and stress the need to study them in a broad variety of in /uniFB02 ammatory contexts.

The question of how well mouse models mimic human immunology is an area of ongoing debate. Even the same data can support different conclusions 56,57 , highlighting the impact of analytical decisions. Furthermore, it is important to compare suitable datasets, control for batch effects, and make comparisons to varying controls to avoid a shared denominator effect 56,58,59 .

In the context of neutrophils, fundamental differences between humans and mice exist 60,61 . Those differences must be considered when using the mouse as a model to study neutrophil function, especially in disease, as previously discussed 62 . Granule proteins found in neutrophils play a key role in defense against infection. An important difference in the granule protein repertoire includes α -defensins, which exercise antimicrobe 63,64 and chemotactic 65 activity and are absent in mouse neutrophils. It is also known that mouse neutrophils express less MPO, leading to a more limited capability to produce hypochlorous acid compared to their human counterpart 66 . The importance of cytokine production by neutrophils has been increasingly recognized 67,68 , with some cytokines such as IFNβ and IL-17 apparently expressed in mouse and not human neutrophils. The different immunoreceptor reservoir 69 is, in part, a result of pathogen responses that are exclusive to the human species. For example, human neutrophils express speci /uniFB01 c CEACAMs that mediate uptake of the human-speci /uniFB01 c pathogen Neisseria gonorrhea . 70 , which must be taken into account when modeling neutrophil responses to this pathogen 71 . Taken together, these studies provide important context to be taken into account when interpreting the core in /uniFB02 ammation program identi /uniFB01 ed.

<!-- image -->

The derivation of the core in /uniFB02 ammation program was limited to bulk RNA-sequencing samples since a similar analysis using single-cell studies requires datasets that are only now beginning to emerge. To circumvent potential batch effects, we focused our analysis on studies with internal controls of resting neutrophils, excluding other potentially interesting studies containing only neutrophils harvested from in /uniFB02 amedsites.Analyzedsamples werealsolimited by technical factors,

including the known intron retention in neutrophils 72 , as well as the less complex transcriptome associated with low RNA and high RNase content. Furthermore, analysis of single-cell RNA sequencing data, the ATAC-seq data from the air pouch model of in /uniFB02 ammation, and RNA-seq data from zymosan-activated HoxB8 samples represent only selected validation strategies in speci /uniFB01 c modalities of in /uniFB02 ammation, which might limit the generalizability of some of the /uniFB01 ndings.

Fig. 5 | Genes in the core in /uniFB02 ammation program are predisposed to be upregulated with maturation and activation. a Shownisthe meanlog2 fold change of gene expressions across all comparisons versus the regulatory activity (inverse logarithm of ChEA3 Scores per species). Colors and sizes indicate -log10( P ), using the Benjamini-Hochberg adjusted P -values from a Fisher s combined test (Fig. 3). ' b d -ATAC-sequencing from the air pouch model 36 . b Members of the core in /uniFB02 ammation program show increasing chromatin accessibility (blood vs. bone marrow; membrane and air pouch vs. bone marrow or blood). Genes part of the in /uniFB02 ammatoryresponse program were compared with the list of genes that showed increased/decreased accessibility in the depicted comparisons. Asterisks indicate signi /uniFB01 cance versus 1000 repeats of an accessibility analysis of random RNAexpression-matched background genes (two-sided studentized bootstrap: P 1 : 7.26 × 10 -8 ; P 2 : 6.86 × 10 -17 ; P 3 : 2.09× 10 -21 ; P 4: 1.56 × 10 -18 ; P 5 : 3.07 × 10 -22 ). Bottomright: Two-sided Fisher s exact test on the number of core in ' /uniFB02 ammatorygenes with increased accessibility versus no increase. FDR-adjusted P -values. c Core in /uniFB02 ammation program gene accessibility for each comparison. Rows ordered by nested decreasing rank of peaks associated with an increase, with both, with none, and

with a decrease. d A subset of transcription factors shows increased motif enrichment and increased gene expression in in /uniFB02 amed neutrophils. Motif enrichment analysis was performed using HOMER and is compared to the mean log2 fold change across species. A one-sided motif enrichment analysis was run separately for increased and decreased accessibility to calculate l n ð P Þ . ρ , Spearman s rank ' correlation coef /uniFB01 cient with its respective P -value (two-sided). e Analysis of HoxB8 cells that were treated with zymosan 36 . Core in /uniFB02 ammationgenesshowupregulation versus random genes in zymosan-stimulated HoxB8 cells and are downregulated in JunB - -/ . Core in /uniFB02 ammation genes in HoxB8 neutrophil RNA-Seq data 36 . One row per comparison. Left, experimental conditions for each comparison and respective statistics. Middle, volcano plots for each comparison. Red, Core in /uniFB02 ammation program members. Members with the highest combined signi /uniFB01 cance and effect sizes are labeled. Right, histograms showing the percentage of expression-matched background genes (equally sized gene sets, 1000 simulations) up/downregulated (see x -axes) in each comparison. Red arrow indicates observed percentage for core in /uniFB02 ammation program members, annotated with its P overrepresentation (one-sided, Wallenius method 99 ). Source data are provided as a Source Data /uniFB01 le.

Nevertheless, our combined analysis of 11 human and mouse neutrophil transcriptomic datasets identi /uniFB01 ed a largely conserved transcriptomic landscape across species, supporting the use of mouse neutrophils to illuminate human biology. We furthermore predicted and experimentally con /uniFB01 rmed the existence of a core in /uniFB02 ammation program conserved across human and mouse in /uniFB02 amed neutrophils. This study sets the stage for more /uniFB01 ne-grained analyses of the epigenome, transcriptome, and proteome of neutrophils across varying conditions, which together will paint a clearer picture of the neutrophil response to different environments. Going forward, genetic perturbations and pharmacological interventions to interfere with pathologic neutrophil activation will be particularly informative if focused on programs conserved across species. The systems biology approach presented here can be transferred to other cell types and organisms to facilitate further studies comparing gene expression across species.

## Methods

## Ethics approval

Research with healthy human participants followed the declaration of Helsinki. Blood of healthy donors was collected under IRB-approved protocols (Heidelberg S-272/2021 and Heidelberg S-285-2015) approved by the ethics committee of the University of Heidelberg, Heidelberg, Germany. Informed consent was obtained from all participants.

Experiments involving animals were conducted under the approval of the Animal Care Facility Heidelberg and the Animal welfare of /uniFB01 cers (approval #T66/21) at the University of Heidelberg, Heidelberg, Germany.

Weobtained publicly available RNA sequencing data from mouse andhumanleukocytesthroughGEO(262samplesfrom24studies)and integrated these data by mapping orthologous genes. Differential expression analysis between resting and in /uniFB02 amed neutrophils was performed separately for each dataset, and the core in /uniFB02 ammation program was derived using Fisher s combined test. Transcription fac-' tor enrichment analysis was performed using ChEA3 and DoRothEA and compared to chromatin accessibility data from ATAC-seq (GSE161765). The impact of Cebp β and JunB knockout on the core in /uniFB02 ammation program was studied using RNA-seq data from HoxB8 cells (GSE161765). The core in /uniFB02 ammation program was validated in stimulated mouse and human neutrophils by /uniFB02 ow cytometry.

## Datasets

For all analyses, we used the following datasets:

## RNA sequencing

Datasets of interest were identi /uniFB01 ed through a literature search on PubMedandthe NCBI Gene Expression Omnibus. In total, 262 publicly available RNA sequencing samples from 24 studies were included.

- GLYPH&lt;129&gt; Lineage atlas dataset (Table 1): 76 samples, 40 human samples, 36 mouse samples. This dataset is a curated subset of the Haemopedia RNA-Seq atlas. Human cells were from buffy coats of healthy donors, and mouse cells were from blood, bone marrow, spleen, and lymph nodes.
- GLYPH&lt;129&gt; Neutrophil dataset (Table 2): 195 samples (including the 9 Haemopedia neutrophil samples, Choi J 2019), 136 human samples from 13 studies, 59 mouse samples from 11 studies. All studies in this dataset were selected only to contain neutrophils. A subset of this dataset from studies with in /uniFB02 amed samples as well as healthy controls was used for differential expression testing and in /uniFB02 ammatory core signature construction. Other subsets of samples from studies not selected for differential expression analysis have been used in analyses focusing on healthy control samples (Fig. 2).

## RNA-Seq of HoxB8 cells

- GLYPH&lt;129&gt; Khoyratty TE 2021 36 18 samples

## ATAC-Seq

- GLYPH&lt;129&gt; Khoyratty TE 2021 36 5 peak annotations

## Flow cytometry

- GLYPH&lt;129&gt; This study samples from 8 human donors and 9 mice
- GLYPH&lt;129&gt; This study samples from different organs of 6 mice

## Single-cell RNA sequencing

- GLYPH&lt;129&gt; Xie et al., 2020
- GLYPH&lt;129&gt; Montaldo et al., 2022
- GLYPH&lt;129&gt; Combes et al., 2021

## Data retrieval and processing

Wedownloaded raw sequencing reads for the selected studies to the MLS&amp;WISO bwForCluster using release 1.5 of the nf-core 73 fetchngs pipeline and quanti /uniFB01 ed them using release 3.6 of the nf-core rnaseq pipeline. The pipelines were launched using next /uniFB02 ow 74 (v22.04.0). To ensure high reproducibility, all pipeline processes were run inside singularity (v3.9.2) containers. For bulk RNA-seq samples, we mapped all downloaded samples using salmon 75 (v1.5.2) with the parameters libType set to A and indexing the reference genomes with 21 ' ' base k-mers. Quanti /uniFB01 ed transcripts were summarized to the gene level using bioconductor-tximeta 76 (v1.8.0). All human samples were mapped to the GRCh38 genome. All mouse samples were mapped to

<!-- image -->

the GRCm39 genome unless stated otherwise. Quality control was conducted using FastQC (Supplementary Data 1). Author-supplied metadata was queried using GEOquery 77 (v2.64.0) and integrated manually to ensure consistency across studies (Supplementary Data 2). R (v4.2.0) was used for downstream analyses. Bioconductor (v3.15) and additional packages were used for downstream analyses

and visualizations 51,78 -80 . Sequencing depths (total amount of mapped reads) for human samples in the lineage atlas dataset ranged between 11,970,326 and 16,060,356 (median 13,267,958), for mouse samples between 16,076,257 and 33,595,867 (median 18,689,418; Supplementary Fig. 2a, b). In the neutrophil dataset, sequencing depths ranged between 195,712 and 57,144,004 (median 29,741,078)

## Fig. 6 | Experimental validation of the core in /uniFB02 ammation program on the

protein level. a In /uniFB02 ammation-speci /uniFB01 c protein-coding genes were identi /uniFB01 ed by /uniFB01 ltering the genes depicted in Fig. 3c for the surfaceome as previously described 45 . Genes that encode proteins selected for validation (based on antibody availability and panel design) are labeled in red. b Experimental overview. Human and mouse neutrophils were isolated from peripheral blood or bone marrow, respectively, cultured 48 h, and analyzed in /uniFB02 owcytometry. c Flow cytometry analysis of resting and activated mouse and human neutrophils. The gating strategy is depicted in Supplementary Fig. 11. Signi /uniFB01 cance indicates adjusted P -values of a Dunn s test '

for human and between 1,022,486 and 42,005,334 (median 12,429,230) for mouse samples. The subset of samples that was selected for differential expression testing and in /uniFB02 ammatory core program calculation was sequenced between 8,135,455 and 57,144,004 (median 33,522,466) for human and between 1,022,486 and 36,405,228 (median 6,388,735; Supplementary Fig. 2c, d) for mouse samples.

For single-cell RNA sequencing data, the raw sequencing reads were downloaded as described above and aligned using cellranger (v7.1.0) using the GRCh38 genome for human datasets and mm10 genome for mouse samples, respectively. Downstream analysis was carried out in Python (v3.10) using the scanpy 81,82 API (v1.9.3) for data analysis and visualization.

## Orthology analyses and mapping

For downstreamanalyses,genes were mappedusingENSEMBL Version 107 2 . We restricted all our composite cross-species analyses to proteincoding genes with a high-con /uniFB01 dence orthology relationship and available gene symbols in both species. Mouse and human gene expression datasets were combined based on these orthologs.

## Identi /uniFB01 cation of lineage-associated genes

Lineage-associated genes were identi /uniFB01 ed using a linear modelbased differential expression test, implemented in limma 83 (v3.52.0) and edgeR 84 86 -(v3.38.0). Differential expression testing was restricted to protein-coding genes that could be assigned highcon dence orthologs between human and mouse samples. We con/uniFB01 structed a cross-species count matrix based on those mappings and referred to each mapped gene by its human gene symbol. Counts were /uniFB01 ltered using edgeR s ' /uniFB01 lterByExpr /uniFB01 ltering approach. We applied TMM normalization to account for differences in library composition. We then transformed counts to log2(CPM) values and estimated weights for each observation using voom. We applied limma to /uniFB01 t a linear model to our data and calculated differential expression for a given lineage against all remaining lineages. Lineageassociated genes were de /uniFB01 ned as genes that were differentially expressed in each lineage against all other lineages at a BenjaminiHochberg corrected P -value of ≤ 0.05 and a log2 FC &gt;0. Genes were ranked according to their F statistic, and up to 200 genes were selected per lineage.

## Lineage PCA, correlation analysis, and clustering

We used these balanced lineage-associated gene sets to perform PCA as well as correlation and clustering analysis on all samples. Human and mouse samples were combined as described above. To emphasize our focus on comparisons between lineages, we meancentered log2(CPM) for each species prior to combining the count matrices. A PCA was computed for all integrated samples, taking the concatenated lineage-associated gene sets as input features. Correlation of expression analyses was performed based on the same features, calculating Pearson s ' r correlation coef /uniFB01 cient for each inter-sample combination. We subsequently performed a hierarchical clustering analysis on the obtained correlation coef /uniFB01 cients.

(two-sided) that followed a Kruskal-Wallis H test (signi /uniFB01 cant for all markers). Exact P -values are provided in the Source Data /uniFB01 le. d Top, diffusion map embedding of neutrophils from humans and mice cultured for 48 h with or without GM-CSF + LPS andGM-CSF+IFN- .DiffusionmapembeddingcalculatedbasedonCD69,CD14,ILγ 4R, and PD-L1. Bottom, diffusion map embedding of human and mouse neutrophils, colored by species. e Diffusion map embedding colored by marker expression highlights a continuum driven by increasing expression of the activation markers. Source data are provided as a Source Data /uniFB01 le.

## Comparison of neutrophil lineage gene expression pro /uniFB01 les in resting neutrophils

To compare expression patterns of neutrophil lineage-associated genes in resting human and mouse neutrophils, we /uniFB01 rst de ned /uniFB01 lineage-associated genes for human and mouse samples separately. We de ned those genes as lineage-associated that were upregulated /uniFB01 (Benjamini-Hochberg corrected P -value of ≤ 0.05 and a log2 FC &gt;1) in neutrophils against all other lineages. We next mapped those gene sets to their human and mouse counterparts, considering only highcon dence one-to-one, one-to-many, and many-to-many orthology /uniFB01 relationships. Based on those mappings, we merged all genes detected as lineage-speci /uniFB01 c in either of the considered species. We also included genes detected as lineage-speci /uniFB01 c in either species but could not be mapped to a high-con /uniFB01 dence ortholog. The obtained genes were subset only to include genes that showed evidence of expression in the in /uniFB02 ammatory dataset.

Taking the computed mappings and log2(TPM+1) expression values of mapped gene-gene pairs, we tested for differential expression of those pairs between species using a linear mixed model 87 (lme4 v1.1-29) accounting for study-related batch effects by including the study annotation as a random effect:

Full model: log2(TPM+1) ~ species + (1|study)

Null model: log2(TPM+1) ~ (1|study)

P -values were computed by performing a likelihood ratio test between these models. We subsequently adjusted those values using the Benjamini-Hochberg correction method based on the total number of tested gene-gene pairs (genes that appeared as lineage-speci /uniFB01 c in either species were expressed in the in /uniFB02 ammatorydatasetandcould be mapped to one or more counterparts with high con /uniFB01 dence).

Using the average expression of mapped gene-gene pairs and differential expression P -value, we de /uniFB01 ned 5 different expression pro /uniFB01 les: Genes that showed high (&gt;95th percentile of all genes that were detected as lineage-speci /uniFB01 c in either species) average expression levels in both species and did not exhibit differential expression between species (Benjamini-Hochberg corrected P -value ≥ 0.05, absolute beta &lt; 1). Additionally, we de /uniFB01 ned 4 divergent clusters of genes that had high expression levels in only one of both species and showed evidence of differential expression (Benjamini-Hochberg corrected P -value &lt; 0.05, absolute β ≥ 1) or were abundantly expressed but could not be assigned an orthologous gene in the other species respectively.

## Differential expression testing

We performed differential expression analyses between in /uniFB02 amed and resting conditions on a total of 112 samples from N =11 (human: 7, mouse: 4) studies. To account for potential batch effects between studies, we used DESeq2 88 (v1.36.0) in each of the studies individually to identify differentially expressed genes in in /uniFB02 amed compared to healthy control samples. Each study s gene list was pre-' /uniFB01 ltered to only include genes with counts &gt;1 in at least 1 sample before differential expression analysis, based on the negative binomial distribution. To removenoise while preserving signi /uniFB01 cant differences, log2 fold change results were then shrunk using the apeglm package 89 . Differential gene expression results were additionally /uniFB01 ltered through DESeq2 s default ' independent /uniFB01 ltering approach, as well as its count outlier /uniFB01 ltering.

PCI

Fig. 7 | Neutrophil origin and cytokine stimulation determine the manifestation of the core in /uniFB02 ammation program. a Left: Principal component analysis performed on the median marker expressions per sample reveals distinct phenotypes of neutrophils driven by organ of isolation (color coded) as well as cytokine stimulation (line-segment coded). Right: PCA plots colored by the scaled expression for each of the quanti /uniFB01 ed markers. b Diffusion Map embedding of neutrophils

<!-- image -->

D

iff. comp. 1

from bone marrow, blood, and spleen cultured for 8 h with or without GM-CSF + LPS and GM-CSF+ IFN- . Embeddings were calculated based on the expression γ levels of CD69, CD14,IL-4R, PD-L1, and CD40. c Diffusion Mapembeddingofresting and cytokine-stimulated neutrophils (as in b ) from bone marrow, blood, and spleen, colored by marker expression. Source data are provided as a Source Data /uniFB01 le.

## Table 1 | Lineage atlas dataset

Table 2 | Neutrophil dataset

| Lineage         | Species   |   N samples |
|-----------------|-----------|-------------|
| B cells         | Human     |           8 |
| Dendritic cells | Human     |           7 |
| Monocytes       | Human     |           7 |
| Neutrophils     | Human     |           3 |
| NK cells        | Human     |           5 |
| T cells         | Human     |          10 |
| B cells         | Mouse     |           2 |
| Dendritic cells | Mouse     |           4 |
| Monocytes       | Mouse     |           6 |
| Neutrophils     | Mouse     |           6 |
| NK cells        | Mouse     |           2 |
| T cells         | Mouse     |          16 |

| Species   | Study name           | Usedfor signature construction   |   N samples |
|-----------|----------------------|----------------------------------|-------------|
| Human     | Adrover JM 2020 10   | FALSE                            |           6 |
| Human     | Catapano M 2020 11   | FALSE                            |          11 |
| Human     | Choi J 2019 12       | FALSE                            |           3 |
| Human     | Franco LM 2019 13    | FALSE                            |           2 |
| Human     | Grabowski P 2019 14  | FALSE                            |          22 |
| Human     | Vecchio F 2018 19    | FALSE                            |           8 |
| Human     | McCreary M 2019      | TRUE                             |          10 |
| Human     | Miralda I 2020 16    | TRUE                             |          16 |
| Human     | Mistry P 2019 17     | TRUE                             |          28 |
| Human     | Ter Haar NM 2018 107 | TRUE                             |           6 |
| Human     | Thomas HB 2015 18    | TRUE                             |          12 |
| Human     | Wright HL 2013 21    | TRUE                             |           6 |
| Human     | Wright HL 2020 20    | TRUE                             |           6 |
| Mouse     | Bhalla M 2021 22     | FALSE                            |           7 |
| Mouse     | Casulli J 2019 23    | FALSE                            |           3 |
| Mouse     | Coffelt SB 2015 24   | FALSE                            |           4 |
| Mouse     | Choi J 2019 12       | FALSE                            |           6 |
| Mouse     | Germann M 2020 26    | FALSE                            |           4 |
| Mouse     | Hsu BE 2019 27       | FALSE                            |           4 |
| Mouse     | Zhu YP 2018 31       | FALSE                            |           3 |
| Mouse     | Gal-Oz ST 2019 25    | TRUE                             |          12 |
| Mouse     | Hutchins AP 2015 28  | TRUE                             |           4 |
| Mouse     | Stasulli NM 2015 29  | TRUE                             |           6 |
| Mouse     | Yan Z 2019 30        | TRUE                             |           6 |

## Identi /uniFB01 cation of a core in /uniFB02 ammation program

To assess which in /uniFB02 ammation-driven changes in the neutrophil transcriptome are shared across conditions and conserved across species, we applied a Fisher s combined test to the adjusted ' P -values of each gene in each study, restricting the analysis to genes that passed our expression /uniFB01 lter as well as DESeq2 /uniFB01 lters in ≥ 80% of studies. This analysis provided a Benjamini-Hochberg-corrected composite P -value for all genes and allowed us to rank genes by their likelihood of dysregulation in in /uniFB02 ammation. Additionally, we calculated a mean log2 fold change for each gene across all studies.

Based on a rankP -value plot (Fig. 3b), we determined a P -value cutoff at a rank equaling 500, corresponding to an adjusted Fisher P ≤ 6.164117 × 10 -40 . Genes with an absolute log2 fold change greater than or equal to 0.5 and an adjusted P -value below our de /uniFB01 ned threshold were considered conserved in in /uniFB02 ammation. We de /uniFB01 ned the

upregulated subset (log2 FC ≥ 0.5) of those conserved genes as the core in /uniFB02 ammation program.

## Pathway enrichment analysis

In /uniFB02 ammatory pathway enrichment analysis was performed for each study individually using the fGSEA implementation of the Gene Set Enrichment Analysis method. For each study, the differential expression analysis results were ranked by log2 fold change. Enrichment was calculated for hallmark gene sets that were retrieved from the Molecular Signatures Database 90 (v7.5.1).

## Data preprocessing for single-cell RNA-seq

Datasets were imported using the raw count matrices from cellranger. First, empty droplets were determined by estimating the pro /uniFB01 le of ambient mRNA and testing deviations from this pro le /uniFB01 using a Dirichlet-multinomial model of UMI count sampling as implemented in the EmptyDrops method 91 (implemented in the DropletUtils package, v1.18.1). Ambient RNA correction was applied using the soupXalgorithm 92 (v1.6.2), and doublets were determined using a computational doublet detection tool that uses arti /uniFB01 cially created cell doublets to identify real cell doublets by nearest-neighbor-analysis in gene expression space 93 (v1.12.0). Cells expressing hemoglobin-related genes in a proportion above 0.02 were excluded, as well as cells containing less than 250 (Xie et al., Montaldo et al.) or 100 (Combes et al.) unique genes per cell. Cells with a content above 5% (Xie et al.) or 10% (Combes et al., Montaldo et al.) of mitochondrial genes were also excluded. Cell types were identi /uniFB01 ed using the SingleR package 94 (v2.0.0) in R with BlueprintEncodeData and MonacoImmuneData as reference datasets for human datasets and ImmGenData as reference dataset for mouse data, as provided by the package celldex 94 (v1.8.0). Data were log-normalized, and neutrophils were selected. For UMAP visualization, the 2000 genes containing the highest variance were selected and UMAP was computed using the scanpy API with default settings.

## Gene set enrichment in single-cell RNA-seq

The gene counts were normalized and log1p transformed using scanpy. The enrichment of genes belonging to the core program was quanti /uniFB01 ed using the difference between the average expression of the core in /uniFB02 ammation program genes and the average expression of a random reference set of genes 95 that have been sampled to match the expression distribution of the core in /uniFB02 ammation program (scanpy score\_genes function with default settings). We tested for enrichment in in /uniFB02 amed conditions using a linear mixed model with the sample (and organ for the dataset from Xie et al.) as a random effect and the respective treatment as a /uniFB01 xed effect. For datasets with multiple in /uniFB02 amed conditions, a respective model was created for each comparison separately. P -values were calculated by performing a maximum likelihood test between both models as described above. For visualization, the gene set scores were quantile-capped to the 5 th and 95 th percentile.

## Transcription factor enrichment analysis

In order to identify regulators associated with genes induced or downregulated in in /uniFB02 ammation, we used ChEA3 96 with default settings as described , using the 250 most signi 9 /uniFB01 cantly up- and downregulated genes, respectively, for each condition, ranked by their adjusted P -value. We then calculated the arithmetic mean of the negative logarithms of the ChEA3 scores per species and transcription factor to compare average TF activity across species.

We used a paired t-test to assess signi /uniFB01 cant differences between a TFs ChEA3-enrichment in up- against downregulated genes across all comparisons. The resulting P -values were corrected using a BenjaminiHochberg correction for all tested TFs. We used these corrected P -values to determine if a TF was signi /uniFB01 cantly more enriched in genes

upregulated in in /uniFB02 ammation or vice-versa. We subsequently inferred transcription factor activity using DoRothEA 97 (v1.8.0) and decoupleR 98 (v2.2.2), taking advantage of the species-speci /uniFB01 c transcription factor databases. Here, log2 fold change matrices per species served as input, leading to enrichment scores with their respective P -values. For downstream analyses, we calculated the mean enrichment scores per species and preserved the highest observed P -value for each transcription factor. For data visualization (Fig. 5a), only transcription factors where the respective gene had an assigned P -value in Fisher s combined test are ' shown( N =680).Genesencodingtranscription factors with a mean log2 fold change ≥ 0 were merged with transcription factor scores that were derived from the upregulated score set (as in Supplementary Fig. 8b), and genes with a mean log2 fold change &lt;0 were merged with transcription factor scores that were derived from the downregulated score set (as in Supplementary Fig. 8a). Labeling was selectively applied for genes encoding transcription factors with the 10 highest absolute log2 fold changes per direction which fall under the adjusted Fisher s com-' bined P -rank cutoff of 500 genes, as well as the 5 transcription factors with the lowest P -values and CEBPB .

## ATAC-sequencing analysis

We retrieved ATAC-sequencing data from mice that were subjected to the air pouch model of acute in /uniFB02 ammation (GEO: GSE161765, mapped to the GRCm38 genome). Genes annotated based on differentially accessible peaks as de /uniFB01 ned in the study ( Padj &lt;0.05, log2 fold change &gt; 1.5) were compared with the conserved upregulated genes as de /uniFB01 ned in the core in /uniFB02 ammation program. The ratio and number of core in /uniFB02 ammation program genes that were associated with projected increased accessibility served as an input for pairwise Fisher s exact tests, and ' P -values were adjusted using the BenjaminiHochberg method. For each comparison, the signi /uniFB01 cance of the number of core in /uniFB02 ammation genes with increased accessibility was retrieved by comparing the number with the results of this analysis using a 1000-fold repeated random selection of expression-matched background genes (as described below for RNA sequencing).

## RNA-sequencing analysis of zymosan-treated HoxB8 cells

We retrieved featureCounts (per ENSEMBL-ID) from HoxB8 cells that were subjected to differentiation and zymosan treatment (GEO: GSE161765, mapped to the GRCm38 genome). Differential expression analysis was performed as described in the respective section above. We restricted the analysis to HoxB8 cells that were differentiated for 5 days and then compared (1) wild-type cells that were treated for 2 h with zymosan (50 µ g/ml) or DMSO (control), (2) resting stable knockout HoxB8 cell lines versus wild type, (3) zymosan-treated stable knockout HoxB8 cell lines versus zymosan-treated wild-type HoxB8 cells. A signi /uniFB01 cant up- or downregulation of core in /uniFB02 ammation program genes was then assessed by performing pairwise overrepresentation analyses. For each overrepresentation analysis, we de ned differentially expressed genes as genes with an /uniFB01 FDR ≤ 0.05 and a |log2 fold change| ≥ 1. We then used goseq (v1.48.0) to calculate a Probability Weighting Function for the given set of genes, and calculated P -values by approximating the true distribution by the Wallenius non-central hypergeometric distribution as previously described 99 .

The control expression was calculated as previously described 95 . For each comparison, the gene expression was distributed in 25 bins. Then, each core in /uniFB02 ammation program member was assigned to its respective bin. The randomized sets were then sampled according to the distribution of core in /uniFB02 ammation program gene expressions. This sampling was repeated 1000 times.

## Experimental validation

The list of ranked conserved in /uniFB02 ammatory response genes was /uniFB01 ltered to include genes encoding surface proteins using the surfaceome resource 45 . The remaining N =69surface protein-encoding genes were

then /uniFB01 ltered by available human and mouse antibodies (BioLegend), and a panel consisting of CD14, CD69, CD40, IL-4R, and PD-L1 was selected for validation.

## Human samples

Neutrophils were isolated using density gradient centrifugation with Polymorphprep as previously described : 8 30ml whole blood was layered onto 20 ml Polymorphprep (Progen #1114683)and centrifuged at 535 × g for 35 min. The PBMC-containing layer was discarded by suction, and neutrophils were recovered and subjected to hypotonic lysis using 0.2% NaCl. The cells were subsequently washed with cell culture medium (RPMI 1640 (Gibco #21875-034)) supplemented with 10% heat-inactivated FBS (PAN Biotech #3302/P101102) and 1% GlutaMAX (Gibco #35050-061) and seeded at 5 million cells per 6 wells in a total volume of 5 ml at a humidi /uniFB01 ed atmosphere at 37 °C with 5% CO2. The cells were cultured over 48 h either in the absence of cytokines (vehicle control), with GM-CSF + IFNγ or GM-CSF + LPS. GM-CSF was usedata /uniFB01 nal concentration of 100 U/ml(R&amp;D #215GM), IFNγ at 10 ng/ ml (BioLegend #570208), and LPS at 100ng/ml (Invivogen #tlrl3pelps). After 48 h, 1 million cells were collected and stained using the Zombie Yellow Fixable Viability Kit (BioLegend #423103) for live/dead discrimination, followed by an antibody panel (Supplementary Table 1) in 50 µ l of FACS buffer (2% FBS, 5 mM EDTA and 0.1 sodium azide in PBS) for 25 min.

## Mouse samples

Mice were housed under SPF conditions with a 12 h light/dark cycle, a humidity of 50 -60%, a temperature of 22 ± 2 °C and food and water available ad libitum. Male and female C57BL/6J mice were sacri /uniFB01 ced by cervical dislocation, and bone marrow was extracted by /uniFB02 ushing with RPMI. Neutrophils were enriched by density centrifugation using Histopaque 1077 (Sigma-Aldrich #10771) and Histopaque 1119 (SigmaAldrich #11191). Cells were recovered from the interphase of both Histopaque layers and centrifuged. Cells were washed with RPMI containing 10% FBS and 1% Glutamax and seeded at 10 6 cells/ml in 48 well plates in a total volume of 500 µ l. Mouse GM-CSF (Peprotech #31503, 100 U/ml), mouse IFNγ (Peprotech #315-05, 10 ng/ml), and LPS (Invivogen #tlrl-3pelps, 100 ng/ml) were added to the medium for 24 h and 48h in combination as indicated in the respective /uniFB01 gures. Cells cultured in the absence of cytokines were used as controls. After the indicated times, cells were collected and stained with the antibody panel (Supplementary Table 2) in 50 µ l of FACS buffer containing 2% FBS, 5 mM EDTA and 0.1% sodium azide.

To assess neutrophils from different organs, mice were sacri /uniFB01 ced by cardiac puncture under generalized anesthesia. Subsequently, the femora and tibiae were /uniFB02 ushed with PBS to obtain bone marrow. Any remaining fat was removed from spleens, and splenic tissue was mechanically disintegrated using the back of a syringe. Cells were pelleted at 400× , and erythrocytes were lysed using ACK Lysing g Buffer (Lonza #10-548E) for 5 min at 4 °C. Cells were seeded at 10 6 cells/ml in 48 well plates in a total volume of 500 µ l. Cytokines were added as described above for a total of 8 h.

## Flow cytometry

Flow cytometry was performed on a BD LSRII /uniFB02 ow cytometer. At least 50,000 events were recorded per sample. FCS /uniFB01 les were exported by FACSDiva and subsequently gated and compensated in FlowJo (v10.8.0) for single, living, and CD15 + (human) and Ly6G + (mouse) cells. Eosinophils were excluded based on high auto /uniFB02 uorescence in the live/ dead (Paci /uniFB01 c Orange) channel (Supplementary Fig. 11). Gated events and their median /uniFB02 uorescence intensity values were exported and concatenatedinto a single-cell experiment using CATALYST 100 (v1.16.2) in R (v4.2.0). The dataset was arcsinh transformed using manually determined cofactors 8,101 and clustered by FlowSOM clustering and Consensus-Plus-Metaclustering. For combined analysis of human and

mousecells, both datasets were mean-centered, scaled, and combined into one SingleCellExperiment. Dimensionality reduction was performed using the DiffusionMap algorithm as implemented in the CATALYSTpackagewithstandardsettings. Forvisualization, a random subset of 1500 cells per sample was plotted using ggplot2 102 (v3.3.5). Principal components were calculated based on the median /uniFB02 uorescence values of the respective marker proteins per sample and plotted using matplotlib (v3.5.1) in Python (v3.9.1).

## Gene ontology enrichment analysis

We used EnrichR 103 105 -to assess enriched gene sets in a given list of genes. The analysis was restricted to terms annotated in GO\_Biological\_Process\_2021.

## Linear mixed-effect model

To validate the core in /uniFB02 ammation program derived from Fisher s ' combined test, we globally tested for differential expression between resting and in /uniFB02 amed cells including all samples used in the Fisher s ' combined testing approach. We accounted for batch effects by correcting gene counts for the study using ComBat-Seq 106 (sva v3.44.0). From batch-corrected counts, we calculated TMM-normalized log2 countspermillionthatweresubsequentlyquantilenormalizedandthen used as input for linear modeling. Modeling was implemented using lme4 87 (v1.1-29) to /uniFB01 t a linear mixed-effects model (LMM) to normalized counts. The linear formulae we /uniFB01 t for each gene were de /uniFB01 ned as f ull : expression ∼ condition +1 j study and reduced : expression ∼ 1 j study , where the variable to test for was condition , and the study was used as the covariate that was considered to be the random effect. We retrieved β as an estimate for the log2(FC) from the full model and subsequently performed a likelihood ratio test to compare the full with the reduced model and to retrieve the respective P -values. P -values were then adjusted using the Benjamini-Hochberg procedure. We accounted for batch effects by correcting gene counts using ComBat-Seq 106 (sva v3.44.0).

## π 1 -statistic

Using the qvalue-package 39,50,51 (v2.28.0), we calculated the π 1 -statistic (1π 0) as an estimated proportion of truly signi /uniFB01 cantly differentially expressed genes for a given set of P -values. To account for a selection of genes potentially biased toward low P -values when testing for the replicability of DEGs between studies, qvalue-calculation was implemented via the qvalue\_truncp function.

## Gene expression modules using WGCNA

For WGCNA 39 analysis, we selected the same samples that were used for differential expression testing. We accounted for batch effects by correcting gene counts using ComBat-Seq 106 (sva v3.44.0). From batchcorrected counts, we calculated TMM-normalized log2 counts per million that were subsequently quantile normalized and then used as input for WGCNA. The network was constructed as a signed network, using a soft thresholding power of 13, a minimum module size of 30, and a merge cut height of 0.25. Modules with more than 1000 genes were removed from subsequent analyses.

## Statistical analyses

Correlations indicated on scatter plots represent Pearson s ' R (Pearson s ' correlation coef /uniFB01 cient) with their respective P -value. For comparisons of the mean, we used the Mann-Whitney U test (two groups) or KruskalWallis H test (three groups) if the Shapiro-Wilk test indicated nonnormality in at least one group. When multiple comparisons were performed, P -values and/or asterisks indicate adjusted P -values using the Holm-Bonferroni method unless stated otherwise. For pairwise comparisons, the Mann-Whitney U test was used post-hoc, taking multiple comparisons into account using the Holm-Bonferroni method. To test for categorical associations, we used Fisher s exact test. Asterisks '

represent the following P -value ranges: P &gt;0.05, ns. 0.01 &lt; P ≤ 0.05, *. 0.001 &lt; P ≤ 0.01, **. 0.0001 &lt; P ≤ 0.001, ***. P ≤ 0.0001, ****.

## Reporting summary

Further information on research design is available in the Nature Portfolio Reporting Summary linked to this article.

## Data availability

All sequencing data was used from publicly available platforms (Gene Expression Omnibus and European Nucleotide Archive), and all accession numbers are listed in Supplementary Data 2. Flow cytometry data have been deposited at /uniFB02 owrepository.org under the accession FR-FCM-Z6U3 and FR-FCM-Z6U4. All other data are available in the article and its Supplementary /uniFB01 les or from the corresponding author upon request. Source data are provided with this paper.

## Code availability

Analysis code is publicly available on GitHub: https://github.com/rgblab/in /uniFB02 amed\_neutrophil\_transcriptome.

## References

- 1. Brubaker, D. K. &amp; Lauffenburger, D. A. Translating preclinical models to humans. Science 367 , 742 -743 (2020).
- 2. Howe, K. L. et al. Ensembl 2021. Nucleic Acids Res. 49 , D884 D891 (2021). -
- 3. Cardoso-Moreira, M. et al. Developmental gene expression differences between humans and mammalian models. Cell Rep. 33 , 108308 (2020).
- 4. Shay, T. et al. Conservation and divergence in the transcriptional programs of the human and mouse immune systems. Proc. Natl Acad. Sci. USA 110 , 2946 -2951 (2013).
- 5. Lin, S. et al. Comparison of the transcriptional landscapes between human and mouse tissues. Proc. Natl Acad. Sci. USA 111 , 17224 17229 (2014). -
- 6. Ballesteros, I. et al. Co-option of neutrophil fates by tissue environments. Cell 183 , 1282 -1297.e1218 (2020).
- 7. Xie, X. et al. Single-cell transcriptome pro /uniFB01 ling reveals neutrophil heterogeneity in homeostasis and infection. Nat. Immunol. 21 , 1119 -1133 (2020).
- 8. Grieshaber-Bouyer, R. et al. Ageing and interferon gamma response drive the phenotype of neutrophils in the in /uniFB02 amed joint. Ann. Rheum. Dis. 81 , 805 -814 (2022).
- 9. Grieshaber-Bouyer, R. et al. The neutrotime transcriptional signature de /uniFB01 nes a single continuum of neutrophils across biological compartments. Nat. Commun. 12 , 2856 (2021).
- 10. Adrover, J. M. et al. Programmed ' disarming of the neutrophil ' proteome reduces the magnitude of in /uniFB02 ammation. Nat. Immunol. 21 , 135 -144 (2020).
- 11. Catapano, M. et al. IL-36 promotes systemic IFN-I responses in severe forms of psoriasis. J. Invest. Dermatol. 140 , 816 826.e813 (2020). -
- 12. Choi, J. et al. Haemopedia RNA-seq: a database of gene expression during haematopoiesis in mice and humans. Nucleic Acids Res. 47 , D780 D785 (2019). -
- 13. Franco, L. M. et al. Immune regulation by glucocorticoids can be linked to cell type-dependent transcriptional responses. J. Exp. Med. 216 , 384 -406 (2019).
- 14. Grabowski, P. et al. Proteome analysis of human neutrophil granulocytes from patients with monogenic disease using dataindependent acquisition. Mol. Cell Proteomics 18 , 760 -772 (2019).
- 15. Jiang, K., Sun, X., Chen, Y., Shen, Y. &amp; Jarvis, J. N. RNA sequencing from human neutrophils reveals distinct transcriptional differences associated with chronic in /uniFB02 ammatory states. BMC Med. Genomics 8 , 55 (2015).

- 16. Miralda, I. et al. Whole transcriptome analysis reveals that Filifactor alocis modulates TNF α -stimulated MAPK activation in human neutrophils. Front. Immunol. 11 , 497 (2020).
- 17. Mistry, P. et al. Transcriptomic, epigenetic, and functional analyses implicate neutrophil diversity in the pathogenesis of systemic lupus erythematosus. Proc. Natl Acad. Sci. USA 116 , 25222 25228 (2019). -
- 18. Thomas, H. B., Moots, R. J., Edwards, S. W. &amp; Wright, H. L. Whose gene is it anyway? The effect of preparation purity on neutrophil transcriptome studies. PLoS ONE 10 , e0138982 (2015).
- 19. Vecchio, F. et al. Abnormal neutrophil signature in the blood and pancreasofpresymptomaticandsymptomatictype1diabetes. JCI Insight 3 , e122146 (2018).
- 20. Wright, H. L., Lyon, M., Chapman, E. A., Moots, R. J. &amp; Edwards, S. W. Rheumatoid arthritis synovial /uniFB02 uid neutrophils drive in /uniFB02 ammation through production of chemokines, reactive oxygen species, and neutrophil extracellular traps. Front. Immunol. 11 , 584116 (2020).
- 21. Wright, H. L., Thomas, H. B., Moots, R. J. &amp; Edwards, S. W. RNAseq reveals activation of both common and cytokine-speci /uniFB01 c pathways following neutrophil priming. PLoS ONE 8 , e58598 (2013).
- 22. Bhalla, M. et al. Transcriptome pro /uniFB01 ling reveals CD73 and agedriven changes in neutrophil responses against Streptococcus pneumoniae Infect. Immun. . 89 , e0025821 (2021).
- 23. Casulli, J. et al. CD200R deletion promotes a neutrophil niche for Francisella tularensis and increases infectious burden and mortality. Nat. Commun. 10 , 2121 (2019).
- 24. Coffelt, S. B. et al. IL-17-producing γδ T cells and neutrophils conspire to promote breast cancer metastasis. Nature 522 , 345 348 (2015). -
- 25. Gal-Oz, S. T. et al. ImmGen report: sexual dimorphism in the immune system transcriptome. Nat. Commun. 10 , 4295 (2019).
- 26. Germann, M. et al. Neutrophils suppress tumor-in /uniFB01 ltrating T cells in colon cancer via matrix metalloproteinase-mediated activation of TGFbeta. EMBO Mol. Med. 12 , e10681 (2020).
- 27. Hsu, B. E. et al. Immature low-density neutrophils exhibit metabolic /uniFB02 exibility that facilitates breast cancer liver metastasis. Cell Rep. 27 , 3902 3915.e3906 (2019). -
- 28. Hutchins, A. P., Takahashi, Y. &amp; Miranda-Saavedra, D. Genomic analysis of LPS-stimulated myeloid cells identi /uniFB01 es a common proin /uniFB02 ammatory response but divergent IL-10 anti-in /uniFB02 ammatory responses. Sci. Rep. 5 , 9100 (2015).
- 29. Stasulli, N. M. et al. Spatially distinct neutrophil responses within the in /uniFB02 ammatory lesions of pneumonic plague. mBio 6 , e0153015 (2015).
- 30. Yan, Z. et al. De /uniFB01 ciency of Socs3 leads to brain-targeted EAE via enhancedneutrophil activation and ROS production. JCI Insight 5 , e126520 (2019).
- 31. Zhu, Y. P. et al. Identi /uniFB01 cation of an early unipotent neutrophil progenitor with pro-tumoral activity in mouse and human bone marrow. Cell Rep. 24 , 2329 -2341.e2328 (2018).
- 32. de Graaf, C. A. et al. Haemopedia: an expression atlas of murine hematopoietic cells. Stem Cell Rep. 7 , 571 -582 (2016).
- 33. Cunningham, F. et al. Ensembl 2022. Nucleic Acids Res. 50 , D988 D995 (2022). -
- 34. Borregaard, N. Neutrophils, from marrow to microbes. Immunity 33 , 657 -670 (2010).
- 35. Ng, L. G., Ostuni, R. &amp; Hidalgo, A. Heterogeneity of neutrophils. Nat. Rev. Immunol. 19 , 255 -265 (2019).
- 36. Khoyratty, T. E. et al. Distinct transcription factor networks control neutrophil-driven in /uniFB02 ammation. Nat. Immunol. 22 , 1093 1106 (2021). -
- 37. Neuenfeldt, F. et al. In /uniFB02 ammationinducespro-NEToticneutrophils via TNFR2 signaling. Cell Rep. 39 , 110710 (2022).

- 38. Yoon, S. I. et al. Structural basis of TLR5/uniFB02 agellin recognition and signaling. Science 335 , 859 -864 (2012).
- 39. Langfelder, P. &amp; Horvath, S. WGCNA: an R package for weighted correlation network analysis. BMC Bioinformatics 9 , 559 (2008).
- 40. Combes, A. J. et al. Global absence and targeting of protective immune states in severe COVID-19. Nature 591 , 124 -130 (2021).
- 41. Montaldo, E. et al. Cellular and transcriptional dynamics of human neutrophils at steady state and upon stress. Nat. Immunol. 23 , 1470 1483 (2022). -
- 42. Buenrostro, J. D., Giresi, P. G., Zaba, L. C., Chang, H. Y. &amp; Greenleaf, W. J. Transposition of native chromatin for fast and sensitive epigenomic pro /uniFB01 ling of open chromatin, DNA-binding proteins and nucleosome position. Nat. Methods 10 , 1213 -1218 (2013).
- 43. Fischer, J. et al. Safeguard function of PU.1 shapes the in /uniFB02 ammatory epigenome of neutrophils. Nat. Immunol. 20 , 546 -558(2019).
- 44. Hirai, H. et al. C/EBPbeta is required for ' emergency granulopoi-' esis. Nat. Immunol. 7 , 732 -739 (2006).
- 45. Bausch-Fluck, D. et al. The in silico human surfaceome. Proc. Natl Acad. Sci. USA 115 , E10988 E10997 (2018). -
- 46. Perazzio, S. F. et al. Soluble CD40L is associated with increased oxidative burst and neutrophil extracellular trap release in Behcet s disease. ' Arthritis Res. Ther. 19 , 235 (2017).
- 47. Risso, A. Leukocyte antimicrobial peptides: multifunctional effector molecules of innate immunity. J. Leukoc. Biol. 68 , 785 792 (2000). -
- 48. Silvestre-Roig, C., Fridlender, Z. G., Glogauer, M. &amp; Scapini, P. Neutrophil diversity in health and disease. Trends Immunol. 40 , 565 583 (2019). -
- 49. Grieshaber-Bouyer, R. &amp; Nigrovic, P. A. Neutrophil heterogeneity as therapeutic opportunity in immune-mediated disease. Front. Immunol. 10 , 346 (2019).
- 50. Zhang, B. &amp; Horvath, S. A general framework for weighted gene co-expression network analysis. Stat. Appl. Genet. Mol. Biol. 4 , 17 (2005).
- 51. Storey, J. D. &amp; Tibshirani, R. Statistical signi /uniFB01 cance for genomewide studies. Proc. Natl Acad. Sci. USA 100 , 9440 9445 (2003). -
- 52. Baik, B., Yoon, S. &amp; Nam, D. Benchmarking RNA-seq differential expression analysis methods using spike-in and simulation data. PLoS ONE 15 , e0232271 (2020).
- 53. Jin, H. et al. Antigen-presenting aged neutrophils induce CD4 + T cells to exacerbate in /uniFB02 ammation in sepsis. J. Clin. Invest. 133 , e164585 (2023).
- 54. Panda, S. K. et al. IL-4 controls activated neutrophil FcgammaR2b expression and migration into in /uniFB02 amedjoints. Proc. Natl Acad. Sci. USA 117 , 3103 -3113 (2020).
- 55. Muendlein, H. I. et al. Neutrophils and macrophages drive TNFinduced lethality via TRIF/CD14-mediated responses. Sci. Immunol. 7 , eadd0665 (2022).
- 56. Takao, K. &amp; Miyakawa, T. Genomic responses in mouse models greatly mimic human in /uniFB02 ammatory diseases. Proc. Natl Acad. Sci. USA 112 , 1167 -1172 (2015).
- 57. Seok, J. et al. Genomic responses in mouse models poorly mimic human in /uniFB02 ammatory diseases. Proc. Natl Acad. Sci. USA 110 , 3507 3512 (2013). -
- 58. Warren, H. S. et al. Mice are not men. Proc. Natl Acad. Sci. USA 112 , E345 (2015).
- 59. Shay, T., Lederer, J. A. &amp; Benoist, C. Genomic responses to in /uniFB02 ammation in mouse models mimic humans: we concur, apples to oranges comparisons won t do. ' Proc. Natl Acad. Sci. USA 112 , E346 (2015).
- 60. Styrt, B. Species variation in neutrophil biochemistry and function. J. Leukoc. Biol. 46 , 63 -74 (1989).
- 61. Mestas, J. &amp; Hughes, C. C. Of mice and not men: differences between mouse and human immunology. J. Immunol. 172 , 2731 2738 (2004). -

- 62. Nauseef, W. M. Human neutrophils ≠ murine neutrophils: does it matter? Immunol. Rev. 314 , 442 -456 (2023).
- 63. Wilson, S. S., Wiens, M. E. &amp; Smith, J. G. Antiviral mechanisms of human defensins. J. Mol. Biol. 425 , 4965 4980 (2013). -
- 64. Xu, D. &amp; Lu, W. Defensins: a double-edged sword in host immunity. Front. Immunol. 11 , 764 (2020).
- 65. Yang, D., Chertov, O. &amp; Oppenheim, J. J. Participation of mammalian defensins and cathelicidins in anti-microbial immunity: receptors and activities of human defensins and cathelicidin (LL37). J. Leukoc. Biol. 69 , 691 -697 (2001).
- 66. Rausch, P. G. &amp; Moore, T. G. Granule enzymes of polymorphonuclear neutrophils: a phylogenetic comparison. Blood 46 , 913 919 (1975). -
- 67. Tecchio, C., Micheletti, A. &amp; Cassatella, M. A. Neutrophilderived cytokines: facts beyond expression. Front. Immunol. 5 , 508 (2014).
- 68. Cassatella, M. A., Ostberg, N. K., Tamassia, N. &amp; Soehnlein, O. Biological roles of neutrophil-derived granule proteins and cytokines. Trends Immunol. 40 , 648 -664 (2019).
- 69. vanRees, D. J., Szilagyi, K., Kuijpers, T. W., Matlung, H. L. &amp; van den Berg, T. K. Immunoreceptors on neutrophils. Semin. Immunol. 28 , 94 108 (2016). -
- 70. Gray-Owen, S. D., Dehio, C., Haude, A., Grunert, F. &amp; Meyer, T. F. CD66 carcinoembryonic antigens mediate interactions between Opa-expressing Neisseria gonorrhoeae and human polymorphonuclear phagocytes. EMBO J. 16 , 3435 -3445 (1997).
- 71. Sarantis, H. &amp; Gray-Owen, S. D. De /uniFB01 ning the roles of human carcinoembryonic antigen-related cellular adhesion molecules during neutrophil responses to Neisseria gonorrhoeae Infect. Immun. . 80 , 345 -358 (2012).
- 72. Ullrich, S. &amp; Guigo, R. Dynamic changes in intron retention are tightly associated with regulation of splicing factors and proliferative activity during B-cell development. Nucleic Acids Res. 48 , 1327 -1340 (2020).
- 73. Ewels, P. A. et al. The nf-core framework for community-curated bioinformatics pipelines. Nat. Biotechnol. 38 , 276 -278 (2020).
- 74. Di Tommaso, P. et al. Next /uniFB02 ow enables reproducible computational work /uniFB02 ows. Nat. Biotechnol. 35 , 316 -319 (2017).
- 75. Patro, R., Duggal, G., Love, M. I., Irizarry, R. A. &amp; Kingsford, C. Salmon provides fast and bias-aware quanti /uniFB01 cation of transcript expression. Nat. Methods 14 , 417 -419 (2017).
- 76. Love, M. I. et al. Tximeta: reference sequence checksums for provenance identi /uniFB01 cation in RNA-seq. PLoS Comput. Biol. 16 , e1007664 (2020).
- 77. Davis, S. &amp; Meltzer, P. S. GEOquery: a bridge between the Gene Expression Omnibus (GEO) and BioConductor. Bioinformatics 23 , 1846 1847 (2007). -
- 78. Gu, Z., Eils, R. &amp; Schlesner, M. Complex heatmaps reveal patterns and correlations in multidimensional genomic data. Bioinformatics 32 , 2847 -2849 (2016).
- 79. Huber, W. et al. Orchestrating high-throughput genomic analysis with Bioconductor. Nat. Methods 12 , 115 -121 (2015).
- 80. Schroder, M. S., Culhane, A. C., Quackenbush, J. &amp; Haibe-Kains, B. survcomp: an R/Bioconductor package for performance assessment and comparison of survival models. Bioinformatics 27 , 3206 3208 (2011). -
- 81. Virshup, I. et al. The scverse project provides a computational ecosystem for single-cell omics data analysis. Nat. Biotechnol. 41 , 604 606 (2023). -
- 82. Wolf, F. A., Angerer, P. &amp; Theis, F. J. SCANPY: large-scale singlecell gene expression data analysis. Genome Biol. 19 , 15 (2018).
- 83. Ritchie, M. E. et al. limma powers differential expression analyses for RNA-sequencing and microarray studies. Nucleic Acids Res. 43 , e47 (2015).

- 84. Robinson, M. D., McCarthy, D. J. &amp; Smyth, G. K. edgeR: a Bioconductor package for differential expression analysis of digital gene expression data. Bioinformatics 26 , 139 -140 (2010).
- 85. McCarthy, D. J., Chen, Y. &amp; Smyth, G. K. Differential expression analysis of multifactor RNA-Seq experiments with respect to biological variation. Nucleic Acids Res. 40 , 4288 4297 (2012). -
- 86. Chen, Y., Lun, A. T. &amp; Smyth, G. K. From reads to genes to pathways: differential expression analysis of RNA-Seq experiments using Rsubread and the edgeR quasi-likelihood pipeline. F1000Res 5 , 1438 (2016).
- 87. Bates, D., Mächler, M., Bolker, B. &amp; Walker, S. Fitting linear mixedeffects models using lme4. J. Stat. Softw. 67 , 1 -48 (2015).
- 88. Love, M. I., Huber, W. &amp; Anders, S. Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2. Genome Biol. 15 , 550 (2014).
- 89. Zhu, A., Ibrahim, J. G. &amp; Love, M. I. Heavy-tailed prior distributions for sequence count data: removing the noise and preserving large differences. Bioinformatics 35 , 2084 2092 (2019). -
- 90. Liberzon, A. et al. The Molecular Signatures Database (MSigDB) hallmark gene set collection. Cell Syst. 1 , 417 -425 (2015).
- 91. Lun, A. T. L. et al. EmptyDrops: distinguishing cells from empty droplets in droplet-based single-cell RNA sequencing data. Genome Biol. 20 , 63 (2019).
- 92. Young, M. D. &amp; Behjati, S. SoupX removes ambient RNA contamination from droplet-based single-cell RNA sequencing data. Gigascience 9 , giaa151 (2020).
- 93. Germain, P. L., Lun, A., Garcia Meixide, C., Macnair, W. &amp; Robinson, M. D. Doublet identi /uniFB01 cation in single-cell sequencing data using scDblFinder. F1000Res 10 , 979 (2021).
- 94. Aran, D. et al. Reference-based analysis of lung single-cell sequencing reveals a transitional pro /uniFB01 brotic macrophage. Nat. Immunol. 20 , 163 -172 (2019).
- 95. Tirosh, I. et al. Dissecting the multicellular ecosystem of metastatic melanoma by single-cell RNA-seq. Science 352 , 189 196 (2016). -
- 96. Keenan, A. B. et al. ChEA3: transcription factor enrichment analysis by orthogonal omics integration. Nucleic Acids Res. 47 , W212 W224 (2019). -
- 97. Garcia-Alonso, L., Holland, C. H., Ibrahim, M. M., Turei, D. &amp; SaezRodriguez, J. Benchmark and integration of resources for the estimation of human transcription factor activities. Genome Res. 29 , 1363 -1375 (2019).
- 98. Badia-i-Mompel, P. et al. decoupleR: ensemble of computational methods to infer biological activities from omics data. Bioinform. Adv. 2 , vbac016 (2022).
- 99. Young, M. D., Wake /uniFB01 eld, M. J., Smyth, G. K. &amp; Oshlack, A. Gene ontology analysis for RNA-seq: accounting for selection bias. Genome Biol. 11 , R14 (2010).
- 100. Crowell, H. L., Zanotelli, V. R., Chevrier, S., Robinson, M. D. &amp; Bodenmiller, B. CATALYST: Cytometry dATa anALYSis Tools. R package version 1.16.2 (2021).
- 101. Melsen, J. E., van Ostaijen-ten Dam, M. M., Lankester, A. C., Schilham, M. W. &amp; van den Akker, E. B. A comprehensive work /uniFB02 ow for applying single-cell clustering and pseudotime analysis to /uniFB02 ow cytometry data. J. Immunol. 205 , 864 -871 (2020).
- 102. Wickham, H. ggplot2: Elegant Graphics for Data Analysis (Springer, 2016).
- 103. Chen,E.Y.etal. Enrichr: interactive and collaborative HTML5 gene list enrichment analysis tool. BMC Bioinformatics 14 , 128 (2013).
- 104. Kuleshov, M. V. et al. Enrichr: a comprehensive gene set enrichment analysis web server 2016 update. Nucleic Acids Res. 44 , W90 W97 (2016). -
- 105. Xie, Z. et al. Gene set knowledge discovery with Enrichr. Curr. Protoc. 1 , e90 (2021).

- 106. Zhang, Y., Parmigiani, G. &amp; Johnson, W. E. ComBat-seq: batch effect adjustment for RNA-seq count data. NARGenom.Bioinform. 2 , lqaa078 (2020).
- 107. Ter Haar, N. M. et al. Reversal of sepsis-like features of neutrophils by interleukin-1 blockade in patients with systemic-onset juvenile idiopathic arthritis. Arthritis Rheumatol. 70 , 943 -956 (2018).

## Acknowledgements

N.S.H. and F.A.R. were supported by MD fellowships from the Boehringer Ingelheim Fonds. F.A.R. and T.E. were supported by an MD/PhD fellowship from the Medical Faculty of Heidelberg. P.A.N. was supported by NIH grants R01AR065538 and P30AR070253. This work was supported by grants to R.G.-B. from Deutsche Forschungsgemeinschaft (DFG, GR 5979/2-1, 517717827), Else Kröner-Fresenius-Stiftung (2022\_EKEA.72), state of Baden-Wuerttemberg within the Centers for Personalized Medicine Baden-Wuerttemberg (ZPM) and a research grant from the German Society for Rheumatology (DGRh). Figure 6b and Supplementary Fig. 1 were created with BioRender.com. The authors acknowledge support by the state of Baden-Württemberg through bwHPC and the German Research Foundation (DFG) through grant INST 35/1597-1 FUGG.

## Author contributions

N.S.H. and F.A.R. conceptualized and designed the study, performed computational and statistical analysis, provided conceptual input in experimental planning, analyzed experiments, conceptualized the core in /uniFB02 ammation program, and wrote the manuscript. T.E. performed computational and statistical analysis, planned experiments, processed human and mouse samples, performed and analyzed /uniFB02 ow cytometry, and wrote the manuscript. H.-M.L., C.M.-T., P.A.N. and G.W. guided data analysis, interpretation, and validation. R.G.-B. conceptualized and designed the study, performed computational and statistical analysis, provided conceptual input in experimental planning, analyzed experiments, conceptualized the core in /uniFB02 ammation program, supervised the entire project, and wrote the manuscript.

## Funding

## Competing interests

The authors declare no competing interests.

## Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-023-43573-9.

Correspondence and requests for materials should be addressed to Ricardo Grieshaber-Bouyer.

Peer review information Nature Communications thanks Monowar Aziz, David Casero and the other anonymous reviewer(s) for their contribution to the peer review of this work. A peer review /uniFB01 le is available.

Reprints and permissions information is available at

http://www.nature.com/reprints

Publisher s note ' Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional af /uniFB01 liations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article s Creative Commons licence, unless ' indicated otherwise in a credit line to the material. If material is not included in the article s Creative Commons licence and your intended ' use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/ licenses/by/4.0/.

- ©The Author(s) 2023

Open Access funding enabled and organized by Projekt DEAL.

1 Division of Rheumatology, Department of Medicine V, HeidelbergUniversity Hospital, Heidelberg, Germany. 2 Institute for Immunology,Heidelberg University Hospital, Heidelberg, Germany. 3 Division of Immunology, Boston Children s Hospital, Harvard Medical School, Boston, MA, USA. ' 4 Broad Institute of MIT and Harvard, Cambridge, MA, USA. 5 Division of Rheumatology, In /uniFB02 ammation and Immunity, Brigham and Women s Hospital, Harvard Medical School, Boston, ' MA, USA. 6 MRC Molecular Haematology Unit, MRC Weatherall Institute of Molecular Medicine, University of Oxford, Oxford, UK. 7 Oxford Centre for HaematologyUnit, MRC WeatherallInstituteof Molecular Medicine, University of Oxford, Oxford, UK. 8 DepartmentofMedicine V, Hematology, Oncology and Rheumatology, Heidelberg University Hospital, Heidelberg, Germany. 9 Molecular Medicine Partnership Unit, European Molecular Biology Laboratory (EMBL), University of Heidelberg, Heidelberg, Germany. 10 Deutsches Zentrum für Immuntherapie (DZI), Friedrich Alexander Universität Erlangen-Nürnberg and Universitätsklinikum Erlangen, Erlangen, Germany. 11 Department of Internal Medicine 3 -Rheumatology and Immunology, Friedrich Alexander Universität Erlangen-Nürnberg and Universitätsklinikum Erlangen, Erlangen, Germany. 12 These authors contributed equally: Nicolaj S. Hackert, Felix A. Radtke, Tarik Exner. e-mail: ricardo.grieshaber@fau.de