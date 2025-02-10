## CELL DEATH

## Gasdermin D plays a vital role in the generation of neutrophil extracellular traps

Gabriel Sollberger , Axel Choidas , Garth Lawrence Burn , Peter Habenberger , 1 2 1 2 Raffaella Di Lucrezia , Susanne Kordes , Sascha Menninger , Jan Eickhoff , 2 2 2 2 Peter Nussbaumer 2 , Bert Klebl , Renate Krüger , Alf Herzig , Arturo Zychlinsky * 2 3 1 1

The death of a cell is an inevitable part of its biology. During homeostasis, most cells die through apoptosis. If homeostasis is disturbed, cell death can switch to proinflammatory forms of death, such as necroptosis, pyroptosis, or NETosis. We demonstrate that the formation of neutrophil extracellular traps (NETs), a special form of neutrophil cell death that releases chromatin structures to the extracellular space, is dependent on gasdermin D (GSDMD). GSDMD is a pore-forming protein and an executor of pyroptosis. We screened a chemical library and found a small molecule based on the pyrazolo-oxazepine scaffold that efficiently blocks NET formation and GSDMD-mediated pyroptotic cell death in human cells. During NETosis, GSDMD is proteolytically activated by neutrophil proteases and, in turn, affects protease activation and nuclear expansion in a feed-forward loop. In addition to the central role of GSDMD in pyroptosis, we propose that GSDMD also plays an essential function in NETosis.

## INTRODUCTION

Disturbance of host homeostasis can lead to proinflammatory forms of cell death that result in cell lysis ( 1 ). This lysis is beneficial for the host because it amplifies inflammatory signals, but it can have patho­ logical consequences. Inflammasomes are protein complexes that as­ semble upon sensing a broad variety of danger signals and activate inflammatory caspases. These cysteine proteases activate the pro­ inflammatory cytokines interleukin­1  (IL­1  ) and IL­18 and are re­ quired for pyroptosis ( 2 3 , ). Caspase­1 processes IL­1  /IL­18 during canonical inflammasome activation, whereas caspase­4 and caspase­5 in humans (or their ortholog caspase­11 in mice) are activated in noncanonical inflammasomes in response to intracellular lipopoly­ saccharide (LPS) ( 4 5 , ). The pyroptotic substrate is the pore­forming protein gasdermin D (GSDMD) ( 6 , 7 ). The C­terminal domain of GSDMD inhibits the pore­forming capacity of the N terminus. Caspase­mediated cleavage liberates the N­terminal domain that multimerizes and lyses the cell by membrane rupture ( 8 -11 ). Caspase­11- and GSDMD­deficient mice are protected from septic shock induced by LPS ( 4 , 7 ), demonstrating the importance of py­ roptosis in driving LPS­induced inflammation in vivo.

Distinct from pyroptosis that preferentially occurs in macro­ phages and monocytes, NETosis is a neutrophil cell death pathway that leads to the release of chromatin decorated with specific pro­ teins ( 12 ). These chromatin protein structures, called neutrophil ex­ tracellular traps (NETs), capture microorganisms, activate myeloid cells, and promote coagulation ( 13 ). During NETosis, in contrast to other forms of cell death, the nucleus disintegrates before the cyto­ plasmic membrane is compromised and chromatin is released to the extracellular space. NETs are a double­edged sword; they are bene­ ficial in infections but pathogenic by exposing autoantigens and

promoting thrombosis ( 14 ). Hence, NETs are a promising drug tar­ get for various pathologies ( 13 ).

Different NET­inducing stimuli engage diverse pathways, com­ plicating the analysis of NETosis ( 15 ). Activation with microbes or mitogens ( 16 ), like phorbol 12­myristate 13­acetate (PMA), gener­ ates reactive oxygen species (ROS) by the NADPH (reduced form of nicotinamide adenine dinucleotide phosphate) oxidase complex (NOX2), which activates mitogen­activated protein (MAP) kinase signaling. ROS signaling releases a macromolecular complex called azurosome from granules, which translocates neutrophil elastase (NE) to the nucleus ( 17 18 , ). NE processes histones, which coincides with chromatin expansion in the whole cell before the plasma membrane rupture and NET release ( 19 ). We do not understand how neutro­ phils lyse to liberate NETs. Here, through a large screen of small mole­ cules, we have identified a compound that blocks NET formation. This compound blocks cell lysis by binding to GSDMD and inhibits both pyroptosis and NETosis. In neutrophils, GSDMD is cleaved by serine proteases, like NE, and allows the release of granular proteins that are required for NETosis progression in a feed­forward loop.

## RESULTS

## Identification of molecules that inhibit NET formation

Because neutrophils are short­lived, terminally differentiated cells that preclude genetic manipulation, we screened a library of 182,710 small molecules to identify PMA­induced NETosis inhibitors in neutrophils isolated from healthy volunteers. We scored cells for NET formation by automated microscopy (fig. S1A) ( 17 ). We iden­ tified a compound class of NET formation inhibitors based on the pyrazolo­oxazepine scaffold, which potently inhibited PMA­induced NETosis (Fig. 1, A and B). A member of this class, LDC7559, was not toxic to peripheral blood mononuclear cells (PBMCs). It efficiently inhibited PMA­induced NET formation with an IC50 (median in­ hibitory concentration) of 5.61  M and the biologically relevant cho­ lesterol crystal­induced NET formation ( 20 ) with an IC50 of 0.304  M (Fig. 1B and fig. S1, B to D). This compound did not block NADPH oxi­ dase, NE, or myeloperoxidase (MPO) activity (Fig. 1B and fig. S1, E to G), suggesting that it acted downstream of NOX2 and the azurosome.

Copyright © 2018 The Authors, some rights reserved; exclusive licensee American Association for the Advancement of Science. No claim to original U.S. Government Works

|

Fig. 1. A chemical screen identifies a compound that inhibits NET formation and binds to GSDMD. ( A ) Screening results. NETs were quantified by image acquisition. A total of 6397 compounds reduced NET incidence to less than 50%, resulting in ≈3.4% hit rate. ( B ) Structure and characterization of LDC7559, showing the IC50 (in  M) for NET formation induced by PMA and cholesterol crystals, viability in PBMCs, NADPH oxidase, MPO, and NE activity; only NET formation was affected. ( C to E ) Human primary neutrophils were treated with 1 or 10  M LDC7559. (C) ROS production of human primary neutrophils activated with PMA. (D) Percentage of neutrophils that phagocytosed fluorescent beads, analyzed 30 min after incubation with beads by flow cytometry. (E) NET formation upon treatment with PMA. Cell death was assessed by adding the cell-impermeable DNA dye SYTOX Green and measuring fluorescent signal over time. ( F ) Affinity chromatography. LDC2618 was coupled to beads and incubated with HL-60 lysates (1) without (2) or with (3) competition by the initial hit compound LDC7559. After washing, the precipitated peptides were analyzed by MS. ( G ) Results of MS, showing enrichment of GSDMD peptides upon pulldown with LDC2618 and competition by LDC7559 in two independent experiments. Peptides for NOX2 and MPO were identified but not enriched upon pulldown and not competed by LDC7559. (C to E) Mean ± SEM of three independent experiments. * P &lt; 0.05, oneway analysis of variance (ANOVA) with Dunnett's multiple comparisons test. DMSO, dimethyl sulfoxide; ns, not significant.

<!-- image -->

M

|

LDC7559 transiently decreased ROS production after the initial peak in human primary neutrophils (Fig. 1C), although this reduction was too small to affect NETosis, as shown later in this study (Fig. 6B). The compound did not block phagocytic activity of human primary neutrophils, which is in line with our findings that it specifically in­ hibited NET formation (Fig. 1D). We verified our results from the screen by treating neutrophils with PMA and measuring NET for­ mation over time and found that even 1  M LDC7559 potently de­ layed NET formation (Fig. 1E and fig. S2A).

## LDC7559 binds to GSDMD and inhibits inflammasome activation

We identified the target of LDC7559 by affinity chromatography. We used LDC2618 (fig. S2B), a derivative of the initial hit as bait, to pull down proteins bound to this compound class from cell lysates and verified specific binding by competition with the initial hit com­

<!-- image -->

LDC7559

<!-- image -->

LDC7559

pound LDC7559 (Fig. 1F). We analyzed the pulldowns by mass spec­ trometry (MS) and identified several peptides corresponding to GSDMD, which was the most enriched protein (Fig. 1G and fig. S2, C and D). Furthermore, in the affinity chromatography, we did not enrich peptides corresponding to NOX2 or MPO (Fig. 1G), two abun­ dant proteins in neutrophils. These results are consistent with the fact that LDC7559 did not inhibit the activity of these two enzymes (Fig. 1B) and suggest that the compound specifically binds GSDMD.

To confirm that LDC7559 inhibits GSDMD­dependent processes, we tested the effects of this compound on pyroptosis in human pri­ mary monocytes, the monocytic cell line THP­1 and murine immor­ talized bone marrow-derived macrophages (BMDMs). LDC7559 blocked IL­1  release in human primary monocytes incubated with silica crystals to activate the NLRP3 inflammasome (Fig. 2A) and upon poly(deoxyadenosine­deoxythymidine) [poly(dA­dT)] transfection to stimulate the Aim2 inflammasome (Fig. 2B). Previous studies

<!-- image -->

<!-- image -->

<!-- image -->

LDC7559

Fig. 2. LDC7559 inhibits GSDMD and blocks IL-1  release and pyroptosis. ( A and B ) Human primary monocytes were primed with ultrapure LPS, and the inflammasome was activated with silica (A) or by transfection of poly(dA-dT) (B); IL-1  release was measured by enzyme-linked immunosorbent assay (ELISA). Values are shown as relative to non-inhibitor-treated cells due to donor variability in absolute IL-1  amounts. Cells were treated with LDC7559 at 1 or 10  M or with caspase-1/4 (Casp-1/4) inhibitor (VX-765, 50  M) as a control. ( C ) THP-1 cells were differentiated for 8 hours with PMA, transfected with LPS, and incubated overnight in the absence or presence of LDC7559 (1, 5, or 10  M). IL-1  release was measured by ELISA. ( D ) Murine immortalized BMDMs were primed with Pam3CSK4 for 5 hours, transfected with LPS, and incubated overnight in the absence or presence of LDC7559 (1, 5, and 10  M). IL-1  release was measured by ELISA. ( E and F ) HEK293T cells were transfected with fulllength (FL), C-terminal (CT), and N-terminal (NT) human (hGSDMD; E) or murine (mGSDMD; F) GSDMD constructs. LDH release was measured 16 hours later. When indicated, LDC7559 was added at 1, 5, or 10  M (E) or at 5  M (F) 2 hours after transfection. (E) Caspase-1/4 inhibitor (VX-765, 50  M) or pan-caspase inhibitor (Z-VAD-FMK, 20  M) was added at the same time as LDC7559. (A to F) Mean ± SEM of three independent experiments or four independent experiments (A). * P &lt; 0.05, ** P &lt; 0.01, *** P &lt; 0.001, one-way ANOVA with Dunnett's multiple comparisons test.

<!-- image -->

|

demonstrated that lysis by canonical inflammasomes depends only partially on GSDMD because deficiency in this gene delays, rather than abolishes, IL­1  release  ( 7 ).  Therefore, we also activated the noncanonical inflammasome by LPS transfection in THP­1 cells and showed that the LDC7559 treatment inhibited IL­1  release (Fig. 2C). In immortalized murine BMDMs, LDC7559 also reduced IL­1  release upon LPS delivery to the cytoplasm, demonstrating that LDC7559 is active on human and murine cells (Fig. 2D).

Human embryonic kidney (HEK) 293T cells do not express GSDMD; however, transfection of the N terminus, but not the full length or C terminus of this protein, is toxic ( 6 ). LDC7559 blocked the toxicity of the N terminus of both human and murine GSDMD (Fig. 2, E and F), indicating that LDC7559 affects GSDMD activity directly. As expected, because the toxicity of the N­terminal GSDMD

is independent of caspases, inhibitors of these proteases did not in­ hibit cell death in this assay (Fig. 2E). Together, these data show that LDC7559 blocks the activity of the GSDMD N terminus.

## GSDMD is cleaved during NET formation and localizes to the plasma membrane

Upon neutrophil activation with PMA, full­length GSDMD levels were reduced (fig. S3A). As controls, we used neutrophils isolated from a patient with X­linked chronic granulomatous disease (CGD). CGD patients carry mutations in NOX2 and do not form NETs upon PMA stimulation ( 21 ). In PMA­treated neutrophils isolated from this CGD patient, levels of full­length GSDMD remained intact (fig. S3A). In some cases, probably dependent on donors and timing, we observed the appearance of a 25­ to 30­kDa fragment, corresponding

Fig. 3. GSDMD localizes to the plasma membrane and is processed during NET formation. ( A ) Western blot of human primary neutrophils isolated from a control donor (ctr.) or from a patient with X-linked CGD after stimulation with PMA for 2.5 hours. GSDMD was detected with an antibody directed against full-length GSDMD. In this control, donor loss of full-length GSDMD corresponded with the occurrence of a processed N terminus, which is marked by an arrow. ( B ) Microscopy images of human primary neutrophils activated for the indicated time points with PMA and stained with antibodies against GSDMD and NE as well as with the DNA dye DAPI; membranes were stained with DiI. GSDMD is detected in remnants of cells that had made a NET (white arrows). Images were acquired at the coverslip level; therefore, spread NETs are not seen. Scale bars, 10  m. ( C ) High-resolution TIRF microscopy of human primary neutrophils undergoing NET formation. Cells were fixed at the indicated time points after PMA stimulation in the presence or absence of 5  M LDC7559. Plasma membranes were stained with DiD. Scale bars, 10  m. ( D ) Quantification of TIRF microscopy. Background signal was determined outside the cells, and GSDMD signal (at least 2× background fluorescence intensity) in the TIRF zone was analyzed. Mean ± SEM of three independent experiments is depicted. *** P &lt; 0.001, unpaired two-tailed   test. t

<!-- image -->

|

Fig. 4. NE cleaves and activates GSDMD. ( A and B ) Human neutrophils were treated with caspase inhibitors (Z-VAD-FMK, 20  M; VX-765, 50  M) before activation with PMA. NET formation was assessed by staining cells with SYTOX Green and measuring fluorescent signal over time. ( C ) GSDMD-expressing HEK293T lysates were incubated with lysates of human primary neutrophils for 20 min in the presence of absence of LDC7559 (10  M) or NE inhibitor (NEi; 10  M). ( D to F ) GSDMD-expressing HEK293T lysates were incubated with purified or recombinant proteases for 30 min. (E) Point mutations are indicated in green; caspase cleavage site D275 is marked in purple. Lysates were incubated with NE. (F) Expression of putative NE-cleaved N-terminal fragments of human GSDMD in HEK293T cells. LDH release was measured 16 hours after transfection. Mean ± SEM of three independent experiments is depicted. ( G ) Lysates of HEK293T cells expressing GSDMD with different four amino acid deletions were incubated with NE or caspase-4. The number on the lane of the Western corresponds to the number in the graphical depiction of the deletions at the bottom of the panel (caspase-4 site is marked in purple). FL, full-length GSDMD. (C to E and G) GSDMD was detected by Western blotting using an antibody directed against full-length GSDMD. Arrows indicate active fragment. * P &lt; 0.05, ** P &lt; 0.01, *** P &lt; 0.001, one-way ANOVA with Dunnett's multiple comparisons test.

<!-- image -->

|

to the lytic N terminus of the protein, upon loss of full­length GSDMD (Fig. 3A). Consistent with the data showing that NOX2 is upstream of GSDMD activation, GSDMD was not cleaved upon PMA stimu­ lation in CGD patient neutrophils (Fig. 3A). We stained primary neutrophils for GSDMD with an antibody that recognizes both full­ length and processed GSDMD and found that it localized primarily to the cytoplasm in nonstimulated cells (Fig. 3B). We also found GSDMD on NETs (fig. S3B) and a strong signal in remnants of NET­forming neutrophils (Fig. 3B and fig. S3C). This is consistent with the local­ ization of the GSDMD N terminus to the plasma membrane of cells undergoing pyroptosis ( 8 -11 ). Furthermore, using high­resolution total internal reflection fluorescence (TIRF) microscopy, we found that as NETosis progressed, GSDMD accumulated at the TIRF zone, indicating that it localized to the plasma membrane (Fig. 3, C and D, and fig. S3, D to F). We quantified the percentage of GSDMD de­ tected by TIRF in the presence or absence of LDC7559 and found that GSDMD membrane localization was markedly reduced by the compound, suggesting that it inhibits GSDMD cleavage or mem­ brane integration in neutrophils (Fig. 3, C and D, and fig. S3, D to F). We did not observe NE in the TIRF zone of either naïve or PMA­ treated neutrophils (fig. S4), indicating that the translocation of GSDMD to the membrane is specific. Together, these experiments demonstrate that GSDMD is cleaved during NET formation and then localizes to the plasma membrane of neutrophils.

## Neutrophil serine proteases process GSDMD

NETosis is independent of caspases, because neither the pan­caspase inhibitor Z­VAD­FMK nor the caspase­1/4-specific inhibitor VX­765, which efficiently blocks pyroptosis ( 22 ), was able to reduce NET for­ mation (Fig. 4, A and B, and fig. S5, A to C) ( 23 ). To identify the protease that cleaves GSDMD during NETosis, we incubated lysates of HEK293T cells expressing full­length GSDMD with neutrophil lysates and found processing of the full­length protein into a frag­ ment between 25 and 30 kDa resembling the active GSDMD N ter­ minus (Fig. 4C). Neutrophils express three main proteases-NE,

proteinase 3 (PR3), and cathepsin G (CG)-all of which have pro­ miscuous target recognition. However, inhibition of NE alone was suf­ ficient to substantially reduce GSDMD cleavage (Fig. 4C). LDC7559 did not inhibit this processing (Fig. 4C), in line with the finding that the compound did not inhibit NE activity (Fig. 1C). Complementary to this approach, we incubated GSDMD from HEK293T lysates with purified and recombinant proteases. Whereas caspase­4 and NE readily processed GSDMD into a fragment of similar size, CG and PR3 were far less efficient at cleaving GSDMD (Fig. 4D). Again, LDC7559 did not interfere with GSDMD processing, confirming that it is not a protease inhibitor and showing that it does not render GSDMD cleavage­resistant (fig. S5D).

Because NE and caspase­4 generate an N terminus of similar size, we speculated that the cleavage sites would be in the same region. Caspase­4 cleaves GSDMD at amino acid 275, and the first 243 amino acids of GSDMD are required to induce pyroptosis ( 6 ). Using the ExPASy PeptideCutter tool ( 24 ),  we identified five potential NE cleavage sites in the region between amino acids 243 and 282 that could result in a functional fragment (Fig. 4E). Constructs with single point mutations in these sites were still cleaved by purified NE (Fig. 4E), which is consistent with several redundant cleavage sites. Expression of the GSDMD N terminus corresponding to all but the shortest of the five putative NE­induced fragments induced lysis in HEK293T cells. The fragment ranging from amino acid 1 to 255 was the most effective (Fig. 4F). Lysis induced by these N termini could be inhibited by LDC7559 (fig. S5E). To identify NE cleavage regions, we further gen­ erated deletion mutants lacking four amino acid stretches around the caspase cleavage site and expressed those constructs in HEK293T cells (Fig. 4G). As expected, deletion of D275 abrogated the sensitivity of GSDMD to caspase­4. We also observed that deletion of amino acids 279 to 282 made the protein insensitive to caspase­4, probably due to effects on protein folding. These deletions also made GSDMD less sensitive to NE (Fig. 4G), suggesting that NE cleaves GSDMD at var­ ious positions between amino acids 275 and 282. We also generated a mutant GSDMD lacking amino acids 255 to 258 and found that this

Fig. 5. GSDMD is required for NETosis. ( A ) Murine peritoneal neutrophils of WT ( n = 4) and GSDMD mutant (GSDMDmut; n = 3) mice were seeded and treated with 100 nM PMA for 6 hours, and NETs were analyzed by staining with the cell-permeable DNA dye SYTO Green and the cell-impermeable DNA dye SYTOX Orange. Mean ± SEM is depicted. ** P &lt; 0.01, unpaired two-tailed   test. ( t B ) Representative images of WT and GSDMD mutant neutrophils activated with PMA for 6 hours and stained with an anti-chromatin antibody and the DNA dye DAPI. Scale bars, 25  m.

<!-- image -->

|

mutant was moderately more resistant to NE cleavage, indicating that position 255 could contribute to GSDMD processing (fig. S5F). We found that deletion of amino acids 267 to 270 resulted in a protein that could still be processed by caspase­4 but was more resistant

to NE cleavage (Fig. 4G). This is consistent with a recent report demonstrating that NE cleaves GSDMD at position C268 ( 25 ). NE therefore cleaves GSDMD at several sites, resulting in lysis­inducing fragments.

Fig.  6.  GSDMD  regulates  NE  during NETosis. ( A )  Human primary neutrophils were activated with PMA or nigericin in the presence or absence of 1  M LDC7559 and stained with antibodies against chromatin, MPO, and the DNA dye DAPI. Scale bars, 25  m. ( B ) Neutrophils were treated with 1  M LDC7559 or the indicated doses of pyrocatechol (3.75, 7.5, 15, and 30  M); ROS production was determined by luminometry. ( C ) LDH release of neutrophils 3.5 hours after PMA induction in the presence or absence of LDC7559 or increasing doses of pyrocatechol. ( D ) LDH release of human primary neutrophils after 3.5 hours of activation with PMA. LDC7559 (1  M) was added at the indicated time points before or after PMA stimulation. ( E ) Neutrophils were activated with PMA for 2 hours and stained with an antibody against NE and with phalloidin to stain the actin cytoskeleton. Scale bars, 25  m. ( F ) Neutrophils were stimulated with PMA in the presence or absence of the NE inhibitor or LDC7559, and cells were harvested at 2.5 hours. GSDMD processing was analyzed by Western blot with an antibody directed against full-length GSDMD. ( G ) Neutrophil lysates were harvested 2 hours after PMA stimulation and analyzed by Western blotting using an antihistone H3 antibody to show processing. Arrow indicates processing. (B to D) Mean ± SEM of three independent experiments. * P &lt; 0.05, ** P &lt; 0.01, *** P &lt; 0.001, one-way ANOVA with Dunnett's multiple comparisons test.

<!-- image -->

## GSDMD is required for NETosis

To genetically confirm the requirement of GSDMD in NETosis, we isolated neutrophils of GSDMD mutant mice ( 7 ) and activated them with PMA. NET formation in GSDMD mutant neutrophils was signifi­ cantly reduced (Fig. 5, A and B), demonstrating a requirement of GSDMD for NETosis.

We next asked mechanistically where GSDMD acts in the path­ way of NET formation. LDC7559 did not affect neutrophil lysis upon addition of the detergent digitonin, indicating that the effects of this compound are not simply stabilizing the cell membrane (fig. S6A). Furthermore, when we tried to wash out LDC7559 at different time points after PMA treatment, we did not detect significant changes in cell lysis, arguing that LDC7559 acts intracellularly (fig. S6B). LDC7559 blocked a ROS­dependent NET formation pathway (Figs. 1, C and F, and 6A and fig. S6C) but did not inhibit NET formation in response to nigericin, which acts independent of ROS production (Fig. 6A and fig. S6, D and E). Furthermore, PMA or nigericin treat­

Sollberger et al ., Sci. Immunol. 3 , eaar6689 (2018)     24 August 2018

<!-- image -->

ment did not induce IL­1  release from neutrophils, again demon­ strating that the cell death we saw occurred independent of inflam­ masome activation (fig. S6, F and G). Because LDC7559 transiently reduced ROS production upon PMA treatment, we tested whether this effect was sufficient to block NETosis. To determine the mini­ mal amount of ROS required, we titrated the ROS scavenger pyro­ catechol to reach different levels of ROS production (Fig. 6B). The concentration of pyrocatechol that reduced ROS production simi­ larly to LDC7559 treatment did not inhibit NETosis (Fig. 6C). We also showed that adding LDC7559 blocked NETosis even if added up to 30 min after PMA induction, which is a time point when neu­ trophils had already mounted an oxidative burst (Fig. 6D). Together, these experiments suggest that LDC7559 and GSDMD act down­ stream of the oxidative burst.

During NET formation, ROS production facilitates NE release from granules through dissociation from a multiprotein aggregate. NE then degrades actin and enters the nucleus where it processes

Fig. 7. GSDMD is required for nuclear expansion during NETosis. ( A to D )  Neutrophils were activated with PMA (A and C) or nigericin (B and D) and stained with the cell-permeable DNA dye DRAQ5 and the cell-impermeable DNA dye SYTOX Green. Images were acquired every 2 min for 6 hours. Single cells were selected semiautomatically; nuclear expansion and NET formation were quantified using an automated workflow in ImageJ and R. Bottom panels depict P values determined by unpaired two-tailed   tests at each time point, and red areas t refer to P &lt; 0.05. Mean ± SEM is depicted; n refers to the number of independent experiments. (A and B) NET formation of neutrophils activated with PMA (A) or nigericin (B). (C and D) Quantification of nuclear expansion over time in neutrophils stimulated with PMA (C) or nigericin (D). ( E ) Quantification of the time it took single cells to expand their nucleus upon PMA treatment in the presence or absence of LDC7559; horizontal lines depict the median. P = 1.5384 × 10 -111 , determined by Wilcoxon rank-sum test with continuity correction. ( F ) Quantification of the time it took single PMA-treated cells with an expanded nucleus to lyse; horizontal lines depict the median. LDC7559 treatment did not delay this process. P = 0.0044, determined by Wilcoxon rank-sum test with continuity correction. LDC7559 concentration was 5  M in all experiments.

<!-- image -->

|

|

histones ( 18 19 , ). LDC7559 treatment strongly reduced actin degra­ dation, and both MPO (fig. S6H) and NE (Fig. 6E) remained in granules, indicating that GSDMD has a role upstream of NE mobi­ lization from granules. Together with the observation that NE activity is required for GSDMD processing, these results suggest a feed­ forward loop where GSDMD and NE use each other for their acti­ vation. Both the NE inhibitor and LDC7559 reduced processing of GSDMD during PMA­induced NETosis (Fig. 6F), and LDC7559 re­ duced processing of histone H3, which is an indicator of NE activity during NETosis (Fig. 6G).

## GSDMD affects nuclear expansion during NET formation

Last, we addressed how the NE­GSDMD axis affects the dynamics of NET formation using a live­cell imaging approach with the cell­ permeable DNA dye DRAQ5 and the cell­impermeable DNA dye SYTOX Green. This dual staining allowed us to quantify changes in nuclear area, permeability, and lysis in single cells over time (movie S1 and fig. S7, A to D). LDC7559 strongly reduced NET release upon PMA treatment but not upon NET induction with nigericin, con­ firming our previous results (Fig. 7, A and B, and movies S2 to S5). NET release depends on two processes: nuclear expansion and cel­ lular lysis. NET stimuli that induce no or only marginal GSDMD cleavage, such as nigericin (fig. S7E), showed similar kinetics of nuclear expansion in the presence or absence of LDC7559. However, the nuclear expansion of PMA­treated neutrophils was significantly reduced upon LDC7559 treatment (Fig. 7, C and D). To a lower extent, we also saw an impact of LDC7559 on NET formation and nuclear expansion in response to the calcium ionophore A23187 (fig. S7, F and G).

LDC7559 did not only reduce the number of cells that expanded their nucleus but also slowed down the kinetics of nuclear expan­ sion in the remaining ones (Fig. 7E). This is consistent with the in­ hibition of an NE­GSDMD feedback loop upon PMA induction of NETosis (fig. S8). However, once these cells reached a state with an expanded nucleus, the time interval to cell lysis was similar in the absence or presence of LDC7559 (Fig. 7F). This finding suggests that, once the NE­GSDMD axis resulted in NE activity that allowed nuclear expansion, the levels of cleaved GSDMD are sufficiently high for cellular lysis.

## DISCUSSION

Pyroptosis and NETosis are often activated in similar disease pro­ cesses where immune defense, against either sterile or microbial in­ sults, is required, and both of these forms of cell death are involved in similar pathologies. However, mechanistically, there are differ­ ences between pyroptosis and NETosis: Pyroptosis relies on pro­ inflammatory caspase activity, and it removes the niche for intracellular pathogens and activates IL­1. NETosis, on the other hand, requires neutrophil serine proteases, and NETs capture extracellular micro­ organisms and stimulate other leukocytes. Here, we report that there is a common executioner protein through which both cell death path­ ways converge: GSDMD. Our data show that processing of GSDMD into a lethal fragment can be adapted by different pathways and proteases. This is in line with other reports showing that apoptotic caspases can process the gasdermin family member DFNA5 into a lytic form to drive secondary necrosis ( 26 27 , ).

Also published in this issue, Chen et al . ( 28 ) report that, upon activation of noncanonical inflammasomes, neutrophils also release

NETs dependent on GSDMD. Thus, the two studies together show that, in neutrophils, different stimuli activate diverse proteases that cleave GSDMD to execute NETosis. Intracellular LPS promotes in­ flammasome assembly and caspase cleavage of GSDMD, whereas classical NETosis requires ROS that activate serine proteases that also cleave GSDMD. These data suggest that GSDMD is a hub of proinflammatory cell death.

On the basis of the data presented here, we propose that GSDMD has two functions (fig. S8). First, NE and GSDMD engage in a feed­ forward loop in which the protease activates GSDMD. Activated GSDMD, in turn, forms pores in the granule membrane, thus enhanc­ ing NE release into the cytoplasm and allowing further GSDMD cleavage in a reiterative process. This enables the translocation of NE to the nucleus, where it processes histones and allows nuclear ex­ pansion ( 18 ). Second, upon completion of NETosis, cleaved GSDMD forms pores in the plasma membrane, allowing NET release. Classical NETosis requires ROS production and the activation of MPO to release NE into the cytoplasm ( 18 ). Our data support the model that GSDMD activity is downstream of initial NE release, but further inves­ tigation should address the involvement of MPO, and other putative components required for NETosis, such as PAD4, on GSDMD acti­ vation. This also suggests that degranulation of neutrophils might constitute an event that inhibits NETosis, which would be consist­ ent with the finding that neutrophils treated with formylated pep­ tides such as N ­formyl­Met­Leu­Phe ( MLP) (a strong inducer of f degranulation) produce ROS but do not form NETs ( 16 ), and it will be interesting to analyze the impact of degranulation on GSDMD activation in neutrophils.

Our data are consistent with a recent report by Kambara et al . ( 25 ), describing that GSDMD­deficient neutrophils are longer­lived than wild­type (WT) cells, which is an important aspect of neutro­ phil biology, because these cells are notoriously short­lived. Upon neutrophil aging, NE is released from damaged granules and pro­ cesses GSDMD into an active fragment. Kambara et al . also showed that GSDMD­deficient mice are more resistant to an Escherichia coli challenge, probably because this microbe is susceptible to phagocyto­ sis, and the extended life of neutrophils is protective. Thus, GSDMD activation might be detrimental in infections where neutrophil phago­ cytosis is effective and beneficial when NETs are required, for example, in fungal infections. Furthermore, the N terminus of GSDMD has been shown to have antimicrobial properties ( 8 ). Because we detected GSDMD on NETs, it is possible that this protein contributes to pathogen clearance not only by allowing NET release but also by directly killing extracellular microbes.

By carrying out a chemical screen to identify modulators of NETosis, we unexpectedly uncovered a compound that binds GSDMD and modulates its actions. This compound, or its deriva­ tives, might represent a starting point to target GSDMD function in a plethora of diseases where both inflammasome activation and NET formation are pathological including cancer, autoinflammatory, auto­ immune, and vascular diseases.

## MATERIALS AND METHODS

## Antibodies, staining reagents, and inhibitors

GSDMD antibody (G7422, Sigma), NE antibody (481001, Millipore), MPO antibody (A0398, Dako), glyceraldehyde­3­phosphate dehy­ drogenase (GAPDH) antibody (14C10, Cell Signaling Technology), histone H3 antibody (ab1791, Abcam), chromatin antibody (PL2.3)

|

( 29 ), SYTOX Green nucleic acid stain/SYTO Green nucleic acid stain/ SYTOX Orange nucleic acid stain (Thermo Fisher Scientific), DRAQ5 (Biostatus), Hoechst (Sigma), 4 ,6­diamidino­2­phenylindole (DAPI; ' Sigma), DiI/ DiD (Invitrogen), Z­VAD­FMK (ALX­260­020, Enzo), Z­YVAD­CHO (ALX­260­027, Enzo), Z­LEVD­CHO (ALX­260­065, Enzo), Z­WEHD­CHO (ALX­260­055, Enzo), NE inhibitor (BAY 85­8501) ( 30 ), pyrocatechol (C9510, Sigma), Luminol (11050, AAT­ Bioquest), horseradish peroxidase (31941, Serva), and PMA (P8139, Sigma) were used.

## GSDMD constructs

GSDMD­GFP (green fluorescent protein) was purchased from Origene (catalog no. RG203399). GSDMD full length, GSDMD C terminus (276­484), and GSDMD N terminus (1­275) were cloned into vector PS100085 obtained from Origene (catalog no. PS100085). GSDMD­A244S, GSDMD­A255S, GSDMD­V277E, GSDMD­  A279S, and GSDMD­A282S point mutations were gener­ ated in GSDMD­  GFP vector obtained from Origene (catalog no. RG203399). GSDMD­del255­258, GSDMD­del259­262, GSDMD­ del267­270, GSDMD­del271­274, GSDMD­del275­278, and GSDMD­ del279­282 mutations were generated in PS100085 obtained from Origene (catalog no. PS100085).

## Donor consent

Human primary neutrophils were isolated from blood samples obtained from volunteers according to the Declaration of Helsinki. All participants provided written informed consent. All samples were collected with approval from the local ethics committee.

## Neutrophil isolation

Cells were purified by a first centrifugation of whole blood over Histopaque­1119 (Sigma) and subsequently over a discontinuous Percoll gradient ( 20 ). All experiments, except live imaging, were done in RPMI 1640 (without phenol red; Gibco) supplemented with 10 mM Hepes and 0.02% human serum albumin. Live imaging was done in Agilent Seahorse XF RPMI Medium (Agilent) supplemented with 10 mM glucose, 2 mM glutamine, 20 mM Hepes, and 0.02% human serum albumin at pH 7.4.

## Neutrophil stimulation

Purified neutrophils were seeded at a density of 10  cells in 96­well 5 plates for measurements of ROS or measurements of NET forma­ tion by SYTOX Green. For immunofluorescence stainings and live imaging, neutrophils were seeded in  ­Slide 8 Well ibiTreat dishes (ibidi; see respective sections). Cells were treated with inhibitors 45 min before induction of NET formation. All PMA (Sigma) stimu­ lations were done at 100 nM (except for high­throughput screening where PMA was added at 40 nM), and all nigericin (N7143, Sigma) stimulations were done at 15  M. All A23187 (Santa Cruz Biotech­ nology Inc.) stimulations were done at 5  M. Cholesterol crystals (C3045, Sigma) were added at 1 mg/ml.

## Preparation of neutrophil lysates to visualize GSDMD processing by Western blotting

Neutrophils were seeded at 3 × 10  per well in six­well plates. 6 Cells were treated with 100 nM PMA or 15  M nigericin for the indicated time points and harvested by scraping adherent cells and remnants of dead cells off the plate in 8 M urea containing protease inhibitor cocktail (Sigma) and NE inhibitor. Lysates were

mixed with an equal volume of 2× SDS loading buffer containing 200 mM dithiothreitol (DTT).

## Mice

Mouse breeding and isolation of peritoneal neutrophils were approved by the Berlin state authority Landesamt für Gesundheit und Soziales. Animals were bred at the Max Planck Institute for Infection Biology. Mice were housed in specific pathogen-free conditions, maintained on a 12­hour light/12­hour dark cycle, and fed ad libitum. GSDMD mutant mice ( 7 ) were provided by Genentech.

## Isolation and stimulation of murine peritoneal neutrophils

Murine neutrophils were isolated from peritoneal cavities of WT and GSDMD mutant animals after injection of casein (Sigma) intraperi­ toneally by centrifugation over Percoll ( 31 ). Cells were seeded at 10 5 in 24­well plates in RPMI (Gibco) containing penicillin/streptomycin (Gibco) and glutamine (Gibco), 1% murine DNase -/-serum, and murine granulocyte colony­stimulating factor (100 ng/ml; PeproTech). Forty­five minutes after seeding, cells were stimulated with 100 nM PMA for 6 hours. NETs were quantified with microscopic images after staining unfixed cells with the cell­permeable DNA dye SYTO Green and the cell­impermeable DNA dye SYTOX Orange.

For immunofluorescence staining, neutrophils were seeded at 10  per well in 5  ­Slide 8 Well glass­bottom dishes (ibidi) and treated with 100 nM PMA for 6 hours. Cells were fixed with 2% paraformaldehyde (PFA) for 30 min at room temperature. After washing with phosphate­buffered saline (PBS), cells were per­ meabilized with 0.1% Triton X­100 at 4°C for 5 min, washed again with PBS, and blocked with 3% bovine serum albumin (BSA). Primary antibodies were added to samples overnight at 4°C. After washing with PBS, secondary antibodies were added in 3% BSA for 30 min, and after washing with PBS, images were acquired on a Leica SP8 confocal microscope. DNA was counterstained with DAPI (1  g/ml).

## Transfection of GSDMD constructs in HEK293T cells

HEK293T cells were seeded the day before transfection at a density of 5 × 10  cells/ml. Transfection was done in Opti­MEM (Gibco) 5 using 2  g of DNA and 7  l of Lipofectamine 2000 (Thermo Fisher Scientific) for a six­well plate or respective scaling for other surface areas. LDC7559 or caspase inhibitors were added 2 hours after trans­ fection, and lactate dehydrogenase (LDH) release of cells was mea­ sured 16 hours after transfection.

## Incubation of HEK293T lysates with recombinant proteases

HEK293T cell lysate was harvested 16 hours after transfection by changing the medium of a six well to 200  l of Opti­MEM containing 0.05% (v/v) Triton X­100 and scraping cells off the bottom of the well. After 10 min of centrifugation at full speed and 4°C in a tabletop centrifuge, supernatants were used for cleav­ age assays. Fifty microliters of lysate were incubated with 10 mU of purified human NE (324681, Calbiochem), 2 U of recombinant caspase­4 (ab51994, Abcam), 4  g of purified CG (RP­77525, Thermo Fisher Scientific), or 6.25  g of recombinant PR3 (C628, Novoprotein) for the indicated time points at 25°C on a shaking incubator. Reactions were stopped by directly adding 50  l of 2× SDS loading buffer (at 98°C) containing 200 mM DTT and by im­ mediately boiling samples before loading on SDS-polyacrylamide gel electrophoresis gels.

## Immunofluorescence staining

Neutrophils were resuspended at 6.6 × 10  cells/ml in RPMI con­ 5 taining 0.02% human serum albumin and 10 mM Hepes, and 300  l of cell suspension was dropped into  ­Slide 8 Well glass­bottom dishes (ibidi). After 30 min, PMA was added. A pH shift fix was performed [3% PFA-K­Pipes (80 mM) (pH 6.8) for 5 min followed by 3% PFA­borax (100 mM) for 10 min]. CellTracker DiI or DiD (Life Technologies) was used at 1  M for 2 min to stain the mem­ brane, and cells were subsequently permeabilized using 0.1% Triton X­100 at 4°C for 2 min. Cells were then blocked (5% goat serum, 1% fish gelatin, 2% BSA) for 1 hour followed by incubation with pri­ mary antibody in 0.1% BSA at 4°C overnight, washed once, and then incubated with Alexa Fluor-coupled secondary antibodies (Life Technologies) at room temperature for 20 min. After three PBS washes and one incubation in distilled water for 20 min, cells were imaged in PBS using either Leica SP8 confocal microscopy or total internal reflection microscopy. DNA was counterstained with Hoechst (5  g/ml) or DAPI (1  g/ml).

## Total internal reflection microscopy

TIRF imaging was performed with a Nikon N­STORM microscope using a 100× (1.46 numerical aperture) oil immersion objective. Fixed neutrophils were imaged under TIRF illumination using a quad cube and the 488­ and 647­nm lasers. Fluorescence was collected using an Andor iXon EMCCD camera.

## TIRF microscopy quantification

To quantify GSDMD localization at the plasma membrane, a region of interest (ROI) outside of the cell, as demarcated by DiD, was captured for every image acquired, and the relative mean fluores­ cent intensity (MFI) of GSDMD in this region was calculated using ImageJ (ROI&gt;ANALYSE&gt;MEASURE). This value was defined as the background. The MFI of GSDMD was then calculated within the plasma membrane boundaries using DiD. The background MFI was multiplied by 2 and was used as a threshold to determine GSDMD positivity within the confines of the plasma membrane (MFI GSDMD within cell&gt;2× MFI background).

## Live imaging of neutrophils

Cells were resuspended in an assay medium supplemented with 500 nM SYTOX Green and 2.5  M DRAQ5 and seeded at a density of 5 × 10  cells per well into 5  ­Slide 8 Well ibiTreat dishes (ibidi). After LDC7559 treatment and NET induction, images were col­ lected at 2­min intervals on a Leica TCS SP8 confocal microscope equipped with a climate chamber at 37°C and with a Leica HC PL APO 20×/0.75 IMM CORR CS2 objective using glycerol immersion. The recording of DRAQ5 (cell­permeable DNA dye) was used to track individual nuclei over time and to determine nuclear area. The recording of SYTOX Green (cell­impermeable dye) was used to determine permeability of cells. Bright­field recording was added for a video representation of the data. Automated algorithms were used to determine the time point of permeabilization and to categorize nuclei into 'non­expanded,' 'fully expanded' (filling the entire cell), or 'NET' (extending beyond the maximal area of a cell). The results were then mapped back to a video represen­ tation of the data and manually inspected for accuracy before they were used for further analysis. The complete image analysis pipeline consisting of ImageJ and R scripts will be described else­ where in detail.

## SUPPLEMENTARY MATERIALS

immunology.sciencemag.org/cgi/content/full/3/26/eaar6689/DC1 Materials and Methods

Fig. S1. Screening strategy and titration curves.

Fig. S2. NET-inhibiting compound LDC7559 and its derivative bind to GSDMD.

Fig. S3. GSDMD cleavage and localization during NET formation.

Fig. S4. TIRF microscopy of NE during NET formation.

Fig. S5. NE processes GSDMD.

Fig. S6. Mode of action of LDC7559.

Fig. S7. Live-cell imaging of NET formation.

- Fig. S8. Model of GSDMD involvement in NET formation.
- Movie S1. Classification of cell states during NET formation.

Movie S2. PMA-induced NET formation.

Movie S3. PMA-induced NET formation in the presence of LDC7559.

Movie S4. Nigericin-induced NET formation.

Movie S5. Nigericin-induced NET formation in the presence of LDC7559.

Table S1. Raw data.

References ( 32 -34 )

## REFERENCES AND NOTES

- 1. H. N. Stephenson, A. Herzig, A. Zychlinsky, Beyond the grave: When is cell death critical for immunity to infection? Curr. Opin. Immunol. 38 , 59-66 (2016).
- 2. F. Martinon, K. Burns, J. Tschopp, The inflammasome: A molecular platform triggering activation of inflammatory caspases and processing of proIL-beta. Mol. Cell 10 , 417-426 (2002).
- 3. S. L. Fink, B. T. Cookson, Caspase-1-dependent pore formation during pyroptosis leads to osmotic lysis of infected host macrophages. Cell. Microbiol. 8 , 1812-1825 (2006).
- 4. N. Kayagaki, S. Warming, M. Lamkanfi, L. Vande Walle, S. Louie, J. Dong, K. Newton, Y. Qu, J. Liu, S. Heldens, J. Zhang, W. P. Lee, M. Roose-Girma, V. M. Dixit, Non-canonical inflammasome activation targets caspase-11. Nature 479 , 117-121 (2011).
- 5. J. Shi, Y. Zhao, Y. Wang, W. Gao, J. Ding, P. Li, L. Hu, F. Shao, Inflammatory caspases are innate immune receptors for intracellular LPS. Nature 514 , 187-192 (2014).
- 6. J. Shi, Y. Zhao, K. Wang, X. Shi, Y. Wang, H. Huang, Y. Zhuang, T. Cai, F. Wang, F. Shao, Cleavage of GSDMD by inflammatory caspases determines pyroptotic cell death. Nature 526 , 660-665 (2015).
- 7. N. Kayagaki, I. B. Stowe, B. L. Lee, K. O'Rourke, K. Anderson, S. Warming, T. Cuellar, B. Haley, M. Roose-Girma, Q. T. Phung, P. S. Liu, J. R. Lill, H. Li, J. Wu, S. Kummerfeld, J. Zhang, W. P. Lee, S. J. Snipas, G. S. Salvesen, L. X. Morris, L. Fitzgerald, Y. Zhang, E. M. Bertram, C. C. Goodnow, V. M. Dixit, Caspase-11 cleaves gasdermin D for non-canonical inflammasome signaling. Nature 526 , 666-671 (2015).
- 8. X. Liu, Z. Zhang, J. Ruan, Y. Pan, V. G. Magupalli, H. Wu, J. Lieberman, Inflammasomeactivated gasdermin D causes pyroptosis by forming membrane pores. Nature 535 , 153-158 (2016).
- 9. R. A. Aglietti, A. Estevez, A. Gupta, M. G. Ramirez, P. S. Liu, N. Kayagaki, C. Ciferri, V. M. Dixit, E. C. Dueber, Gsdmd p30 elicited by caspase-11 during pyroptosis forms pores in membranes. Proc. Natl. Acad. Sci. U.S.A. 113 , 7858-7863 (2016).
- 10. J. Ding, K. Wang, W. Liu, Y. She, Q. Sun, J. Shi, H. Sun, D.-C. Wang, F. Shao, Pore-forming activity and structural autoinhibition of the gasdermin family. Nature 535 , 111-116 (2016).
- 11. L. Sborgi, S. Rühl, E. Mulvihill, J. Pipercevic, R. Heilig, H. Stahlberg, C. J. Farady, D. J. Müller, P. Broz, S. Hiller, GSDMD membrane pore formation constitutes the mechanism of pyroptotic cell death. EMBO J. 35 , 1766-1778 (2016).
- 12. V. Brinkmann, U. Reichard, C. Goosmann, B. Fauler, Y. Uhlemann, D. S. Weiss, Y. Weinrauch, A. Zychlinsky, Neutrophil extracellular traps kill bacteria. Science 303 , 1532-1535 (2004).
- 13. S. K. Jorch, P. Kubes, An emerging role for neutrophil extracellular traps in noninfectious disease. Nat. Med. 23 , 279-287 (2017).
- 14. M. J. Kaplan, M. Radic, Neutrophil extracellular traps: Double-edged swords of innate immunity. J. Immunol. 189 , 2689-2695 (2012).
- 15. E. F. Kenny, A. Herzig, R. Krüger, A. Muth, S. Mondal, P. R. Thompson, V. Brinkmann, H. V. Bernuth, A. Zychlinsky, Diverse stimuli engage different neutrophil extracellular trap pathways. eLife 6 , e24437 (2017).
- 16. B. Amulic, S. L. Knackstedt, U. Abu Abed, N. Deigendesch, C. J. Harbort, B. E. Caffrey, V. Brinkmann, F. L. Heppner, P. W. Hinds, A. Zychlinsky, Cell-cycle proteins control production of neutrophil extracellular traps. Dev. Cell 43 , 449-462.e5 (2017).
- 17. A. Hakkim, T. A. Fuchs, N. E. Martinez, S. Hess, H. Prinz, A. Zychlinsky, H. Waldmann, Activation of the Raf-MEK-ERK pathway is required for neutrophil extracellular trap formation. Nat. Chem. Biol. 7 , 75-77 (2011).
- 18. K. D. Metzler, C. Goosmann, A. Lubojemska, A. Zychlinsky, V. Papayannopoulos, A myeloperoxidase-containing complex regulates neutrophil elastase and actin dynamics during NETosis. Cell Rep. 7 , 883-896 (2014).

|

## SCIENCE IMMUNOLOGY  RESEARCH ARTICLE

|

- 19. V. Papayannopoulos, K. D. Metzler, A. Hakkim, A. Zychlinsky, Neutrophil elastase and myeloperoxidase regulate the formation of neutrophil extracellular traps. J. Cell Biol. 191 , 677-691 (2010).
- 20. A. Warnatsch, M. Ioannou, Q. Wang, V. Papayannopoulos, Neutrophil extracellular traps license macrophages for cytokine production in atherosclerosis. Science 349 , 316-320 (2015).
- 21. T. A. Fuchs, U. Abed, C. Goosmann, R. Hurwitz, I. Schulze, V. Wahn, Y. Weinrauch, V. Brinkmann, A. Zychlinsky, Novel cell death program leads to neutrophil extracellular traps. J. Cell Biol. 176 , 231-241 (2007).
- 22. K. S. Schneider, C. J. Groß, R. F. Dreier, B. S. Saller, R. Mishra, O. Gorka, R. Heilig, E. Meunier, M. S. Dick, T. Ć ikovi ć , J. Sodenkamp, G. Médard, R. Naumann, J. Ruland, B. Kuster, P. Broz, O. Groß, The inflammasome drives GSDMD-independent secondary pyroptosis and IL-1 release in the absence of caspase-1 protease activity. Cell Rep. 21 , 3846-3859 (2017).
- 23. Q. Remijsen, T. Vanden Berghe, E. Wirawan, B. Asselbergh, E. Parthoens, R. De Rycke, S. Noppen, M. Delforge, J. Willems, P. Vandenabeele, Neutrophil extracellular trap cell death requires both autophagy and superoxide generation. Cell Res. 21 , 290-304 (2011).
- 24. E. Gasteiger, C. Hoogland, A. Gattiker, S. Duvaud, M. R. Wilkins, R. D. Appel, A. Bairoch, Protein identification and analysis tools on the ExPASy server, in The Proteomics Protocols Handbook , J. M. Walker, Ed. (Humana Press, 2005), pp. 571-607.
- 25. H. Kambara, F. Liu, X. Zhang, P. Liu, B. Bajrami, Y. Teng, L. Zhao, S. Zhou, H. Yu, W. Zhou, L. E. Silberstein, T. Cheng, M. Han, Y. Xu, H. R. Luo, Gasdermin D exerts anti-inflammatory effects by promoting neutrophil death. Cell Rep. 22 , 2924-2936 (2018).
- 26. C. Rogers, T. Fernandes-Alnemri, L. Mayes, D. Alnemri, G. Cingolani, E. S. Alnemri, Cleavage of DNFA5 by caspase-3 during apoptosis mediates progression to secondary necrotic/pyroptotic cell death. Nat. Commun. 3 , 14128 (2017).
- 27. Y. Wang, W. Gao, X. Shi, J. Ding, W. Liu, H. He, K. Wang, F. Shao, Chemotherapy drugs induce pyroptosis through caspase-3 cleavage of a gasdermin. Nature 547 , 99-103 (2017).
- 28. K. W. Chen, M. Monteleone, D. Boucher, G. Sollberger, D. Ramnath, N. D. Condon, J. B. von Pein, P. Broz, M. J. Sweet, K. Schroder, Noncanonical inflammasome signaling elicits gasdermin D-dependent neutrophil extracellular traps. Sci. Immunol. 3 , eaar6676 (2018).
- 29. M. J. Losman, T. M. Fasy, K. E. Novick, M. Monestier, Monoclonal autoantibodies to subnucleosomes from a MRL/Mp(-)+/+ mouse. Oligoclonality of the antibody response and recognition of a determinant composed of histones H2A, H2B, and DNA. J. Immunol. 148 , 1561-1569 (1992).
- 30. F. Von Nussbaum, V. M. Li, S. Allerheiligen, S. Anlauf, L. Bärfacker, M. Bechem, M. Delbeck, M. F. Fitzgerald, M. Gerisch, H. Gielen-Haertwig, H. Haning, D. Karthaus, D. Lang, K. Lustig, D. Meibom, J. Mittendorf, U. Rosentreter, M. Schäfer, S. Schäfer, J. Schamberger, L. A. Telan, A. Teerstegen, Freezing the bioactive conformation to boost potency: The identification of BAY 85-8501, a selective and potent inhibitor of human neutrophil elastase for pulmonary diseases. ChemMedChem 10 , 1163-1173 (2015).

- 31. M. Swamydas, Y. Luo, M. E. Dorf, M. S. Lionakis, Isolation of mouse neutrophils. Curr. Protoc. Immunol. 110 , 3.20.1-3.20.15 (2015).
- 32. J. E. Elisa, W. Haas, B. K. Faherty, S. P. Gygi, Comparative evaluation of mass spectrometry platforms used in large-scale proteomics investigations. Nat. Methods 2 , 667-675 (2005).
- 33. J. Cox, M. Mann, MaxQuant enables high peptide identification rates, individualized p.p.b.-range mass accuracies and proteome-wide protein quantification. Nat. Biotechnol. 26 , 1367-1372 (2008).
- 34. S. Wind, K. Beuerlein, T. Eucker, H. Müller, P. Scheurer, M. E. Armitage, H. Ho, H. H. Schmidt, K. Wingler, Comparative pharmacology of chemically distinct NADPH oxidase inhibitors. Br. J. Pharmacol. 161 , 885-898 (2010).

Acknowledgments: We thank our colleagues for neutrophil preparation and for their help to facilitate the NET formation project. We thank the Advanced Medical BioImaging Core Facility (Charité Universitätsmedizin Berlin) for the use of their facilities. We further thank S. Müller (Evotec Martinsried) for expert liquid chromatography-tandem MS data generation, M. Bickle (MPI Cell Biology, Dresden) for screening analysis, and B. Raupach for reading and commenting on the manuscript. Funding: G.S. was funded by an Advanced Postdoc.Mobility grant from the Swiss National Science Foundation. This project was funded by the Max Planck Society. Author contributions: G.S., B.K., and A.Z. designed the study. A.C., P.H., S.M., and J.E. designed, performed, and analyzed high-throughput screening. B.K. and A.C. designed target identification strategy and triaging of compounds. S.K. performed affinity chromatography experiments. R.D.L., A.C., B.K., and P.N. designed and synthesized compounds. R.K. contributed medical expertise. G.S., G.L.B., and A.H. performed experiments and analyzed data. G.S. and A.Z. wrote the manuscript. Competing interests: G.S., B.K., and A.Z. are involved in a patent application. G.S. and A.Z. are inventors on priority application submitted by the Max Planck Society. A.Z. is a shareholder and consultant in Quench Bio Inc., a start-up company funded by Atlas Venture and Arix Bioscience. Data and materials availability: All live-cell imaging data sets generated will be available from the corresponding author upon reasonable request. Data from the chemical library screen will not be publicly available yet due to ongoing analysis of hit compounds.

Submitted 5 December 2017 Accepted 16 July 2018 Published 24 August 2018 10.1126/sciimmunol.aar6689

Citation: G. Sollberger, A. Choidas, G. L. Burn, P. Habenberger, R. Di Lucrezia, S. Kordes, S. Menninger, J. Eickhoff, P. Nussbaumer, B. Klebl, R. Krüger, A. Herzig, A. Zychlinsky, Gasdermin D plays a vital role in the generation of neutrophil extracellular traps. Sci. Immunol. 3 , eaar6689 (2018).

<!-- image -->

## Gasdermin D plays a vital role in the generation of neutrophil extracellular traps

Menninger, Jan Eickhoff, Peter Nussbaumer, Bert Klebl, Renate Krüger, Alf Herzig and Arturo Zychlinsky Gabriel Sollberger, Axel Choidas, Garth Lawrence Burn, Peter Habenberger, Raffaella Di Lucrezia, Susanne Kordes, Sascha

DOI: 10.1126/sciimmunol.aar6689 , eaar6689. 3 Sci. Immunol.

## Casting NETs

. report necrosulfonamide to be an inhibitor of GSDMD. et al in NETosis, and Rathkey . also report a role for GSDMD et al molecule that binds GSDMD to be an inhibitor of NETosis. In the same issue, Chen based -. identified a pyrazolo-oxazepine scaffold et al screen to identify molecules that block NETosis, Sollberger and antimicrobial proteins and are cast by dying neutrophils in a process termed NETosis. While carrying out a chemical activated in neutrophils, during the generation of neutrophil extracellular traps (NETs). NETs are composed of chromatin . demonstrate that GSDMD is et al of cell death induced by intracellular lipopolysaccharide (LPS). Here, Sollberger Gasdermin D (GSDMD), a pore-forming protein, has emerged as a key downstream effector in pyroptosis, a form

ARTICLE TOOLS

MATERIALS SUPPLEMENTARY

REFERENCES

http://immunology.sciencemag.org/content/3/26/eaar6689

http://immunology.sciencemag.org/content/suppl/2018/08/21/3.26.eaar6689.DC1

http://immunology.sciencemag.org/content/3/26/eaar6689#BIBL This article cites 33 articles, 9 of which you can access for free

Terms of Service Use of this article is subject to the

a registered trademark of AAAS. is Science Immunology Association for the Advancement of Science. No claim to original U.S. Government Works. The title New York Avenue NW, Washington, DC 20005. 2017 ' The Authors, some rights reserved; exclusive licensee American (ISSN 2470-9468) is published by the American Association for the Advancement of Science, 1200 Science Immunology