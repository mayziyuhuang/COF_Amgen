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
load_gram_17 = 819.5


#sample: rubber pieces (small), substrate: teflon
#0 um PAC on small rubber(2cm*2cm) vs teflon, load = 656.8, load = 205.7
teflon_srubber0um1 = 'data/20171201_smallrubber_1_vs_teflon_656.8g_load_1.xlsx'
teflon_srubber0um1df = data.friction_data(teflon_srubber0um1, load_gram_14)
teflon_srubber0um2 = 'data/20171201_smallrubber_1_vs_teflon_205.7g_load_1.xlsx'
teflon_srubber0um2df = data.friction_data(teflon_srubber0um2, load_gram_16)

#0.2 um PAC on small rubber (2cm*2cm) vs teflon, load = 656.8
teflon_srubber0_2um1 = 'data/20171201_smallrubber_0.2um_1_vs_teflon_656.8g_load_2.xlsx'
teflon_srubber0_2um1df = data.friction_data(teflon_srubber0_2um1, load_gram_14)
teflon_srubber0_2um2 = 'data/20171201_smallrubber_0.2um_2_vs_teflon_656.8g_load_2.xlsx'
teflon_srubber0_2um2df = data.friction_data(teflon_srubber0_2um2, load_gram_14)
teflon_srubber0_2um3 = 'data/20171201_smallrubber_0.2um_3_vs_teflon_656.8g_load_2.xlsx'
teflon_srubber0_2um3df = data.friction_data(teflon_srubber0_2um3, load_gram_14)
teflon_srubber0_2um4 = 'data/20171201_smallrubber_0.2um_4_vs_teflon_656.8g_load_2.xlsx'
teflon_srubber0_2um4df = data.friction_data(teflon_srubber0_2um4, load_gram_14)

#0.6 um PAC on small rubber (2cm*2cm) vs teflon, load = 656.8
teflon_srubber0_6um1 = 'data/20171201_smallrubber_0.6um_1_vs_teflon_656.8g_load_1.xlsx'
teflon_srubber0_6um1df = data.friction_data(teflon_srubber0_6um1, load_gram_14)
teflon_srubber0_6um2 = 'data/20171201_smallrubber_0.6um_2_vs_teflon_656.8g_load_1.xlsx'
teflon_srubber0_6um2df = data.friction_data(teflon_srubber0_6um2, load_gram_14)
teflon_srubber0_6um3 = 'data/20171201_smallrubber_0.6um_3_vs_teflon_656.8g_load_1.xlsx'
teflon_srubber0_6um3df = data.friction_data(teflon_srubber0_6um3, load_gram_14)
teflon_srubber0_6um4 = 'data/20171201_smallrubber_0.6um_4_vs_teflon_656.8g_load_1.xlsx'
teflon_srubber0_6um4df = data.friction_data(teflon_srubber0_6um4, load_gram_14)

#7.3 um PAC on small rubber (2cm*2cm) vs teflon, load = 656.8
teflon_srubber7_3um1 = 'data/20171201_smallrubber_7.3um_1_vs_teflon_656.8g_load_2.xlsx'
teflon_srubber7_3um1df = data.friction_data(teflon_srubber7_3um1, load_gram_14)
teflon_srubber7_3um2 = 'data/20171201_smallrubber_7.3um_2_vs_teflon_656.8g_load_2.xlsx'
teflon_srubber7_3um2df = data.friction_data(teflon_srubber7_3um2, load_gram_14)
teflon_srubber7_3um3 = 'data/20171201_smallrubber_7.3um_3_vs_teflon_656.8g_load_2.xlsx'
teflon_srubber7_3um3df = data.friction_data(teflon_srubber7_3um3, load_gram_14)
teflon_srubber7_3um4 = 'data/20171201_smallrubber_7.3um_4_vs_teflon_656.8g_load_2.xlsx'
teflon_srubber7_3um4df = data.friction_data(teflon_srubber7_3um4, load_gram_14)
teflon_srubber7_3um5 = 'data/20171201_smallrubber_7.3um_5_vs_teflon_656.8g_load_2.xlsx'
teflon_srubber7_3um5df = data.friction_data(teflon_srubber7_3um5, load_gram_14)

#sample: teflon block, substrate: teflon
#teflon vs teflon, load = 819.5
teflon_teflon1 = 'data/20171201_teflon_vs_teflon_819.5g_load_1.xlsx'
teflon_teflon1df = data.friction_data(teflon_teflon1, load_gram_17)
teflon_teflon2 = 'data/20171201_teflon_vs_teflon_819.5g_load_2.xlsx'
teflon_teflon2df = data.friction_data(teflon_teflon2, load_gram_17)



plt.plot(teflon_srubber0um1df['travel'], teflon_srubber0um1df['load'], marker='.', linestyle='-', label = 'rubber vs teflon', color = 'k')
plt.plot(teflon_srubber0um2df['travel'], teflon_srubber0um2df['load']*load_gram_14/load_gram_16, marker='.', linestyle='-', label = '_nolegend_', color = 'k')


plt.plot(teflon_srubber0_2um1df['travel'], teflon_srubber0_2um1df['load'], marker='.', linestyle='-', label = '0.2 um PA-C on rubber vs teflon', color = '#1f77b4ff')
plt.plot(teflon_srubber0_2um2df['travel'], teflon_srubber0_2um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')
plt.plot(teflon_srubber0_2um3df['travel'], teflon_srubber0_2um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')
plt.plot(teflon_srubber0_2um4df['travel'], teflon_srubber0_2um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')

plt.plot(teflon_srubber0_6um1df['travel'], teflon_srubber0_6um1df['load'], marker='.', linestyle='-', label = '0.6 um PA-C on rubber vs teflon', color = '#ff7f0eff')
plt.plot(teflon_srubber0_6um2df['travel'], teflon_srubber0_6um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')
plt.plot(teflon_srubber0_6um3df['travel'], teflon_srubber0_6um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')
plt.plot(teflon_srubber0_6um4df['travel'], teflon_srubber0_6um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')

# plt.plot(teflon_srubber1_1um1df['travel'], teflon_srubber1_1um1df['load'], marker='.', linestyle='-', label = '1.1 um PA-C on rubber vs teflon', color = '#2ca02cff')
# plt.plot(teflon_srubber1_1um2df['travel'], teflon_srubber1_1um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
# plt.plot(teflon_srubber1_1um3df['travel'], teflon_srubber1_1um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
# plt.plot(teflon_srubber1_1um4df['travel'], teflon_srubber1_1um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
# plt.plot(teflon_srubber1_1um5df['travel'], teflon_srubber1_1um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
#
# plt.plot(teflon_srubber3_6um1df['travel'], teflon_srubber3_6um1df['load'], marker='.', linestyle='-', label = '3.6 um PA-C on rubber vs teflon', color = '#d62728ff')
# plt.plot(teflon_srubber3_6um2df['travel'], teflon_srubber3_6um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#d62728ff')
# plt.plot(teflon_srubber3_6um3df['travel'], teflon_srubber3_6um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#d62728ff')
# plt.plot(teflon_srubber3_6um4df['travel'], teflon_srubber3_6um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#d62728ff')
# plt.plot(teflon_srubber3_6um5df['travel'], teflon_srubber3_6um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#d62728ff')
# #
# plt.plot(teflon_srubber5_4um1df['travel'], teflon_srubber5_4um1df['load'], marker='.', linestyle='-', label = '5.4 um PA-C on rubber vs teflon', color = '#e2e200')
# plt.plot(teflon_srubber5_4um2df['travel'], teflon_srubber5_4um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#e2e200')
# plt.plot(teflon_srubber5_4um3df['travel'], teflon_srubber5_4um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#e2e200')
# plt.plot(teflon_srubber5_4um4df['travel'], teflon_srubber5_4um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#e2e200')

plt.plot(teflon_srubber7_3um1df['travel'], teflon_srubber7_3um1df['load'], marker='.', linestyle='-', label = '7.3 um PA-C on rubber vs teflon', color = '#9467bdff')
plt.plot(teflon_srubber7_3um2df['travel'], teflon_srubber7_3um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#9467bdff')
plt.plot(teflon_srubber7_3um3df['travel'], teflon_srubber7_3um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#9467bdff')
plt.plot(teflon_srubber7_3um4df['travel'], teflon_srubber7_3um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#9467bdff')
plt.plot(teflon_srubber7_3um5df['travel'], teflon_srubber7_3um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#9467bdff')

# plt.plot(teflon_srubber8_9um1df['travel'], teflon_srubber8_9um1df['load'], marker='.', linestyle='-', label = '8.9 um PA-C on rubber vs teflon', color = '#8c564bff')
# plt.plot(teflon_srubber8_9um2df['travel'], teflon_srubber8_9um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#8c564bff')
# plt.plot(teflon_srubber8_9um3df['travel'], teflon_srubber8_9um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#8c564bff')
# plt.plot(teflon_srubber8_9um4df['travel'], teflon_srubber8_9um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#8c564bff')
# plt.plot(teflon_srubber8_9um5df['travel'], teflon_srubber8_9um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#8c564bff')

plt.plot(teflon_teflon1df['travel'], teflon_teflon1df['load'], marker='.', linestyle='-', label = 'teflon vs teflon', color = '#e2e200')
plt.plot(teflon_teflon2df['travel'], teflon_teflon2df['load']*load_gram_14/load_gram_17, marker='.', linestyle='-', label = '_nolegend_', color = '#e2e200')


plt.ylim(-0.2, 7)
# plt.ylim(-0.2, 3.5)
plt.xlim(-2, 110)
plt.margins(0.2)
plt.xlabel('Travel Distance (mm)', fontsize=20)#
plt.ylabel('Frictional Force (N)', fontsize=20)
plt.legend(loc = 'upper right' ,prop={'size':10})
plt.tick_params(axis='both', which='major', labelsize=16)#
#plt.title('load vs distance', fontsize=24)#

plt.show()
