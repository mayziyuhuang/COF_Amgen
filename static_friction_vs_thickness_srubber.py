import numpy as np
import scipy.special

import matplotlib
matplotlib.use
import matplotlib.pyplot as plt
plt.style.use('seaborn-talk')

import pandas as pd

import friction_functions as data

excel_file = pd.ExcelFile('data/friction_data.xlsx')
df = excel_file.parse('mean_std_noncontinuous')

df_soda = df[df['substrate'] == 'soda lime']
df_soda_srubber = df_soda[df_soda['sample_material'] == 'rubber_sheet']
df_soda_srubber_PAC = df_soda_srubber[df_soda_srubber['parylene_type'] != 'PAHT']
df_soda_srubber_PAHT = df_soda_srubber[df_soda_srubber['parylene_type'] == 'PAHT']


df_c = df[df['substrate'] == 'COP']
df_c_r = df_c[df_c['sample_material'] == 'rubber_sheet']
df_c_sr = df_c_r[df_c_r['sample_size'] == 'small']
df_c_sr_PAC = df_c_sr[df_c_sr['parylene_type']!= 'PAHT']
df_c_sr_PAHT = df_c_sr[df_c_sr['parylene_type']== 'PAHT']

df_PAC_soda = df[df['substrate'] == 'soda lime 3.6 um PAC']
df_PAC_soda_srubber = df_PAC_soda[df_PAC_soda['sample_material'] == 'rubber_sheet']
df_PAC_soda_srubber_PAC = df_PAC_soda_srubber[df_PAC_soda_srubber['parylene_type'] != 'PAHT']
df_PAC_soda_srubber_PAHT = df_PAC_soda_srubber[df_PAC_soda_srubber['parylene_type'] == 'PAHT']

df_teflon = df[df['substrate'] == 'teflon']
df_teflon_srubber = df_teflon[df_teflon['sample_material'] == 'rubber_sheet']
df_teflon_srubber_PAC = df_teflon_srubber[df_teflon_srubber['parylene_type']!= 'PAHT']

df_teflon = df[df['substrate'] == 'teflon']
df_teflon_teflon = df_teflon[df_teflon['sample_material'] == 'teflon']

#x = [0, 0.1, 1.1, 3.3, 5.9]
#y = [0.11796, 0.11038, 0.11156, 0.11016, 0.10578]
#e = [0.007737, 0.011587, 0.014482, 0.020042, 0.011896]
#plt.errorbar(x, y, yerr=e, fmt='o')
plt.errorbar(df_soda_srubber_PAC['parylene_thickness'], df_soda_srubber_PAC['mean static'], yerr = df_soda_srubber_PAC['std static'], fmt='o', label = 'PA-C on gray rubber vs soda lime wafer', color = '#1f77b4ff')
plt.errorbar(df_soda_srubber_PAHT['parylene_thickness'], df_soda_srubber_PAHT['mean static'], yerr = df_soda_srubber_PAHT['std static'], fmt='s', label = 'PA-HT on gray rubber vs soda lime wafer', color = '#1f77b4ff')

plt.errorbar(df_PAC_soda_srubber_PAC['parylene_thickness'], df_PAC_soda_srubber_PAC['mean static'], yerr = df_PAC_soda_srubber_PAC['std static'], fmt='o', label = 'PA-C on gray rubber vs PA-C on soda lime wafer', color = '#ff7f0eff')
plt.errorbar(df_PAC_soda_srubber_PAHT['parylene_thickness'], df_PAC_soda_srubber_PAHT['mean static'], yerr = df_PAC_soda_srubber_PAHT['std static'], fmt='s', label = 'PA-HT on gray rubber vs PA-C on soda lime wafer', color = '#ff7f0eff')

# plt.errorbar(df_c_sr_PAC['parylene_thickness'], df_c_sr_PAC['mean static'], yerr = df_c_sr_PAC['std static'], fmt='o', label = 'PA-C on gray rubber vs COP', color ='#2ca02cff' )
# plt.errorbar(df_c_sr_PAHT['parylene_thickness'], df_c_sr_PAHT['mean static'], yerr = df_c_sr_PAHT['std static'], fmt='s', label = 'PA-HT on gray rubber vs COP', color ='#2ca02cff' )

plt.errorbar(df_teflon_srubber_PAC['parylene_thickness'], df_teflon_srubber_PAC['mean static'], yerr = df_teflon_srubber_PAC['std static'], fmt='o', label = 'PA-C on gray rubber vs teflon', color ='#d62728ff' )

# plt.errorbar(df_teflon_teflon['parylene_thickness'], df_teflon_teflon['mean static'], yerr = df_teflon_teflon['std static'], fmt='s', label = 'teflont vs teflon', color ='#e2e200' )


# df_g = df[df['substrate'] == 'glass']
# df_g_r = df_g[df_g['sample_material'] == 'rubber_sheet']
# df_g_r = df_g_r[df_g_r['sample_size'] == 'big']
# df_g_r_PAC = df_g_r[df_g_r['parylene_type']!= 'PAHT']
#
# df_c = df[df['substrate'] == 'COP']
# df_c_r = df_c[df_c['sample_material'] == 'rubber_sheet']
# df_c_r = df_c_r[df_c_r['sample_size'] == 'big']
# df_c_r_PAC = df_c_r[df_c_r['parylene_type']!= 'PAHT']


# plt.errorbar(df_g_r_PAC['parylene_thickness'], df_g_r_PAC['mean'], yerr = df_g_r_PAC['std'], fmt='o', label = 'PA-C on rubber sheet vs glass', color = '#2ca02cff')
# plt.errorbar(df_c_r_PAC['parylene_thickness'], df_c_r_PAC['mean'], yerr = df_c_r_PAC['std'], fmt='o', label = 'PA-C on rubber sheet vs COP', color = '#d62728ff')
#




plt.xlabel(r'Parylene Thickness ($\mu$m)', fontsize=20)
plt.ylabel('Static Friction Coefficient', fontsize=20)
plt.margins(0.2)
plt.ylim(0, 2)
#plt.ylim(0, 2.5)
plt.xlim(-0.5, 20)
plt.legend(loc = 'upper right' ,prop={'size':14})
plt.tick_params(axis='both', which='major', labelsize=16)#
#plt.title('friction coefficient vs thickness', fontsize=24)#

plt.show()
