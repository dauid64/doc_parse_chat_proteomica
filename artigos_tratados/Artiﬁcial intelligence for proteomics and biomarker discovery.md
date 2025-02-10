## Perspective

## Artificial intelligence for proteomics and biomarker discovery

Matthias Mann, 1, * Chanchal Kumar, 2, * Wen-Feng Zeng, 1, * and Maximilian T. Strauss 3, * 1 Proteomics and Signal Transduction, Max Planck Institute of Biochemistry, Martinsried, Germany 2 Translational Science &amp; Experimental Medicine, Research and Early Development, Cardiovascular, Renal and Metabolism (CVRM), BioPharmaceuticals R&amp;D, AstraZeneca, Gothenburg, Sweden 3 OmicEra Diagnostics, Planegg, Germany *Correspondence: mmann@biochem.mpg.de (M.M.), chanchal.kumar@astrazeneca.com (C.K.), wzeng@biochem.mpg.de (W.-F.Z.), strauss@omicera.com (M.T.S.)

https://doi.org/10.1016/j.cels.2021.06.006

## SUMMARY

There is an avalanche of biomedical data generation and a parallel expansion in computational capabilities to analyze and make sense of these data. Starting with genome sequencing and widely employed deep sequencing technologies, these trends have now taken hold in all omics disciplines and increasingly call for multi-omics integration as well as data interpretation by artificial intelligence technologies. Here, we focus on mass spectrometry (MS)-based proteomics and describe how machine learning and, in particular, deep learning now predicts experimental peptide measurements from amino acid sequences alone. This will dramatically improve the quality and reliability of analytical workflows because experimental results should agree with predictions in a multi-dimensional data landscape. Machine learning has also become central to biomarker discovery from proteomics data, which now starts to outperform existing best-in-class assays. Finally, we discuss model transparency and explainability and data privacy that are required to deploy MS-based biomarkers in clinical settings.

## INTRODUCTION

After decades of being somewhat of a ''soft science,'' biomedicine is now increasingly dominated by large-scale data, illustrated by the billions of sequencing reads generated in deep sequencing experiments. Dealing with such data has initially been a tremendous challenge but is becoming increasing routine-enabled by the continuing exponential growth in information processing capabilities. In this context, the biomedical field has enthusiastically adopted and even driven the open-access movement, including sharing of data and analysis tools. From its start in genomics, further ''omics'' disciplines, representing the different layers of gene expression and generation of small molecules have also come into their own-increasingly producing datasets that are just as large and often more multidimensional than genomics ones. Our own area of mass spectrometry (MS)-based proteomics is a good example of this (Aebersold and Mann, 2016; Sinha and Mann, 2020). Previously, results could be summarized in some spreadsheets, but today individual projects produce many gigabytes of data that need to be processed and interpreted in the best way. Although there has been steady progress over the years in algorithmic solutions to this challenge, artificial intelligence (AI) is now adding a substantially new perspective to it. Here, we describe the promises and pitfalls of this coming revolution. Our perspective is addressed to an audience that does not necessarily have a detailed background in either MS-based proteomics or AI. To set the scene, it will be helpful to briefly introduce this topic in general and then in the context of MS-based proteomics.

<!-- image -->

Deep learning (DL), a subset of machine learning (ML), which itself is a disciple of AI, is reshaping much of society. AI is a conceptual departure from classical statistics, not only in the amount of data that it deals with but also in making fewer assumptions about the underlying distributions and models, such as linearity and normality. These assumptions are replaced by large datasets and computational power. ML algorithms learn from the data they are exposed to and make predictions without being explicitly programed for the specific application at hand. DL is the technical term of creating deep neural networks consisting of many layers and it achieves unprecedented accuracy for various AI tasks such as image recognition. In a sense, these networks go further than ML by learning complex features and ''embeddings'' of the data without the need to have them declared beforehand. To illustrate, while a classical ML algorithm can learn to distinguish flowers based on measured characteristics such as the length and the width of the sepals and petals, DL would deduce such features itself when being exposed to images of different flower classes.

MS-based proteomics employs the technology of mass spectrometry, a field that is more than a century old but keeps advancing dramatically. Applied to the proteome-the totality of expressed proteins in a given cellular state, its main attractions are its extreme specificity of detection and quantification, its sensitivity, and the fact that it is not directed only against specific proteins and is unbiased in this sense. Furthermore, proteins represent the end point of gene expression and they are the main functional components of the cell, providing structural support, the enzymatic machinery, and even control gene

<!-- image -->

Figure 1. Classical and AI approaches to data interpretation

<!-- image -->

<!-- image -->

expression from DNA and RNA in the first place. Furthermore, the majority of biomarkers and drug targets are proteins. However, despite the powers of mass spectrometry, the extreme complexity of the proteome, the fact that it cannot be amplified, presents a tremendous analytical challenge. This is the reason that so far proteomics has been most successful in elucidating specific biological mechanisms and that it cannot yet compete with the completeness of deep-sequencing-based methods. Webelieve that applying AI to this challenge can help to dramatically improve MS-based proteomics that it is an intellectual and practical endeavor of highest importance.

Depending on the experiment, the proteomics data generated are quite complex and multi-dimensional with millions of data points routinely recorded. It is becoming increasingly clear that these data are a perfect match for the AI capabilities described earlier. This goes for enhancing data quality in any proteomic experiment, biological interpretation, and its use in clinical decision support using proteomic biomarkers. As we will describe below, AI has already made its mark on the field and is starting to contribute to every step along the analytical pipeline.

Although AI is has now achieved breakthroughs in a wide range of applications, this power does not come completely for free (Figure 1). As AI capabilities are becoming more accessible to non-professional users in and outside of science, it is necessary to keep some of their potential pitfalls in mind. By far the most prominent of these is ''overfitting'' when training ML and DL models. As the name suggests, overfitting happens when the training data are ''over-learned''; therefore, the model remembers the training data and will not generalize to new and previously unseen data. For example, if a model is only trained

<!-- image -->

Statistical models often allow to directly interpret features and models. With machine learning one can utilize the interplay of many features and potentially increase model performance, however, generally at the cost of interpretability. DL helps to uncover previously unknown features in an ''end to end'' fashion, but further decreasing interpretability. Some of the standard methods of the different approaches are depicted.

to find biomarkers in one clinical cohort, it may learn spurious differences between cases and controls specific to that cohort, which may not be disease related and quite different in another population. Therefore, it is imperative to distinguish AI from classical statistical models with well-defined probabilities.

There are established and rigorous methods to avoid these problems, mainly the separation of training and evaluation datasets, which in practice are sometimes compromised because there is not sufficient ''ground truth'' data. In our opinion, one should always start with the simplest methods, such as linear or naive Bayes models, using the largest training and

testing data possible, followed by rigorous cross-validation on training data and evaluation on data unseen by the model. Simple models have the advantage that they can be intuitively interpreted, such as regression models where weights simply describe the coefficients of a parametrized curve. This is less true of DL models, which often comprise thousands of nodes and, hence, lose interpretability and in practice are often treated as a black box. This poses practical limitations as the model could result in unexpected edge cases with unexpected behavior as well as ethical and legal issues when patient treatment is decided partly by such models. In a biological context, it may limit what humans can learn from the systems they study. These issues are not unique to biomedicine and there is much ongoing research into how DL models can be employed within a statistical and explainable framework.

In the remainder of the paper, we first describe where AI is making an impact on each of the subsequent steps of the proteomics workflow. The key parameters here are how to assign more of the fragmentation spectra to actual peptide identifications and how to provide the best peptide and protein quantification. These are much more complex issues in proteomics than they are in deep-sequencing-based technologies and much progress can still be made. We describe data integration of different proteomics modes, such as expression proteomics, interaction proteomics, and post-translational modifications, integration with other omics modes, as well as biological interpretation. Then we describe how MLisbecominganindispensable part of biomarker discovery and how transparency in this field is paramount. Finally, we give an outlook of what we think are likely developments and challenges of AI in proteomics in the next years.

Figure 2. AI support of the MS-based shotgun proteomics workflow

<!-- image -->

Perspective

<!-- image -->

Each droplet represents one of the steps of shotgun proteomics workflows. This includes protein digestion, liquid chromatography separation, ionization, ion mobility separation, MS1 detection, peptide fragmentation, MS2 detection, and protein identification and quantification. General ML applications to proteomics began in the 2000, focusing on retention time prediction, MS2 prediction, and peptide identification. DL entered the stage in 2017, and it has now been used in almost all steps of the proteomics workflows although ML is still preferred where it achieves similar performance at higher interpretability. MS1 signal prediction for any peptide sequence would be important but has not been convincingly solved yet. Representative publications employing ML/DL methods are listed at respective step of proteomics workflow within rectangular boxes (terracotta for ML; blue for DL).

## AI IN THE PROTEOMICS WORKFLOW

In outline, the proteomics workflow has remained relatively stable over the last 20 years although resolution and accuracy of the data, sensitivity, and overall performance have increased by orders of magnitude (Aebersold and Mann, 2003, 2016). Proteins are enzymatically digested to peptides, chromatographically separated, ionized by electrospray (ES), and eluting peptides are mass measured and fragmented. The overall purpose of the experiment is to identify and quantify as many of the eluting peptides as possible. Furthermore, data completeness is important-especially for ML applications.

There are a variety of acquisition schemes, with different tradeoffs between depth of proteome coverage (percentage of the expressed proteome captured), speed, robustness, and quantitative accuracy. Chemical labeling methods isotopically encode peptides from different experimental states and use the patterns of ''reporter ions'' to quantify between them. In contrast, ''labelfree quantification'' directly uses the mass spectrometric signal of the peptides or their fragments. Among these, the increasingly popular data independent acquisition (DIA) methods repeatedly cycle through the mass range to generate maps of fragments over elution time, which are then matched to libraries.

MS-based proteomics workflows involve many biological and physicochemical processes, including protein digestion, liquid chromatography separation, peptide ionization, (increasingly) ion-mobility separation, full MS (MS1) detection, peptide fragmentation, and tandem mass spectra (MS/MS or MS2) detection. Many of these processes are highly predictable by ML given sufficient training data; therefore, statistical approaches can be

employed, and significance may be directly estimated when examining the distributions of selected features. A typical example is estimating the significance of protein upregulation from repeated measurements in two conditions for which classical t tests or ANOVA tests should be used. In contrast, whenever many features are available, one can employ ML methods to find underlying patterns in the data such as extracting panels of biomarker proteins, which depend on each other in non-linear ways (discussed below). Although the latter may increase model performance, this may come at the cost of interpretability. DL may additionally extract features not obvious to the scientist, often drastically improving performances, but further lowering interpretability (Figure 1).

As illustrated in Figure 2, AI has already been applied to almost all steps of MS-based proteomics. In the past decade, researchers often employed traditional ML methods (typically support vector machines, random forests, and gradient boosting) for peptide identification, retention time prediction (Moruz and Kall, 2016; Moruz et al., 2010; Pfeifer et al., 2007), and MS/MS spectrum prediction (Arnold et al., 2006; Degroeve et al., 2013; Elias et al., 2004). In MS/MS, peptide fragments are generated by fragmentation mainly at the amino acid bonds, so that these masses (but not the intensities) can be readily calculated once the peptide sequence is known. Therefore, experimentally measured fragments in the peptide identification process are matched against in silico calculated ones for the entire database, employing a sequence reversed ''non-sense'' database for controlling the false discovery rate (FDR, reviewed in Elias and Gygi, 2007). The confidence in a match can be assessed by statistical means, e.g., by simply correlating experimental and calculated

<!-- image -->

spectra to assess their similarity or scoring the number of hits (fragment peaks that occur in both spectra). These statistical approaches can be made more sophisticated; for instance, the MS-GF software employs a ''generating function approach'' to calculate rigorous E values for every single spectrum (Kim et al., 2008), and it further extended the scoring function by a probabilistic ML approach (Kim and Pevzner, 2014). Humandefined features such as the number of hits allows incorporating background (''domain'') knowledge and to directly interpret the confidence. However, the selected features could be suboptimal, and it is difficult to combine and weigh them correctly. The Percolator algorithm deserves special mention because it is one of the earliest and most widely used ML tools in proteomics (Kall et al., 2007). It optimizes the number of true hits at € a specified FDR, by taking account of multiple peptide sequence features as well as other experimental peptide data to re-score peptides in a semi-supervised manner. A large number of such features is offered for learning, and the ML algorithm will automatically select and combine the most important ones. These MLdetermined features can subsequently be used by the scientist to improve the measurements. Percolator boosted the number of identified peptides by 5%-16% compared with the aforementioned MS-GF, highlighting the power of a ML-based method (Granholm et al., 2014). Such algorithms have been used in peptide identification with or without enzyme and modification specificity, intact protein search, cross-linked peptide search, and DIA-based peptide search. It has also recently been repurposed for efficiently matching identified MS1-features (non-fragmented peptide signals in the raw data) to corresponding non-identified ones in other experimental runs for the purpose of protein quantification (''match between runs'') (The and Kall, 2020). €

The properties of peptides and proteins are ultimately determined by their (modified) amino acid sequences alone and there is a long history of predicting, i.e., the chromatographic retention time in this way, to see if it concurs with the experimentally determined one. One of the long-elusive goals of the computational proteomics community had been the prediction of the intensity pattern of MS/MS spectra from the sequence alone. MS2PIP is an ensemble learning (random forest and XGBoost)-based tool, which considers chemical properties of amino acids and other fragment-related features for spectrum prediction (Degroeve et al., 2013). Recently, MS2PIP achieved 0.9 to 0.95 median Pearson correlation coefficients (R) between experimental and predicted spectra on different test datasets (Xu et al., 2020). Mobile proton model-based tools such as MassAnalyzer (Zhang, 2004) and MS-simulator (Sun et al., 2012) incorporate several assumptions to simplify this problem and, hence, made their prediction interpretable. However, these assumptions do not cover all different peptide fragmentation situations, which mayresult in varying prediction accuracies on different test datasets (0.72 to 0.92 mean Pearson R values Sun et al., 2012).

As the universe of possible peptides is astronomically large, the prediction of peptide behavior from sequences is potentially an ideal match to DL methods, especially as many millions of identified MS/MS spectra are available in public repositories such as PRIDE (Perez-Riverol et al., 2019). As DL has achieved breakthroughs in other fields, the proteomics community has become very interested in this approach (Wen et al., 2020).

<!-- image -->

The sequence of amino acids resembles sequential input similar to text and can be modeled in similar ways. Arguably, the breakthrough for DL occurred in 2017, when it was demonstrated that the fragmentation spectra in MS-based proteomics could be accurately predicted for any peptide from its sequence alone (pDeep, Zhou et al., 2017). The challenge in this problem is that the fragmentation of a peptide bond and the detectability of the fragments greatly depend not only on the adjacent amino acids but also the ones remote to the bond. In other words, the identity of an amino acid at a given position influences the fragmentation probability not only at the position next to it but also those far away, making fragment spectrum prediction intractable by classical computational means. Deep neural networks, especially recurrent neural networks (RNN), naturally capture the long-term sequential dependencies, just like they do in analyzing text and speech sequences. Note that AI efforts in proteomics have almost always used standard architectures of the neural nets such as RNNs/convolutional neural networks (CNNs)/variational autoencoders (VAEs) and associated concepts. This topic is covered in a recent review (Wen et al., 2020) and is beyond the scope of this perspective. In the Prosit software, DL models were trained on fragmentation data systematically acquired at different collision energies (Gessulat et al., 2019), and in an academic collaboration with Google called DeepMass:Prism, tens of millions of spectra from various sources were trained and evaluated (Tiwary et al., 2019). DL-based prediction tools steadily achieved 0.97 to 0.99 median Pearson R values, much higher than ML-based methods (Xu et al., 2020). Although none of these models have been integrated into popular peptide search engines yet, their power has already become apparent in rescoring peptide hits based on similarity between experimental and predicted spectra. Interestingly, DL can now predict full MS/MS spectra, as opposed to just backbone fragment intensities, using ''end to end'' learning-something out of reach of classical ML techniques (Liu et al., 2020). Once prediction models are part of the routine workflow, we believe identification rates, especially in challenging situations, will increase substantially, leading to more comprehensive and even more reliable results.

Post-translational modifications (PTMs) of proteins are very important to detect and quantify because they often function as activity switches, localization signals, degradation makers, and many other dynamic functions. Analysis of these PTM bearing peptides is challenging as there are many isoforms and their fragmentation spectra may not follow the simple rules of breakage at the bonds between the amino acids, making the PTM site localization more difficult than peptide sequence identification by using masses and intensities. AI methods are starting to be adapted to these challenges (Wang et al., 2017; Yang et al., 2021b), but much work remains to be done. Likewise, the body contains many bioactive peptides with signaling functions. These do not follow the tryptic cleavage rules as they are endogenously generated, again making them complex and leading to low identification rates. We predict that AI will be particularly beneficial for these peptides and for the peptides presented to the immune system-the MHC class I and II peptides. Our and other's experience indicates that identification rates can be improved by several folds when using DL models

## Perspective

DL generally needs large datasets because a very large number of parameters needs to be ''learned.'' As each layer of a DL network will learn distinct characteristics of objects, such as edges in images, they can be transferred to be used in related settings. This is commonly known as transfer learning and enables reuse of previously trained models without requiring many training samples. In proteomics, this powerful strategy has recently been shown to improve prediction of the spectra of phosphorylated and otherwise modified peptides by 30% to 60% with only thousands of training spectra, which is important because there are few large-scale datasets of rare modifications. Furthermore, predictions could be adjusted to different mass spectrometers and settings with only a few hundred spectra (Zeng et al., 2019) and spectra predicted for different fragmentation modes (Tarn and Zeng, 2021). We believe that transfer learning will be very useful in many situations in proteomics, alleviating the need for large datasets and leading to accurate models even for specialized application areas.

One of the key parameters needed in spectral library search for DIA data analysis is predicting retention times in chromatographic separation, where DL was also very successful. Apart from reverse-phase liquid chromatography, ion exchange, and hydrophilicity, retention times can also be modeled directly or by transfer learning (Ma et al., 2018). Prediction of MS/MS spectra together with the retention time is starting to outperform experimental spectral library search in DIA (Yang et al., 2020b). Such predicted retention time were recently used to globally target peptides for MS/MS analysis, from organisms for which no experimental results had ever been obtained previously (Muller et al., 2020). This also underlines the great potential of € coupling DL with real-time, intelligent data acquisition.

Furthermore, DL facilitates new ways for peptide identification. DeepNovo set out to use the image captioning technique common in DL to solve the de novo peptide sequencing problem, i.e., sequencing peptides from their MS/MS spectra without the help a database, and demonstrated 5%-20% improvement comparing with some existing de novo sequencing tools (Tran et al., 2017). The DIA-NN program uses ensembles of deep neural networks to increase the sensitivity of matching DIA fragmentation patterns to experimental or in silico -derived spectral libraries (Demichev et al., 2020). Compared with other widely used tools, DIA-NN identifies many more peptides, especially in short-gradient LC-MS data. In all these applications the challenge of overfitting mentioned earlier needs to be kept in mind. There are many more DL-based applications in proteomics, such as collisional cross section (CCS) prediction for ion mobility mass spectrometers (Meier et al., 2021) and a wide range these have recently been reviewed (Wen et al., 2020).

As shown in Figure 2, there are still open problems for ML or DL in proteomics workflows. A central one is the prediction of the MS1 signal that a peptide with a given sequence will have. This signal intensity depends not only on the initial number of protein copies but also on the peptide digestion probabilities (Yang et al., 2021a), propensity of ionization of the peptide in ES, ion loss during ion transmission, and ion detection probabilities. Predicting these processes would allow us to convert the relative intensities obtained in MS-based proteomics into absolute ones. However, modeling each of these steps is very difficult, especially for the last three ones, since there is no interme-

<!-- image -->

diate information after peptides are injected into the chromatographic column and the detector signal that they give rise to. In principle, DL might be able to consider all these steps in a single model (''end-to-end'' learning) rather than regarding them individually.

## AI IN PROTEOMICS DATA INTEGRATION

Proteomics is not restricted to the accurate measurement of the expression of the proteins and proteoforms (Smith and Kelleher, 2018) present in a biological system. It can also be used as a ''readout'' after any kind of procedure that enriches specific functional subclasses of proteins (Figure 3, central part). In interactomics, for instance, proteins are pulled down with a bait that could be a protein of interest or also small molecule drugs (Bludau and Aebersold, 2020). Doing this in a systems wide manner leads to a network of interactions, whose perturbations can be studies. Similarly, the cellular proteome can be separated by centrifugation, for instance, followed by MS-based proteomics of the fractions, which leads to a map of cellular organelles. Finally, the activity status, localization, and turn-over of many if not most proteins is regulated by PTMs. MS-based proteomics has been a game changer over the last two decades in bringing to light an unimagined complexity of these PTMs and their regulation (Aebersold and Mann, 2016). Beyond the different dimensions of proteomics itself, the proteomics data need to be integrated with other omics data or clinical data in the same project.

In comparison with genomics, applications of ML and DL techniques to downstream metabolomics, lipidomics, and proteomics data analysis are generally still in their infancy and most widely applied in data pre-processing steps (Pomyen et al., 2020; Sen et al., 2021). This may be because of low sample sizes, lack of interpretability, and general lack of sufficient reference, training, and validation data. Proof of concept ML applications using lipidomics datasets have emerged, for instance for prediction of T2D status (Ho et al., 2020) and to predict clinical lipid concentration from lipid profile data using dried blood spots (Snowden et al., 2020).

In multi-omics, very disparate datasets need to be integrated-potentially across omics hierarchies of genomic, epigenomics, proteomics, and lipidomics (top of Figure 3). A perennial question is to what degree changes in transcriptome levels predict those in the proteome (Landi et al., 2020). As could be expected from the complex regulatory steps between gene expression at the mRNA level and translation to proteins as well as from intricate, regulated protein degradation processes, there is far from a one-to-one correspondence between a transcript and the protein or proteins it gives rise to. Recently, Julio Saez-Rodriguez and co-workers leveraged crowdsourcing via the NCI-CPTAC DREAM proteogenomic challenge to predict (phospho)proteins from DNA and RNA data (Yang et al., 2020a). An array of ML techniques was employed, including, tree- and ensemble-based models, but the prediction performances were below the baseline methodology, and in some instances even performed close to random. Thus, the authors concluded that it is essential to measure the proteome rather than relying on transcriptome or copy numbers as proxies.

<!-- image -->

<!-- image -->

Figure 3. Multi-level biomedical data integration using ML- and DL-based approach

<!-- image -->

Key applications of MS-based proteomics in proteome-wide investigations are shown (middle panel)-expression as a function of biological perturbation, identification, and quantification of diverse post translational modifications, protein interaction mapping, and spatial or organellular proteomics. The data acquired in proteome-wide studies can be integrated with complementary omics datasets, including, genomics, epigenomics, transcriptomics, metabolomics, and lipidomics (upper panel). Omics data integration results are further interpreted by including the existing biomedical literature and databases, leveraging ontologies, for instance, for a specific disease or cellular system (left subpanel). For clinical omics investigations, further integration of imaging, electronic health records and clinical lab tests (right subpanel) can further strengthen the results and biological insights (bottom).

Omics datasets can be complemented with classical lab tests and with imaging datasets from different platforms (MRI/CT scans, IHCs) to provide novel biological insights into disease pathophysiology and prognosis (Fu et al., 2020) and disease risks (Rawshani et al., 2020). Further integration with patient medical record (EHRs) can help stratify patients and elucidate clinical risks thereby enabling precision medicine (Jensen et al., 2012; Landi et al., 2020) (Figure 3, right).

The results generated in any one study also need to be interpreted in light of what is already known. The biomedical literature continues to grow unabated, data repositories are expanding, and a wide range of human biology and disease annotations

are available in form of databases or knowledgebase. This resource is often under-explored because it is overwhelming to the individual researcher, presenting a clear opportunity for ML and DL technologies. For instance, text mining has long been used to extract relationships between entities by tracking comentioning (Jensen et al., 2006; Rebholz-Schuhmann et al., 2012), but this area is clearly ripe for application of recent DL breakthroughs in text mining (Brasoveanu et al., 2020; Minaee et al., 2021). Holistic understanding of biology necessitates an integrative approach that combines all these different data types (omics, imaging, chemical, healthcare, etc.) and uncovers complex interrelationships of the involved entities. Such diverse

<!-- image -->

datasets and databases can be further integrated by leveraging ontologies as a semantic framework (Kulmanov et al., 2020). The wealth of biomedical data is being harnessed by sophisticated ML, DL, and NLP approaches to derive interconnections between various entities (genes, proteins, diseases, pathways, etc.), generating biological and clinical insights in the form of knowledge graphs (Callahan et al., 2020). Knowledge graphs use graph data structures (or databases) to store data directly in the form of connections (annotations to edges in a large graph) between entities (the nodes of the graph), and in a proteomics knowledge graph, the MS data and proteins are the nodes. In our group, we have developed the ''Clinical Knowledge Graph'' (CKG) (Santos et al., 2020), which currently contains millions of protein nodes and more than 100 million connections between them and has already been used to integrate background knowledge in the kingdom of life proteome project (Muller et al., 2020). € As methods are developed to apply ML and DL methods on top of graph structures, it will be interesting to follow their use in proteomics knowledge graphs.

## AI SUPPORTED BIOMARKER DISCOVERY

Diagnostic laboratory tests are a cornerstone of modern medicine, applied to detect the risk or onset of disease. The majority of clinical decisions are based on such tests but existing biomarkers are often not very specific or sensitive and there are no biomarkers for the majority of diseases (ICD: https://www. who.int/standards/classifications/classification-of-diseases).

Cells, DNA, or small molecules can all be analyzed by laboratory tests, but proteins are the class with the highest number and frequency of assays, reflecting their central role in medicine. These facts also indicate the huge potential of new protein-based biomarkers in medicine. Furthermore, clinical assays are mostly performed against single targets in the form of enzymatic tests or immunoassays. A promise of MS-based proteomics is that it could measure a large number of proteins simultaneously and with much higher specificity. However, due to technological and conceptual limitations, this promise is only now starting to be realized (Geyer et al., 2017). Note that in biomarker discovery, the accurate quantification of the proteins is perhaps even more important than the identification of as many as possible of them.

To meet the urgent need for new and better biomarkers, clinical cohorts have to be recruited, participants have to be carefully assessed or ''phenotyped,'' and samples have to be archived in biobanks (Figure 4A). In the ''triangular'' strategy of biomarker discovery, a small number of samples is measured in great depth (largest number of quantified proteins), followed by testing a few markers in a larger cohort. In contrast, we have advocated a ''rectangular strategy,'' in which several cohorts, ideally of hundreds of samples are all measured in as great depth as routinely possible (Geyer et al., 2017). Longitudinal studies are especially attractive because each person can serve as their own control, effectively eliminating the base-line inter-individual variation in protein levels (Dodig-Crnkovic et al., 2020; /C19 Geyer et al., 2016).

Having obtained such extensive datasets, the next step is bioinformatic analysis, specifically the quantification of proteome differences between cases and controls. This ideally leads to candidate hits (statistical outlier proteins) associated with the

<!-- image -->

investigated condition (Figure 4B). In case of longitudinal data, proteins can be clustered by their trajectories, with the just mentioned additional advantage that protein levels tend to be more stable within a person than between them, making such profiles particularly informative. Bioinformatic enrichment analysis is then performed on the outlier proteins or those that cluster in the time course analysis, revealing biological processes and themes. Proteomics datasets have a very large number of data points, which can be aggregated in ''global proteome correlation maps,'' which we have found to be excellent guides to interpretation (Wewer Albrechtsen et al., 2018) (Figure 4C). Here, proteins that tend to be co-regulated between conditions and participants group together, revealing important connections and underlying networks. Importantly, clinical ''meta data,'' such as existing lab tests are also contained in these clusters, allowing functional insights into the nature of potential biomarkers.

The statistical and bioinformatic analysis mentioned earlier results in sets of outlier proteins, which need to be combined to yield actionable biomarkers for clinical use. In current medical practice, the levels of a single protein or a few measurements are incorporated into simple decision charts using cutoff values. Examples of these are the time honored De-Ritis-Ratio, the Child-Pugh-Score, CHA2DS2-VASc score, or the Bartels-index (Lip et al., 2010; Mahoney and Barthel, 1965; Pugh et al., 1973; De Ritis et al., 1957). However, in the case of MS-based proteomics, such schemes would not make optimal use of the large amount of data available, and it would not be obvious how to manually combine the different protein values into a trustworthy score. Conversely, uncovering signals and predictors from thousands of features is what ML excels at. For instance, decision trees are first trained on ''ground truth'' data from which they learn how to group classes-based decision boundaries for the most important features. In the biomarker case, the classes could be cases and controls whereas the levels of proteins are the features. There are well-established methods to determine which features contribute most to distinguishing the classes. This also aids interpretability and helps to avoid classifying on proteins that are unlikely to be medically relevant but are instead due to different sample handing in cohort groups (Geyer et al., 2019).

There are set procedures in ML to prevent overfitting the data, referring to the fact that given a sufficiently large feature set any arbitrary cohort can be perfectly separated. However, such an ML model would be specific to the training dataset and would not generalize to new cases. Good ML practice includes strict splitting of training and evaluation data-where the evaluation data are never employed in training. When sample numbers are very restricting, methods such as cross-validation can still help to evaluate model performance. Still, overfitting is an ever-present issue, which always needs to be kept in mind, and is a prime reason for having independent cohorts. Evaluation of biomarkers found by ML should be done in standard ways, such as ''confusion matrices'' (correctly classified positives and negatives in the diagonal and incorrect ones in the off-diagonal) and ROC curves, which summarize performance in a robust way. Permutation-based FDR testing further adds insights into the robustness of results at a chosen cutoff. However, in the end AI-derived biomarkers still need to conform to the same criteria of verification in independent and large cohorts

Figure 4. ML supported proteomic biomarker discovery

<!-- image -->

<!-- image -->

<!-- image -->

## Rectangular strategy

(A) Matching experimental cohorts of cases (blue) and controls (gray). Clinical samples are typically tissues (difficult to obtain), tissue biopsies such as needle biopsies (easier) and body fluids such as cerebrospinal fluid (CZE), and the very easily obtained urine and plasma/serum samples (left panel). In the ''rectangular strategy,'' discovery and validation cohorts are all measured to the greatest depth that is routinely possible (right panel). (B) Volcano plot depicting outliers (proteins significantly different between cases and controls) and the time course of one of these potential biomarkers over the disease course.

(C) Protein correlation map summarizing all correlations of proteins in the patients and conditions. Proteins cluster into informative groups that also contain clinical parameters such as lab values.

(D) ML-often ensemble decision trees-results in the selection of several potential biomarkers and decision boundaries (left). Performance of the model is rigorously evaluated on data previously unseen by the model, and, for example, summarized as area under the curve (AUC) (TP true positive, FP false positive). (E) A long term goal of MS-based clinical proteomics is decision support for doctors and patients based on proteomics tests, the previously developed ML models and other pertinent information.

that have been established over decades in clinical practice and in epidemiology.

We have employed ML-based techniques in plasma and liver proteomics datasets to identify circulating biomarkers in alcoholic liver disease, where they now start to outperform the established biomarkers (liver enzyme tests combined with ultrasound stiffness measures) in the diagnosis of early stages of fibrosis (Niu et al., 2020). Likewise, we obtained promising classification results for Alzheimer's disease from CSF in a three-cohort study (Bader et al., 2020), whose signature overlapped with a similar study (Higginbotham et al., 2020) and in a two-cohort study of the urinary proteome of Parkinson's disease (Virreira Winter et al., 2021).

In our experience, the established ML methods perform well in this task and prediction performance is generally limited not by model sophistication but by the number of datapoints to train the model on. Furthermore, the clinical ground truth is often somewhat uncertain as well, for instance, because different centers may use different criteria to establish disease and because these methods also have error rates.

Once a set of potential biomarkers has been defined, this needs to be translated into a clinical test. In the past, regulatory agencies have mainly dealt with the approval of single-analyte immunological tests. This process is already arduous and protracted but is made much more complex by multi-analyte readouts using novel technology. This is another reason to make the

Figure 5. Explainability and privacy

<!-- image -->

<!-- image -->

<!-- image -->

Transparent learning is composed of several parts and is necessary to generate trust in decision support applications and to help explain biological mechanisms to advance human understanding. There are many research efforts and increasing ethical and legal imperatives to make algorithms explainable instead of ''black box'' (left). The tension between goals of open science, including assess to data and the legal and ethical requirements for data privacy can be alleviated to some degree by repositories for sensitive data that are only open to qualified researchers and by technologies such as federated learning, where the data remain in place.

biomarker discovery pipeline, including ML, as simple, robust, explainable, and reproducible as possible.

Alternatively, the results of proteomics and ML could be distilled into a few biomarker candidates that are then measured and approved in the established manner. Although possible in principle, we do not believe that this is optimal, because it forfeits the specificity and multi-analyte advantages of the technology and because antibody-based quantification may not be sufficiently accurate for the subtle quantitative changes routinely uncovered by proteomics. Furthermore, MS-technology is much superior at specifically detecting and quantifying post-translationally modified peptides or proteins.

In the biomedical field, we have described how ML is a necessary last step to distill the proteomics data into biomarker panels that can diagnose, prognoses or report on the efficacy of intervention in disease. Here, transparency of models and their explainability are not only desirable but a necessary requirement for acceptance by the health care system. This is also increasingly codified in legal regulations. A general challenge in AI prediction models has been their potential for bias because the datasets were drawn from non-diverse sources or were ''learning'' markers for disadvantaged status instead. In the biomedical context, this manifests as the requirement to include diverse populations and diseases, to the greatest extent possible. Apart from the categories of gender and ethnicity, socio-economic status and age are frequently overlooked, despite their often-dominant effects.

The proteomics community should be commended on their efforts to make data conform to community standards (Jones and Orchard, 2008) and freely and readily available in repositories such as PRIDE and MassIVE (Perez-Riverol et al., 2019; Wang et al., 2018). Note that this is still not the case for related fields such as metabolomics, which is similar to proteomics in using

MS-based technology but aims at comprehensive identification of the small molecules in a biological system. Wide-spread data sharing has had the beneficial effect of making proteomics an attractive field for applying AI efforts. That said, we have noted an increasing tension between the imperatives for data accessibility, as formalized in the FAIR principles (Wilkinson et al., 2016), and the desire for data privacy, such as embodied in the GDPR regulation of the European Union (Ducato, 2020) (Figure 5). This has only recently become an issue in proteomics as data quality has increased to an extent that it potentially allows (re)identification of individuals, which now raises ethical and philosophical questions (Geyer et al., 2021; Mann et al., 2021). It is important that the different stakeholders and authorities recognize these challenges and deal with them in a way that does not prevent scientific and medical progress. One solution is the establishment of databases of sensitive data to which only qualified and approved researchers have access. Although against the FAIR spirit, this already has become common practice for genomics data (Byrd et al., 2020; Grishin et al., 2019).

Interestingly, ML and DL themselves may help to ameliorate this potential conflict. For instance, the premise of ''federated learning'' is that the sensitive data do not leave the original, authorized place. AI learning happens locally; only the models and not the data are aggregated (Rieke et al., 2020). In another approach, autoencoders are employed to ''abstract'' the data such that models leaned on them are the same, whereas personal identification is no longer possible (Figure 5).

## CONCLUSION

In this perspective, we have summarized how advances in AI have already become an indispensable part of the data generation pipeline of MS-based proteomics. Given a peptide

<!-- image -->

sequence, it is now possible to predict nearly all the analytical properties measured by this inherently multi-dimensional technology. One of the few exceptions is the prediction of the MSresponse of a peptide with a given sequence. Furthermore, DL and AI methods still need to be improved to incorporate this information in a transparent and FDR controlled manner in the peptide identification or matching process. The accuracy of quantification of peptides and proteins-usually the end goals of the proteomics experiment-could likewise gain from these new methods.

We note the increasing importance of transfer learning to adapt DL models to the proteomics instruments and questions, dramatically decreasing the amount of data needed for DL methods. Next steps should include more transparent opensource architecture that allow seamless combination of data analysis and different AI algorithms, something that we are promoting with the AlphaPept framework (Strauss et al., 2021).

Proteomics datasets are increasingly part of larger projects that include other omics data and even diverse ''meta data'' such as microscopy images. All these results need to be related to the existing biomedical literature and to the knowledge captured in ever-growing databases. Today, this is still largely done manually, a situation that is not only time-consuming but also suboptimal. We believe that graph databases (such as those underlying social media) and AI on graph data structures are excellent ways to move forward. In the future, AI methods will themselves drive the integration of all the different strands of results and previous knowledge in proteomics projects.

A longstanding goal of systems biology is the modeling of cellular behavior, for instance, using stoichiometric or kinetic models (Ferrell et al., 2011). Despite success in specialized and bounded areas, the large number of datapoints provided by modern proteomics methods quickly make them mathematically intractable. This is because biological systems are highly interconnected and therefore, difficult to modularize. These very attributes, however, might make the prediction of cellular decision making amenable to machine or deep learning. In our opinion, current efforts in this direction do not yet directly or optimally use the large volume and accurate quantification data available from proteomics experiments. By comparison, models trained on the much more widespread transcriptomics datasets have already reached remarkable performance in predicting a range of cellular outcomes (Lotfollahi et al., 2019). Given the high specificity and quantitative accuracy with which proteomics can measure proteins and the fact that these are more directly connected to biological function, we believe that ML or DL modeling of cells based on that technology will have a bright future. To this end, we urge the generation of high accuracy, temporally resolved datasets based on systematic and homogeneous perturbation, as well as further research into the appropriate ML or DL architectures. In this context, explainability of the methods is crucial, as ''black box'' models would not actually advance our biological knowledge, however good they are at predicting cellular behavior.

In conclusion, AI has become an integral part of the proteomics enterprise. This technology is rapidly becoming established in data generation and integration. Clearly, the greatest opportunities are yet to come and will allow unprecedented insights into biological systems and novel ways to diagnose and

<!-- image -->

influence disease course. Together, the advances in biomedical data generation, including MS-based proteomics, coupled with breakthroughs in ML and DL for data analytics and integration, will move us toward the goals of data-driven precision medicine (Goecks et al., 2020; Topol, 2019).

## ACKNOWLEDGMENTS

We thank our colleagues at the Max-Planck Society, AstraZeneca, and OmicEra for fruitful discussions and especially Dr. Philipp Geyer for his input into the biomarker section. Furthermore, we acknowledge the efforts of the open-source community to make tools available to the community and thereby foster science and transparency. M.S. acknowledges funding by the German Federal Ministry of Education and Research (BMBF) project ProDiag (grant number: 01KI20377B).

## DECLARATION OF INTERESTS

C.K. is an employee of AstraZeneca and M.S. of OmicEra.

## REFERENCES

Aebersold, R., and Mann, M. (2003). Mass spectrometry-based proteomics. Nature 422 , 198-207.

Aebersold, R., and Mann, M. (2016). Mass-spectrometric exploration of proteome structure and function. Nature 537 , 347-355.

Arnold, R.J., Jayasankar, N., Aggarwal, D., Tang, H., and Radivojac, P. (2006). A machine learning approach to predicting peptide fragmentation spectra. Pac. Symp. Biocomput. 219-230.

Bader, J.M., Geyer, P.E., Muller, J.B., Strauss, M.T., Koch, M., Leypoldt, F., € Koertvelyessy, P., Bittner, D., Schipke, C.G., Incesoy, E.I., et al. (2020). Proteome profiling in cerebrospinal fluid reveals novel biomarkers of Alzheimer's disease. Mol. Syst. Biol. 16 , e9356.

Bludau, I., and Aebersold, R. (2020). Proteomic and interactomic insights into the molecular basis of cell functional diversity. Nat. Rev. Mol. Cell Biol. 21 , 327-340.

Brasoveanu, A., Moodie, M., and Agrawal, R. (2020). Textual evidence for the perfunctoriness of independent medical reviews. In CEUR Workshop Proceedings (CEUR-WS), pp. 1-9.

Byrd, J.B., Greene, A.C., Prasad, D.V., Jiang, X., and Greene, C.S. (2020). Responsible, practical genomic data sharing that accelerates research. Nat. Rev. Genet. 21 , 615-629.

Callahan, T.J., Tripodi, I.J., Pielke-Lombardo, H., and Hunter, L.E. (2020). Knowledge-based biomedical data science. Annu. Rev. Biomed. Data Sci. 3 , 23-41.

DeRitis, F., Coltorti, M., and Giusti, G. (1957). An enzymic test for the diagnosis of viral hepatitis; the transaminase serum activities. Clin. Chim. Acta 2 , 70-74.

Degroeve, S., Martens, L., and Jurisica, I. (2013). MS2PIP: A tool for MS/MS peak intensity prediction. Bioinformatics 29 , 3199-3203.

Demichev, V., Messner, C.B., Vernardis, S.I., Lilley, K.S., and Ralser, M. (2020). DIA-NN: neural networks and interference correction enable deep proteome coverage in high throughput. Nat. Methods 17 , 41-44.

Dodig-Crnkovic, T., Hong, M.G., Thomas, C.E., Haussler, R.S., Bendes, A., /C19 € Dale, M., Edfors, F., Forsstro m, B., Magnusson, P.K.E., Schuppe-Koistinen, I., et al. (2020). Facets of individual-specific health signatures determined from longitudinal plasma proteome profiling. EBiomedicine 57 , 102854.

Ducato, R. (2020). Data protection, scientific research, and the role of information. Comput. Law Secur. Rev. 37 , 105412.

Elias, J.E., Gibbons, F.D., King, O.D., Roth, F.P., and Gygi, S.P. (2004). Intensity-based protein identification by machine learning from a library of tandem mass spectra. Nat. Biotechnol. 22 , 214-219.

## Perspective

Elias, J.E., and Gygi, S.P. (2007). Target-decoy search strategy for increased confidence in large-scale protein identifications by mass spectrometry. Nat. Methods 4 , 207-214.

Ferrell, J.E., Tsai, T.Y.C., and Yang, Q. (2011). Modeling the cell cycle: why do certain circuits oscillate? Cell 144 , 874-885.

Fu, Y., Jung, A.W., Torne, R.V., Gonzalez, S., Vo hringer, H., Shmatko, A., Yates, L.R., Jimenez-Linan, M., Moore, L., and Gerstung, M. (2020). Pan-cancer computational histopathology reveals mutations, tumor composition and prognosis. Nat. Cancer 1 , 800-810.

Gessulat, S., Schmidt, T., Zolg, D.P., Samaras, P., Schnatbaum, K., Zerweck, J., Knaute, T., Rechenberger, J., Delanghe, B., Huhmer, A., et al. (2019). Prosit: proteome-wide prediction of peptide tandem mass spectra by deep learning. Nat. Methods 16 , 509-518.

Geyer, P.E., Holdt, L.M., Teupser, D., and Mann, M. (2017). Revisiting biomarker discovery by plasma proteomics. Mol. Syst. Biol. 13 , 942.

Geyer, P.E., Mann, S.P., Treit, P.V., and Mann, M. (2021). Plasma proteomes can be re-identifiable and potentially contain personally sensitive and incidental findings. Mol. Cell. Proteomics, 100035.

Geyer, P.E., Voytik, E., Treit, P.V., Doll, S., Kleinhempel, A., Niu, L., Muller, J.B., € Buchholtz, M.L., Bader, J.M., Teupser, D., et al. (2019). Plasma Proteome Profiling to detect and avoid sample related -biases in biomarker studies. EMBO Mol. Med. 11 , e10427.

Geyer, P.E., Wewer Albrechtsen, N.J., Tyanova, S., Grassl, N., Iepsen, E.W., Lundgren, J., Madsbad, S., Holst, J.J., Torekov, S.S., and Mann, M. (2016). Proteomics reveals the effects of sustained weight loss on the human plasma proteome. Mol. Syst. Biol. 12 , 901.

Goecks, J., Jalili, V., Heiser, L.M., and Gray, J.W. (2020). How machine learning will transform biomedicine. Cell 181 , 92-101.

Granholm, V., Kim, S., Navarro, J.C.F., Sjo lund, E., Smith, R.D., and Kall, L. € (2014). Fast and accurate database searches with MS-GF+percolator. J. Proteome Res. 13 , 890-897.

Grishin, D., Obbad, K., and Church, G.M. (2019). Data privacy in the age of personal genomics. Nat. Biotechnol. 37 , 1115-1117.

Higginbotham, L., Ping, L., Dammer, E.B., Duong, D.M., Zhou, M., Gearing, M., Hurst, C., Glass, J.D., Factor, S.A., Johnson, E.C.B., et al. (2020). Integrated proteomics reveals brain-based cerebrospinal fluid biomarkers in asymptomatic and symptomatic Alzheimer's disease. Sci. Adv. 6 , eaaz9360.

Ho, S.Y., Phua, K., Wong, L., and Bin Goh, W.W. (2020). Extensions of the external validation for checking learned model interpretability and generalizability. Patterns (N Y) 1 , 100129.

Jensen, L.J., Saric, J., and Bork, P. (2006). Literature mining for the biologist: Frominformation retrieval to biological discovery. Nat. Rev. Genet. 7 , 119-129.

Jensen, P.B., Jensen, L.J., and Brunak, S. (2012). Mining electronic health records: Towards better research applications and clinical care. Nat. Rev. Genet. 13 , 395-405.

Jones, A.R., and Orchard, S. (2008). Minimum reporting guidelines for proteomics released by the proteomics standards initiative. Mol. Cell. Proteomics 7 , 2067-2068.

Kall, L., Canterbury, J.D., Weston, J., Noble, W.S., and MacCoss, M.J. (2007). € Semi-supervised learning for peptide identification from shotgun proteomics datasets. Nat. Methods 4 , 923-925.

Kim, S., Gupta, N., and Pevzner, P.A. (2008). Spectral probabilities and generating functions of tandem mass spectra: a strike against decoy databases. J. Proteome Res. 7 , 3354-3363.

Kim, S., and Pevzner, P.A. (2014). MS-GF+ makes progress towards a universal database search tool for proteomics. Nat. Commun. 5 , 5277.

Kulmanov, M., Smaili, F.Z., Gao, X., and Hoehndorf, R. (2020). Semantic similarity and machine learning with ontologies. Brief. Bioinform. 2020 , bbaa199.

Landi, I., Glicksberg, B.S., Lee, H.C., Cherng, S., Landi, G., Danieletto, M., Dudley, J.T., Furlanello, C., and Miotto, R. (2020). Deep representation learning of electronic health records to unlock patient stratification at scale. npj Digit. Med. 3 , 96.

<!-- image -->

Li, K., Jain, A., Malovannaya, A., Wen, B., and Zhang, B. (2020). DeepRescore: leveraging deep learning to improve peptide identification in immunopeptidomics. Proteomics 20 , e1900334.

Lip, G.Y.H., Nieuwlaat, R., Pisters, R., Lane, D.A., and Crijns, H.J.G.M. (2010). Refining clinical risk stratification for predicting stroke and thromboembolism in atrial fibrillation using a novel risk factor-based approach: the euro heart survey on atrial fibrillation. Chest 137 , 263-272.

Liu, K., Li, S., Wang, L., Ye, Y., and Tang, H. (2020). Full-spectrum prediction of peptides tandem mass spectra using deep neural network. Anal. Chem. 92 , 4275-4283.

Lotfollahi, M., Wolf, F.A., and Theis, F.J. (2019). scGen predicts single-cell perturbation responses. Nat. Methods 16 , 715-721.

Ma, C., Ren, Y., Yang, J., Ren, Z., Yang, H., and Liu, S. (2018). Improved peptide retention time prediction in liquid chromatography through deep learning. Anal. Chem. 90 , 10881-10888.

Mahoney, F.I., and Barthel, D.W. (1965). Functional evaluation: the Barthel index. Md. State Med. J. 14 , 61-65.

Mann, S.P., Treit, P.V., Geyer, P.E., Omenn, G.S., and Mann, M. (2021). Ethical principles, constraints and opportunities in clinical proteomics. Mol. Cell. Proteomics, 100046.

Meier, F., Ko hler, N.D., Brunner, A.D., Wanka, J.H., Voytik, E., Strauss, M.T., Theis, F.J., and Mann, M. (2021). Deep learning the collisional cross sections of the peptide universe from a million experimental values. Nat. Commun. 12 , 1185.

Minaee, S., Kalchbrenner, N., Cambria, E., Nikzad, N., Chenaghlu, M., and Gao, J. (2021). Deep learning based text classification: a comprehensive review. arXiv, arXiv:2004.03705.

Moruz, L., and Kall, L. (2017). Peptide retention time prediction. Mass Spec-€ trom. Rev. 36 , 615-623.

Moruz, L., Tomazela, D., and Kall, L. (2010). Training, selection, and robust € calibration of retention time models for targeted proteomics. J. Proteome Res. 9 , 5209-5216.

Muller, J.B., Geyer, P.E., Colac ¸ o, A.R., Treit, P.V., Strauss, M.T., Oroshi, M., € Doll, S., Virreira Winter, S., Bader, J.M., Ko hler, N., et al. (2020). The proteome landscape of the kingdoms of life. Nature 582 , 592-596.

Niu, L., Thiele, M., Geyer, P.E., Rasmussen, D.N., Webel, H.E., Santos, A., Gupta, R., Meier, F., Strauss, M., Kjaergaard, M., et al. (2020). A paired liver biopsy and plasma proteomics study reveals circulating biomarkers for alcoholrelated liver disease. bioRxiv. https://doi.org/10.1101/2020.10.16.337592.

Perez-Riverol, Y., Csordas, A., Bai, J., Bernal-Llinares, M., Hewapathirana, S., Kundu, D.J., Inuganti, A., Griss, J., Mayer, G., Eisenacher, M., et al. (2019). The PRIDE database and related tools and resources in 2019: improving support for quantification data. Nucleic Acids Res. 47 , D442-D450.

Pfeifer, N., Leinenbach, A., Huber, C.G., and Kohlbacher, O. (2007). Statistical learning of peptide retention behavior in chromatographic separations: A new kernel-based approach for computational proteomics. BMC Bioinformatics 8 , 468.

Pomyen, Y., Wanichthanarak, K., Poungsombat, P., Fahrmann, J., Grapov, D., and Khoomrung, S. (2020). Deep metabolome: applications of deep learning in metabolomics. Comput. Struct. Biotechnol. J. 18 , 2818-2825.

Pugh, R.N.H., Murray-Lyon, I.M., Dawson, J.L., Pietroni, M.C., and Williams, R. (1973). Transection of the oesophagus for bleeding oesophageal varices. Br. J. Surg. 60 , 646-649.

Rawshani, A., Eliasson, B., Rawshani, A., Henninger, J., Mardinoglu, A., Carlsson, A ˚ ., Sohlin, M., Ljungberg, M., Hammarstedt, A., Rosengren, A., and Smith, U. (2020). Adipose tissue morphology, imaging and metabolomics predicting cardiometabolic risk and family history of type 2 diabetes in non-obese men. Sci. Rep. 10 , 9973.

Rebholz-Schuhmann, D., Oellrich, A., and Hoehndorf, R. (2012). Text-mining solutions for biomedical research: enabling integrative biology. Nat. Rev. Genet. 13 , 829-839.

Rieke, N., Hancox, J., Li, W., Milletarı ', F., Roth, H.R., Albarqouni, S., Bakas, S., Galtier, M.N., Landman, B.A., Maier-Hein, K., et al. (2020). The future of digital health with federated learning. NPJ Digit. Med. 3 , 119.

<!-- image -->

Santos, A., Colac ¸ o, A.R., Nielsen, A.B., Niu, L., Geyer, P.E., Coscia, F., Wewer Albrechtsen, N.J., Mundt, F., Jensen, L.J., and Mann, M. (2020). Clinical knowledge graph integrates proteomics data into clinical decision-making. bioRxiv. https://doi.org/10.1101/2020.05.09.084897.

Sen, P., Lamichhane, S., Mathema, V.B., McGlinchey, A., Dickens, A.M., Khoomrung, S., and Oresic, M. (2021). Deep learning meets metabolomics: /C20 /C20 a methodological perspective. Brief. Bioinform. 22 , 1531-1542.

Sinha, A., and Mann, M. (2020). A beginner's guide to mass spectrometrybased proteomics. Biochemist 42 , 64-69.

Smith, L.M., and Kelleher, N.L. (2018). Proteoforms as the next proteomics currency. Science 359 , 1106-1107.

Snowden, S.G., Korosi, A., de Rooij, S.R., and Koulman, A. (2020). Combining lipidomics and machine learning to measure clinical lipids in dried blood spots. Metabolomics 16 , 83.

Strauss, M.T., Bludau, I., Zeng, W.F., Voytik, E., Ammar, C., Schessner, J., Ilango, R., Gill, M., Meier, F., and Willems, S. (2021). AlphaPept, a modern and open framework for MS-based proteomics. bioRxiv. https://doi.org/10. 1101/2021.07.23.453379.

Sun, S., Yang, F., Yang, Q., Zhang, H., Wang, Y., Bu, D., and Ma, B. (2012). MS-simulator: predicting y-ion intensities for peptides with two charges based on the intensity ratio of neighboring ions. J. Proteome Res. 11 , 4509-4516.

Tarn, C., and Zeng, W.F. (2021). pDeep3: Toward more accurate spectrum prediction with fast few-shot learning. Anal. Chem. 93 , 5815-5822.

The, M., and Kall, L. (2020). Focus on the spectra that matter by clustering of € quantification data in shotgun proteomics. Nat. Commun. 11 , 3234.

Tiwary, S., Levy, R., Gutenbrunner, P., Salinas Soto, F., Palaniappan, K.K., Deming, L., Berndl, M., Brant, A., Cimermancic, P., and Cox, J. (2019). High-quality MS/MS spectrum prediction for data-dependent and data-independent acquisition data analysis. Nat. Methods 16 , 519-525.

Topol, E.J. (2019). High-performance medicine: the convergence of human and artificial intelligence. Nat. Med. 25 , 44-56.

Tran, N.H., Zhang, X., Xin, L., Shan, B., and Li, M. (2017). De novo peptide sequencing by deep learning. Proc. Natl. Acad. Sci. USA 114 , 8247-8252.

Virreira Winter, S., Karayel, O., Strauss, M.T., Padmanabhan, S., Surface, M., Merchant, K., Alcalay, R.N., and Mann, M. (2021). Urinary proteome profiling for stratifying patients with familial Parkinson's disease. EMBO Mol. Med. 13 , e13257.

Wang, D., Zeng, S., Xu, C., Qiu, W., Liang, Y., Joshi, T., and Xu, D. (2017). MusiteDeep: A deep-learning framework for general and kinase-specific phosphorylation site prediction. Bioinformatics 33 , 3909-3916.

<!-- image -->

Wang, M., Wang, J., Carver, J., Pullman, B.S., Cha, S.W., and Bandeira, N. (2018). Assembling the community-scale discoverable human proteome. Cell Syst. 7 , 412-421.e5.

Wen, B., Zeng, W.F., Liao, Y., Shi, Z., Savage, S.R., Jiang, W., and Zhang, B. (2020). Deep learning in proteomics. Proteomics 20 , e1900335.

Wewer Albrechtsen, N.J., Geyer, P.E., Doll, S., Treit, P.V., Bojsen-Møller, K.N., Martinussen, C., Jørgensen, N.B., Torekov, S.S., Meier, F., Niu, L., et al. (2018). Plasma proteome profiling reveals dynamics of inflammatory and lipid homeostasis markers after Roux-en-Y gastric bypass surgery. Cell Syst. 7 , 601-612.e3.

Wilkinson, M.D., Dumontier, M., Aalbersberg, I.J., Appleton, G., Axton, M., Baak, A., Blomberg, N., Boiten, J.W., da Silva Santos, L.B., Bourne, P.E., et al. (2016). Comment: The FAIR Guiding Principles for scientific data management and stewardship. Sci. Data 3 , 1-9.

Xu, R., Sheng, J., Bai, M., Shu, K., Zhu, Y., and Chang, C. (2020). A comprehensive evaluation of MS/MS spectrum prediction tools for shotgun proteomics. Proteomics 20 , e1900345.

Yang, J., Gao, Z., Ren, X., Sheng, J., Xu, P., Chang, C., and Fu, Y. (2021a). DeepDigest: prediction of protein proteolytic digestion with deep learning. Anal. Chem. 93 , 6094-6103.

Yang, M., Petralia, F., Li, Z., Li, H., Ma, W., Song, X., Kim, S., Lee, H., Yu, H., Lee, B., et al. (2020a). Community assessment of the predictability of cancer protein and phosphoprotein levels from genomics and transcriptomics. Cell Syst. 11 , 186-195.e9.

Yang, Y., Horvatovich, P., and Qiao, L. (2021b). Fragment mass spectrum prediction facilitates site localization of phosphorylation. J. Proteome Res. 20 , 634-644.

Yang, Y., Liu, X., Shen, C., Lin, Y., Yang, P., and Qiao, L. (2020b). In silico spectral libraries by deep learning facilitate data-independent acquisition proteomics. Nat. Commun. 11 , 146.

Zeng, W.F., Zhou, X.X., Zhou, W.J., Chi, H., Zhan, J., and He, S.M. (2019). MS/ MSspectrum prediction for modified peptides using pDeep2 trained by transfer learning. Anal. Chem. 91 , 9724-9731.

Zhang, Z. (2004). Prediction of low-energy collision-induced dissociation spectra of peptides. Anal. Chem. 76 , 3908-3922.

Zhou, X.X., Zeng, W.F., Chi, H., Luo, C., Liu, C., Zhan, J., He, S.M., and Zhang, Z. (2017). pDeep: predicting MS/MS spectra of peptides with deep learning. Anal. Chem. 89 , 12690-12697.