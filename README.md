# **Monitoring Bacterial Movement and Populations**
## _Description_
This project aims to compare the bacterial movement and population growth under specific nutrient or stress conditions. 

The data were obtained from a simulation of bacterial tracking experiment. Each input contains the ID of experiment run, number of bacteria tracked, their 3D momentum components (px, py, pz) in 10⁻²⁰ kg m/s and ID of bacterial strain or genetic variant.

The data set contains following bacterial strains:

* _E. coli WT_ (wild type)
* _E. coli mutant_
* _Bacillus subtilis WT_ (wild type)
* _Bacillus subtilis mutant_
* _Pseudomonas aeruginosa WT_ (wild type)
* _Pseudomonas aeruginosa antibiotic-resistant_
* _Streptococcus pneumoniae_
* _Capsule-deficient streptococcus pneumoniae_
* _Mycobacterium tuberculosis_
* _Drug-resistant mycobacterium tuberculosis_
* _Salmonella enterica_
* _Salmonella mutant_

## _Research Questions_
The project focuses on answering the following research questions:

1. What are the average counts and statistical uncertainties of each bacterial strain?
2. Is there any asymmetry between the normal and the mutant strain, if so - how large is it?
3. Is there any asymmetry between the normal and the mutant strain as a function of their momentum?

## _Results_

Empty events were removed from further analyses and therefore 4614632 events were analysed in this experiment. 

To calculate average bacterial count the subsampling method was applied. Each file was treated as one subsample.
Uncertainties were calculated as standard deviations of subsample averages.

__1. The project indicates the following average counts and statistical uncertainties for each bacterial strain (results were rounded to 7 decemals):__

* E. coli WT: 19.964037869108523 ± 0.03277297367603035

* E. coli mutant: 19.93171763208854 ± 0.031862995623137325

* Bacillus subtilis WT: 2.5109753063732927 ± 0.004760470013110588

* Bacillus subtilis mutant: 2.505280161018257 ± 0.005510374977956562

* Pseudomonas aeruginosa WT: 1.2089139502348183 ± 0.0019158652790257898

* Pseudomonas aeruginosa antibiotic-resistant: 1.1850234211525426 ± 0.002419119037614167

* Streptococcus pneumoniae:  0.2767999701818043 ± 0.0010762078233972018

* Capsule-deficient streptococcus pneumoniae: 0.27189383682165774 ± 0.0009852549484234705

* Mycobacterium tuberculosis: 0.03946988622278006 ± 0.0002835326780196852

* Drug-resistant mycobacterium tuberculosis: 0.03902889764557607 ± 0.00040171753717196235

* Salmonella enterica: 0.0011879603834065208 ± 4.1700896418102735e-05

* Salmonella mutant: 0.0011524212548259536 ± 5.083297255816441e-05

__2. The table below illustrates the differences between the normal and the mutant strain:__


| Bacterial strains | Reported difference | Difference / Uncertainty | Significant (>3std) |
|:---:|:---:| :--:| :--: |
| E. coli WT VS E. coli mutant | 0.0323202370199831 ± 0.004522323370133003| 6.4 | Yes |
|Bacillus subtilis WT VS Bacillus subtilis mutant | 0.005695145355036046 ± 0.0032959418543238657| 2| No |
|Pseudomonas aeruginosa WT VS Pseudomonas aeruginosa antibiotic-resistant | 0.02389052908227569 ± 0.002374703366663008| 6| Yes |
|Streptococcus pneumoniae VS Capsule-deficient streptococcus pneumoniae | 0.004906133360146596 ± 0.0005836584978728003| 5| Yes |
|Mycobacterium tuberculosis VS Drug-resistant mycobacterium tuberculosis | 0.0004409885772039886 ± 0.000488300925559704| 1| No |
|Salmonella enterica VS Salmonella mutant| 3.5539128580567214e-05 ± 6.859368307476926e-05| 0.516| No |

<br>
<br>
The difference was considered significant if it exceeded 3 standard-deviations. It was discovered that:

* E. coli (WT,mutant) 
* Pseudomonas aeruginosa (WT, antibiotic-resistant) 
* Streptococcus pneumoniae (normal, capsule-deficient)

differ significantly.
 
## _Installation_
1. Make sure you have Python 3 installed. 
2. Additionally Numpy package is required:
```bash
pip install numpy
```

3. Clone the repository
```bash
git clone https://github.com/sofijaponomarjova/Monitoring-Bacterial-Movement-and-Population.git
cd Monitoring-Bacterial-Movement-and-Population
```
**Alternatively, download the repository as a ZIP file:**
* Press green button "<> Code"
* Click "Download ZIP"

**Dataset**

You can download the dataset files here: https://surfdrive.surf.nl/index.php/s/7udCnWTk4yMUASD 

Please store all the files in one folder as program asks for folder's pathway!!

## _Usage_
1. Open the repository in your VSC
2. Run in Terminal file of your choice:

```python3 *file of your choice*```

* task2.py - cleans the data and then calculates the momentum for each bacteria
* week3.py - calculates the average amount of a bacterial strain per event/experiment in 1 sample
* week4.py - calculates the average amount of a bacterial strain per event/experiment in all 10 samples (main results)


