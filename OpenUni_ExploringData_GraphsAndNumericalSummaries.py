# -*- coding: utf-8 -*-
"""

OpedUni - 
https://www.open.edu/openlearn/science-maths-technology/mathematics-statistics/exploring-data-graphs-and-numerical-summaries/content-section-2.5

"""

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

data = pd.read_csv('OpenLearn_ExploringDataGraphsAndNumericalSummaries.csv')

#Activity 2: Alcohol consumption and death rate

#Rename All Columns
data.columns = ['Country', 'Alcohol consumption', 'Death rate']

#figures

#1
plt.plot(data.loc[:, 'Alcohol consumption'], data.loc[:, 'Death rate'], marker = 'o')

plt.xlabel("Annual alcohol consumption")
plt.ylabel("Death tate (/1000)")

plt.show()

#2
plt.plot(data.loc[:, 'Country'], data.loc[:, 'Death rate'], marker = 'o')

plt.xlabel("Country")
plt.ylabel("Death tate (/1000)")

plt.show()

#Activity 3: Tattoo sizes

total_no = 30+16+9

tattoo_no = int(input('Tattoo: '))

angle_for_tattoos = 360 * (tattoo_no/(total_no))

#Activity 4: USA workforce

#https://www.open.edu/openlearn/science-maths-technology/mathematics-statistics/exploring-data-graphs-and-numerical-summaries/content-section-3.6

#The grey colour bars are for males and white colour bars are for females and the plot shows that
#Only in Sales sector, Males and Females are employed almost equally and in most of the employment sectors,
#males are employed significantly more than females although the it's the other way round in 'Service' and 'Clerical' sector.

males = 15 + 12.5 + 12 + 7 + 6 + 4 + 3 #in millions
females = 11.5 + 4.5 + 1 + 7 + 10 + 15 + 1 #in millions

#Activity 5: Comparing histograms

#According to Figure 10 & 11, the Birth weights are skewed towards the left.
#Only Figures 10 and 12(b) give a really clear indication that the data are split into two ‘clumps’.
#Figures 10, 11 and 12(a) all give, to varying degrees, the impression that there is perhaps an identifiable group of babies with particularly low birth weights.

#Activity 6: Interpreting a scatterplot

#body weight and brain weight almost have a linear relationship with three outliers at the end.
#Although there are two or three points that are slightly above the general pattern of the others and hence appear to have high brain weight to body weight ratios.

#Activity 7: Birth weights of infants with SIRDS

live_list = np.sort([1.720,2.090,2.570,2.600,1.410,1.760,2.200,2.700,1.130,2.830,1.575,2.400,2.950,1.930,3.005,1.680,3.160,1.715,2.015,2.550,3.400,2.040,3.640])

pos_birth_weight_infants_survived = len(live_list)

midpos = (round(pos_birth_weight_infants_survived/2)) - 1 #as element positions will start from 0

live_list = pd.DataFrame(live_list)

median_birth_weight_infants_survived = live_list.iloc[midpos]

dead_list = np.sort([1.030,1.300,1.050,1.310,1.750,2.200,1.100,1.500,1.770,2.270,2.730,1.175,1.550,1.820,2.275,1.185,1.890,1.225,1.600,2.440,1.230,1.940,2.500,1.262,1.295,1.720,2.560])

pos_weight_infants_dead = len(dead_list)

midposd = (round(pos_weight_infants_dead/2)) - 1 #as element positions will start from 0

dead_list = pd.DataFrame(dead_list)

median_weight_infants_dead = dead_list.iloc[midposd]

#Activity 8: Beta endorphin concentration (successful runners)

Difference = np.sort([25.3,20.5,10.3,24.4,17.5,30.6,11.8,12.9,3.8,20.6,28.4])

pos_Difference = len(Difference)

midposDiff = (round(pos_Difference/2)) - 1 #as element positions will start from 0

Difference = pd.DataFrame(Difference)

median_Difference = Difference.iloc[midposDiff]

#Activity 9: Beta endorphin concentration (successful runners)

mean_Difference1 = np.sum(Difference) / pos_Difference

#Alternatively

mean_Difference2 = np.mean(Difference)

#Activity 10: More on the SIRDS data

qlpos = (round(pos_weight_infants_dead/4)) - 1 #as element positions will start from 0

lquartiles_weight_infants_dead = dead_list.iloc[qlpos]

qupos = (3*(round(pos_weight_infants_dead/4))) - 1 #as element positions will start from 0

uquartiles_weight_infants_dead = dead_list.iloc[qupos]

interquartile_range = uquartiles_weight_infants_dead - lquartiles_weight_infants_dead

#Activity 11: Chondrite meteors

meteors_list = np.sort([20.77,22.56,22.71,22.99,26.39,27.08,27.3,27.33,27.57,27.81,28.69,29.36,30.25,31.89,32.88,33.23,33.28,33.40,33.52,33.83,33.95,34.82])

pos_met = len(meteors_list)
#length of elements show there are even numbers of elements

###Note: It is important to check if the length is odd or even

midposmet1 = (round(pos_met/2)) - 1
midposmet2 = round(pos_met/2)

meteors_listd = pd.DataFrame(meteors_list)

median_meteors = (meteors_listd.iloc[midposmet1] + meteors_listd.iloc[midposmet2]) / 2

qlposmet1 = round((pos_met/4) - 1) #as element positions will start from 0
qlposmet2 = (round(pos_met/4) - 1)

meteors_listql = pd.DataFrame(meteors_list)

lowerquartiles_meteors = (meteors_listql.iloc[qlposmet1] + meteors_listql.iloc[qlposmet2]) / 2

uqposmet1 = round((3*(pos_met/4)) - 1) #as element positions will start from 0
uqposmet2 = round(3*(pos_met/4)) 

meteors_listul = pd.DataFrame(meteors_list)

upperquartiles_meteors = (meteors_listul.iloc[uqposmet1] + meteors_listul.iloc[uqposmet2]) / 2

interquartile_range_meteors = upperquartiles_meteors - lowerquartiles_meteors

#Activity 12: Calculating standard deviations

x = [66,72,79,84,102,110,123,144,162,169,414]

mean_x = np.mean(x) #find mean of x

x_mean_x = []

for i in x:
    x_mean_x_each = i - mean_x
    x_mean_x.append(x_mean_x_each)

summation = 0

for i in x_mean_x:
    summation += (i)*(i)

elementnumber = len(x_mean_x) - 1

standard_deviation = math.sqrt(summation / elementnumber)

#Activity 13: Calculating standard deviations

x = [66,72,79,84,102,110,123,144,162,169]

mean_x = np.mean(x) #find mean of x

x_mean_x = []

for i in x:
    x_mean_x_each = i - mean_x
    x_mean_x.append(x_mean_x_each)

summation = 0

for i in x_mean_x:
    summation += (i)*(i)

elementnumber = len(x_mean_x) - 1

new_standard_deviation = math.sqrt(summation / elementnumber)

###Calculate interquartile range

#Taking more manual approach

x = [66,72,79,84,102,110,123,144,162,169,414]

elementnum = len(x) - 1

#as there are even number of elements

lq = 79

uq = 162

interquartile_range = uq - lq

#when the outlier is omitted

nlq = 72 + (3 * ((79 - 72) / 4))

nuq = 144 + ((162 - 144) / 4)

ninterquartile_range = nuq - nlq

#Exercise 1: Family size

sixy = np.sort([14,13,4,14,10,2,13,5,0,0,13,3,9,2,10,11,13,5,14])

seveny = np.sort([0,4,0,2,3,3,0,4,7,1,9,4,3,2,3,2,16,6,0,13,6,6,5,9,10,5,4,3,3,5,2,3,5,15,5])

#1

range_sixy = np.max(sixy) - np.min(sixy)

range_seveny = np.max(seveny) - np.min(seveny)

numsixy = len(sixy) - 1

numseveny = len(seveny) - 1

#for median

#as there are odd elements

midpossixy = round(numsixy / 2)

midposseveny = round(numseveny / 2)

sixyd = pd.DataFrame(sixy)

sevenyd = pd.DataFrame(seveny)

median_sixy = sixyd.loc[midpossixy]

median_seveny = sevenyd.loc[midposseveny]

#for quartiles processing

qlpossixy = round(numsixy / 4)

qlposseveny = round(numseveny / 4)

qupossixy = round(3 * (numsixy / 4))

quposseveny = round(3 * (numseveny / 4))

sixydq = pd.DataFrame(sixy)

sevenydq = pd.DataFrame(seveny)

#quartiles

ql_sixy = sixydq.loc[qlpossixy] 

qu_sixy = sixydq.loc[qupossixy]

ql_seveny = sevenydq.loc[qlposseveny]

qu_seveny = sevenydq.loc[quposseveny]

#interquartile range

interquartile_sixy = qu_sixy - ql_sixy 

interquartile_seveny = qu_seveny - ql_seveny

#2

mean_sixy = np.mean(sixy) #find mean of x

sixy_mean = []

for i in sixy:
    sixy_mean_each = i - mean_sixy
    sixy_mean.append(sixy_mean_each)

summationsixy = 0

for i in sixy_mean:
    summationsixy += (i)*(i)

elementnumsixy = len(sixy_mean) - 1

standard_deviation_sixy = math.sqrt(summationsixy / elementnumsixy)

variance_sixy = standard_deviation_sixy * standard_deviation_sixy

###

mean_seveny = np.mean(seveny) #find mean of x

seveny_mean = []

for i in seveny:
    seveny_mean_each = i - mean_seveny
    seveny_mean.append(seveny_mean_each)

summationseveny = 0

for i in seveny_mean:
    summationseveny += (i)*(i)

elementnumseveny = len(seveny_mean) - 1

standard_deviation_seveny = math.sqrt(summationseveny / elementnumseveny)

variance_seveny = standard_deviation_seveny * standard_deviation_seveny


#Exercise 2 Alcohol consumption

alcohol = np.sort([3.1,3.9,4.2,5.6,5.7,5.8,6.6,7.2,8.3,9.9,10.8,10.9,12.3,15.2])

num = len(alcohol)

#for median

midpos1 = num / 2

#as there are even number of elements

midpos2 = (num / 2) + 1

alcoholpd = pd.DataFrame(alcohol)

median_x = (alcoholpd.loc[midpos1] + alcoholpd.loc[midpos2]) / 2

#for quartiles

lqpos1 = round(num / 4) - 1
lqpos2 = round(num / 4)

lq_alcohol = alcoholpd.loc[lqpos1] + (0.25 * (alcoholpd.loc[lqpos2] - alcoholpd.loc[lqpos1]))

uqpos1 = 3*(round(num / 4)) - 1
uqpos2 = 3*(round(num / 4))

uq_alcohol = alcoholpd.loc[uqpos1] + (0.75 * (alcoholpd.loc[uqpos2] - alcoholpd.loc[uqpos1]))

interquartile_range_alcohol = uq_alcohol - lq_alcohol

