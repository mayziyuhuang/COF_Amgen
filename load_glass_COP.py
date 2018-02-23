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

#1.1 um PAC on glass vs COP, load = 657.8
COP1um1 = 'data/20171003_PAC1.1umglass_7_vs_COP_657.8g_load_1.xlsx'
COP1um1df = data.friction_data(COP1um1, load_gram_1)
COP1um2 = 'data/20171003_PAC1.1umglass_8_vs_COP_657.8g_load_1.xlsx'
COP1um2df = data.friction_data(COP1um2, load_gram_1)
COP1um3 = 'data/20171003_PAC1.1umglass_9_vs_COP_657.8g_load_1.xlsx'
COP1um3df = data.friction_data(COP1um3, load_gram_1)
COP1um4 = 'data/20171003_PAC1.1umglass_10_vs_COP_657.8g_load_1.xlsx'
COP1um4df = data.friction_data(COP1um4, load_gram_1)
COP1um5 = 'data/20171003_PAC1.1umglass_11_vs_COP_657.8g_load_1.xlsx'
COP1um5df = data.friction_data(COP1um5, load_gram_1)

#3.3um PAC on glass vs COP, load = 657.8
COP3um1 = 'data/20171003_PAC3.3umglass_3_vs_COP_657.8g_load_1.xlsx'
COP3um1df = data.friction_data(COP3um1, load_gram_1)
COP3um2 = 'data/20171003_PAC3.3umglass_5_vs_COP_657.8g_load_1.xlsx'
COP3um2df = data.friction_data(COP3um2, load_gram_1)
COP3um3 = 'data/20171003_PAC3.3umglass_6_vs_COP_657.8g_load_1.xlsx'
COP3um3df = data.friction_data(COP3um3, load_gram_1)
COP3um4 = 'data/20171003_PAC3.3umglass_7_vs_COP_657.8g_load_1.xlsx'
COP3um4df = data.friction_data(COP3um4, load_gram_1)
COP3um5 = 'data/20171003_PAC3.3umglass_9_vs_COP_657.8g_load_1.xlsx'
COP3um5df = data.friction_data(COP3um5, load_gram_1)

#0.1 um PAC on glass vs COP, load = 657.4
COP0_1um1 = 'data/20171006_PAC_0.1um_6_vs_COP_657.4g_load_1.xlsx'
COP0_1um1df = data.friction_data(COP0_1um1, load_gram_2)
COP0_1um2 = 'data/20171006_PAC_0.1um_7_vs_COP_657.4g_load_1.xlsx'
COP0_1um2df = data.friction_data(COP0_1um2, load_gram_2)
COP0_1um3 = 'data/20171006_PAC_0.1um_8_vs_COP_657.4g_load_1.xlsx'
COP0_1um3df = data.friction_data(COP0_1um3, load_gram_2)
COP0_1um4 = 'data/20171006_PAC_0.1um_9_vs_COP_657.4g_load_1.xlsx'
COP0_1um4df = data.friction_data(COP0_1um4, load_gram_2)
COP0_1um5 = 'data/20171006_PAC_0.1um_10_vs_COP_657.4g_load_1.xlsx'
COP0_1um5df = data.friction_data(COP0_1um5, load_gram_2)

#5.6 um PAHT on glass vs COP, load = 657.4
COP5_6umHT1 = 'data/20171006_HT5.6um_6_vs_COP_657.4g_load_1.xlsx'
COP5_6umHT1df = data.friction_data(COP5_6umHT1, load_gram_2)
COP5_6umHT2 = 'data/20171006_HT5.6um_7_vs_COP_657.4g_load_1.xlsx'
COP5_6umHT2df = data.friction_data(COP5_6umHT2, load_gram_2)
COP5_6umHT3 = 'data/20171006_HT5.6um_8_vs_COP_657.4g_load_1.xlsx'
COP5_6umHT3df = data.friction_data(COP5_6umHT3, load_gram_2)
COP5_6umHT4 = 'data/20171006_HT5.6um_9_vs_COP_657.4g_load_1.xlsx'
COP5_6umHT4df = data.friction_data(COP5_6umHT4, load_gram_2)
COP5_6umHT5 = 'data/20171006_HT5.6um_10_vs_COP_657.4g_load_1.xlsx'
COP5_6umHT5df = data.friction_data(COP5_6umHT5, load_gram_2)

#bare glass (0um) vs COP, load = 657.4
COP0um1 = 'data/20171006_glass_6_vs_COP_657.4g_load_1.xlsx'
COP0um1df = data.friction_data(COP0um1, load_gram_2)
COP0um2 = 'data/20171006_glass_7_vs_COP_657.4g_load_1.xlsx'
COP0um2df = data.friction_data(COP0um2, load_gram_2)
COP0um3 = 'data/20171006_glass_8_vs_COP_657.4g_load_1.xlsx'
COP0um3df = data.friction_data(COP0um3, load_gram_2)
COP0um4 = 'data/20171006_glass_9_vs_COP_657.4g_load_1.xlsx'
COP0um4df = data.friction_data(COP0um4, load_gram_2)
COP0um5 = 'data/20171006_glass_10_vs_COP_657.4g_load_1.xlsx'
COP0um5df = data.friction_data(COP0um5, load_gram_2)

#5.9 um PAC on glass vs COP, load = 657.2
COP5_9um1 = 'data/20171009_PAC_5.9umglass_6_vs_COP_657.2g_load_1.xlsx'
COP5_9um1df = data.friction_data(COP5_9um1, load_gram_4)
COP5_9um2 = 'data/20171009_PAC_5.9umglass_7_vs_COP_657.2g_load_1.xlsx'
COP5_9um2df = data.friction_data(COP5_9um2, load_gram_4)
COP5_9um3 = 'data/20171009_PAC_5.9umglass_8_vs_COP_657.2g_load_1.xlsx'
COP5_9um3df = data.friction_data(COP5_9um3, load_gram_4)
COP5_9um4 = 'data/20171009_PAC_5.9umglass_9_vs_COP_657.2g_load_1.xlsx'
COP5_9um4df = data.friction_data(COP5_9um4, load_gram_4)
COP5_9um5 = 'data/20171009_PAC_5.9umglass_12_vs_COP_657.2g_load_1.xlsx'
COP5_9um5df = data.friction_data(COP5_9um5, load_gram_4)


# plt.plot(COP0um1df['travel'], COP0um1df['load'], marker='.', linestyle='-', label = 'glass (0 um PA-C) vs COP', color = '#1f77b4ff')
# plt.plot(COP0um2df['travel'], COP0um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')
# plt.plot(COP0um3df['travel'], COP0um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')
# plt.plot(COP0um4df['travel'], COP0um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')
# plt.plot(COP0um5df['travel'], COP0um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')

# plt.plot(COP0_1um1df['travel'], COP0_1um1df['load'], marker='.', linestyle='-', label = '0.1 um PA-C on glass vs COP', color = '#ff7f0eff')
# plt.plot(COP0_1um2df['travel'], COP0_1um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')
# plt.plot(COP0_1um3df['travel'], COP0_1um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')
# plt.plot(COP0_1um4df['travel'], COP0_1um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')
# plt.plot(COP0_1um5df['travel'], COP0_1um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')

# plt.plot(COP1um1df['travel'], COP1um1df['load'], marker='.', linestyle='-', label = '1.1 um PA-C on glass vs COP', color = '#2ca02cff')
# plt.plot(COP1um2df['travel'], COP1um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
# plt.plot(COP1um3df['travel'], COP1um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
# plt.plot(COP1um4df['travel'], COP1um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
# plt.plot(COP1um5df['travel'], COP1um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')

# plt.plot(COP3um1df['travel'], COP3um1df['load'], marker='.', linestyle='-', label = '3.3 um PA-C on glass vs COP', color = '#d62728ff')
# plt.plot(COP3um2df['travel'], COP3um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#d62728ff')
# plt.plot(COP3um3df['travel'], COP3um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#d62728ff')
# plt.plot(COP3um4df['travel'], COP3um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#d62728ff')
# plt.plot(COP3um5df['travel'], COP3um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#d62728ff')

# plt.plot(COP5_9um1df['travel'], COP5_9um1df['load'], marker='.', linestyle='-', label = '5.9 um PA-C on glass vs COP', color = '#9467bdff')
# plt.plot(COP5_9um2df['travel'], COP5_9um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#9467bdff')
# plt.plot(COP5_9um3df['travel'], COP5_9um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#9467bdff')
# plt.plot(COP5_9um4df['travel'], COP5_9um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#9467bdff')
# plt.plot(COP5_9um5df['travel'], COP5_9um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#9467bdff')

plt.plot(COP5_6umHT1df['travel'], COP5_6umHT1df['load'], marker='.', linestyle='-', label = '5.6 um PA-HT on glass vs COP', color = '#8c564bff')
plt.plot(COP5_6umHT2df['travel'], COP5_6umHT2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#8c564bff')
plt.plot(COP5_6umHT3df['travel'], COP5_6umHT3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#8c564bff')
plt.plot(COP5_6umHT4df['travel'], COP5_6umHT4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#8c564bff')
plt.plot(COP5_6umHT5df['travel'], COP5_6umHT5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#8c564bff')



plt.ylim(-0.2, 3.0)
plt.xlim(-2, 110)
plt.margins(0.2)
plt.xlabel('Travel Distance (mm)', fontsize=20)#
plt.ylabel('Frictional Force (N)', fontsize=20)
plt.legend(loc = 'upper right' ,prop={'size':10})
plt.tick_params(axis='both', which='major', labelsize=16)#
#plt.title('load vs distance', fontsize=24)#

plt.show()
