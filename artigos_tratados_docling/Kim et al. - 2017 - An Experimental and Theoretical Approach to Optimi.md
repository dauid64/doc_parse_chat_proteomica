<!-- image -->

## ORIGINAL ARTICLE

## An Experimental and Theoretical Approach to Optimize a Three-Dimensional Clinostat for Life Science Experiments

Sun Myong Kim 1

· Hyunju Kim 2 · Dongmin Yang 2 · Jihyung Park 3 ·

Sim Namkoong 2 · Jin I. Lee 2 · Inho Choi 2 ·

Rackhyun Park 2 · Han-Sung Kim 3 · Hyoungsoon Kim 4 · Junsoo Park 2

Received: 15 September 2015 / Accepted: 11 December 2016 / Published online: 27 December 2016 'Springer Science+Business Media Dordrecht 2016

Abstract Gravity affects all biological systems, and various types of platforms have been developed to mimic microgravity on the Earth's surface. A three-dimensional clinostat (3D clinostat) has been constructed to reduce the directionality of gravitation. In this report, we attempted to optimize a 3D clinostat for a life science experiment. Since a 3D clinostat is equipped with two motors, we fixed the angular velocity of one (primary) motor and varied it for the other (secondary) motor. In this condition, each motor ran constantly and continuously in one direction during the experiment. We monitored the direction of the normal vector using a 3D acceleration sensor, and also performed a computer simulation for comparison with the experimental data. To determine the optimal revolution for our life science experiment (i.e., a revolution yielding the strongest effects), we examined the promoter activity of two genes that were reported to be affected by microgravity. We found

Sun Myong Kim, Hyunju Kim and Dongmin Yang are contributed equally to this work.

- /envelopeback Hyoungsoon Kim hkim2@yonsei.ac.kr
- /envelopeback Junsoo Park junsoo@yonsei.ac.kr
- 1 Department of Physics, Yonsei University, Wonju, 220-710, South Korea
- 2 Division of Biological Science and Technology, Yonsei University, Wonju, 220-710, South Korea
- 3 Department of Biomedical Engineering, Yonsei University, Wonju, 220-710, Korea
- 4 Department of Mathematics, Yonsei University, Wonju, 220-710, South Korea

that the ratio of velocity of 4:1.8 (0.55) was optimal for our biological system. Our results indicate that changes of the revolutions of a 3D clinostat have a direct impact on the result and furthermore that the revolutions of the two motors have to be separately adjusted in order to guarantee an optimal simulation of microgravity.

Keywords Microgravity · Clinostat · Optimization · Life science

## Introduction

Gravity is one of the fundamental forces in nature and affects every living organism on earth. For this reason, gravity has been rarely regarded as an experimental parameter in the study of life science except in gravitational biology. Even so, the effect of microgravity on biological systems is not completely understood (Becker, Souza 2013). Recently, several studies reported that prolonged exposure to microgravity in space effects several physiological phenomena such as bone loss and muscle atrophy (Tamma et al. 2009; Vandenburgh et al. 1999). These studies indicate that gravity is an important parameter for biological studies. Access to space is expensive and also limited. Therefore, many attempts have been undertaken to mimic microgravity on earth (Herranz et al. 2013; Brungs et al. 2016). The rat hindlimb unloading model has been used to study various aspects of musculoskeletal loading (Morey-Holton, Globus 2002). Recently, magnetic levitation was applied to simulate microgravity conditions by counterbalancing the gravitational force by a magnetic force Hammer et al. (2009). However, exposing cells revealed that the effects of the magnetic field itself have to be discussed (Hemmersbach et al. 2014). The clinostat and the random positioning

machine are further approaches to simulate microgravity in cell culture systems (Becker, Souza 2013). On Earth, gravity has directionality, and clinostats and random positioning machines can effectively reduce this directionality by rotating an object. A 3D clinostat is equipped with two independent rotating axes to disperse the directionality of gravity. Random Positioning Machine (RPM) was also developed and used to simulate microgravity (Hoson et al. 1992; Borst, van Loon 2009). The directionality of gravity is randomized by continuously changing the speed of rotation of the two frames at random (3D clinostat) or -additionally - with randomized direction (RPM). In contrast, a two-dimensional (2D) clinostat rotates around one single axis perpendicular to the gravity vector. Special care has been taken to keep the effective diameter of the sample and consequently the residual accelerations at a minimum (Brungs et al. 2016).

The possibility to simulate microgravity to at least some extent on ground has been accepted by the scientific community; however comparative studies and careful discussion of side effects have to be taken into account (Ryu et al. 2014; Takeda et al. 2009; Becker, Souza 2013).

Simulated microgravity obtained by different experimental approaches affects several cellular processes. For example, simulated microgravity affects cell proliferation and apoptosis (RPM and 2D-clinostat) (Grimm et al. 2002; Kang et al. 2011) and cellular differentiation (3D-clinostat) (Yuge et al. 2003; Yuge et al. 2006). Few studies have been performed to obtain the least gravitational effects on a biological systems and random positioning machines (Russomano et al. 2005; Borst, van Loon 2009; Hoson et al. 1992). Since a 3D clinostat is equipped with two axes, varying the rotational speed of each motor can affect the motion and the dispersion of gravity. In this study, we monitored the direction of the normal vector using a 3D acceleration sensor, and also performed a computer simulation for comparison to the experimental data.

## Materials and Methods

## Cell culture and reporter assay

The human kidney cell line HEK293 was grown in Dulbecco's modified Eagle medium (DMEM) supplemented with 10 % fetal bovine serum. Transfection of the HEK293 cells was performed using lipofectamine (Invitrogen, Carlsbad, CA, USA). For the reporter assay, cells were seeded in 24-well plates in DMEM 18 h prior to transfection. The total DNA for the transfection was typically 0.5 µ g per well, and each assay was normalized with renilla luciferase activity. Each plate was sealed with the cover glass and 3M tape to avoid the leakage of the medium.

## Three-dimensional clinorotation and gravity monitoring

The 3D clinostat was designed by Prof. Han-Sung Kim (Yonsei University, Korea) and the sample stage was rotated with two independent axes at the indicated angular velocity (rpm - revolutions per minute) (Fig. 1A). The entire system was placed in a CO2 incubator set at 37 · C, control cells also in the incubator, however without rotation. To monitor the dispersion of gravity, the accelerometer of a Galaxy S (Samsung, Seoul, Korea) was used. The dispersed gravity was monitored and visualized by Microsoft Excel software (Microsoft, Redmond, WA, USA).

## Computer simulation of a three dimensional clinostat motion

The required experimental environment can be obtained using a 3D clinostat equipped with two rotational axes, which are orthogonal to each other with possible independent angular velocities. We will briefly describe a theoretical analysis of the situation. Let us consider an arbitrary vector A. When this vector is located at the origin of the /vector coordinate system that rotates with an angular velocity /vector ω , then the vector changes in time as

<!-- formula-not-decoded -->

The angular velocity /vector ω in our experimental setup consists of two angular velocities with each angular velocity component from an independent rotation:

<!-- formula-not-decoded -->

Here we chose /vector ω ' and /vector ω '' to represent the rotation around the z-axis in the coordinate system S, which is at rest on Earth, and the rotation around the x -axis in the coordinate system ' S , which rests on the z-axis rotating system, respectively. '

Consider the rotation with angle ϕ around the z-axis. The matrix form of the corresponding rotation around the z-axis from S to S ' can be expressed as

<!-- formula-not-decoded -->

The resulting unit vectors in the rotated frame can also be expressed in matrix form as

<!-- formula-not-decoded -->

A

<!-- image -->

<!-- image -->

## 3D acceleration sensor

Fig. 1 3D acceleration sensor can monitor the dispersion of gravity. A Photograph of our 3D clinostat (top panel) and the schematic diagram of the 3D acceleration sensor (bottom panel). By rotation, the directionality of gravitation is dispersed into x-, y-, and z-components. B The 3D acceleration sensor is installed on the plate of the 3D clinostat

<!-- image -->

We have the following relationships for the systems S and S : '

<!-- formula-not-decoded -->

where e1, e2, and e3 ˆ ˆ ˆ are the unit vectors in the directions of the x-, y-, and z-axes, respectively, of system S, and e ˆ ' 1 , ˆ ' e , 2 and e ˆ ' 3 are the unit vectors in the directions of the x -, y -, ' ' and z -axes, respectively, of system S . ' '

[Note that the sub-indices 1, 2, and 3 represent the x, y, and z coordinates, respectively, in the corresponding coordinate system. We also need to be careful about the fact that ˆ ' e k (k = 1 2 3 , , ) is time-dependent.]

From the definition of the angular velocity ω ' , which is constant for the initial condition, ϕ = 0 at t = 0, we can write ϕ as

<!-- formula-not-decoded -->

Since any vector can be expressed in terms of unit vectors in the coordinate system, we can write /vector ω ' and /vector ω '' in their respective coordinate systems:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

to monitor gravity, and the directionality of gravity, expressed as x-, y-, and z-components is shown in the 3D graph. When the clinostat is fixed, the sensor indicates a single spot (top panel). When the clinostat is rotated around a single axis, the sensor produces a circular pattern

Therefore, we can express the final form of the angular velocity /vector ω as

<!-- formula-not-decoded -->

Note that ω ' and ω '' are constants in our experiment.

The normal direction of the sample in the experiment changes during the rotational motion of the base of the sample. We represent the normal direction as the vector A. We /vector will also call this vector the 'normal vector'. For the given vector A /vector = ( A1A2A3 , we have the following equation: )

<!-- formula-not-decoded -->

This is a vector equation and dA /vector / dt contains the following three equations to solve.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The solutions to these equations give the trace of the unit vector, which has the normal direction of the sample. Unfortunately, these equations cannot be solved analytically. We attempted to solve /vector A t ( ) numerically using Mathematica (Wolfram Research, Champaign, IL, USA).

To test the changes in the direction of the normal vector numerically in Mathematica , we needed to choose the ratio of the angular velocities of ω ' to ω '' . Choosing the appropriate ratio of the angular velocities is very important, since the coverage of the solid angle by the normal vector depends on it. We traced the normal vector for several values of the ratio. We draw the trace using Mathematica and compared it to what we found in the experiment, confirming that the two traces were identical.

Next, we needed a good criterion to judge which rotation ratio produces the best non-directionality. One may demand that the normal vector should vary over the range of largest possible angles for a cycle. To check whether the vector achieves such a goal, we introduced the following three variables representing the integration of each coordinate of normal vector components over a time t,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

∣ ∣ where x, y, and z are the coordinates of the normal vectors. When any of h values becomes smaller for a given time t, say a period, the non-directionality would be better in the direction of the axis. To measure the non-directionality in all three directions, we propose to calculate the following value for each of the chosen rotation ratios:

<!-- image -->

We also calculated the maximum value of these functions simultaneously for an additional check:

Max hi [ ( ) t ] and

<!-- formula-not-decoded -->

## Results

## 3D acceleration sensor can monitor the dispersion of gravity

To optimize a 3D clinostat for life science studies, we developed a system to monitor the dispersion of gravity. We

introduced the normal vector of the sample, which is represented in terms of x, y, and z coordinates during rotation. A mobile apparatus containing a 3D acceleration sensor was installed in the 3D clinostat, and we monitored the dispersion of gravity from the normal vector (Fig. 1A). The 3D acceleration sensor data were recorded as x, y, and z components and these data were used to draw a 3D graph. When the 3D clinostat was fixed, the sensor output was not changed, and the data were changed by shifting the clinostat's position (Fig. 1B, top panel). Next, we monitored the normal vector while rotating one motor and plotted the graph with the measured data (Fig. 1B, bottom panel). The rotation with one motor shows a flat round pattern, and the rotation with the other motor shows the same round pattern with a shifted axis (Fig. 1B, bottom panel). These results indicate that our 3D acceleration sensor can monitor the normal vector representing the dispersion of gravity in the clinostat.

Since the 3D clinostat is equipped with two motors, changing the rotational speed produces a different pattern of movement due to the variations in the normal vector. Thus, we could monitor the dispersion of the normal vector by varying the revolutions and observed the variations in the graph from the measured data. Various patterns of graphs were obtained by changing the revolutions of the 3D clinostat, and each pattern was unique (Fig. 2). Equal revolutions (4:4 or 1:1), which are commonly used in many 3D clinostat experiments resulted in a simple pattern, and the trace of the normal vector was concentrated on one side of the sphere (Fig. 2). While the cases of simple ratios such as 4:4, 4:3, 4:2, and 4:1 showed relatively simple patterns, the patterns with ratios of 4:3.4, 4:2.6, 4:2.2, 4:1.8, 4:0.6 and 4:0.2 showed widely distributed patterns covering almost an entire sphere. Because these graphs indicate the trace of the normal vector, the widely distributed patterns imply that gravity was widely dispersed.

## The computer simulation data are consistent with the experimental data

Since we obtained the graph from the 3D acceleration sensor, the gravitation vector data and the gravity patterns are dependent on the accuracy of the clinostat. If the machine did not rotate precisely, the data could be meaningless. We wanted to confirm that the 3D clinostat rotated precisely. We compared the pattern of the gravity dispersion from the experiment with the ones from the computer simulation. The computer simulation pattern matched the experimental data well. Equal revolutions (4:4) produced a saddle shape in both the computer simulation and the experiment (Fig. 3, i) and the ratios such as 4:3 or 4:2 produced the same characteristic patterns in both trials (Fig. 3 v, vii). These results

Fig. 2 A 3D clinostat can produce different patterns of motion by varying the revolution. The rotational speed of the primary axis was fixed, while the speed of the second axis varied as shown in the figure. The data of the 3D acceleration sensor were recorded for five minutes and are shown in the 3D graph

<!-- image -->

support that our 3D clinostat works precisely as predicted in the computer simulation.

## Optimization of a 3D clinostat

As the clinostat was developed to reduce the directionality of gravitation-by rotation, we examined the accumulation value of the gravity vector. When 1 g ( = 9.8 m/s 2 ) exists, the accumulation value of the gravity vector will increase in a timedependent manner. When the clinostat rotates with a single axis, the accumulation value of the gravity vector will become zero after one period of rotation. For this reason, the smaller the accumulation value of the gravity vector is, the less is the directionality of gravity. We calculated the accumulation values of the gravity vector from the computer simulation, and these data are presented as a graph (Fig. 4) and a table (Table 1). Table 1 shows how the numerical values of the ratio play roles

in the simulation. We calculated 'the length of the curve', 'maximum values of h1, h2,h3,' 'Max ∑ 3 i = 1 hi ( ) t ,' and ' ∫ 5 0 ∑ 3 i = 1 hi ( ) t dt' to find the best ratio. We used revolutions per minute as the unit for the numerical values of angular velocities.

Since the changes in the revolution produce diverse patterns of the gravity dispersion and the cumulative values of the gravity vector, we attempted to optimize the 3D clinostat with these parameters. When we compared the cumulative values of the gravity vector in various revolution ratios from the experiments, the values of the equal revolution relation increased, but the other values were similar (Fig. 4A). Next, we calculated the maximum cumulative values of the gravity vector during 5 min by computer simulation. The maximum value graph is U shaped, and the maximum value at 4:2 is minimal (Fig. 4B). These data suggest that a 3D clinostat with a revolution ratio of around 4:2 shows a lower cumulative value of the gravity vector.

Fig. 3 The computer simulation data are consistent with the data from the experimental trials. Computer simulation data with the different revolution ratios were generated by the Mathematica software, and

<!-- image -->

the cumulative values of the gravity vector were calculated ( Simulation, left panel ). The experimental values were recorded and calculated ( Sensor, right panel )

## Application of the optimal data for the life science study

Previous studies showed that the cell cycle inhibitor p21 transcription and the NFκ B dependent transcription are affected by simulated microgravity (Coinu et al. 2006; Cotrupi et al. 2005; Thiel et al. 2012). Because we generated various conditions for the simulated microgravity approach with our 3D clinostat, we examined the activity of these promoters using a reporter assay. HEK293 cells were transfected with the reporter plasmid containing either the p21 promoter (WWP-Luc) or the NFκ B dependent promoter (pELAM-Luc), and the transfected cells were subjected to clinorotation for 24 h. While the transcription activity of these promoters was slightly increased (about 10 %) by 3D clinorotation at 4:4, the activity was markedly increased (about 40 %) by clinorotation at 4:1.8 rpm (Figs. 5A and

5B). It is quite striking that both promoters showed higher values at 4: 1.8 rpm ratio than at other ratios. These results suggest that a revolution ratio of 4:1.8 result in the highest change in activity, and we suggest that this condition is optimal to simulate microgravity with a 3D clinostat for our chosen test system.

## Discussion

Although space is the ideal place to perform an experiment to study the effects of microgravity on a biological system, access to it is very limited. One way to get around this limitation is to find a method to simulate the microgravity effects on earth (Herranz et al. 2013). Among a few apparatuses developed to accomplish this, a 3D clinostat seems to

Fig. 4 The dispersion of gravity with equal rotational speeds (4:4) of both rotors was worse than with different ratios of revolutions. A Cumulative values of the gravity vector with different revolutions. The

<!-- image -->

numerical values of the revolution ratio (4:4) were increasing. B Maximum values of the cumulative gravity vector with different rotational speeds over 5 min

be suitable, since it is relatively easy to operate and allows an incubation of biological samples for a long period of time With our 3D clinostat system, we contribute to optimize experimental conditions to simulate microgravity and thus extrapolate the impact of gravity on cellular responses.

The previously mentioned theoretical analysis of our 3D clinostat system enabled us to calculate the dispersion of gravity and to compare them to the experimental results. The simulated pattern from the trace of the normal vector on the arbitrary normalized sphere is almost identical to the experimental result (Fig. 3). This result confirms that the 3D clinostat was operating precisely according to the theoretical analysis.

Each of the two motors of our 3D clinostat can regulate the movement of the normal vector. For simplicity, we fixed the rotational speed (angular velocity) of one (primary) motor and varied the speed of the other one. Fast rotation can produce strong shear stresses on the cells. For example,

when we incubated the cells with 20 rpm of clinorotation within a radius of 1.75 cm, the cells were detached from the plate and their viability was significantly diminished (data not shown). In contrast, low rotational speed cannot increase the dispersion of gravity efficiently. In this experiment, we used 4 rpm as the rotational speed of the primary axis for the cell culture, and the cell viability was not reduced significantly (data not shown). However, the proper speed of rotation should be adjusted depending on the types of cells and the various experimental situations.

To monitor the motion of the normal vector, we used a 3D acceleration sensor, which detected the x-, y-, and z-components of the gravitational acceleration of the vector. We obtained a corresponding 3D graph visualizing the trace of the normal vector on a sphere, since the sum of the squares of each component of the vector remained constant. The clinorotations with some integer ratios (of the rotational speed around the primary rotational axis to that

Table 1 All values are for 5 minutes

|   Frequency around z-axis ( ω ' ) (RPM) |   Frequency around x-axis ( ω '' ) (RPM) |   Length of curve |   Maxh1 t ( ) ( × 10 - 3 ) |   Maxh2 t ( ) ( × 10 - 3 ) |   Maxh3 t ( ) ( × 10 - 3 ) |   Max 3 ∑ i = 1 hi ( ) t ( × 10 - 3 ) |   ∫ 5 0 3 ∑ i = 1 hi ( ) t dt( × 10 - 3 |
|-----------------------------------------|------------------------------------------|-------------------|----------------------------|----------------------------|----------------------------|---------------------------------------|-----------------------------------------|
|                                       4 |                                      0.2 |             80.49 |                         40 |                         42 |                        796 |                                   854 |                                    2696 |
|                                       4 |                                      0.4 |             81.67 |                         40 |                         44 |                        398 |                                   457 |                                    1433 |
|                                       4 |                                      0.6 |             83.4  |                         41 |                         47 |                        265 |                                   329 |                                    1018 |
|                                       4 |                                      0.8 |             85.58 |                         39 |                         42 |                        199 |                                   246 |                                     807 |
|                                       4 |                                      1   |             88.14 |                         42 |                         50 |                        159 |                                   226 |                                     695 |
|                                       4 |                                      1.2 |             91.05 |                         44 |                         56 |                        133 |                                   207 |                                     627 |
|                                       4 |                                      1.4 |             94.27 |                         45 |                         61 |                        114 |                                   194 |                                     583 |
|                                       4 |                                      1.6 |             97.75 |                         45 |                         64 |                         99 |                                   185 |                                     555 |
|                                       4 |                                      1.8 |            101.47 |                         50 |                         72 |                         88 |                                   181 |                                     544 |
|                                       4 |                                      2   |            105.41 |                         53 |                         64 |                         80 |                                   171 |                                     521 |
|                                       4 |                                      2.2 |            109.54 |                         57 |                         88 |                         72 |                                   184 |                                     556 |
|                                       4 |                                      2.4 |            113.84 |                         59 |                         99 |                         66 |                                   177 |                                     578 |
|                                       4 |                                      2.6 |            118.3  |                         69 |                        113 |                         61 |                                   203 |                                     622 |
|                                       4 |                                      2.8 |            122.91 |                         78 |                        132 |                         57 |                                   221 |                                     684 |
|                                       4 |                                      3   |            127.64 |                         91 |                        152 |                         53 |                                   247 |                                     775 |
|                                       4 |                                      3.2 |            132.48 |                        105 |                        193 |                         49 |                                   285 |                                     928 |
|                                       4 |                                      3.4 |            137.43 |                        143 |                        265 |                         47 |                                   370 |                                    1192 |
|                                       4 |                                      3.6 |            142.47 |                        209 |                        395 |                         44 |                                   527 |                                    1723 |
|                                       4 |                                      3.8 |            147.6  |                        408 |                        795 |                         42 |                                  1006 |                                    3343 |
|                                       4 |                                      4   |            152.81 |                       2500 |                         20 |                         40 |                                  2537 |                                    6426 |

of the secondary axis) of 4:4 or 4:2 covered only part of the sphere, while the ratio of 4:1.8 covered most of the sphere. The coverage of a wider region of the sphere (a larger solid angle of the sphere) indicates that gravity is more evenly dispersed. When the clinorotation covers a limited region (small solid angle) of the sphere, the normal vector moves in the specific region for a short time, resulting in a biased dispersion rather than a uniform dispersion. We introduced the cumulative values (hi ) of gravity vector mentioned earlier in this report as one way of checking this mechanism. Next, we compared the maximum cumulative values of gravity vector over a 5-min period. The theoretical values were the largest for the case of the rpm ratios of 4:4 or 1:1. This suggests that the rotation with the 4:4 rpm ratio is not a good choice for the dispersion of gravity. Among the many ratios evaluated, the theoretical data suggest that the rpm ratios of 4:2 or 1:0.5 showed the smallest cumulative values. The cumulative value of the trace helps one to choose better ratios of rotational speed without doing experiments. Therefore, it is a good criterion to find an appropriate rotation speed ratio for the dispersion of gravity, although it is not an absolute one. Finding a more mathematically solid criterion is needed and we leave it for future work.

After performing the theoretical and experimental analyses, we decided to perform additional fine-tuning tests on the biological system with the 3D clinostat operating at different revolutions. The reporter assay using luciferase is very sensitive and is commonly used to study cell signaling (Park et al. 2007; Chae et al. 2008). The results were quite surprising, and the case of the revolution ratio of 4:1.8 showed the best simulated results. There are several clues to explain the results. The revolution ratios around 4:2 showed the smallest values of cumulative gravity vector. However, the trace of the normal vector for the ratio of 4:2.0 covers only part of the sphere, while that for the ratio of 4:1.8 covers most of the sphere. For this reason, it is assumed that this ratio, 4:1.8 produces the best simulated microgravity. We still question why the revolution of 4:2.2 would show a similar behavior but produce inferior results (Fig. 5). The cumulative value alone cannot pinpoint the optimal ratio, and a further modification of this method will be needed, although it greatly reduces the number of experiments required.

For preparing the spaceflight experiments, ground-based simulators of microgravity are valuable tools, however they have some limitations (Herranz et al. 2013; Brungs et al.

<!-- image -->

Fig. 5 Optimization of our 3D clinostat by using a biological system. HEK293 cells were transfected with the reporter plasmids containing either the p21 (WWP) promoter ( A ) or the pELAM promoter ( B ). 24 h hours after transfection, cells were subjected to the clinorotation for 24 h, the clinostat was stopped and the cells were then lysed for the luciferase assay. Renilla luciferase was used to measure the transfection efficiency, and the relative luciferase activity is shown in the graphs. The experiments were performed in triplicate, and the mean and standard deviations are shown. Control vs 3D clinostat, NS; non-specific, * P &lt; 0.05, ** P &lt; 0.01

<!-- image -->

2016). In contrast to a 3D clinostat, it is very difficult to design an RPM which can provide repeatable and reproducible conditions due to the random movement (Borst, van Loon 2009). In addition, a RPM may produce unwanted vibration and acceleration due to the continuous change of rotational speed. In this study, we did not perform the experiments with a RPM or a clinostat with one axis, and further work will be required for comparative studies. In addition, the experimental results under simulated microgravity should be confirmed in real microgravity. Our study clearly demonstrates that adjustment of the speed how fast clinostats are rotated have a direct effect on the result and are necessary to optimize the simulation approach.

In this study, we identified optimal rotation conditions (rotational ratio of 4:1.8) by rotating the two rotors with different speeds, that reduced the gravitational effect and thus simulated microgravity more efficiently. In contrast

previous studies usually used equal revolutions for both rotors (4:4) (Borst, van Loon 2009). As rotation can produce shear stress, the control of the motion of the fluid and the cells seems to be necessary.

Among many clinorotation conditions tested, one specific ratio (4:1.8) produced the most notable biological differences with respect to the transcription activity of promoters measured 24 h after exposure. Other conditions with smaller differences in the ratio (4:2.0 and 4:2.2) produced less activity change. Therefore, we conclude that the biological responses we identified are caused by the reduction in gravity rather than by cell motion. We recommend future studies of cell signaling pathways by taking the rotational speed of the simulator into account.

Acknowledgments This study was supported by a grant from the Leading Space Core Technology Development Program through the National Research Foundation funded by the Ministry of Science, ICT &amp; Future Planning (2013M1A3A3A02042433) and by the Leading Foreign Research Institute Recruitment Program through the National Research Foundation of Korea (NRF) funded by the Ministry of Science, ICT &amp; Future Planning (2010-00757).

## References

Becker, J.L., Souza, G.R.: Using space-based investigations to inform cancer research on Earth. Nat. Rev. Cancer 13 (5), 315-327 (2013). doi:10.1038/nrc3507

Borst, A.G., van Loon, J.J.W.A.: Technology and developments for the random positioning machine. RPM Microgravity Sci. Technol. 21 , 287-292 (2009)

Brungs, S., Egli, M., Wuest, S.L., Christianen, P.C.M., van Loon, J.W.A., Anh, T.J.N., Hemmersbach, R.: Facilities for simulation of microgravity in the ESA ground-based facility programme. Microgravity Sci. Technol. 28 (3), 191-203 (2016)

Chae, M., Kim, K., Park, S.M., Jang, I.S., Seo, T., Kim, D.M., Kim, I.C., Lee, J.H., Park, J.: IRF-2 regulates NF-kappaB activity by modulating the subcellular localization of NF-kappaB. Biochem. Biophys. Res. Commun. 370 (3), 519-524 (2008). doi:10.1016/j.bbrc.2008.03.136 S0006-291X(08)00630-X [pii]

Coinu, R., Chiaviello, A., Galleri, G., Franconi, F., Crescenzi, E., Palumbo, G.: Exposure to modeled microgravity induces metabolic idleness in malignant human MCF-7 and normal murine VSMC cells. FEBS Lett. 580 (10), 2465-2470 (2006). S00145793(06)00405-4 [pii] doi:10.1016/j.febslet.2006.03.078

Cotrupi, S., Ranzani, D., Maier, J.A.: Impact of modeled microgravity on microvascular endothelial cells. Biochim. Biophys. Acta 1746 (2), 163-168 (2005). S0167-4889(05)00217-X [pii] doi:10.1016/j.bbamcr.2005.10.002

Grimm, D., Bauer, J., Kossmehl, P., Shakibaei, M., Schoberger, J., Pickenhahn, H., Schulze-Tanzil, G., Vetter, R., Eilles, C., Paul, M., Cogoli, A.: Simulated microgravity alters differentiation and increases apoptosis in human follicular thyroid carcinoma cells. FASEB J. 16 (6), 604-606 (2002)

Hammer, B.E., Kidder, L.S., Williams, P.C., Xu, W.W.: Magnetic Levitation of MC3T3 Osteoblast Cells as a Ground-Based Simulation of Microgravity. Microgravity Sci. Technol. 21 (4), 311-318 (2009). doi:10.1007/s12217-008-9092-6

Hemmersbach, R., Simon, A., Wa β er, K., Hauslage, J., Christianen, P.C., Albers, P.W., Lebert, M., Richter, P., Alt, W., Anken, R.: Impact of a high magnetic field on the orientation of gravitactic unicellular organisms-a critical consideration about the application of magnetic fields to mimic functional weightlessness. Astrobiology 14 (3), 205-215 (2014). doi:10.1089/ast.2013.1085

Herranz, R., Anken, R., Boonstra, J., Braun, M., Christianen, P.C., De Geest, M., Hauslage, J., Hilbig, R., Hill, R.J., Lebert, M., Medina, F.J., Vagt, N., Ullrich, O., Van Loon, J.J., Hemmersbach, R.: Ground-based facilities for simulation of microgravity: organism-specific recommendations for their use, and recommended terminology. Astrobiology 13 (1), 1-17 (2013). doi:10.1089/ast.2012.0876

Hoson, T., Kamisaka, S., Masuda, Y., Yamashita, H.: Changes in plant growth processes under microgravity conditons simulated by a three dimensional clinostat. Bot. Mag. 105 (1), 53-70 (1992)

Kang, C.Y., Zou, L., Yuan, M., Wang, Y., Li, T.Z., Zhang, Y., Wang, J.F., Li, Y ., Deng, X.W., Liu, C.T.: Impact of simulated microgravity on microvascular endothelial cell apoptosis. Eur. J. Appl. Physiol. 111 (9), 2131-2138 (2011). doi:10.1007/s00421-011-1844-0

Morey-Holton, E.R., Globus, R.K.: Hindlimb unloading rodent model: technical aspects. J. Appl. Physiol. (1985) 92 (4), 1367-1377 (2002). doi:10.1152/japplphysiol.00969.2001

Park, J., Kim, K., Lee, E.J., Seo, Y.J., Lim, S.N., Park, K., Rho, S.B., Lee, S.H., Lee, J.H.: Elevated level of SUMOylated IRF-1 in tumor cells interferes with IRF-1-mediated apoptosis. Proc. Natl. Acad. Sci. USA 104 (43), 17028-17033 (2007). 0609852104 [pii] doi:10.1073/pnas.0609852104

Russomano, T., Cardoso, R., Falcao, F., Dalmarco, G., C, V.D.S., L, F.D.S., D, G.d.A., Dos Santos, M., Martinelli, L., Motta, J., Forraz, N., McGuckin, C.: Development and validation of a 3d clinostat for the study of cells during microgravity simulation. conference proceedings: Annual international conference of the IEEE engineering in medicine and biology society. IEEE Eng. Med. Biol. Soc. Ann. Conf. 1 , 564-566 (2005). doi:10.1109/IEMBS.2005.1616474

Ryu, H.W., Choi, S.H., Namkoong, S., Jang, I.S., Seo, D.H., Choi, I., Kim, H.S., Park, J.: Simulated microgravity contributes to autophagy induction by regulating AMP-activated protein kinase. DNA Cell Biol. 33 (3), 128-135 (2014). doi:10.1089/dna.2013.2089

Takeda, M., Magaki, T., Okazaki, T., Kawahara, Y., Manabe, T., Yuge, L., Kurisu, K.: Effects of simulated microgravity on proliferation and chemosensitivity in Malignant glioma cells. Neurosci Lett. 463 (1), 54-59 (2009). doi:10.1016/j.neulet.2009.07.045

Tamma, R., Colaianni, G., Camerino, C., Di Benedetto, A., Greco, G., Strippoli, M., Vergari, R., Grano, A., Mancini, L., Mori, G., Colucci, S., Grano, M., Zallone, A.: Microgravity during spaceflight directly affects in vitro osteoclastogenesis and bone resorption. FASEB J 23 (8), 2549-2554 (2009). doi:10.1096/fj.08-127951 fj.08-127951 [pii]

Thiel, C.S., Paulsen, K., Bradacs, G., Lust, K., Tauber, S., Dumrese, C., Hilliger, A., Schoppmann, K., Biskup, J., Golz, N., Sang, C., Ziegler, U., Grote, K.H., Zipp, F., Zhuang, F., Engelmann, F., Hemmersbach, R., Cogoli, A., Ullrich, O.: Rapid alterations of cell cycle control proteins in human T lymphocytes in microgravity. Cell Commun. Signal 10 (1), 1 (2012). doi:10.1186/1478-811X-10-1 1478-811X-10-1 [pii]

Vandenburgh, H., Chromiak, J., Shansky, J., Del Tatto, M., Lemaire, J.: Space travel directly induces skeletal muscle atrophy. FASEB J. 13 (9), 1031-1038 (1999)

Yuge, L., Hide, I., Kumagai, T., Kumei, Y., Takeda, S., Kanno, M., Sugiyama, M., Kataoka, K.: Cell differentiation and p38(MAPK) cascade are inhibited in human osteoblasts cultured in a three-dimensional clinostat. In vitro cellular &amp; developmental biology. Animal 39 (1-2), 89-97 (2003). doi:10.1290/1543-706X(2003)039(0089:CDAPCA)2.0.CO;2

Yuge, L., Kajiume, T., Tahara, H., Kawahara, Y., Umeda, C., Yoshimoto, R., Wu, S.L., Yamaoka, K., Asashima, M., Kataoka, K., Ide, T.: Microgravity potentiates stem cell proliferation while sustaining the capability of differentiation. Stem Cells Dev. 15 (6), 921-929 (2006). doi:10.1089/scd.2006.15.921