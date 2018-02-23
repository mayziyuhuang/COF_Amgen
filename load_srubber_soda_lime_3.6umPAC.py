import numpy as np
import scipy.special

import matplotlib
matplotlib.use
import matplotlib.pyplot as plt
plt.style.use('seaborn-talk')

import pandas as pd

import friction_functions as data

load_gram_1 = 657.8
load_gram_2 = 657.4
load_gram_3 = 204.2
load_gram_4 = 657.2
load_gram_5 = 653
load_gram_6 = 200.7
load_gram_7 = 657.5
load_gram_8 = 205.5
load_gram_9 = 657.6
load_gram_10 = 205.7
load_gram_11 = 657.1
load_gram_12 = 205.8
load_gram_13 = 206
load_gram_14 = 656.8
load_gram_15 = 205.9
load_gram_16 = 205.7

#sample: rubber pieces (small), substrate: soda lime wafer with 3.6 um PAC
#0 um PAC on small rubber(2cm*2cm) vs soda lime wafer, load = 205.5
soda3_6um_srubber0um1 = 'data/20171024_smallrubber_1_vs_sodalime_3.3um_205.5g_load_1.xlsx'
soda3_6um_srubber0um1df = data.friction_data(soda3_6um_srubber0um1, load_gram_8)

#0.2 um PAC on small rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 206
soda3_6um_srubber0_2um1 = 'data/20171121_smallrubber_0.2um_1_vs_sodalime_3.6um_206.0g_load_1.xlsx'
soda3_6um_srubber0_2um1df = data.friction_data(soda3_6um_srubber0_2um1, load_gram_13)
soda3_6um_srubber0_2um2 = 'data/20171121_smallrubber_0.2um_2_vs_sodalime_3.6um_206.0g_load_1.xlsx'
soda3_6um_srubber0_2um2df = data.friction_data(soda3_6um_srubber0_2um2, load_gram_13)
soda3_6um_srubber0_2um3 = 'data/20171121_smallrubber_0.2um_3_vs_sodalime_3.6um_206.0g_load_1.xlsx'
soda3_6um_srubber0_2um3df = data.friction_data(soda3_6um_srubber0_2um3, load_gram_13)
soda3_6um_srubber0_2um4 = 'data/20171121_smallrubber_0.2um_4_vs_sodalime_3.6um_206.0g_load_1.xlsx'
soda3_6um_srubber0_2um4df = data.friction_data(soda3_6um_srubber0_2um4, load_gram_13)

#0.2 um PAC on small rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 205.9
soda3_6um_srubber0_6um1 = 'data/20171122_smallrubber_0.6um_1_vs_sodalime_3.6um_206.0g_load_1.xlsx'
soda3_6um_srubber0_6um1df = data.friction_data(soda3_6um_srubber0_6um1, load_gram_15)
soda3_6um_srubber0_6um2 = 'data/20171122_smallrubber_0.6um_2_vs_sodalime_3.6um_206.0g_load_1.xlsx'
soda3_6um_srubber0_6um2df = data.friction_data(soda3_6um_srubber0_6um2, load_gram_15)
soda3_6um_srubber0_6um3 = 'data/20171122_smallrubber_0.6um_3_vs_sodalime_3.6um_206.0g_load_1.xlsx'
soda3_6um_srubber0_6um3df = data.friction_data(soda3_6um_srubber0_6um3, load_gram_15)
soda3_6um_srubber0_6um4 = 'data/20171122_smallrubber_0.6um_4_vs_sodalime_3.6um_206.0g_load_1.xlsx'
soda3_6um_srubber0_6um4df = data.friction_data(soda3_6um_srubber0_6um4, load_gram_15)

#1.1 um PAC on small rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 205.5
soda3_6um_srubber1_1um1 = 'data/20171024_smallrubber_1.1um_1_vs_sodalime_3.6um_205.5g_load_1.xlsx'
soda3_6um_srubber1_1um1df = data.friction_data(soda3_6um_srubber1_1um1, load_gram_8)
soda3_6um_srubber1_1um2 = 'data/20171024_smallrubber_1.1um_2_vs_sodalime_3.6um_205.5g_load_1.xlsx'
soda3_6um_srubber1_1um2df = data.friction_data(soda3_6um_srubber1_1um2, load_gram_8)
soda3_6um_srubber1_1um3 = 'data/20171024_smallrubber_1.1um_3_vs_sodalime_3.6um_205.5g_load_1.xlsx'
soda3_6um_srubber1_1um3df = data.friction_data(soda3_6um_srubber1_1um3, load_gram_8)
soda3_6um_srubber1_1um4 = 'data/20171024_smallrubber_1.1um_4_vs_sodalime_3.6um_205.5g_load_1.xlsx'
soda3_6um_srubber1_1um4df = data.friction_data(soda3_6um_srubber1_1um4, load_gram_8)
soda3_6um_srubber1_1um5 = 'data/20171024_smallrubber_1.1um_5_vs_sodalime_3.6um_205.5g_load_1.xlsx'
soda3_6um_srubber1_1um5df = data.friction_data(soda3_6um_srubber1_1um5, load_gram_8)

#3.6 um PAC on samll rubber(2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 200.7
soda3_6um_srubber3_6um1 = 'data/20171019_smallrubber_3.6um_1_vs_sodalime_PAC3.6um_200.7g_load_1.xlsx'
soda3_6um_srubber3_6um1df = data.friction_data(soda3_6um_srubber3_6um1, load_gram_6)
soda3_6um_srubber3_6um2 = 'data/20171019_smallrubber_3.6um_2_vs_sodalime_PAC3.6um_200.7g_load_1.xlsx'
soda3_6um_srubber3_6um2df = data.friction_data(soda3_6um_srubber3_6um2, load_gram_6)
soda3_6um_srubber3_6um3 = 'data/20171019_smallrubber_3.6um_3_vs_sodalime_PAC3.6um_200.7g_load_1.xlsx'
soda3_6um_srubber3_6um3df = data.friction_data(soda3_6um_srubber3_6um3, load_gram_6)
soda3_6um_srubber3_6um4 = 'data/20171019_smallrubber_3.6um_4_vs_sodalime_PAC3.6um_200.7g_load_1.xlsx'
soda3_6um_srubber3_6um4df = data.friction_data(soda3_6um_srubber3_6um4, load_gram_6)
soda3_6um_srubber3_6um5 = 'data/20171019_smallrubber_3.6um_5_vs_sodalime_PAC3.6um_200.7g_load_1.xlsx'
soda3_6um_srubber3_6um5df = data.friction_data(soda3_6um_srubber3_6um5, load_gram_6)

#7.3 um PAC on small rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 206
soda3_6um_srubber7_3um1 = 'data/20171121_smallrubber_7.3um_1_vs_sodalime_3.6um_206.0g_load_1.xlsx'
soda3_6um_srubber7_3um1df = data.friction_data(soda3_6um_srubber7_3um1, load_gram_13)
soda3_6um_srubber7_3um2 = 'data/20171121_smallrubber_7.3um_2_vs_sodalime_3.6um_206.0g_load_1.xlsx'
soda3_6um_srubber7_3um2df = data.friction_data(soda3_6um_srubber7_3um2, load_gram_13)
soda3_6um_srubber7_3um3 = 'data/20171121_smallrubber_7.3um_3_vs_sodalime_3.6um_206.0g_load_1.xlsx'
soda3_6um_srubber7_3um3df = data.friction_data(soda3_6um_srubber7_3um3, load_gram_13)
soda3_6um_srubber7_3um4 = 'data/20171121_smallrubber_7.3um_4_vs_sodalime_3.6um_206.0g_load_1.xlsx'
soda3_6um_srubber7_3um4df = data.friction_data(soda3_6um_srubber7_3um4, load_gram_13)
soda3_6um_srubber7_3um5 = 'data/20171121_smallrubber_7.3um_5_vs_sodalime_3.6um_206.0g_load_1.xlsx'
soda3_6um_srubber7_3um5df = data.friction_data(soda3_6um_srubber7_3um5, load_gram_13)

#8.9 um PAC on samll rubber(2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 205.8
soda3_6um_srubber8_9um1 = 'data/20171113_smallrubber_8.9um_1_vs_sodalime_3.6um_205.8g_load_1.xlsx'
soda3_6um_srubber8_9um1df = data.friction_data(soda3_6um_srubber8_9um1, load_gram_12)
soda3_6um_srubber8_9um2 = 'data/20171113_smallrubber_8.9um_2_vs_sodalime_3.6um_205.8g_load_1.xlsx'
soda3_6um_srubber8_9um2df = data.friction_data(soda3_6um_srubber8_9um2, load_gram_12)
soda3_6um_srubber8_9um3 = 'data/20171113_smallrubber_8.9um_3_vs_sodalime_3.6um_205.8g_load_1.xlsx'
soda3_6um_srubber8_9um3df = data.friction_data(soda3_6um_srubber8_9um3, load_gram_12)
soda3_6um_srubber8_9um4 = 'data/20171113_smallrubber_8.9um_4_vs_sodalime_3.6um_205.8g_load_1.xlsx'
soda3_6um_srubber8_9um4df = data.friction_data(soda3_6um_srubber8_9um4, load_gram_12)
soda3_6um_srubber8_9um5 = 'data/20171113_smallrubber_8.9um_5_vs_sodalime_3.6um_205.8g_load_1.xlsx'
soda3_6um_srubber8_9um5df = data.friction_data(soda3_6um_srubber8_9um5, load_gram_12)


#1.1 um PAHT on small rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 205.7
soda3_6um_srubber1_1umHT1 = 'data/20171031_smallrubber_1.1um_HT_1_vs_sodalime_3.3um_205.7g_load_1.xlsx'
soda3_6um_srubber1_1umHT1df = data.friction_data(soda3_6um_srubber1_1umHT1, load_gram_10)
soda3_6um_srubber1_1umHT2 = 'data/20171031_smallrubber_1.1um_HT_2_vs_sodalime_3.3um_205.7g_load_1.xlsx'
soda3_6um_srubber1_1umHT2df = data.friction_data(soda3_6um_srubber1_1umHT2, load_gram_10)
soda3_6um_srubber1_1umHT3 = 'data/20171031_smallrubber_1.1um_HT_3_vs_sodalime_3.3um_205.7g_load_1.xlsx'
soda3_6um_srubber1_1umHT3df = data.friction_data(soda3_6um_srubber1_1umHT3, load_gram_10)
soda3_6um_srubber1_1umHT4 = 'data/20171031_smallrubber_1.1um_HT_4_vs_sodalime_3.3um_205.7g_load_1.xlsx'
soda3_6um_srubber1_1umHT4df = data.friction_data(soda3_6um_srubber1_1umHT4, load_gram_10)
soda3_6um_srubber1_1umHT5 = 'data/20171031_smallrubber_1.1um_HT_5_vs_sodalime_3.3um_205.7g_load_1.xlsx'
soda3_6um_srubber1_1umHT5df = data.friction_data(soda3_6um_srubber1_1umHT5, load_gram_10)

#4.5 um PAHT on small rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 205.8
soda3_6um_srubber4_5umHT1 = 'data/20171113_smallrubber_4.5um_HT_1_vs_sodalime_3.6um_205.8g_load_1.xlsx'
soda3_6um_srubber4_5umHT1df = data.friction_data(soda3_6um_srubber4_5umHT1, load_gram_12)
soda3_6um_srubber4_5umHT2 = 'data/20171113_smallrubber_4.5um_HT_2_vs_sodalime_3.6um_205.8g_load_1.xlsx'
soda3_6um_srubber4_5umHT2df = data.friction_data(soda3_6um_srubber4_5umHT2, load_gram_12)
soda3_6um_srubber4_5umHT3 = 'data/20171113_smallrubber_4.5um_HT_3_vs_sodalime_3.6um_205.8g_load_1.xlsx'
soda3_6um_srubber4_5umHT3df = data.friction_data(soda3_6um_srubber4_5umHT3, load_gram_12)
soda3_6um_srubber4_5umHT4 = 'data/20171113_smallrubber_4.5um_HT_4_vs_sodalime_3.6um_205.8g_load_1.xlsx'
soda3_6um_srubber4_5umHT4df = data.friction_data(soda3_6um_srubber4_5umHT4, load_gram_12)
soda3_6um_srubber4_5umHT5 = 'data/20171113_smallrubber_4.5um_HT_5_vs_sodalime_3.6um_205.8g_load_1.xlsx'
soda3_6um_srubber4_5umHT5df = data.friction_data(soda3_6um_srubber4_5umHT5, load_gram_12)

#6.9 um PAHT on small rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 205.8
soda3_6um_srubber6_9umHT1 = 'data/20171113_smallrubber_6.9um_HT_1_vs_sodalime_3.6um_205.8g_load_1.xlsx'
soda3_6um_srubber6_9umHT1df = data.friction_data(soda3_6um_srubber6_9umHT1, load_gram_12)
soda3_6um_srubber6_9umHT2 = 'data/20171113_smallrubber_6.9um_HT_2_vs_sodalime_3.6um_205.8g_load_1.xlsx'
soda3_6um_srubber6_9umHT2df = data.friction_data(soda3_6um_srubber6_9umHT2, load_gram_12)
soda3_6um_srubber6_9umHT3 = 'data/20171113_smallrubber_6.9um_HT_3_vs_sodalime_3.6um_205.8g_load_1.xlsx'
soda3_6um_srubber6_9umHT3df = data.friction_data(soda3_6um_srubber6_9umHT3, load_gram_12)
soda3_6um_srubber6_9umHT4 = 'data/20171113_smallrubber_6.9um_HT_4_vs_sodalime_3.6um_205.8g_load_1.xlsx'
soda3_6um_srubber6_9umHT4df = data.friction_data(soda3_6um_srubber6_9umHT4, load_gram_12)
soda3_6um_srubber6_9umHT5 = 'data/20171113_smallrubber_6.9um_HT_5_vs_sodalime_3.6um_205.8g_load_1.xlsx'
soda3_6um_srubber6_9umHT5df = data.friction_data(soda3_6um_srubber6_9umHT5, load_gram_12)



#sample: rubber pieces (small), substrate: soda lime wafer with 1.1 um PAHT
#1.1 um PAHT on small rubber (2cm*2cm) vs soda lime wafer with 1.1 um PAC, load = 205.7
soda1_1umHT_srubber1_1umHT1 = 'data/20171031_smallrubber_1.1um_HT_1_vs_sodalime_1.1um_HT_205.7g_load_1.xlsx'
soda1_1umHT_srubber1_1umHT1df = data.friction_data(soda1_1umHT_srubber1_1umHT1, load_gram_10)
soda1_1umHT_srubber1_1umHT2 = 'data/20171031_smallrubber_1.1um_HT_2_vs_sodalime_1.1um_HT_205.7g_load_1.xlsx'
soda1_1umHT_srubber1_1umHT2df = data.friction_data(soda1_1umHT_srubber1_1umHT2, load_gram_10)
soda1_1umHT_srubber1_1umHT3 = 'data/20171031_smallrubber_1.1um_HT_3_vs_sodalime_1.1um_HT_205.7g_load_1.xlsx'
soda1_1umHT_srubber1_1umHT3df = data.friction_data(soda1_1umHT_srubber1_1umHT3, load_gram_10)
soda1_1umHT_srubber1_1umHT4 = 'data/20171031_smallrubber_1.1um_HT_4_vs_sodalime_1.1um_HT_205.7g_load_1.xlsx'
soda1_1umHT_srubber1_1umHT4df = data.friction_data(soda1_1umHT_srubber1_1umHT4, load_gram_10)
soda1_1umHT_srubber1_1umHT5 = 'data/20171031_smallrubber_1.1um_HT_5_vs_sodalime_1.1um_HT_205.7g_load_1.xlsx'
soda1_1umHT_srubber1_1umHT5df = data.friction_data(soda1_1umHT_srubber1_1umHT5, load_gram_10)


#sample: rubber piece (small), substrate: soda lime wafer with oil on 16 um PAC
#0um parylene on small rubber (2cm*2cm) vs soda lime wafer with oil on 16 um PAC, load = 205.9
oil_soda_1_srubber_1 = 'data/20171108_smallrubber_vs_oil_sodalime_#1_205.9g_load_1.xlsx'
oil_soda_1_srubber_1df = data.friction_data(oil_soda_1_srubber_1, load_gram_12)
oil_soda_2_srubber_1 = 'data/20171108_smallrubber_vs_oil_sodalime_#2_205.9g_load_1.xlsx'
oil_soda_2_srubber_1df = data.friction_data(oil_soda_2_srubber_1, load_gram_12)
#16 um PAC on small rubber (2cm*2cm) vs soda lime wafer with oil on 16 um PAC, load = 205.9
oil_soda_1_srubber16um_1 = 'data/20171108_smallrubber_16um_1_vs_oil_sodalime_#1_205.9g_load_1.xlsx'
oil_soda_1_srubber16um_1df = data.friction_data(oil_soda_1_srubber16um_1, load_gram_12)
oil_soda_2_srubber16um_1 = 'data/20171108_smallrubber_16um_1_vs_oil_sodalime_#2_205.9g_load_1.xlsx'
oil_soda_2_srubber16um_1df = data.friction_data(oil_soda_2_srubber16um_1, load_gram_12)
#oil on 16 um PAC on small rubber (2cm*2cm) vs soda lime wafer with oil on 16 um PAC, load = 205.9
oil_soda_1_srubber_oil_16um_1 = 'data/20171108_smallrubber_16um+oil_1_vs_oil_sodalime_#1_205.9g_load_1.xlsx'
oil_soda_1_srubber_oil_16um_1df = data.friction_data(oil_soda_1_srubber_oil_16um_1, load_gram_12)

#sample: rubber piece (small), substrate: soda lime wafer
#16 um PAC on small rubber (2cm*2cm) vs soda lime wafer, load = 205.9
soda_1_srubber16um_1 = 'data/20171108_smallrubber_16um_1_vs_newly_washed_sodalime_#1_205.9g_load_1.xlsx'
soda_1_srubber16um_1df = data.friction_data(soda_1_srubber16um_1, load_gram_12)
soda_2_srubber16um_1 = 'data/20171108_smallrubber_16um_1_vs_newly_washed_sodalime_#2_205.9g_load_1.xlsx'
soda_2_srubber16um_1df = data.friction_data(soda_2_srubber16um_1, load_gram_12)
soda_3_srubber16um_1 = 'data/20171108_smallrubber_16um_1_vs_newly_washed_sodalime_#3_205.9g_load_1.xlsx'
soda_3_srubber16um_1df = data.friction_data(soda_3_srubber16um_1, load_gram_12)
soda_4_srubber16um_1 = 'data/20171108_smallrubber_16um_1_vs_newly_washed_sodalime_#4_205.9g_load_1.xlsx'
soda_4_srubber16um_1df = data.friction_data(soda_4_srubber16um_1, load_gram_12)
#oil on 16 um PAC on small rubber (2cm*2cm) vs soda lime wafer, load = 205.9
soda_3_srubber_oil_16um_1 = 'data/20171108_smallrubber_16um+oil_1_vs_sodalime_#3_205.9g_load_1.xlsx'
soda_3_srubber_oil_16um_1df = data.friction_data(soda_3_srubber_oil_16um_1, load_gram_12)


plt.plot(soda3_6um_srubber0um1df['travel'], soda3_6um_srubber0um1df['load'], marker='.', linestyle='-', label = 'rubber vs 3.6 um PA-C on soda lime wafer', color = 'k')
#plt.plot(soda3_6um_srubber0um2df['travel'], soda3_6um_srubber0um2df['load'], marker='.', linestyle='-', label = 'rubber vs 3.6 um PA-C on soda lime wafer', color = '#1f77b4ff')
#
# plt.plot(soda3_6um_srubber0_2um1df['travel'], soda3_6um_srubber0_2um1df['load'], marker='.', linestyle='-', label = '0.2 um PA-C on rubber vs 3.6 um PA-C on soda lime wafer', color = '#1f77b4ff')
# plt.plot(soda3_6um_srubber0_2um2df['travel'], soda3_6um_srubber0_2um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')
# plt.plot(soda3_6um_srubber0_2um3df['travel'], soda3_6um_srubber0_2um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')
# plt.plot(soda3_6um_srubber0_2um4df['travel'], soda3_6um_srubber0_2um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')
#
# plt.plot(soda3_6um_srubber0_6um1df['travel'], soda3_6um_srubber0_6um1df['load'], marker='.', linestyle='-', label = '0.6 um PA-C on rubber vs 3.6 um PA-C on soda lime wafer', color = '#ff7f0eff')
# plt.plot(soda3_6um_srubber0_6um2df['travel'], soda3_6um_srubber0_6um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')
# plt.plot(soda3_6um_srubber0_6um3df['travel'], soda3_6um_srubber0_6um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')
# plt.plot(soda3_6um_srubber0_6um4df['travel'], soda3_6um_srubber0_6um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')
#
# plt.plot(soda3_6um_srubber1_1um1df['travel'], soda3_6um_srubber1_1um1df['load'], marker='.', linestyle='-', label = '1.1 um PA-C on rubber vs 3.6 um PA-C on soda lime wafer', color = '#2ca02cff')
# plt.plot(soda3_6um_srubber1_1um2df['travel'], soda3_6um_srubber1_1um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
# plt.plot(soda3_6um_srubber1_1um3df['travel'], soda3_6um_srubber1_1um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
# plt.plot(soda3_6um_srubber1_1um4df['travel'], soda3_6um_srubber1_1um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
# plt.plot(soda3_6um_srubber1_1um5df['travel'], soda3_6um_srubber1_1um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
# #
# plt.plot(soda3_6um_srubber3_6um1df['travel'], soda3_6um_srubber3_6um1df['load'], marker='.', linestyle='-', label = '3.6 um PA-C on rubber vs 3.6 um PA-C on soda lime wafer', color = '#d62728ff')
# plt.plot(soda3_6um_srubber3_6um2df['travel'], soda3_6um_srubber3_6um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#d62728ff')
# plt.plot(soda3_6um_srubber3_6um3df['travel'], soda3_6um_srubber3_6um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#d62728ff')
# plt.plot(soda3_6um_srubber3_6um4df['travel'], soda3_6um_srubber3_6um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#d62728ff')
# plt.plot(soda3_6um_srubber3_6um5df['travel'], soda3_6um_srubber3_6um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#d62728ff')
#
# plt.plot(soda3_6um_srubber7_3um1df['travel'], soda3_6um_srubber7_3um1df['load'], marker='.', linestyle='-', label = '7.3 um PA-C on rubber vs 3.6 um PA-C on soda lime wafer', color = '#9467bdff')
# plt.plot(soda3_6um_srubber7_3um2df['travel'], soda3_6um_srubber7_3um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#9467bdff')
# plt.plot(soda3_6um_srubber7_3um3df['travel'], soda3_6um_srubber7_3um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#9467bdff')
# plt.plot(soda3_6um_srubber7_3um4df['travel'], soda3_6um_srubber7_3um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#9467bdff')
# plt.plot(soda3_6um_srubber7_3um5df['travel'], soda3_6um_srubber7_3um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#9467bdff')
#
# plt.plot(soda3_6um_srubber8_9um1df['travel'], soda3_6um_srubber8_9um1df['load'], marker='.', linestyle='-', label = '8.9 um PA-C on rubber vs 3.6 um PA-C on soda lime wafer', color = '#8c564bff')
# plt.plot(soda3_6um_srubber8_9um2df['travel'], soda3_6um_srubber8_9um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#8c564bff')
# plt.plot(soda3_6um_srubber8_9um3df['travel'], soda3_6um_srubber8_9um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#8c564bff')
# plt.plot(soda3_6um_srubber8_9um4df['travel'], soda3_6um_srubber8_9um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#8c564bff')
# plt.plot(soda3_6um_srubber8_9um5df['travel'], soda3_6um_srubber8_9um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#8c564bff')

plt.plot(soda3_6um_srubber1_1umHT1df['travel'], soda3_6um_srubber1_1umHT1df['load'], marker='.', linestyle='-', label = '1.1 um PA-HT on rubber vs 3.6 um PA-C on soda lime wafer', color = '#1f77b4ff')
plt.plot(soda3_6um_srubber1_1umHT2df['travel'], soda3_6um_srubber1_1umHT2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')
plt.plot(soda3_6um_srubber1_1umHT3df['travel'], soda3_6um_srubber1_1umHT3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')
plt.plot(soda3_6um_srubber1_1umHT4df['travel'], soda3_6um_srubber1_1umHT4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')
plt.plot(soda3_6um_srubber1_1umHT5df['travel'], soda3_6um_srubber1_1umHT5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')

plt.plot(soda3_6um_srubber4_5umHT1df['travel'], soda3_6um_srubber4_5umHT1df['load'], marker='.', linestyle='-', label = '4.5 um PA-HT on rubber vs 3.6 um PA-C on soda lime wafer', color = '#ff7f0eff')
plt.plot(soda3_6um_srubber4_5umHT2df['travel'], soda3_6um_srubber4_5umHT2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')
plt.plot(soda3_6um_srubber4_5umHT3df['travel'], soda3_6um_srubber4_5umHT3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')
plt.plot(soda3_6um_srubber4_5umHT4df['travel'], soda3_6um_srubber4_5umHT4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')
plt.plot(soda3_6um_srubber4_5umHT5df['travel'], soda3_6um_srubber4_5umHT5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')

plt.plot(soda3_6um_srubber6_9umHT1df['travel'], soda3_6um_srubber6_9umHT1df['load'], marker='.', linestyle='-', label = '6.9 um PA-HT on rubber vs 3.6 um PA-C on soda lime wafer', color = '#2ca02cff')
plt.plot(soda3_6um_srubber6_9umHT2df['travel'], soda3_6um_srubber6_9umHT2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
plt.plot(soda3_6um_srubber6_9umHT3df['travel'], soda3_6um_srubber6_9umHT3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
plt.plot(soda3_6um_srubber6_9umHT4df['travel'], soda3_6um_srubber6_9umHT4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
plt.plot(soda3_6um_srubber6_9umHT5df['travel'], soda3_6um_srubber6_9umHT5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')



plt.ylim(-0.2, 4)
plt.xlim(-2, 50)
plt.margins(0.2)
plt.xlabel('Travel Distance (mm)', fontsize=20)#
plt.ylabel('Frictional Force (N)', fontsize=20)
plt.legend(loc = 'upper right' ,prop={'size':10})
plt.tick_params(axis='both', which='major', labelsize=16)#
#plt.title('load vs distance', fontsize=24)#

plt.show()
