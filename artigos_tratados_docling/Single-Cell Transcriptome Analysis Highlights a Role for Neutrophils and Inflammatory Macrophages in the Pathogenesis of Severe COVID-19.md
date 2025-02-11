<!-- image -->

<!-- image -->

Article

## Single-Cell Transcriptome Analysis Highlights a Role for Neutrophils and Inflammatory Macrophages in the Pathogenesis of Severe COVID-19

Hibah Shaath 1,2 , Radhakrishnan Vishnubalaji 1 , Eyad Elkord 1,2 and Nehad M. Alajez 1,2, *

- 1 College of Health &amp; Life Sciences, Hamad Bin Khalifa University (HBKU), Qatar Foundation (QF), PO Box 34110, Doha, Qatar; hshaath@hbku.edu.qa (H.S.); vbradhakrishnan@hbku.edu.qa (R.V.); eelkord@hbku.edu.qa (E.E.)
- 2 Cancer Research Center, Qatar Biomedical Research Institute (QBRI), Hamad Bin Khalifa University (HBKU), Qatar Foundation (QF), PO Box 34110, Doha, Qatar
- * Correspondence: nalajez@hbku.edu.qa; Tel.: + 974-4454-7252; Fax: + 974-4454-0281

/gid00001

<!-- image -->

Received: 17 September 2020; Accepted: 20 October 2020; Published: 29 October 2020

Abstract: Cumulative data link cytokine storms with coronavirus disease 2019 (COVID-19) severity. The precise identification of immune cell subsets in bronchoalveolar lavage (BAL) and their correlation with COVID-19 disease severity are currently being unraveled. Herein, we employed iterative clustering and guide-gene selection 2 (ICGS2) as well as uniform manifold approximation and projection (UMAP) dimensionality reduction computational algorithms to decipher the complex immune and cellular composition of BAL, using publicly available datasets from a total of 68,873 single cells derived from two healthy subjects, three patients with mild COVID-19, and five patients with severe COVID-19. Our analysis revealed the presence of neutrophils and macrophage cluster-1 as a hallmark of severe COVID-19. Among the identified gene signatures, IFITM2 IFITM1 H3F3B SAT1 , , , , and S100A8 gene signatures were highly associated with neutrophils, while CCL8 CCL3 CCL2 KLF6 , , , , and SPP1 were associated with macrophage cluster-1 in severe-COVID-19 patients. Interestingly, although macrophages were also present in healthy subjects and patients with mild COVID-19, they had di GLYPH&lt;11&gt; erent gene signatures, indicative of interstitial and cluster-0 macrophage (i.e., FABP4 APOC1 , , APOE C1QB , , and NURP1 ). Additionally, MALAT1 NEAT1 , , and SNGH25 were downregulated in patients with mild and severe COVID-19. Interferon signaling, FC γ receptor-mediated phagocytosis, IL17, and Tec kinase canonical pathways were enriched in patients with severe COVID-19, while PD-1 and PDL-1 pathways were suppressed. A number of upstream regulators (IFNG, PRL, TLR7, PRL, TGM2, TLR9, IL1B, TNF, NFkB, IL1A, STAT3, CCL5, and others) were also enriched in BAL cells from severe COVID-19-a GLYPH&lt;11&gt; ected patients compared to those from patients with mild COVID-19. Further analyses revealed genes associated with the inflammatory response and chemotaxis of myeloid cells, phagocytes, and granulocytes, among the top activated functional categories in BAL from severe COVID-19-a GLYPH&lt;11&gt; ected patients. Transcriptome data from another cohort of COVID-19-derived peripheral blood mononuclear cells (PBMCs) revealed the presence of several genes common to those found in BALfrompatientswithsevereandmildCOVID-19( IFI27 IFITM3 IFI6 IFIT3 MX1 IFIT1 OASL IFI30 , , , , , , , , OAS1 ) or to those seen only in BAL from severe-COVID-19 patients ( S100A8 IFI44 IFI44L , , , CXCL8 , CCR1 PLSCR1 EPSTI1 FPR1 OAS2 OAS3 IL1RN TYMP BCL2A1 , , , , , , , , ). Taken together, our data reveal the presence of neutrophils and macrophage cluster-1 as the main immune cell subsets associated with severe COVID-19 and identify their inflammatory and chemotactic gene signatures, also partially reflected systemically in the circulation, for possible diagnostic and therapeutic interventions.

Keywords: SARS-Cov-2; COVID-19; neutrophils; inflammatory macrophages; bronchoalveolar lavage (BAL); ICGS2; UMAP

Cells 2020 , 9 , 2374; doi:10.3390 cells9112374 /

## 1. Introduction

As part of the continuing e GLYPH&lt;11&gt; orts to further understand the mechanisms underlying viral infection and disease severity, unraveling the role of the immune system is imperative to develop possible therapeutic interventions. The spread of severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) causing coronavirus disease 2019 (COVID-19) continues to devastate many communities and economies, placing healthcare systems under mass pressures. In cases with severe or fatal outcomes, a hyper-production of cytokines is often observed as a result of an overreaction of the immune system to the infection, causing an imbalance known as cytokine storm [1]. The consequences of a cytokine storm can range from alveolar injury to multi-organ failure, sepsis, or even death. Due to the resulting devastating e GLYPH&lt;11&gt; ects on the host, many studies are now focusing on how cytokine storms can be minimized, as increasing evidence has shown cytokine storms to be in direct association with more severe cases of COVID-19 [2].

Based on previous studies conducted after the emergence of prior coronaviruses, including SARS-CoV-1 and the Middle East respiratory syndrome coronavirus (MERS-CoV), the entry receptor for SARS-CoV-2 was identified as human angiotensin converting enzyme 2 (hACE2) [3]. Viral entry was found to be facilitated through distinct hotspots on hACE2, forming energetically stable tunnel structures for viral binding on hACE2-positive host cells [4]. hACE2 expression on the apical surface of polarized human airway epithelia positively correlates with coronavirus infection, whereas undi GLYPH&lt;11&gt; erentiated cells expressing little ACE2 had lower rates of infection [5]. Other tissue groups with ACE2 expression, and therefore susceptible to coronavirus infection, include lung, heart, kidney, and gastrointestinal tract [6,7]. Korber et al. reported a SARS-CoV-2 variant harboring the D614G spike protein amino acid change as the most prevalent form in the COVID-19 global pandemic. Interestingly, the authors reported the G614 variant to be associated with higher viral loads in patients but not with increased disease severity [8].

Recognition of a foreign infection triggers innate immune responses leading to mass recruitment of immune cells to the sites of infection. Studies have shown that higher plasma levels of Interleukin 2 (IL2), Interleukin 7 (IL7), Interleukin 10 (IL10), Granulocyte colony-stimulating factor (GCSF), Interferon gamma-induced protein 10 (IP10), monocyte chemoattractant protein 1 (MCP1), Macrophage Inflammatory Proteins 1A (MIP1A), and Tumor Necrosis Factor Alpha (TNF α ) were found in intensive care unit (ICU) patients compared to non-ICU patients [9,10], supporting the evidence which attributes severe cases of COVID-19 to an intense immune response. Emerging data have increased our understanding of hallmarks of severe cases of COVID-19. Shi et al. showed a decrease in the number of circulating CD4 + cells, CD8 + cells, B cells, and natural killer (NK) cells, as well as a decrease of monocytes, eosinophils, and basophils [11]. In addition to this, both human monocytes and macrophages express ACE2 and can be directly infected with SARS-CoV-2, increasing the transcription of pro-inflammatory genes associated with increased COVID-19 severity [1].

Interestingly, Pujhari et al. suggested that more than 70% of COVID-19 deaths are attributed to clotting-associated complications, emphasizing the role of cytokine storms, activation of neutrophils, and release of neutrophil extracellular traps as possible mechanisms contributing to blood clotting disorders [12]. Neutrophilia-induced lung injury in severe COVID-19 patients was also reported by Wang et al., who observed lesions after the second week of disease onset, coinciding with neutrophilia progression [13].

A deep analysis of our complex immune system is important to identify key players involved in COVID-19 severity. Single-cell analysis is therefore a valuable approach that has been utilized to elucidate phenotypic and expressional di GLYPH&lt;11&gt; erences between cell subsets involved in the peripheral immune response in relation to COVID-19 infection [2,14]. In our current study, publicly available single-cell data from bronchoalveolar lavage (BAL) comprising a total of 68,873 single cells derived from two healthy subjects, three patients with mild COVID-19, and five patients with severe COVID-19 were subjected to iterative clustering and guide-gene selection 2 (ICGS2) and AltAnalyze algorithms, identifying gene signatures associated with COVID-19 severity and revealing the presence of neutrophils

and macrophage cluster-1 as hallmarks of severe COVID-19. Further computational analyses identified several functional categories to be enriched in BAL from severe cases of infection, including inflammatory response, chemotaxis of myeloid cells, phagocytes, and granulocytes. Changes in BAL cells were further extrapolated to peripheral blood mononuclear cells (PBMCs) from a second cohort of COVID-19 patients. Deepening our understanding of the specific cell subsets responsible for severe outcomes in patients and expanding our knowledge on how these subsets contribute to the overall immune response according to their genes signatures will bring us closer to identifying possible therapeutic interventions for the treatment of COVID-19, in particular of those cases associated with severe complications.

## 2. Materials and Methods

## 2.1. Single-Cell Data Retrieval and Bioinformatics

Aschematic presentation of the experimental and bioinformatics workflow for transcriptome analysis from BAL and PBMCs from COVID-19 patients and healthy subjects is provided in Supplementary Figure S1. Read count matrices (.H5) were retrieved from the SRP250732 GSM4475052 dataset. Expression values / were first normalized to counts per ten thousand (CPTT) and were then subjected to the ICGS2 algorithm to identify cell types using Pearson correlation &gt; 0.2. Detailed description of the computational algorithm employed can be found in Venkatasubramanian et al. [15]. ICGS2 and AltAnalyze pipelines were found to outperform state-of-the-art scRNA-Seq detection workflows when applied to well-established benchmarks, as they combine multiple complementary subtype detection methods; Hierarchical Ordered Partitioning And Collapsing Hybrid (HOPACH, sparse non-negative matrix factorization, cluster 'fitness', support vector machine) to resolve rare and common cell states. ICGS2 identified cell clusters through a complex process of PageRank down-sampling, feature selection ICGS2, dimension reduction and clustering (sparse NMF, SNMF), cluster refinement (MarkerFinder algorithm), and finally cluster re-assignments using support vector machine (SVM). The top 500 genes with the highest dispersion were initially identified, followed by pairwise correlations of variable genes. Dimension reduction with sparse NMF was employed to improve the delineation of cell clusters following HOPACH clustering. The MarkerFinder algorithm was subsequently applied to identify rigorously defined cell clusters with unique gene expression for downstream cell cluster assignment, which identified genes that are positively correlated with an idealized cluster-specific expression profile. Cell cluster assignment was finally achieved from the marker genes identified for su GLYPH&lt;14&gt; ciently fitting clusters, based on the cells assigned to the specific SNMF.

## 2.2. Gene Set Enrichment and Modeling of Gene Interactions Networks

Average gene expression levels across all cells (bulk) from each sample were subjected to comparative analysis (i.e., severe vs. healthy, severe vs. mild, and mild vs. healthy) using AltAnalyze v.2.1.3 pipeline. Di GLYPH&lt;11&gt; erentially expressed genes were imported into the Ingenuity Pathways Analysis (IPA) software (Ingenuity Systems; www.ingenuity.com ) and were subjected to functional annotations / and regulatory network analysis using upstream regulator analysis (URA) to analyze upstream molecules, which are connected to genes in the dataset via a set of either direct or indirect relationships with respect to their expression changes. Mechanistic networks (MN) takes URA further via the generation of plausible directional networks from these regulators, employing the IPA computational algorithm. Downstream e GLYPH&lt;11&gt; ects analysis (DEA) identifies biological processes (disease) and functions, which are casually a GLYPH&lt;11&gt; ected by the deregulation of genes in datasets and predicts the outline of biological process, whether upregulated or downregulated. IPA uses precise algorithms to predict functional regulatory networks from gene expression data and provides a significance score for each network according to the fit of the network to the set of focus genes in the database. The p -value is the negative log of P and represents the possibility that focus genes in the network are found together by chance [16,17].

Cells

2020

,

9

, x

4  of  20

<!-- image -->

Figure 1. Representative single-cell analysis of bronchoalveolar lavage (BAL) from healthy subjects. ( a ) Representative single-cell analysis of BAL from healthy subjects employing the iterative clustering and guide-gene selection 2 (ICGS2) algorithm depicted as heat map. The text on the left indicates enriched cell-type  markers  from  the  default  gene-set  enrichment  analysis  and  corresponding  'Z' score p value. ( b ) Uniform manifold approximation and projection (UMAP) dimensionality reduction Figure 1. Representative single-cell analysis of bronchoalveolar lavage (BAL) from healthy subjects. ( a ) Representative single-cell analysis of BAL from healthy subjects employing the iterative clustering and guide-gene selection 2 (ICGS2) algorithm depicted as heat map. The text on the left indicates enriched cell-type markers from the default gene-set enrichment analysis and corresponding 'Z' score p value. ( b ) Uniform manifold approximation and projection (UMAP) dimensionality reduction visualization of cell clusters corresponding to data presented in panel ( a ).

<!-- image -->

visualization of cell clusters corresponding to data presented in panel a.

2.2. Gene Set Enrichment and Modeling of Gene Interactions Networks

Average  gene  expression  levels  across  all  cells  (bulk)  from  each  sample  were  subjected  to

comparative analysis (i.e., severe vs. healthy, severe vs. mild, and mild vs. healthy) using AltAnalyze

v.2.1.3 pipeline. Differentially expressed genes were imported into the Ingenuity Pathways Analysis

(IPA)

software  (Ingenuity

Systems;  www.ingenuity.com/)  and  were  subjected  to  functional

## 2.3. RNA-Seq Analysis of PBMCs from COVID-19 Patients

Raw sequencing data (fastq) from COVID-19 PBMCs were retrieved from the SRP262058 dataset and were subsequently pseudo-aligned to the Gencode release 33 index; reads were subsequently counted using KALLISTO 0.42.1 [18], as we described before [19,20]. Normalized transcripts per million (TPM) expression values were subsequently subjected to di GLYPH&lt;11&gt; erential analysis and hierarchical clustering as described before [21]. A volcano plot was used to illustrate the most di GLYPH&lt;11&gt; erentially expressed genes (log 2-fold change) vs. log10 p value.

## 2.4. Statistical Analyses

Statistical analyses and graphing were performed using Microsoft excel 2016 and GraphPad Prism 8.0 software (GraphPad, San Diego, CA, USA). Two-tailed t -test was used for comparative groups; p -values GLYPH&lt;20&gt; 0.05 (two-tailed t -test) were considered significant. For IPA analyses, the activation z-score was utilized to infer the activation states of the indicated network and functional categories. A Z score of GLYPH&lt;0&gt; 2.0 GLYPH&lt;21&gt; Z GLYPH&lt;21&gt; 2.0 was considered significant.

## 3. Results

3.1. Single-Cell Transcriptome Analysis of BAL Revealed Variable Cellular Composition in Severe and Mild COVID-19 Patients Compared to Healthy Subjects

ICGS2 algorithm was employed to decipher the cellular composition of BAL from two healthy, three mild, and five severe COVID-19 patients. Clustering patterns from representative healthy subjects identified seven cell clusters enriched in T cells, lung macrophages (perivascular interstitial, Cluster-0, Cluster-1, alveolar), neutrophils, and dendritic cells (Figure 1a). Figure 1b displays an alternative visualization, dimensionally reducing the data from Figure 1a via UMAP. Cell clusters exhibited a significant overlap between di GLYPH&lt;11&gt; erent gene signatures of di GLYPH&lt;11&gt; erent cell populations from healthy subjects.

ICGS2 analysis of patients with mild COVID-19 revealed distinct cell composition compared to the healthy control. Representative data from mild-COVID-19 BAL were mostly consistent of lung macrophages (cluster GLYPH&lt;0&gt; 0, GLYPH&lt;0&gt; 1, and GLYPH&lt;0&gt; 2), CD19, CD4, CD4 Th1, CD8, and NK cells, as well as lung and bronchial epithelial cells (Figure 2a). Figure 2b illustrates the data from a representative mild-COVID-19 patient using UMAP. Clusters 1, 2, 6, and 21 display significant distinction from other clusters, while the majority of other clusters were found centered around UMAP-X; 0, UPMA-Y; 5.

We subsequently characterized the cellular composition from severe-COVID-19 patients. Single-cell analysis of a representative severe-COVID-19 patient highlighted a massive enrichment in neutrophils and macrophages, especially cluster-1 (Figure 3a). Similar to what found for mild-COVID-19 patients, BAL from severe-COVID-19 patients also included lung epithelial and bronchial cells. Top enriched markers in severe-COVID-19 BAL were spermidine spermine N1-acetyltransferase 1 (SAT1), / involved in the catabolic pathway of polyamine metabolism, LY8E, Spi-1 proto-oncogene (SPI1), Fc fragment of IgE, high-a GLYPH&lt;14&gt; nity I, receptor for gamma polypeptide involved in allergic reactions (FCER1G), and transforming growth factor beta 1 (TGFB1). A UMAP visualization of cell clusters corresponding to panel (a) is presented in Figure 1b.

<!-- image -->

Figure 2. Representative single-cell analysis of BAL from a mild COVID-19 patient. ( a ) Representative single-cell analysis of BAL from a mild-COVID-19 patient employing the ICGS2 algorithm depicted Figure 2. Representative single-cell analysis of BAL from a mild COVID-19 patient. ( a ) Representative single-cell analysis of BAL from a mild-COVID-19 patient employing the ICGS2 algorithm depicted as heat map. ( b ) UMAP dimensionality reduction visualization of cell clusters corresponding to data presented in panel ( a ).

<!-- image -->

as heat map. (

b

) UMAP dimensionality reduction visualization of cell clusters corresponding to data

presented in panel a.

We subsequently characterized the cellular composition from severe-COVID-19 patients. Single-

cell  analysis  of  a  representative  severe-COVID-19  patient  highlighted  a  massive  enrichment  in

neutrophils  and  macrophages,  especially  cluster-1  (Figure  3a).  Similar  to  what  found  for  mild-

COVID-19 patients, BAL from severe-COVID-19 patients also included lung epithelial and bronchial

cells.

Top

enriched

markers

in

severe-COVID-19

BAL

were

spermidine/spermine

N1-

acetyltransferase 1 (SAT1), involved in the catabolic pathway of polyamine metabolism, LY8E, Spi-1

proto-oncogene (SPI1), Fc fragment of IgE, high-affinity I, receptor for gamma polypeptide involved

Cells

2020

,

9

, x

7  of  20

reactions  (FCER1G),  and  transforming  growth  factor  beta  1  (TGFB1).  A  UMAP

visualization of cell clusters corresponding to panel (a) is presented in Figure 1b.

<!-- image -->

Figure 3. Representative single-cell analysis of BAL  from  a severe-COVID-19  patient. ( a ) Representative single-cell  analysis  of  BAL  from  a  severe  COVID-19  patient  employing  the  ICGS2 algorithm depicted as heat map. ( b )  UMAP dimensionality reduction visualization of cell clusters corresponding to data presented in panel a. Figure 3. Representative single-cell analysis of BAL from a severe-COVID-19 patient. ( a ) Representative single-cell analysis of BAL from a severe COVID-19 patient employing the ICGS2 algorithm depicted as heat map. ( b ) UMAP dimensionality reduction visualization of cell clusters corresponding to data presented in panel ( a ).

<!-- image -->

- 3.2. Combination Analysis of Single-Cell Transcriptomes of BAL from Severe- and Mild-COVID-19 Patients Compared to Healthy Subjects 3.2. Combination Analysis of Single-Cell Transcriptomes of BAL from Severe- and Mild-COVID-19 Patients Compared to Healthy Subjects

For a more comprehensive and comparative look into the single-cell transcriptome data and to avoid  over-representation  from  different  samples,  equal  number  of  single  cells  were  randomly selected from each sample, hence, a total of 16,310 cells were subjected to ICGS2 analysis (Figure 4a, For a more comprehensive and comparative look into the single-cell transcriptome data and to avoid over-representation from di GLYPH&lt;11&gt; erent samples, equal number of single cells were randomly selected from each sample, hence, a total of 16,310 cells were subjected to ICGS2 analysis (Figure 4a, Supplementary Table S1). Firstly, we observed single cells from each of the three severity subsets to largely cluster together, with some overlap in the mild and severe cases. Whereas control and milder cases presented upregulation in gene markers associated with lung perivascular interstitial macrophages and lung macrophage cluster-0, single cells from the severe, and to a lesser extent, mild cases showed an upregulation in cell markers pertaining to lung neutrophils, lung CCR7, and dendritic cells (DCs), indicating a distinct immune response. Interestingly, severe-COVID-19 patients displayed

Supplementary Table S1). Firstly, we observed single cells from each of the three severity subsets to

largely cluster together, with some overlap in the mild and severe cases. Whereas control and milder

cases  presented  upregulation  in  gene  markers  associated  with  lung  perivascular  interstitial

macrophages and lung macrophage cluster-0, single cells from the severe, and to a lesser extent, mild

cases  showed  an  upregulation  in  cell  markers  pertaining  to  lung  neutrophils,  lung  CCR7,  and

dendritic cells (DCs), indicating a distinct immune response. Interestingly, severe-COVID-19 patients

a remarkable enrichment in neutrophils and macrophage cluter-1 compared to mild-COVID-19 patients and healthy controls. UMAP illustration of cell distribution from the same study group is shown in Figure 4b, with selected cell clusters being marked. displayed  a  remarkable  enrichment  in  neutrophils  and  macrophage  cluter-1  compared  to  mildCOVID-19 patients and healthy controls. UMAP illustration of cell distribution from the same study group is shown in Figure 4b, with selected cell clusters being marked.

Figure 4. Combined single-cell analysis of BAL from severe- and mild-COVID-19 patients compared to healthy subjects. A total of 16,310 BAL-derived single cells from two healthy subjects, three patients with mild COVID-19, and five patients with severe COVID-19 were subjected to singl- cell analysis. Data are displayed as heat map ( a ) with the enriched cell population indicated on the left. ( b ) UMAP Figure 4. Combined single-cell analysis of BAL from severe- and mild-COVID-19 patients compared to healthy subjects. A total of 16,310 BAL-derived single cells from two healthy subjects, three patients with mild COVID-19, and five patients with severe COVID-19 were subjected to singl- cell analysis. Data are displayed as heat map ( a ) with the enriched cell population indicated on the left. ( b ) UMAP dimensionality reduction visualization of cell clusters corresponding to data presented in panel a with selected enriched cell populations indicated. M F : macrophages.

<!-- image -->

3.3. Enriched Gene Markers in Patients with Mild or Severe COVID-19 Compared to Healthy Subjects

The ICGS2 algorithm identified gene signatures with the strongest correlation with the indicated cell types. We subsequently explored the expression of selected gene markers indicative of neutrophils, macrophage (M F ) cluster 1, macrophage cluster 0 interstitial, and noncoding RNAs (ncRNAs) in a / total of 68,873 single cells derived from the same cohort of patients with varying COVID-19 severity. Representative gene signatures of each cell population are shown in Figure 5a-d. Neutrophil-derived signature ( IFITM2 , IFITM1 , H3F3B , SAT1 , and S100A8 ) exhibited significantly higher expression

cell

types.  We  subsequently  explored  the  expression  of  selected  gene  markers  indicative  of

neutrophils,  macrophage  (M

Φ

)  cluster  1,  macrophage  cluster  0/interstitial,  and  noncoding  RNAs

(ncRNAs) in a total of 68,873 single cells  derived  from  the  same  cohort  of  patients  with  varying

COVID-19 severity. Representative gene signatures of each cell population are shown in Figure 5a-

d. Neutrophil-derived signature (

IFITM2  IFITM1  H3F3B  SAT1

,

,

,

, and

S100A8

) exhibited significantly

( p &lt; 0.0001) in severe cases compared to normal, with the mild cases exhibiting intermediate expression between the normal and the severe cases (Figure 5a). The macrophage cluster-1-derived signature ( CCL8 , CCL3 , CCL2 , KLF6 , and SPP1 ) was confirmed to be significantly higher in severe cases of COVID-19 compared to control and mild cases (Figure 5b). Patients with devere and mild COVID-19 exhibited substantial reduction in the expression of FABP4 APOC1 APOE C1QB , , , , and NURP1 , all associated with interstitial and macrophage cluster-0 (Figure 5c). MALAT1 NEAT1 , , and SNHG25 long noncoding RNAs (lncRNAs) were downregulated in mild and severe COVID-19 BAL cells. Further downregulation of MALAT1 and NEAT1 was observed in mild-COVID-19 BAL cells, while SNHG25 was markedly downregulated in both mild- and severe-COVID-19 BAL cells (Figure 5d). higher expression ( p &lt; 0.0001) in severe cases compared to normal, with the mild cases exhibiting intermediate  expression  between  the  normal  and  the  severe  cases  (Figure  5a).  The  macrophage cluster-1-derived signature ( CCL8  CCL3  CCL2  KLF6 , , , , and SPP1 ) was confirmed to be significantly higher in severe cases of COVID-19 compared to control and mild cases (Figure 5b). Patients with devere  and  mild  COVID-19  exhibited  substantial  reduction  in  the  expression  of FABP4  APOC1 , , APOE   C1QB , ,  and NURP1 ,  all  associated  with  interstitial  and  macrophage  cluster-0  (Figure  5c). MALAT1  NEAT1 , , and SNHG25 long noncoding RNAs (lncRNAs) were downregulated in mild and severe COVID-19 BAL cells. Further downregulation of MALAT1 and NEAT1 was observed in mildCOVID-19 BAL cells, while SNHG25 was markedly downregulated in both mild- and severe-COVID19 BAL cells (Figure 5d).

Figure 5. Expression of enriched gene markers in patients with mild or severe COVID-19 compared to healthy subjects. Expression of gene signatures derived from neutrophils ( a ),  macrophage (M Φ ) cluster 1 ( b ),  macrophage cluster 0/interstitial ( c ),  and  noncoding RNAs (ncRNA) ( d )  in  a  total  of 68,873 single cells derived from two healthy subjects, three patients with mild COVID-19, and five patients with severe COVID-19. Data are presented as violin plots. N: control, M: mild, S: Severe. Statistical analysis revealed significant differences in gene expression ( p ≤ 0.0001) when comparing S vs. M, S vs. N, and M vs. N for the indicated genes. Figure 5. Expression of enriched gene markers in patients with mild or severe COVID-19 compared to healthy subjects. Expression of gene signatures derived from neutrophils ( a ), macrophage (M F ) cluster 1 ( b ), macrophage cluster 0 interstitial ( / c ), and noncoding RNAs (ncRNA) ( d ) in a total of 68,873 single cells derived from two healthy subjects, three patients with mild COVID-19, and five patients with severe COVID-19. Data are presented as violin plots. N: control, M: mild, S: Severe. Statistical analysis revealed significant di GLYPH&lt;11&gt; erences in gene expression ( p GLYPH&lt;20&gt; 0.0001) when comparing S vs. M, S vs. N, and Mvs. N for the indicated genes.

<!-- image -->

3.4. Canonical and Upstream Regulator Pathway Analyses Highlighted Activation of Innate Immune Response in BAL Cells from Severe COVID-19 3.4. Canonical and Upstream Regulator Pathway Analyses Highlighted Activation of Innate Immune Response in BAL Cells from Severe COVID-19

The average gene expression levels across all cells in each sample were subjected to differential expression analysis comparing patients with severe (Supplementary Table S2) and mild COVID-19 The average gene expression levels across all cells in each sample were subjected to di GLYPH&lt;11&gt; erential expression analysis comparing patients with severe (Supplementary Table S2) and mild COVID-19 (Supplementary Table S3) to healthy subjects. Di GLYPH&lt;11&gt; erentially expressed genes were subsequently subjected to comparative canonical pathway analysis in IPA, revealing modest enrichment in a number of canonical pathways including innate immunity associated with interferon signaling, FC gamma, IL17, and Tec kinase signaling in severe-COVID-19 BAL cells, while PD-1 and PDL-1 pathways were suppressed (Figure 6a). Furthermore, pathways associated with adaptive immune responses were predominantly signaling pathways that contribute to the regulation of activated e GLYPH&lt;11&gt; ector T-cell functions such as iCOS-iCOSL, Th1, protein kinase C-theta (PKC theta), calcium-induced T lymphocyte apoptosis and dendritic cell maturation pathways, which were downregulated in both severe- and mild-COVID-19 BAL cells (Figure 6a). Similarly, an in-depth comparative analysis of severe- and mild-COVID-19 BAL transcriptome data showed significant enrichment of several upstream regulators. In particular, IFNG, PRL, TGM2, TLR9, PAF1, IL1B, TNF, and NFKB were activated in severe-COVID-19 BAL cells (Figure 6b). However, several other upstream regulators were suppressed in severe- and mild- COVID-19 BAL cells compared to healthy individuals.

The ICGS2 algorithm identified gene signatures with the strongest correlation with the indicated

9

11  of  20

Figure  6. Identification  of  canonical  pathways  and  upstream  regulator  networks  associated  with severe and mild COVID-19. Differentially expressed genes in patients with severe vs. control and mild  vs.  control  COVID-19  were  subjected  to  canonical  and  upstream  regulator  analysis  using ingenuity  pathways  analysis  (IPA).  ( a ) Comparative  analysis  of  significantly  altered  canonical Figure 6. Identification of canonical pathways and upstream regulator networks associated with severe and mild COVID-19. Di GLYPH&lt;11&gt; erentially expressed genes in patients with severe vs. control and mild vs. control COVID-19 were subjected to canonical and upstream regulator analysis using ingenuity pathways analysis (IPA). ( a ) Comparative analysis of significantly altered canonical pathways in mildand severe-COVID-19 BAL transcriptome data. ( b ) Comparative analysis of significantly altered upstream regulatory networks in mild- and severe-COVID-19 BAL transcriptome data. Red indicates activated, while blue indicates suppressed pathways. Activation Z score is depicted according to the color scale.

<!-- image -->

We subsequently sought to identify the pathways and functional categories unique to severe-COVID-19 BAL cells. Di GLYPH&lt;11&gt; erential gene expression analysis of BAL cells from severe- compared to mild-COVID-19 patients revealed 53 upregulated and 34 downregulated genes (Supplementary Table S4). Mechanistic network analysis elucidates the pragmatic alterations in appropriate gene expression through upstream regulator prediction. The activated mechanistic networks in patients with severe COVID-19 highlighted the predicted relationship between IL1A, IL1B, and TNF, and their regulation in gene datasets based on Z scores. Herein, the main IL1B upstream regulator activated 16 downstream molecules including two upstream regulators, TNF and IL1A, and inhibited two downstream genes, HLA-DRA and APOE . Similarly, TNF activated 16 and inhibited 6 downstream target genes, among those 9 genes (upregulated CCL3, CCL4, ILR1, DUSP1, BCL2A1 and downregulated APOE ) including IL1A upstream regulator, which were common between IL1B and TNF. Furthermore, the upstream regulator IL1A was predicted to activate seven downstream targets, among which, four shared with IL1B (M2A, CXCL8, CXCL2, TNF, and CCL8) and two shared with TNF (NFKBIA and FOS) (Figure 7a). Similarly, another mechanistic network illustrates the relationship between CCL5, TLR7, and TLR9. Mainly, the upstream regulator TLR7 was predicted to activate 11 downstream targets including two upstream regulators, TLR9 and CCL5. Further analysis with TLR9 revealed direct activation of two downstream targets (IFITM1 and NAMPT) shared with CCL5 and another target, ISG20, which is shared with TLR7 through seven intermediated targets, including the main upstream regulator CCL5. Interestingly, CCL5 is predicted to exert the same stimulatory e GLYPH&lt;11&gt; ect on CCL2 as TLR9 and TLR7 and have distinct e GLYPH&lt;11&gt; ects on four more downstream targets (Figure 7b). Cells 2020 , 9 , x 12  of  20 pathways  in  mild-  and  severe-COVID-19  BAL  transcriptome  data.  ( b )  Comparative  analysis  of significantly altered upstream regulatory networks in mild- and severe-COVID-19 BAL transcriptome data.  Red  indicates  activated,  while  blue  indicates  suppressed  pathways.  Activation  Z  score  is depicted according to the color scale.

Figure  7. Illustration  of  selected  activated  upstream  networks  in  patients  with  severe  COVID-19. Graphical presentation of IL1A, IL1B, and TNF ( a ) networks in patients with severe COVID-19. ( b ) Figure 7. Illustration of selected activated upstream networks in patients with severe COVID-19. Graphical presentation of IL1A, IL1B, and TNF ( a ) networks in patients with severe COVID-19. ( b ) Presentation of CCL5, TLR7, and TLR9 upstream regulator networks.

<!-- image -->

Presentation of CCL5, TLR7, and TLR9 upstream regulator networks.

3.5. Disease and Functional Analysis of Differentially Expressed Genes in BAL from Severe- and Mild-

COVID-19 Patients Indicated the Activation of Innate Immune Responses

In order to understand the downstream functional effects of upstream regulators in severe- and

mild-COVID-19 BAL cells, we employed IPA downstream effector analysis. Our analysis predicted

## 3.5. Disease and Functional Analysis of Di GLYPH&lt;11&gt; erentially Expressed Genes in BAL from Severe- and MildCOVID-19 Patients Indicated the Activation of Innate Immune Responses

In order to understand the downstream functional e GLYPH&lt;11&gt; ects of upstream regulators in severe- and mild-COVID-19 BAL cells, we employed IPA downstream e GLYPH&lt;11&gt; ector analysis. Our analysis predicted the various disease and functional activities based on the deregulated upstream regulator molecules in the dataset portrayed as a vertical heat map. Comparative analysis revealed common deregulated disease activities and functions in BAL cells from patients with severe and mild COVID-19, including the downregulation of RNA virus replication, viral infection, replication of influenza, and hepatitis C and vesicular stomatitis virus, and the upregulation of multiple sclerosis inflammatory response and activation of myeloid cells and phagocytes (Supplementary Table S5). Comparatively, many disease and functional pathways were upregulated only in severe-COVID-19 BAL cells, including chemotaxis, cell adhesion, cell movement, migration of myeloid cells, phagocytes, granulocytes, monocytes, and cell movement of NK cells. Interestingly, activation of total lymphocyte and T lymphocyte pathways were downregulated. Therefore, our downstream e GLYPH&lt;11&gt; ector analysis revealed the augmentation of innate immune responses in severe-COVID-19 patients (Figure 8a). Disease and function analysis of BAL from severe- vs. mild-COVID-19 patients revealed a number of activated functional categories (Supplementary Table S6). Of particular interest, our regulator e GLYPH&lt;11&gt; ector analysis in severe-COVID-19 BAL cells revealed activation of CCL2, CCL3, CCL3L1, CCL4, CCL7, CCL8, CXCL8, SPP1, S100A8, and S100A9, and inhibition of MT-ND1 and FN1 upstream regulators which is predicted to trigger the chemotaxis of phagocytes and cellular movement of neutrophils in severe-COVID-19 BAL cells (Figure 8b,c).

## 3.6. Similarities in Transcriptome Data from BAL and PBMCs from COVID-19 Patients

To further highlight if the observed changes in BAL cells can be reflected in the circulation, we explored PBMCs transcriptome data from an independent cohort of seven COVID-19 patients and six healthy controls, revealing commonalities for several genes di GLYPH&lt;11&gt; erentially expressed in BAL and PBMCs. Hierarchical clustering based on di GLYPH&lt;11&gt; erential gene expression (log2) (Figure 9a and Supplementary Table S7) highlighted the enrichment in functional categories (GO) involved in defense responses to viruses, killing cells of other organisms, and activation of innate (complement) immune functions and classical pathways in PBMCs from COVID-19 patients. Other upregulated functions in COVID-19 patients included processes related to acute inflammatory responses, response to interferon gamma, pattern recognition receptor activity, antigen binding, and platelet activation, as well as negative regulation of viral genome replication. On the other hand, the most enriched functional category in the healthy group was positive regulation of NK cell-mediated immunity, suggesting a possible suppression of this cell population in the periphery of COVID-19 patients. Interestingly, when comparing PBMCs and the BAL-derived data from the two independent cohorts, we observed 11 genes ( IFI27 , IFITM3 IFI6, ISG15 , , IFIT3 , RSAD2 MX1 IFIT1 OASL IFI30 , , , , , and OAS1 ) that were found in all three categories, PBMCs, BAL from severe-COVID-19 patients, and BAL from mild-COVID-19 patients. In addition, there were 14 commonly upregulated genes ( S100A8 , IFI44L , IFI44 , CXCL8 , CCR1 PLSCR1 EPSTI1 FPR1 OAS2 IL1RN TYMP BCL2A1 GAPDH , , , , , , , , , and OAS3 ) in severe-Covid-19 BAL cells and PBMCs, and one gene in common ( C1QC ) for BAL and PBMCs form mild cases of COVID-19. (Figure 9b). Volcano plots depicting selected genes common to BAL and PBMCs, indicating the upregulated (red) and downregulated (blue) genes, are shown in Figure 9c. The upregulated genes included S100A8, S100A9, IFI27, EPSTI1 , and EPSTI1 . These genes encode calcium-binding proteins that play important roles in the regulation of inflammatory immune responses. Constitutively expressed in neutrophils and monocytes, they could lead to the induction of neutrophil chemotaxis and adhesion. Such commonalities displayed in BAL and in the circulation could provide us with potential biomarkers to target in the development of therapeutic interventions against viral infections.

in  severe-COVID-19 BAL cells revealed activation of  CCL2,  CCL3,  CCL3L1, CCL4, CCL7, CCL8,

CXCL8, SPP1, S100A8, and S100A9, and inhibition of MT-ND1 and FN1 upstream regulators which

is predicted to trigger the chemotaxis of phagocytes and cellular movement of neutrophils in severe-

COVID-19 BAL cells (Figure 8b,c).

Figure 8. Disease and functional analysis of differentially expressed genes in BAL from patients with mild and severe COVID-19. ( a ) Heat map depicting the activation states of the indicated disease and function categories in mild- and severe-COVID-19 BAL cells. Illustration of chemotaxis of phagocytes Figure 8. Disease and functional analysis of di GLYPH&lt;11&gt; erentially expressed genes in BAL from patients with mild and severe COVID-19. ( a ) Heat map depicting the activation states of the indicated disease and function categories in mild- and severe-COVID-19 BAL cells. Illustration of chemotaxis of phagocytes ( b ) and cell movement of neutrophils ( ) in patients with severe COVID-19 based on IPA analysis. c

<!-- image -->

(

b

) and cell movement of neutrophils ( ) in patients with severe COVID-19 based on IPA analysis.

c

Cells

2020

,

9

, x

15  of  20

<!-- image -->

Figure  9. Similarities  in  transcriptome  data  from  BAL  and  peripheral  blood  mononuclear  cell (PBMCs) in COVID-19 patients. ( a ) Hierarchical clustering summarizing differential gene expression (log2) in PBMCs from COVID-19 and normal controls, highlighting enriched functional categories (GO). ( b ) Venny diagram illustrating the aberrantly expressed genes in common in severe- and mildCovid-19 BAL and PBMC, with 11 genes in common to the three categories. ( ) Volcano plot depicting c selected genes common to BAL and PBMCs, indicating upregulated (red) and downregulated (blue) Figure 9. Similarities in transcriptome data from BAL and peripheral blood mononuclear cell (PBMCs) in COVID-19 patients. ( a ) Hierarchical clustering summarizing di GLYPH&lt;11&gt; erential gene expression (log2) in PBMCs from COVID-19 and normal controls, highlighting enriched functional categories (GO). ( b ) Venny diagram illustrating the aberrantly expressed genes in common in severe- and mild-Covid-19 BAL and PBMC, with 11 genes in common to the three categories. ( ) Volcano plot depicting selected c genes common to BAL and PBMCs, indicating upregulated (red) and downregulated (blue) genes.

<!-- image -->

genes.

## 4. Discussion

4. Discussion BAL  has  been  widely  used  in  diagnosing  lower  respiratory  airway  infections  [22]  and  has recently provided us with data on the pulmonary microenvironment during COVID-19 infection. Utilizing  single-cell  gene  expression  data  from  patients  with  COVID-19  at  varying  severity  in BAL has been widely used in diagnosing lower respiratory airway infections [22] and has recently provided us with data on the pulmonary microenvironment during COVID-19 infection. Utilizing single-cell gene expression data from patients with COVID-19 at varying severity in combination with modern computational analysis identified rigorously defined cell clusters, revealing the presence of neutrophils and macrophages cluster-1 as hallmarks of severe COVID-19. Our data are in agreement

with the work of Liao et al., who reported the presence of proinflammatory monocyte-derived macrophages in the BAL fluid from patients with severe COVID-9 employing the same dataset [2]. Gene signatures highlighted interferon-induced transmembrane (IFITM) protein 1 and 2 ( IFITM1 and IFITM2 ), which have been associated with other viruses including influenza and West Nile Virus [23,24]. We recently reported on the upregulation of several IFITM family members in bronchial epithelial cells infected with SARS-CoV-2 [25]. The involvement of such gene signatures emphasizes the link between innate immune response and e GLYPH&lt;11&gt; ects of COVID-19 on interferon gamma signaling. Histone structure and regulation also play a key role in the gene regulation of any transcript. Modifications in histones such as HAT1, HDAC2, and KDM5B were revealed by network analysis, identifying these histones as potential regulators of the SARS-CoV-2 receptor ACE2 in the human lung. In a cohort of 700 lung transcriptome samples, increased expression of ACE2 and the e GLYPH&lt;11&gt; ect of histone protein modifications in these patients are suggested to induce a severe COVID-19 phenotype [26]. H3 histone, family 3B (H3F3B), associated with neutrophils in our data, has been described in several cancers such as chondroblastoma [27] and hepatocellular carcinoma [28] and in ovarian cancer cell lines [29], where point mutations or upregulation in expression of its corresponding gene caused dysregulations and transcriptional changes leading to disease onset and progression. Another study showed that CCL8 was detected at high levels in the peritoneal fluid of patients who exhibited anastomotic leakage after colorectal surgery [30]. Elevated levels of SPP1 expression were also found to correlate with highly aggressive lung adenocarcinoma [31]. Zuo et al. described the role of neutrophil extracellular traps (NETs) released by neutrophils in order to regulate infection; however, when in excess, they contribute to inflammation and cytokine release, leading to thrombosis in the lungs and respiratory failure in patients with severe COVID-19 [32]. Such evidence backs our findings and confirms the associations between these gene signatures and processes such as the involvement of neutrophils and macrophages in inflammation in several disease types, including viral infection.

Pathological changes are associated with increased vascular permeability induced by the binding of SARS-CoV-2 to ACE2 receptors on endothelial cells, followed by the recruitment of activated neutrophils, macrophages, and other immune cells, which collectively result in increased production of inflammatory cytokines including IL-6, IL-8, G-CSF, MCP1, IL-2, TNFα , and IL-1 β [33,34]. Some of these cytokines further amplify the inflammatory loop and induce the recruitment of more inflammatory cells, while others initiate and activate the coagulation-mediated cascade [33]. In turn, persistent unresolved inflammation leads to endothelial cell dysfunction, Disseminated intravascular coagulation (DIC), alveolar dysfunction, severe acute respiratory distress syndrome (ARDS), and ultimately multi-organ failure and death [33,35]. Higher levels of several inflammatory cytokines including TNFα , IL-6, and IL-1 and inflammatory chemokines such as CCL2, CCL3, and CXCL10 are associated with disease severity and death in COVID-19 patients [36]. TNFα and IL-1 β induce vasodilation and permeability, which allows immune cells to reach the sites of damage, while ILβ and IL-6 induce complement and opsonization. Di GLYPH&lt;11&gt; erent chemokines and cytokines, including CCL2, 3, 5, CXCL8, 9, 10, IFN γ , TNF α , IL-1β , IL-1RA, IL-6, IL-7, IL-8, IL-12, IL33, GCSF, GMCSF, IP10, MCP1, MIP1 α , MIP1 β , PDGFB, and VEGFA, contribute to cytokine storms [37,38]. These chemokines are primarily involved in the recruitment of other leukocytes to tissues, while pro-inflammatory cytokines are involved in e GLYPH&lt;11&gt; ector functions causing damage to cells [39,40]. The resulting intense immune response is extensively documented in ARDS a GLYPH&lt;11&gt; ecting the lungs but leads to multi-organ dysfunction (MODS) and failure via tissue damage and ultimately to death in severe SARS-CoV-2 infections. In line with this, high cytokine levels have been reported in critically ill COVID-19 patients [9].

Ingenuity pathway analysis revealed enrichment of interferon signaling, suggested by Felgenhauer et al. to be a potential key player in the management of COVID-19, since IFNs type I and III inhibited SARS-CoV-2 in a dose-dependent manner [41]. In other reports, increased IFN type I and II production in response to viral infection was found to impair lung epithelial regeneration throughout the duration of recovery from viral infection [42]. The idea of targeting Fc γ receptor (Fc γ R) pathways identified in our ingenuity pathway analysis is in agreement with a study by Chakraborty et al., which

reported a global analysis of antibodies produced during SARS-CoV-2 infections [43]. Reduced Fc glycosylation in COVID-19 patients led up to a 10-fold higher a GLYPH&lt;14&gt; nity for Fc γ RIIIa, which is abundant on monocytes, macrophages, and NK cells, in turn promoting pro-inflammatory cytokine production and cytotoxic e GLYPH&lt;11&gt; ector cell activity [44]. Activation of such pathways could be a contributing factor to severe COVID-19 and provide potential biomarkers for targeted therapy.

Other functional categories in BAL associated with severe-COVID-19 patients include inflammatory response and chemotaxis of myeloid, phagocytes, and granulocytes, among the most activated. This is expected in these cases, as viral recognition by macrophages initiates the recruitment of other immune cells through IL-6, TNFα , IL-1 β , and type-1 interferon signaling [36].

Emerging evidence highlights the roles played by lncRNAs during the course of viral infection. Gene signatures from three lncRNA gene markers ( MALAT1 NEAT1 , , and SNHG25 ) were found to be downregulated in mild and severe cases of COVID-19, compared to normal controls. Studies on MALAT1 in inflammatory injury following lung transplant interestingly showed that the silencing of MALAT1 alleviated inflammatory injury by inhibiting neutrophil chemotaxis and immune cell infiltration to the site of infection [45]. The downregulation of MALAT1 in our analysis could indicate a role for this lncRNA as an agent for the regulation of neutrophil chemotaxis that is rife in severe cases, in e GLYPH&lt;11&gt; orts to naturally alleviate inflammatory injury in COVID-19-positive cases. NEAT1 lncRNA has also been associated with viral infection, namely, HIV-1. Its knockdown, as shown by Zhang et al., led to enhanced viral production and inflammation by promoting the export of HIV-1 mRNA transcripts in HeLa cells [46].

Interestingly, when comparing data from BAL to those from PBMCs in the circulation, several genes were identified in common as aberrantly expressed, highlighting the potential of using PMBCs in the circulation as liquid biopsies in order to identify initial clues surrounding the immune microenvironment upon infection. Several of the commonly upregulated genes in BAL and PBMCs from COVID-19 patients were indicative of an interferon response. Upregulated genes included S100A8 , S100A9 , IFI27 , EPSTI1 , and EPSTI1 . These genes encode calcium-binding proteins that play an important role in the regulation of inflammatory immune responses. Constitutively expressed in neutrophils and monocytes, they could lead to the induction of neutrophil chemotaxis and adhesion, as we have previously reported in Calu-3 human lung epithelial cells [47]. Our data are concordant with those of Wilk and colleagues who also reported the presence of an interferon-stimulated gene signature and neutrophils in the circulation of patients with acute respiratory failure requiring mechanical ventilation [14]. Such commonalities displayed by BAL and the circulation could provide us with potential biomarkers to target in the development of therapeutic interventions against viral infections.

Taken together, our data revealed the presence of neutrophils and macrophage cluster-1 as the main immune cell subsets associated with severe COVID-19 and identified their inflammatory and chemotactic gene signatures, as well as possible upstream regulators and potentially a GLYPH&lt;11&gt; ected mechanistic networks throughout the course of SARS-CoV-2 infection. We also identified commonalties in transcriptome data from BAL and PBMCs in COVID-19 patients. Further functional studies are needed to expand our understanding of how neutrophils and macrophage cluster-1 specifically a GLYPH&lt;11&gt; ect the immune system and of the downstream consequences this has upon SARS-CoV-2 infection. However, this study provides an interesting introduction for the potential identification of possible immune-based therapeutic interventions.

Supplementary Materials: The following are available online at http: // www.mdpi.com 2073-4409 9 11 2374 s1, / / / / / Figure S1: Schematic presentation of the experimental and bioinformatics workflow for transcriptome analysis of BAL and PBMCs from COVID-19 patients and healthy subjects, Table S1: Marker genes associated with the indicated cell clusters in healthy, mild- and severe-COVID-19 BAL cells, Table S2: Di GLYPH&lt;11&gt; erentially expressed genes in BAL cells from mild-COVID-19 patients vs. healthy subjects, Table S3: Di GLYPH&lt;11&gt; erentially expressed genes in BAL cells from severe-COVID-19 patients vs. healthy subjects, Table S4: Comparison of upstream analysis of BAL cells from severe- COVID-19 patients vs. control and mild- COVID-19 patients vs. control, Table S5: Disease and function comparison between severe and mild cases of COVID-19, Table S6: Comparison of disease and function between severe-Covid-19 patients vs. control and mild- Covid-19 patients vs. control, Table S7: Di GLYPH&lt;11&gt; erentially expressed genes in PBMCs from COVID-19 patients vs. control.

Author Contributions: Conceptualization, N.M.A.; methodology, N.M.A.; formal analysis, N.M.A.; data curation, N.M.A.; writing-original draft preparation, H.S., R.V.; writing-review and editing, H.S., E.E., N.M.A. All authors have read and agreed to the published version of the manuscript.

Funding: This work was supported by a start-up grant for Nehad Alajez (QB13) from Qatar Biomedical Research Institute.

Conflicts of Interest: The authors declare no conflict of interest.

## References

- 1. Wang, J.; Jiang, M.; Chen, X.; Montaner, L.J. Cytokine storm and leukocyte changes in mild versus severe SARS-CoV-2 infection: Review of 3939 COVID-19 patients in China and emerging pathogenesis and therapy concepts. J. Leukoc. Biol. 2020 , 108 , 17-41. [CrossRef] [PubMed]
- 2. Liao, M.; Liu, Y.; Yuan, J.; Wen, Y.; Xu, G.; Zhao, J.; Cheng, L.; Li, J.; Wang, X.; Wang, F.; et al. Single-cell landscape of bronchoalveolar immune cells in patients with COVID-19. Nat. Med. 2020 , 26 , 842-844. [CrossRef] [PubMed]
- 3. Ho mann,M.; Kleine-Weber, H.; Schroeder, S.; Krüger, N.; Herrler, T.; Erichsen, S.; Schiergens, T.S.; Herrler, G.; GLYPH&lt;11&gt; Wu, N.-H.; Nitsche, A.; et al. SARS-CoV-2 Cell Entry Depends on ACE2 and TMPRSS2 and Is Blocked by a Clinically Proven Protease Inhibitor. Cell 2020 , 181 . [CrossRef] [PubMed]
- 4. Wu, K.; Chen, L.; Peng, G.; Zhou, W.; Pennell, C.A.; Mansky, L.M.; Geraghty, R.J.; Li, F. A Virus-Binding Hot Spot on Human Angiotensin-Converting Enzyme 2 Is Critical for Binding of Two Di GLYPH&lt;11&gt; erent Coronaviruses. J. Virol. 2011 , 85 , 5331-5337. [CrossRef]
- 5. Jia, H.P.; Look, D.C.; Shi, L.; Hickey, M.; Pewe, L.; Netland, J.; Farzan, M.; Wohlford-Lenane, C.; Perlman, S.; McCray, P.B., Jr. ACE2 Receptor Expression and Severe Acute Respiratory Syndrome Coronavirus Infection Depend on Di GLYPH&lt;11&gt; erentiation of Human Airway Epithelia. J. Virol. 2005 , 79 , 14614-14621. [CrossRef]
- 6. Donnelly, C.A.; Ghani, A.C.; Leung, G.M.; Hedley, A.J.; Fraser, C.; Riley, S.; Abu-Raddad, L.J.; Ho, L.-M.; Thach, T.-Q.; Chau, P.; et al. Epidemiological determinants of spread of causal agent of severe acute respiratory syndrome in Hong Kong. Lancet 2003 , 361 , 1761-1766. [CrossRef]
- 7. Cai, A.; McCla GLYPH&lt;11&gt; erty, B.; Benson, J.; Ramgobin, D.; Kalayanamitra, R.; Shahid, Z.; Gro GLYPH&lt;11&gt; , A.; Aggarwal, C.S.; Patel, R.; Polimera, H.; et al. COVID-19: Catastrophic Cause of Acute Lung Injury. J. South Dak. Med. 2020 , 73 , 252-260.
- 8. Korber, B.; Fischer, W.M.; Gnanakaran, S.; Yoon, H.; Theiler, J.; Abfalterer, W.; Hengartner, N.; Giorgi, E.E.; Bhattacharya, T.; Foley, B.; et al. Tracking Changes in SARS-CoV-2 Spike: Evidence that D614G Increases Infectivity of the COVID-19 Virus. Cell 2020 , 182 . [CrossRef]
- 9. Huang, C.; Wang, Y.; Li, X.; Ren, L.; Zhao, J.; Hu, Y.; Zhang, L.; Fan, G.; Xu, J.; Gu, X.; et al. Clinical features of patients infected with 2019 novel coronavirus in Wuhan, China. Lancet 2020 , 395 , 497-506. [CrossRef]
- 10. Dandekar, A.A.; Perlman, S. Immunopathogenesis of coronavirus infections: Implications for SARS. Nat. Rev. Immunol. 2005 , 5 , 917-927. [CrossRef]
- 11. Shi, H.; Wang, W.; Yin, J.; Ouyang, Y.; Pang, L.; Feng, Y.; Qiao, L.; Guo, X.; Shi, H.; Jin, R.; et al. The inhibition of IL-2 IL-2R gives rise to CD8( / + ) T cell and lymphocyte decrease through JAK1-STAT5 in critical patients with COVID-19 pneumonia. Cell Death Dis. 2020 , 11 , 429. [CrossRef] [PubMed]
- 12. Pujhari, S.; Paul, S.; Ahluwalia, J.; Rasgon, J.L. Clotting disorder in severe acute respiratory syndrome coronavirus 2. Rev. Med Virol. 2020 , 2177. [CrossRef]
- 13. Wang,J.; Li, Q.; Yin, Y. Excessive Neutrophils and Neutrophil Extracellular Traps in COVID-19. Front. Immunol. 2020 , 11 , 2063. [CrossRef]
- 14. Wilk, A.J.; Rustagi, A.; Zhao, N.Q.; Roque, J.; Mart nez-Col í ó n, G.J.; McKechnie, J.L.; Ivison, G.T.; Ranganath, T.; Vergara, R.; Hollis, T.; et al. A single-cell atlas of the peripheral immune response in patients with severe COVID-19. Nat. Med. 2020 , 26 , 1070-1076. [CrossRef] [PubMed]
- 15. Venkatasubramanian, M.; Chetal, K.; Schnell, D.J.; Atluri, G.; Salomonis, N. Resolving single-cell heterogeneity from hundreds of thousands of cells through sequential hybrid clustering and NMF. Bioinformatics 2020 , 36 , 3773-3780. [CrossRef]
- 16. Calvano, S.E.; Xiao, W.; Richards, D.R.; Felciano, R.M.; Baker, H.V.; Cho, R.J.; Chen, R.O.; Brownstein, B.H.; Cobb, J.P.; Tschoeke, S.K.; et al. A network-based analysis of systemic inflammation in humans. Nature 2005 , 437 , 1032-1037. [CrossRef]

- 17. Vishnubalaji, R.; Nair, V.S.; Ouararhni, K.; Elkord, E.; Alajez, N.M. Integrated Transcriptome and Pathway Analyses Revealed Multiple Activated Pathways in Breast Cancer. Front. Oncol. 2019 , 9 , 910. [CrossRef]
- 18. Bray, N.L.; Pimentel, H.; Melsted, P.; Pachter, L. Near-optimal probabilistic RNA-seq quantification. Nat. Biotechnol. 2016 , 34 , 525-527. [CrossRef]
- 19. Elango, R.; Alsaleh, K.A.; Vishnubalaji, R.; Manikandan, M.; Ali, A.M.; El-Aziz, N.A.; AlTheyab, A.; Al-Rikabi, A.; Alfayez, M.; Aldahmash, A.; et al. MicroRNA Expression Profiling on Paired Primary and Lymph Node Metastatic Breast Cancer Revealed Distinct microRNA Profile Associated With LNM. Front. Oncol. 2020 , 10 , 756. [CrossRef]
- 20. Shaath, H.; Toor, S.M.; Nair, V.S.; Elkord, E.; Alajez, N.M. Transcriptomic Analyses Revealed Systemic Alterations in Gene Expression in Circulation and Tumor Microenvironment of Colorectal Cancer Patients. Cancers 2019 , 11 , 1994. [CrossRef]
- 21. Emig, D.; Salomonis, N.; Baumbach, J.; Lengauer, T.; Conklin, B.R.; Albrecht, M. AltAnalyze and DomainGraph: Analyzing and visualizing exon expression data. Nucleic Acids Res. 2010 , 38 , W755-W762. [CrossRef] [PubMed]
- 22. Kahn, F.W.; Jones, J.M. Diagnosing Bacterial Respiratory Infection by Bronchoalveolar Lavage. J. Infect. Dis. 1987 , 155 , 862-869. [CrossRef] [PubMed]
- 23. Bailey, C.C.; Zhong, G.; Huang, I.-C.; Farzan, M. IFITM-Family Proteins: The Cell's First Line of Antiviral Defense. Annu. Rev. Virol. 2014 , 1 , 261-283. [CrossRef]
- 24. Brass, A.L.; Huang, I.-C.; Benita, Y.; John, S.P.; Krishnan, M.N.; Feeley, E.M.; Ryan, B.J.; Weyer, J.L.; Van Der Weyden, L.; Fikrig, E.; et al. The IFITM Proteins Mediate Cellular Resistance to Influenza A H1N1 Virus, West Nile Virus, and Dengue Virus. Cell 2009 , 139 , 1243-1254. [CrossRef] [PubMed]
- 25. Vishnubalaji, R.; Shaath, H.; Alajez, N.M. Protein Coding and Long Noncoding RNA (lncRNA) Transcriptional LandscapeinSARS-CoV-2InfectedBronchialEpithelialCells Highlight a Role for Interferon and Inflammatory Response. Genes 2020 , 11 , 760. [CrossRef]
- 26. Pinto, B.G.G.; Oliveira, A.E.R.; Singh, Y.; Jimenez, L.; Gonçalves, A.N.A.; Ogava, R.L.T.; Creighton, R.; Peron, J.P.S.; Nakaya, H.I. ACE2 Expression Is Increased in the Lungs of Patients with Comorbidities Associated with Severe COVID-19. J. Infect. Dis. 2020 , 222 , 556-563. [CrossRef]
- 27. Roessner, A.; Smolle, M.; Hayback, J. Giant cell tumor of bone: Morphology, molecular pathogenesis, and di GLYPH&lt;11&gt; erential diagnosis. Pathologe 2020 , 41 , 134-142.
- 28. Peng, X.; Wei, F.; Hu, X. Long noncoding RNA DLGAP1-AS1 promotes cell proliferation in hepatocellular carcinoma via sequestering miR-486-5p. J. Cell. Biochem. 2019 , 121 , 1953-1962. [CrossRef] [PubMed]
- 29. Papp, E.; Hallberg, D.; Konecny, G.E.; Bruhm, D.C.; Adle GLYPH&lt;11&gt; , V.; Noë, M.; Kagiampakis, I.; Palsgrove, D.; Conklin, D.; Kinose, Y.; et al. Integrated Genomic, Epigenomic, and Expression Analyses of Ovarian Cancer Cell Lines. Cell Rep. 2018 , 25 , 2617-2633. [CrossRef]
- 30. Klupp, F.; Schuler, S.; Kahlert, C.; Halama, N.; Franz, C.; Mayer, P.; Schmidt, T.; Ulrich, A. Evaluation of the inflammatory markers CCL8, CXCL5, and LIF in patients with anastomotic leakage after colorectal cancer surgery. Int. J. Color. Dis. 2020 , 35 , 1221-1230. [CrossRef]
- 31. Koshimune, S.; Kosaka, M.; Mizuno, N.; Yamamoto, H.; Miyamoto, T.; Ebisui, K.; Toyooka, S.; Ohtsuka, A. Prognostic value of OCT4A and SPP1C transcript variant co-expression in early-stage lung adenocarcinoma. BMC Cancer 2020 , 20 , 521. [CrossRef] [PubMed]
- 32. Zuo, Y.; Yalavarthi, S.; Shi, H.; Gockman, K.; Zuo, M.; Madison, J.A.; Blair, C.N.; Weber, A.; Barnes, B.J.; Egeblad, M.; et al. Neutrophil extracellular traps in COVID-19. JCI Insight 2020 , 5 . [CrossRef] [PubMed]
- 33. Teuwen, L.-A.; Geldhof, V.; Pasut, A.; Carmeliet, P. COVID-19: The vasculature unleashed. Nat. Rev. Immunol. 2020 , 20 , 389-391. [CrossRef] [PubMed]
- 34. Varga, Z.; Flammer, A.J.; Steiger, P.; Haberecker, M.; Andermatt, R.; Zinkernagel, A.S.; Mehra, M.R.; A Schuepbach, R.; Ruschitzka, F.; Moch, H. Endothelial cell infection and endotheliitis in COVID-19. Lancet 2020 , 395 , 1417-1418. [CrossRef]
- 35. Mehta, P.; McAuley, D.F.; Brown, M.; Sanchez, E.; Tattersall, R.S.; Manson, J.J. COVID-19: Consider cytokine storm syndromes and immunosuppression. Lancet 2020 , 395 , 1033-1034. [CrossRef]
- 36. Merad, M.; Martin, J.C. Pathological inflammation in patients with COVID-19: A key role for monocytes and macrophages. Nat. Rev. Immunol. 2020 , 20 , 355-362. [CrossRef]
- 37. Li, X.; Geng, M.; Peng, Y.; Meng, L.; Lu, S. Molecular immune pathogenesis and diagnosis of COVID-19. J. Pharm. Anal. 2020 , 10 , 102-108. [CrossRef]

- 38. Nile, S.H.; Nile, A.; Qiu, J.; Li, L.; Jia, X.; Kai, G. COVID-19: Pathogenesis, cytokine storm and therapeutic potential of interferons. Cytokine Growth Factor Rev. 2020 , 53 , 66-70. [CrossRef]
- 39. Chen, L.; Deng, H.; Cui, H.; Fang, J.; Zuo, Z.; Deng, J.; Li, Y.; Wang, X.; Zhao, L. Inflammatory responses and inflammation-associated diseases in organs. Oncotarget 2017 , 9 , 7204-7218. [CrossRef]
- 40. Palomino, D.C.T.; Marti, L.C. Chemokines and immunity. Einstein (S ã o Paulo) 2015 , 13 , 469-473. [CrossRef] [PubMed]
- 41. Felgenhauer, U.; Schoen, A.; Gad, H.H.; Hartmann, R.; Schaubmar, A.R.; Failing, K.; Drosten, C.; Weber, F. Inhibition of SARS-CoV-2 by type I and type III interferons. J. Biol. Chem. 2020 , 295 , 13958-13964. [CrossRef] [PubMed]
- 42. Major, J.; Crotta, S.; Llorian, M.; McCabe, T.M.; Gad, H.H.; Priestnall, S.L.; Hartmann, R.; Wack, A. Type I and III interferons disrupt lung epithelial repair during recovery from viral infection. Science 2020 , eabc2061. [CrossRef]
- 43. Chakraborty, S.; Edwards, K.; Buzzanco, A.S.; Memoli, M.J.; Sherwood, R.; Mallajosyula, V.; Xie, M.M.; Gonzalez, J.; Bu GLYPH&lt;11&gt; one, C.; Kathale, N.; et al. Symptomatic SARS-CoV-2 infections display specific IgG Fc structures. medRxiv 2020 . [CrossRef]
- 44. Bournazos, S.; Wang, T.T.; Ravetch, J.V. The Role and Function of Fcgamma Receptors on Myeloid Cells. Microbiol. Spectr. 2016 , 4 . [CrossRef]
- 45. Wei, L.; Li, J.; Han, Z.; Chen, Z.; Zhang, Q. Silencing of lncRNA MALAT1 Prevents Inflammatory Injury after Lung Transplant Ischemia-Reperfusion by Downregulation of IL-8 via p300. Mol. Ther. Nucleic Acids 2019 , 18 , 285-297. [CrossRef] [PubMed]
- 46. Zhang, Q.; Chen, C.-Y.; Yedavalli, V.S.R.K.; Jeang, K.-T. NEAT1 Long Noncoding RNA and Paraspeckle Bodies Modulate HIV-1 Posttranscriptional Expression. mBio 2013 , 4 , e00596-12. [CrossRef] [PubMed]
- 47. Shaath, H.; Alajez, N.M. Computational and Transcriptome Analyses Revealed Preferential Induction of Chemotaxis and Lipid Synthesis by SARS-CoV-2. Biology 2020 , 9 , 260. [CrossRef]

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional a GLYPH&lt;14&gt; liations.

<!-- image -->

' 2020 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (http: // creativecommons.org licenses by 4.0 ). / / / /