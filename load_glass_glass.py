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

#1.1um PAC on glass vs glass, load = 657.8
glass1um1 = 'data/20171003_PAC1.1umglass_1_vs_glass_657.8g_load_1.xlsx'
glass1um1df = data.friction_data(glass1um1, load_gram_1)
glass1um2 = 'data/20171003_PAC1.1umglass_2_vs_glass_657.8g_load_1.xlsx'
glass1um2df = data.friction_data(glass1um2, load_gram_1)
glass1um3 = 'data/20171003_PAC1.1umglass_3_vs_glass_657.8g_load_1.xlsx'
glass1um3df = data.friction_data(glass1um3, load_gram_1)
glass1um4 = 'data/20171003_PAC1.1umglass_4_vs_glass_657.8g_load_1.xlsx'
glass1um4df = data.friction_data(glass1um4, load_gram_1)
glass1um5 = 'data/20171003_PAC1.1umglass_5_vs_glass_657.8g_load_1.xlsx'
glass1um5df = data.friction_data(glass1um5, load_gram_1)

#3.3um PAC on glass vs glass, load = 657.8
glass3um1 = 'data/20171003_PAC3.3umglass_1_vs_glass_657.8g_load_1.xlsx'
glass3um1df = data.friction_data(glass3um1, load_gram_1)
glass3um2 = 'data/20171003_PAC3.3umglass_2_vs_glass_657.8g_load_1.xlsx'
glass3um2df = data.friction_data(glass3um2, load_gram_1)
glass3um3 = 'data/20171003_PAC3.3umglass_3_vs_glass_657.8g_load_1.xlsx'
glass3um3df = data.friction_data(glass3um3, load_gram_1)
glass3um4 = 'data/20171003_PAC3.3umglass_4_vs_glass_657.8g_load_1.xlsx'
glass3um4df = data.friction_data(glass3um4, load_gram_1)
glass3um5 = 'data/20171003_PAC3.3umglass_5_vs_glass_657.8g_load_1.xlsx'
glass3um5df = data.friction_data(glass3um5, load_gram_1)

#0.1 um PAC on glass vs glass, load = 657.4
glass0_1um1 = 'data/20171006_PAC0.1umglass_1_vs_glass_657.4g_load_1.xlsx'
glass0_1um1df = data.friction_data(glass0_1um1, load_gram_2)
glass0_1um2 = 'data/20171006_PAC0.1umglass_2_vs_glass_657.4g_load_1.xlsx'
glass0_1um2df = data.friction_data(glass0_1um2, load_gram_2)
glass0_1um3 = 'data/20171006_PAC0.1umglass_3_vs_glass_657.4g_load_1.xlsx'
glass0_1um3df = data.friction_data(glass0_1um3, load_gram_2)
glass0_1um4 = 'data/20171006_PAC0.1umglass_4_vs_glass_657.4g_load_1.xlsx'
glass0_1um4df = data.friction_data(glass0_1um4, load_gram_2)
glass0_1um5 = 'data/20171006_PAC0.1umglass_5_vs_glass_657.4g_load_1.xlsx'
glass0_1um5df = data.friction_data(glass0_1um5, load_gram_2)

#5.6 um PAHT on glass vs glass, load = 657.4
glass5_6umHT1 = 'data/20171006_HT5.6um_glass_1_vs_glass_657.4g_load_1.xlsx'
glass5_6umHT1df = data.friction_data(glass5_6umHT1, load_gram_2)
glass5_6umHT2 = 'data/20171006_HT5.6um_glass_2_vs_glass_657.4g_load_1.xlsx'
glass5_6umHT2df = data.friction_data(glass5_6umHT2, load_gram_2)
glass5_6umHT3 = 'data/20171006_HT5.6um_glass_3_vs_glass_657.4g_load_1.xlsx'
glass5_6umHT3df = data.friction_data(glass5_6umHT3, load_gram_2)
glass5_6umHT4 = 'data/20171006_HT5.6um_glass_4_vs_glass_657.4g_load_1.xlsx'
glass5_6umHT4df = data.friction_data(glass5_6umHT4, load_gram_2)
glass5_6umHT5 = 'data/20171006_HT5.6um_glass_5_vs_glass_657.4g_load_1.xlsx'
glass5_6umHT5df = data.friction_data(glass5_6umHT5, load_gram_2)

#bare glass (0um) vs glass, load = 657.4
glass0um1 = 'data/20171006_bare_glass_1_vs_glass_657.4g_load_1.xlsx'
glass0um1df = data.friction_data(glass0um1, load_gram_2)
glass0um2 = 'data/20171006_bare_glass_2_vs_glass_657.4g_load_1.xlsx'
glass0um2df = data.friction_data(glass0um2, load_gram_2)
glass0um3 = 'data/20171006_bare_glass_3_vs_glass_657.4g_load_1.xlsx'
glass0um3df = data.friction_data(glass0um3, load_gram_2)
glass0um4 = 'data/20171006_bare_glass_4_vs_glass_657.4g_load_1.xlsx'
glass0um4df = data.friction_data(glass0um4, load_gram_2)
glass0um5 = 'data/20171006_bare_glass_5_vs_glass_657.4g_load_1.xlsx'
glass0um5df = data.friction_data(glass0um5, load_gram_2)

#5.9 um PAC on glass vs glass, load = 657.2
glass5_9um1 = 'data/20171009_PAC_5.9umglass_1_vs_glass_657.2g_load_1.xlsx'
glass5_9um1df = data.friction_data(glass5_9um1, load_gram_4)
glass5_9um2 = 'data/20171009_PAC_5.9umglass_2_vs_glass_657.2g_load_1.xlsx'
glass5_9um2df = data.friction_data(glass5_9um2, load_gram_4)
glass5_9um3 = 'data/20171009_PAC_5.9umglass_3_vs_glass_657.2g_load_1.xlsx'
glass5_9um3df = data.friction_data(glass5_9um3, load_gram_4)
glass5_9um4 = 'data/20171009_PAC_5.9umglass_4_vs_glass_657.2g_load_1.xlsx'
glass5_9um4df = data.friction_data(glass5_9um4, load_gram_4)
glass5_9um5 = 'data/20171009_PAC_5.9umglass_5_vs_glass_657.2g_load_1.xlsx'
glass5_9um5df = data.friction_data(glass5_9um5, load_gram_4)

#
# plt.plot(glass0um1df['travel'], glass0um1df['load'], marker='.', linestyle='-', label = 'glass (0 um PA-C) vs glass', color = '#1f77b4ff')
# plt.plot(glass0um2df['travel'], glass0um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')
# plt.plot(glass0um3df['travel'], glass0um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')
# plt.plot(glass0um4df['travel'], glass0um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')
# plt.plot(glass0um5df['travel'], glass0um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')

# plt.plot(glass0_1um1df['travel'], glass0_1um1df['load'], marker='.', linestyle='-', label = '0.1 um PA-C on glass vs glass', color = '#ff7f0eff')
# plt.plot(glass0_1um2df['travel'], glass0_1um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')
# plt.plot(glass0_1um3df['travel'], glass0_1um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')
# plt.plot(glass0_1um4df['travel'], glass0_1um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')
# plt.plot(glass0_1um5df['travel'], glass0_1um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')
#
# plt.plot(glass1um1df['travel'], glass1um1df['load'], marker='.', linestyle='-', label = '1.1 um PA-C on glass vs glass', color = '#2ca02cff')
# plt.plot(glass1um2df['travel'], glass1um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
# plt.plot(glass1um3df['travel'], glass1um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
# plt.plot(glass1um4df['travel'], glass1um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
# plt.plot(glass1um5df['travel'], glass1um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
#
# plt.plot(glass3um1df['travel'], glass3um1df['load'], marker='.', linestyle='-', label = '3.3 um PA-C on glass vs glass', color = '#d62728ff')
# plt.plot(glass3um2df['travel'], glass3um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#d62728ff')
# plt.plot(glass3um3df['travel'], glass3um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#d62728ff')
# plt.plot(glass3um4df['travel'], glass3um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#d62728ff')
# plt.plot(glass3um5df['travel'], glass3um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#d62728ff')
# #
# plt.plot(glass5_9um1df['travel'], glass5_9um1df['load'], marker='.', linestyle='-', label = '5.9 um PA-C on glass vs glass', color = '#9467bdff')
# plt.plot(glass5_9um2df['travel'], glass5_9um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#9467bdff')
# plt.plot(glass5_9um3df['travel'], glass5_9um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#9467bdff')
# plt.plot(glass5_9um4df['travel'], glass5_9um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#9467bdff')
# plt.plot(glass5_9um5df['travel'], glass5_9um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#9467bdff')

plt.plot(glass5_6umHT1df['travel'], glass5_6umHT1df['load'], marker='.', linestyle='-', label = '5.6 um PA-HT on glass vs glass', color = '#8c564bff')
plt.plot(glass5_6umHT2df['travel'], glass5_6umHT2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#8c564bff')
plt.plot(glass5_6umHT3df['travel'], glass5_6umHT3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#8c564bff')
plt.plot(glass5_6umHT4df['travel'], glass5_6umHT4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#8c564bff')
plt.plot(glass5_6umHT5df['travel'], glass5_6umHT5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#8c564bff')



plt.ylim(-0.1, 1.5)
plt.xlim(-2, 110)
plt.margins(0.2)
plt.xlabel('Travel Distance (mm)', fontsize=20)#
plt.ylabel('Frictional Force (N)', fontsize=20)
plt.legend(loc = 'upper right' ,prop={'size':10})
plt.tick_params(axis='both', which='major', labelsize=16)#
#plt.title('load vs distance', fontsize=24)#

plt.show()
