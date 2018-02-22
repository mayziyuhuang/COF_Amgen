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
load_gram_18 = 655.5
load_gram_19 = 655
load_gram_20 = 205.6
load_gram_21 = 654
load_gram_22 = 205.4
load_gram_23 = 652.7
load_gram_24 = 652.5
load_gram_25 = 652
load_gram_26 = 205.3





# #sample: glass slide, substrate: glass (there is so sort of coating on both)
# #bare glass (0um) vs glass, load = 657.4
# glass0um1 = 'data/20171006_bare_glass_1_vs_glass_657.4g_load_1.xlsx'
# glass0um1df = data.friction_data(glass0um1, load_gram_2)
# glass0um2 = 'data/20171006_bare_glass_2_vs_glass_657.4g_load_1.xlsx'
# glass0um2df = data.friction_data(glass0um2, load_gram_2)
# glass0um3 = 'data/20171006_bare_glass_3_vs_glass_657.4g_load_1.xlsx'
# glass0um3df = data.friction_data(glass0um3, load_gram_2)
# glass0um4 = 'data/20171006_bare_glass_4_vs_glass_657.4g_load_1.xlsx'
# glass0um4df = data.friction_data(glass0um4, load_gram_2)
# glass0um5 = 'data/20171006_bare_glass_5_vs_glass_657.4g_load_1.xlsx'
# glass0um5df = data.friction_data(glass0um5, load_gram_2)
#
# #0.1 um PAC on glass vs glass, load = 657.4
# glass0_1um1 = 'data/20171006_PAC0.1umglass_1_vs_glass_657.4g_load_1.xlsx'
# glass0_1um1df = data.friction_data(glass0_1um1, load_gram_2)
# glass0_1um2 = 'data/20171006_PAC0.1umglass_2_vs_glass_657.4g_load_1.xlsx'
# glass0_1um2df = data.friction_data(glass0_1um2, load_gram_2)
# glass0_1um3 = 'data/20171006_PAC0.1umglass_3_vs_glass_657.4g_load_1.xlsx'
# glass0_1um3df = data.friction_data(glass0_1um3, load_gram_2)
# glass0_1um4 = 'data/20171006_PAC0.1umglass_4_vs_glass_657.4g_load_1.xlsx'
# glass0_1um4df = data.friction_data(glass0_1um4, load_gram_2)
# glass0_1um5 = 'data/20171006_PAC0.1umglass_5_vs_glass_657.4g_load_1.xlsx'
# glass0_1um5df = data.friction_data(glass0_1um5, load_gram_2)
#
# #1.1um PAC on glass vs glass, load = 657.8
# glass1um1 = 'data/20171003_PAC1.1umglass_1_vs_glass_657.8g_load_1.xlsx'
# glass1um1df = data.friction_data(glass1um1, load_gram_1)
# glass1um2 = 'data/20171003_PAC1.1umglass_2_vs_glass_657.8g_load_1.xlsx'
# glass1um2df = data.friction_data(glass1um2, load_gram_1)
# glass1um3 = 'data/20171003_PAC1.1umglass_3_vs_glass_657.8g_load_1.xlsx'
# glass1um3df = data.friction_data(glass1um3, load_gram_1)
# glass1um4 = 'data/20171003_PAC1.1umglass_4_vs_glass_657.8g_load_1.xlsx'
# glass1um4df = data.friction_data(glass1um4, load_gram_1)
# glass1um5 = 'data/20171003_PAC1.1umglass_5_vs_glass_657.8g_load_1.xlsx'
# glass1um5df = data.friction_data(glass1um5, load_gram_1)
#
# #3.3um PAC on glass vs glass, load = 657.8
# glass3um1 = 'data/20171003_PAC3.3umglass_1_vs_glass_657.8g_load_1.xlsx'
# glass3um1df = data.friction_data(glass3um1, load_gram_1)
# glass3um2 = 'data/20171003_PAC3.3umglass_2_vs_glass_657.8g_load_1.xlsx'
# glass3um2df = data.friction_data(glass3um2, load_gram_1)
# glass3um3 = 'data/20171003_PAC3.3umglass_3_vs_glass_657.8g_load_1.xlsx'
# glass3um3df = data.friction_data(glass3um3, load_gram_1)
# glass3um4 = 'data/20171003_PAC3.3umglass_4_vs_glass_657.8g_load_1.xlsx'
# glass3um4df = data.friction_data(glass3um4, load_gram_1)
# glass3um5 = 'data/20171003_PAC3.3umglass_5_vs_glass_657.8g_load_1.xlsx'
# glass3um5df = data.friction_data(glass3um5, load_gram_1)
#
# #5.9 um PAC on glass vs glass, load = 657.2
# glass5_9um1 = 'data/20171009_PAC_5.9umglass_1_vs_glass_657.2g_load_1.xlsx'
# glass5_9um1df = data.friction_data(glass5_9um1, load_gram_4)
# glass5_9um2 = 'data/20171009_PAC_5.9umglass_2_vs_glass_657.2g_load_1.xlsx'
# glass5_9um2df = data.friction_data(glass5_9um2, load_gram_4)
# glass5_9um3 = 'data/20171009_PAC_5.9umglass_3_vs_glass_657.2g_load_1.xlsx'
# glass5_9um3df = data.friction_data(glass5_9um3, load_gram_4)
# glass5_9um4 = 'data/20171009_PAC_5.9umglass_4_vs_glass_657.2g_load_1.xlsx'
# glass5_9um4df = data.friction_data(glass5_9um4, load_gram_4)
# glass5_9um5 = 'data/20171009_PAC_5.9umglass_5_vs_glass_657.2g_load_1.xlsx'
# glass5_9um5df = data.friction_data(glass5_9um5, load_gram_4)
#
# #5.6 um PAHT on glass vs glass, load = 657.4
# glass5_6umHT1 = 'data/20171006_HT5.6um_glass_1_vs_glass_657.4g_load_1.xlsx'
# glass5_6umHT1df = data.friction_data(glass5_6umHT1, load_gram_2)
# glass5_6umHT2 = 'data/20171006_HT5.6um_glass_2_vs_glass_657.4g_load_1.xlsx'
# glass5_6umHT2df = data.friction_data(glass5_6umHT2, load_gram_2)
# glass5_6umHT3 = 'data/20171006_HT5.6um_glass_3_vs_glass_657.4g_load_1.xlsx'
# glass5_6umHT3df = data.friction_data(glass5_6umHT3, load_gram_2)
# glass5_6umHT4 = 'data/20171006_HT5.6um_glass_4_vs_glass_657.4g_load_1.xlsx'
# glass5_6umHT4df = data.friction_data(glass5_6umHT4, load_gram_2)
# glass5_6umHT5 = 'data/20171006_HT5.6um_glass_5_vs_glass_657.4g_load_1.xlsx'
# glass5_6umHT5df = data.friction_data(glass5_6umHT5, load_gram_2)



# #sample: rubber strips (big), substrate: glass (coated)
# #bare rubber vs glass, load = 204.2
# glass_rubber0um1 = 'data/20171006_rubber_sheet_1_vs_glass_204.2g_load_1.xlsx'
# glass_rubber0um1df = data.friction_data(glass_rubber0um1, load_gram_3)
# glass_rubber0um2 = 'data/20171006_rubber_sheet_2_vs_glass_204.2g_load_1.xlsx'
# glass_rubber0um2df = data.friction_data(glass_rubber0um2, load_gram_3)
# glass_rubber0um3 = 'data/20171006_rubber_sheet_3_vs_glass_204.2g_load_1.xlsx'
# glass_rubber0um3df = data.friction_data(glass_rubber0um3, load_gram_3)
# glass_rubber0um4 = 'data/20171006_rubber_sheet_4_vs_glass_204.2g_load_1.xlsx'
# glass_rubber0um4df = data.friction_data(glass_rubber0um4, load_gram_3)
#
# #5.4 um PAC on rubber vs glass, load = 657.2
# glass_rubber5_4um1 = 'data/20171009_rubber_5.4um_1_vs_glass_657.2g_load_1.xlsx'
# glass_rubber5_4um1df = data.friction_data(glass_rubber5_4um1, load_gram_4)
# glass_rubber5_4um2 = 'data/20171009_rubber_5.4um_2_vs_glass_657.2g_load_1.xlsx'
# glass_rubber5_4um2df = data.friction_data(glass_rubber5_4um2, load_gram_4)
# glass_rubber5_4um3 = 'data/20171009_rubber_5.4um_3_vs_glass_657.2g_load_1.xlsx'
# glass_rubber5_4um3df = data.friction_data(glass_rubber5_4um3, load_gram_4)
# glass_rubber5_4um4 = 'data/20171009_rubber_5.4um_4_vs_glass_657.2g_load_1.xlsx'
# glass_rubber5_4um4df = data.friction_data(glass_rubber5_4um4, load_gram_4)



# #sample: rubber pieces (small), substrate: glass(coated)
# #5.4 um PAC on small rubber (2cm*2cm) vs glass, load = 657.2
# glass_srubber5_4um1 = 'data/20171009_small_rubber_5.4um_1_vs_glass_653.7g_load_1.xlsx'
# glass_srubber5_4um1df = data.friction_data(glass_rubber5_4um1, load_gram_4)
# glass_srubber5_4um2 = 'data/20171009_small_rubber_5.4um_2_vs_glass_653.7g_load_1.xlsx'
# glass_srubber5_4um2df = data.friction_data(glass_rubber5_4um2, load_gram_4)
# glass_srubber5_4um3 = 'data/20171009_small_rubber_5.4um_3_vs_glass_653.7g_load_1.xlsx'
# glass_srubber5_4um3df = data.friction_data(glass_rubber5_4um3, load_gram_4)
# glass_srubber5_4um4 = 'data/20171009_small_rubber_5.4um_4_vs_glass_653.7g_load_1.xlsx'
# glass_srubber5_4um4df = data.friction_data(glass_rubber5_4um4, load_gram_4)


# #sample: glass slide, substrate: COP
# #bare glass (0um) vs COP, load = 657.4
# COP0um1 = 'data/20171006_glass_6_vs_COP_657.4g_load_1.xlsx'
# COP0um1df = data.friction_data(COP0um1, load_gram_2)
# COP0um2 = 'data/20171006_glass_7_vs_COP_657.4g_load_1.xlsx'
# COP0um2df = data.friction_data(COP0um2, load_gram_2)
# COP0um3 = 'data/20171006_glass_8_vs_COP_657.4g_load_1.xlsx'
# COP0um3df = data.friction_data(COP0um3, load_gram_2)
# COP0um4 = 'data/20171006_glass_9_vs_COP_657.4g_load_1.xlsx'
# COP0um4df = data.friction_data(COP0um4, load_gram_2)
# COP0um5 = 'data/20171006_glass_10_vs_COP_657.4g_load_1.xlsx'
# COP0um5df = data.friction_data(COP0um5, load_gram_2)
#
# #0.1 um PAC on glass vs COP, load = 657.4
# COP0_1um1 = 'data/20171006_PAC_0.1um_6_vs_COP_657.4g_load_1.xlsx'
# COP0_1um1df = data.friction_data(COP0_1um1, load_gram_2)
# COP0_1um2 = 'data/20171006_PAC_0.1um_7_vs_COP_657.4g_load_1.xlsx'
# COP0_1um2df = data.friction_data(COP0_1um2, load_gram_2)
# COP0_1um3 = 'data/20171006_PAC_0.1um_8_vs_COP_657.4g_load_1.xlsx'
# COP0_1um3df = data.friction_data(COP0_1um3, load_gram_2)
# COP0_1um4 = 'data/20171006_PAC_0.1um_9_vs_COP_657.4g_load_1.xlsx'
# COP0_1um4df = data.friction_data(COP0_1um4, load_gram_2)
# COP0_1um5 = 'data/20171006_PAC_0.1um_10_vs_COP_657.4g_load_1.xlsx'
# COP0_1um5df = data.friction_data(COP0_1um5, load_gram_2)
#
# #1.1 um PAC on glass vs COP, load = 657.8
# COP1um1 = 'data/20171003_PAC1.1umglass_7_vs_COP_657.8g_load_1.xlsx'
# COP1um1df = data.friction_data(COP1um1, load_gram_1)
# COP1um2 = 'data/20171003_PAC1.1umglass_8_vs_COP_657.8g_load_1.xlsx'
# COP1um2df = data.friction_data(COP1um2, load_gram_1)
# COP1um3 = 'data/20171003_PAC1.1umglass_9_vs_COP_657.8g_load_1.xlsx'
# COP1um3df = data.friction_data(COP1um3, load_gram_1)
# COP1um4 = 'data/20171003_PAC1.1umglass_10_vs_COP_657.8g_load_1.xlsx'
# COP1um4df = data.friction_data(COP1um4, load_gram_1)
# COP1um5 = 'data/20171003_PAC1.1umglass_11_vs_COP_657.8g_load_1.xlsx'
# COP1um5df = data.friction_data(COP1um5, load_gram_1)
#
# #3.3um PAC on glass vs COP, load = 657.8
# COP3um1 = 'data/20171003_PAC3.3umglass_3_vs_COP_657.8g_load_1.xlsx'
# COP3um1df = data.friction_data(COP3um1, load_gram_1)
# COP3um2 = 'data/20171003_PAC3.3umglass_5_vs_COP_657.8g_load_1.xlsx'
# COP3um2df = data.friction_data(COP3um2, load_gram_1)
# COP3um3 = 'data/20171003_PAC3.3umglass_6_vs_COP_657.8g_load_1.xlsx'
# COP3um3df = data.friction_data(COP3um3, load_gram_1)
# COP3um4 = 'data/20171003_PAC3.3umglass_7_vs_COP_657.8g_load_1.xlsx'
# COP3um4df = data.friction_data(COP3um4, load_gram_1)
# COP3um5 = 'data/20171003_PAC3.3umglass_9_vs_COP_657.8g_load_1.xlsx'
# COP3um5df = data.friction_data(COP3um5, load_gram_1)
#
# #5.9 um PAC on glass vs COP, load = 657.2
# COP5_9um1 = 'data/20171009_PAC_5.9umglass_6_vs_COP_657.2g_load_1.xlsx'
# COP5_9um1df = data.friction_data(COP5_9um1, load_gram_4)
# COP5_9um2 = 'data/20171009_PAC_5.9umglass_7_vs_COP_657.2g_load_1.xlsx'
# COP5_9um2df = data.friction_data(COP5_9um2, load_gram_4)
# COP5_9um3 = 'data/20171009_PAC_5.9umglass_8_vs_COP_657.2g_load_1.xlsx'
# COP5_9um3df = data.friction_data(COP5_9um3, load_gram_4)
# COP5_9um4 = 'data/20171009_PAC_5.9umglass_9_vs_COP_657.2g_load_1.xlsx'
# COP5_9um4df = data.friction_data(COP5_9um4, load_gram_4)
# COP5_9um5 = 'data/20171009_PAC_5.9umglass_12_vs_COP_657.2g_load_1.xlsx'
# COP5_9um5df = data.friction_data(COP5_9um5, load_gram_4)
#
# #5.6 um PAHT on glass vs COP, load = 657.4
# COP5_6umHT1 = 'data/20171006_HT5.6um_6_vs_COP_657.4g_load_1.xlsx'
# COP5_6umHT1df = data.friction_data(COP5_6umHT1, load_gram_2)
# COP5_6umHT2 = 'data/20171006_HT5.6um_7_vs_COP_657.4g_load_1.xlsx'
# COP5_6umHT2df = data.friction_data(COP5_6umHT2, load_gram_2)
# COP5_6umHT3 = 'data/20171006_HT5.6um_8_vs_COP_657.4g_load_1.xlsx'
# COP5_6umHT3df = data.friction_data(COP5_6umHT3, load_gram_2)
# COP5_6umHT4 = 'data/20171006_HT5.6um_9_vs_COP_657.4g_load_1.xlsx'
# COP5_6umHT4df = data.friction_data(COP5_6umHT4, load_gram_2)
# COP5_6umHT5 = 'data/20171006_HT5.6um_10_vs_COP_657.4g_load_1.xlsx'
# COP5_6umHT5df = data.friction_data(COP5_6umHT5, load_gram_2)





# #sample: rubber strips (big), substrate: COP
# #bare rubber vs COP, load = 204.2
# COP_rubber0um1 = 'data/20171006_rubber_sheet_1_vs_COP_204.2g_load_1.xlsx'
# COP_rubber0um1df = data.friction_data(COP_rubber0um1, load_gram_3)
# COP_rubber0um2 = 'data/20171006_rubber_sheet_2_vs_COP_204.2g_load_1.xlsx'
# COP_rubber0um2df = data.friction_data(COP_rubber0um2, load_gram_3)
# COP_rubber0um3 = 'data/20171006_rubber_sheet_3_vs_COP_204.2g_load_1.xlsx'
# COP_rubber0um3df = data.friction_data(COP_rubber0um3, load_gram_3)
# COP_rubber0um4 = 'data/20171006_rubber_sheet_4_vs_COP_204.2g_load_1.xlsx'
# COP_rubber0um4df = data.friction_data(COP_rubber0um4, load_gram_3)
#
# #5.4 um PAC on rubber vs COP, load = 657.2
# COP_rubber5_4um1 = 'data/20171009_rubber_5.4um_1_vs_COP_657.2g_load_1.xlsx'
# COP_rubber5_4um1df = data.friction_data(COP_rubber5_4um1, load_gram_4)
# COP_rubber5_4um2 = 'data/20171009_rubber_5.4um_2_vs_COP_657.2g_load_1.xlsx'
# COP_rubber5_4um2df = data.friction_data(COP_rubber5_4um2, load_gram_4)
# COP_rubber5_4um3 = 'data/20171009_rubber_5.4um_3_vs_COP_657.2g_load_1.xlsx'
# COP_rubber5_4um3df = data.friction_data(COP_rubber5_4um3, load_gram_4)
# COP_rubber5_4um4 = 'data/20171009_rubber_5.4um_4_vs_COP_657.2g_load_1.xlsx'
# COP_rubber5_4um4df = data.friction_data(COP_rubber5_4um4, load_gram_4)


#sample: rubber pieces (small), substrate: COP
#0 um PAC on small rubber(2cm*2cm) vs COP, load = 205.5
COP_srubber0um1 = 'data/20171024_smallrubber_1_vs_COP_205.5g_load_1.xlsx'
COP_srubber0um1df = data.friction_data(COP_srubber0um1, load_gram_8)

#0.2 um PAC on small rubber (2cm*2cm) vs COP, load = 206
COP_srubber0_2um1 = 'data/20171121_smallrubber_0.2um_1_vs_COP_206.0g_load_1.xlsx'
COP_srubber0_2um1df = data.friction_data(COP_srubber0_2um1, load_gram_13)
COP_srubber0_2um2 = 'data/20171121_smallrubber_0.2um_2_vs_COP_206.0g_load_1.xlsx'
COP_srubber0_2um2df = data.friction_data(COP_srubber0_2um2, load_gram_13)
COP_srubber0_2um3 = 'data/20171121_smallrubber_0.2um_3_vs_COP_206.0g_load_1.xlsx'
COP_srubber0_2um3df = data.friction_data(COP_srubber0_2um3, load_gram_13)
COP_srubber0_2um4 = 'data/20171121_smallrubber_0.2um_4_vs_COP_206.0g_load_1.xlsx'
COP_srubber0_2um4df = data.friction_data(COP_srubber0_2um4, load_gram_13)

#0.6 um PAC on small rubber (2cm*2cm) vs COP, load = 205.9
COP_srubber0_6um1 = 'data/20171122_smallrubber_0.6um_1_vs_COP_205.9g_load_1.xlsx'
COP_srubber0_6um1df = data.friction_data(COP_srubber0_6um1, load_gram_15)
COP_srubber0_6um2 = 'data/20171122_smallrubber_0.6um_2_vs_COP_205.9g_load_1.xlsx'
COP_srubber0_6um2df = data.friction_data(COP_srubber0_6um2, load_gram_15)
COP_srubber0_6um3 = 'data/20171122_smallrubber_0.6um_3_vs_COP_205.9g_load_1.xlsx'
COP_srubber0_6um3df = data.friction_data(COP_srubber0_6um3, load_gram_15)
COP_srubber0_6um4 = 'data/20171122_smallrubber_0.6um_4_vs_COP_205.9g_load_1.xlsx'
COP_srubber0_6um4df = data.friction_data(COP_srubber0_6um4, load_gram_15)

#1.1 um PAC on small rubber (2cm*2cm) vs COP, load = 657.5
COP_srubber1_1um1 = 'data/20171024_smallrubber_1.1um_1_vs_COP_657.5g_load_1.xlsx'
COP_srubber1_1um1df = data.friction_data(COP_srubber1_1um1, load_gram_7)
COP_srubber1_1um2 = 'data/20171024_smallrubber_1.1um_2_vs_COP_657.5g_load_1.xlsx'
COP_srubber1_1um2df = data.friction_data(COP_srubber1_1um2, load_gram_7)
COP_srubber1_1um3 = 'data/20171024_smallrubber_1.1um_3_vs_COP_657.5g_load_1.xlsx'
COP_srubber1_1um3df = data.friction_data(COP_srubber1_1um3, load_gram_7)
COP_srubber1_1um4 = 'data/20171024_smallrubber_1.1um_4_vs_COP_657.5g_load_1.xlsx'
COP_srubber1_1um4df = data.friction_data(COP_srubber1_1um4, load_gram_7)
COP_srubber1_1um5 = 'data/20171024_smallrubber_1.1um_5_vs_COP_657.5g_load_1.xlsx'
COP_srubber1_1um5df = data.friction_data(COP_srubber1_1um5, load_gram_7)

#3.6 um PAC on small rubber (2cm*2cm) vs COP, load = 653
COP_srubber3_6um1 = 'data/20171019_smallrubber_3.6um_1_vs_COP_653g_load_1.xlsx'
COP_srubber3_6um1df = data.friction_data(COP_srubber3_6um1, load_gram_5)
COP_srubber3_6um2 = 'data/20171019_smallrubber_3.6um_2_vs_COP_653g_load_1.xlsx'
COP_srubber3_6um2df = data.friction_data(COP_srubber3_6um2, load_gram_5)
COP_srubber3_6um3 = 'data/20171019_smallrubber_3.6um_3_vs_COP_653g_load_1.xlsx'
COP_srubber3_6um3df = data.friction_data(COP_srubber3_6um3, load_gram_5)
COP_srubber3_6um4 = 'data/20171019_smallrubber_3.6um_4_vs_COP_653g_load_1.xlsx'
COP_srubber3_6um4df = data.friction_data(COP_srubber3_6um4, load_gram_5)
COP_srubber3_6um5 = 'data/20171019_smallrubber_3.6um_5_vs_COP_653g_load_1.xlsx'
COP_srubber3_6um5df = data.friction_data(COP_srubber3_6um5, load_gram_5)

#3.6 um PAC on small rubber (2cm*2cm) vs COP, load = 655
COP_srubber3_6um6 = 'data/20171214_smallrubber_3.6um_1_vs_COP_655g_load_1.xlsx'
COP_srubber3_6um6df = data.friction_data(COP_srubber3_6um6, load_gram_19)
COP_srubber3_6um7 = 'data/20171214_smallrubber_3.6um_2_vs_COP_655g_load_1.xlsx'
COP_srubber3_6um7df = data.friction_data(COP_srubber3_6um7, load_gram_19)
COP_srubber3_6um8 = 'data/20171214_smallrubber_3.6um_3_vs_COP_655g_load_1.xlsx'
COP_srubber3_6um8df = data.friction_data(COP_srubber3_6um8, load_gram_19)
COP_srubber3_6um9 = 'data/20171214_smallrubber_3.6um_4_vs_COP_655g_load_1.xlsx'
COP_srubber3_6um9df = data.friction_data(COP_srubber3_6um9, load_gram_19)



#5 um PAC on small rubber (2cm*2cm) vs COP, load = 655.5
COP_srubber5um1 = 'data/20171211_smallrubber_5um_1_vs_old-COP#2_655.5g_load_1.xlsx'
COP_srubber5um1df = data.friction_data(COP_srubber5um1, load_gram_18)
COP_srubber5um2 = 'data/20171211_smallrubber_5um_2_vs_old-COP#2_655.5g_load_1.xlsx'
COP_srubber5um2df = data.friction_data(COP_srubber5um2, load_gram_18)
COP_srubber5um3 = 'data/20171211_smallrubber_5um_3_vs_old-COP#2_655.5g_load_1.xlsx'
COP_srubber5um3df = data.friction_data(COP_srubber5um3, load_gram_18)
COP_srubber5um4 = 'data/20171211_smallrubber_5um_4_vs_old-COP#2_655.5g_load_1.xlsx'
COP_srubber5um4df = data.friction_data(COP_srubber5um4, load_gram_18)

#5.4 um PAC on small rubber (2cm*2cm) vs COP, load = 657.2
COP_srubber5_4um1 = 'data/20171009_small_rubber_5.4um_1_vs_COP_653.7g_load_1.xlsx'
COP_srubber5_4um1df = data.friction_data(COP_srubber5_4um1, load_gram_4)
COP_srubber5_4um2 = 'data/20171009_small_rubber_5.4um_2_vs_COP_653.7g_load_1.xlsx'
COP_srubber5_4um2df = data.friction_data(COP_srubber5_4um2, load_gram_4)
COP_srubber5_4um3 = 'data/20171009_small_rubber_5.4um_3_vs_COP_653.7g_load_1.xlsx'
COP_srubber5_4um3df = data.friction_data(COP_srubber5_4um3, load_gram_4)
COP_srubber5_4um4 = 'data/20171009_small_rubber_5.4um_4_vs_COP_653.7g_load_1.xlsx'
COP_srubber5_4um4df = data.friction_data(COP_srubber5_4um4, load_gram_4)

#7.3 um PAC on small rubber (2cm*2cm) vs COP, load = 656.8
COP_srubber7_3um1 = 'data/20171121_smallrubber_7.3um_1_vs_COP_656.8g_load_1.xlsx'
COP_srubber7_3um1df = data.friction_data(COP_srubber7_3um1, load_gram_14)
COP_srubber7_3um2 = 'data/20171121_smallrubber_7.3um_2_vs_COP_656.8g_load_1.xlsx'
COP_srubber7_3um2df = data.friction_data(COP_srubber7_3um2, load_gram_14)
COP_srubber7_3um3 = 'data/20171121_smallrubber_7.3um_3_vs_COP_656.8g_load_1.xlsx'
COP_srubber7_3um3df = data.friction_data(COP_srubber7_3um3, load_gram_14)
COP_srubber7_3um4 = 'data/20171121_smallrubber_7.3um_4_vs_COP_656.8g_load_1.xlsx'
COP_srubber7_3um4df = data.friction_data(COP_srubber7_3um4, load_gram_14)
COP_srubber7_3um5 = 'data/20171121_smallrubber_7.3um_5_vs_COP_656.8g_load_1.xlsx'
COP_srubber7_3um5df = data.friction_data(COP_srubber7_3um5, load_gram_14)

#8.9 um PAC on small rubber (2cm*2cm) vs COP, load = 657.1
COP_srubber8_9um1 = 'data/20171113_smallrubber_8.9um_1_vs_COP_657.1g_load_1.xlsx'
COP_srubber8_9um1df = data.friction_data(COP_srubber8_9um1, load_gram_11)
COP_srubber8_9um2 = 'data/20171113_smallrubber_8.9um_2_vs_COP_657.1g_load_1.xlsx'
COP_srubber8_9um2df = data.friction_data(COP_srubber8_9um2, load_gram_11)
COP_srubber8_9um3 = 'data/20171113_smallrubber_8.9um_3_vs_COP_657.1g_load_1.xlsx'
COP_srubber8_9um3df = data.friction_data(COP_srubber8_9um3, load_gram_11)
COP_srubber8_9um4 = 'data/20171113_smallrubber_8.9um_4_vs_COP_657.1g_load_1.xlsx'
COP_srubber8_9um4df = data.friction_data(COP_srubber8_9um4, load_gram_11)
COP_srubber8_9um5 = 'data/20171113_smallrubber_8.9um_5_vs_COP_657.1g_load_1.xlsx'
COP_srubber8_9um5df = data.friction_data(COP_srubber8_9um5, load_gram_11)

#15 um PAC on small rubber (2cm*2cm) vs COP, load = 655
COP_srubber15um1 = 'data/20171214_smallrubber_15um_1_vs_COP_655g_load_1.xlsx'
COP_srubber15um1df = data.friction_data(COP_srubber15um1, load_gram_19)
COP_srubber15um2 = 'data/20171214_smallrubber_15um_2_vs_COP_655g_load_1.xlsx'
COP_srubber15um2df = data.friction_data(COP_srubber15um2, load_gram_19)
COP_srubber15um3 = 'data/20171214_smallrubber_15um_3_vs_COP_655g_load_1.xlsx'
COP_srubber15um3df = data.friction_data(COP_srubber15um3, load_gram_19)
COP_srubber15um4 = 'data/20171214_smallrubber_15um_4_vs_COP_655g_load_1.xlsx'
COP_srubber15um4df = data.friction_data(COP_srubber15um4, load_gram_19)

#0.26 um PAHT on small rubber (2cm*2cm) vs COP, load =205.9
COP_srubber0_26umHT1 = 'data/20171211_smallrubber_0.26um_HT_1_vs_old-COP#2_205.9g_load_1.xlsx'
COP_srubber0_26umHT1df = data.friction_data(COP_srubber0_26umHT1, load_gram_15)
COP_srubber0_26umHT2 = 'data/20171211_smallrubber_0.26um_HT_2_vs_old-COP#2_205.9g_load_1.xlsx'
COP_srubber0_26umHT2df = data.friction_data(COP_srubber0_26umHT2, load_gram_15)
COP_srubber0_26umHT3 = 'data/20171211_smallrubber_0.26um_HT_3_vs_old-COP#2_205.9g_load_1.xlsx'
COP_srubber0_26umHT3df = data.friction_data(COP_srubber0_26umHT3, load_gram_15)
COP_srubber0_26umHT4 = 'data/20171211_smallrubber_0.26um_HT_4_vs_old-COP#2_205.9g_load_1.xlsx'
COP_srubber0_26umHT4df = data.friction_data(COP_srubber0_26umHT4, load_gram_15)

#0.64 um PAHT on small rubber (2cm*2cm) vs COP, load =205.9
COP_srubber0_64umHT1 = 'data/20171211_smallrubber_0.64um_HT_1_vs_old-COP#2_205.9g_load_1.xlsx'
COP_srubber0_64umHT1df = data.friction_data(COP_srubber0_64umHT1, load_gram_15)
COP_srubber0_64umHT2 = 'data/20171211_smallrubber_0.64um_HT_2_vs_old-COP#2_205.9g_load_1.xlsx'
COP_srubber0_64umHT2df = data.friction_data(COP_srubber0_64umHT2, load_gram_15)
COP_srubber0_64umHT3 = 'data/20171211_smallrubber_0.64um_HT_3_vs_old-COP#2_205.9g_load_1.xlsx'
COP_srubber0_64umHT3df = data.friction_data(COP_srubber0_64umHT3, load_gram_15)
COP_srubber0_64umHT4 = 'data/20171211_smallrubber_0.64um_HT_4_vs_old-COP#2_205.9g_load_1.xlsx'
COP_srubber0_64umHT4df = data.friction_data(COP_srubber0_64umHT4, load_gram_15)

#1.1 um PAHT on small rubber (2cm*2cm) vs COP, load =657.6
COP_srubber1_1umHT1 = 'data/20171031_smallrubber_1.1um_HT_1_vs_COP_657.6g_load_1.xlsx'
COP_srubber1_1umHT1df = data.friction_data(COP_srubber1_1umHT1, load_gram_9)
COP_srubber1_1umHT2 = 'data/20171031_smallrubber_1.1um_HT_2_vs_COP_657.6g_load_1.xlsx'
COP_srubber1_1umHT2df = data.friction_data(COP_srubber1_1umHT2, load_gram_9)
COP_srubber1_1umHT3 = 'data/20171031_smallrubber_1.1um_HT_3_vs_COP_657.6g_load_1.xlsx'
COP_srubber1_1umHT3df = data.friction_data(COP_srubber1_1umHT3, load_gram_9)
COP_srubber1_1umHT4 = 'data/20171031_smallrubber_1.1um_HT_4_vs_COP_657.6g_load_1.xlsx'
COP_srubber1_1umHT4df = data.friction_data(COP_srubber1_1umHT4, load_gram_9)
COP_srubber1_1umHT5 = 'data/20171031_smallrubber_1.1um_HT_5_vs_COP_657.6g_load_1.xlsx'
COP_srubber1_1umHT5df = data.friction_data(COP_srubber1_1umHT5, load_gram_9)

#4.5 um PAHT on small rubber (2cm*2cm) vs COP, load =657.1
COP_srubber4_5umHT1 = 'data/20171113_smallrubber_4.5um_HT_1_vs_COP_657.1g_load_1.xlsx'
COP_srubber4_5umHT1df = data.friction_data(COP_srubber4_5umHT1, load_gram_11)
COP_srubber4_5umHT2 = 'data/20171113_smallrubber_4.5um_HT_2_vs_COP_657.1g_load_1.xlsx'
COP_srubber4_5umHT2df = data.friction_data(COP_srubber4_5umHT2, load_gram_11)
COP_srubber4_5umHT3 = 'data/20171113_smallrubber_4.5um_HT_3_vs_COP_657.1g_load_1.xlsx'
COP_srubber4_5umHT3df = data.friction_data(COP_srubber4_5umHT3, load_gram_11)
COP_srubber4_5umHT4 = 'data/20171113_smallrubber_4.5um_HT_4_vs_COP_657.1g_load_1.xlsx'
COP_srubber4_5umHT4df = data.friction_data(COP_srubber4_5umHT4, load_gram_11)
COP_srubber4_5umHT5 = 'data/20171113_smallrubber_4.5um_HT_5_vs_COP_657.1g_load_1.xlsx'
COP_srubber4_5umHT5df = data.friction_data(COP_srubber4_5umHT5, load_gram_11)

#6.9 um PAHT on small rubber (2cm*2cm) vs COP, load =657.6
COP_srubber6_9umHT1 = 'data/20171113_smallrubber_6.9um_HT_1_vs_COP_657.1g_load_1.xlsx'
COP_srubber6_9umHT1df = data.friction_data(COP_srubber6_9umHT1, load_gram_11)
COP_srubber6_9umHT2 = 'data/20171113_smallrubber_6.9um_HT_2_vs_COP_657.1g_load_1.xlsx'
COP_srubber6_9umHT2df = data.friction_data(COP_srubber6_9umHT2, load_gram_11)
COP_srubber6_9umHT3 = 'data/20171113_smallrubber_6.9um_HT_3_vs_COP_657.1g_load_1.xlsx'
COP_srubber6_9umHT3df = data.friction_data(COP_srubber6_9umHT3, load_gram_11)
COP_srubber6_9umHT4 = 'data/20171113_smallrubber_6.9um_HT_4_vs_COP_657.1g_load_1.xlsx'
COP_srubber6_9umHT4df = data.friction_data(COP_srubber6_9umHT4, load_gram_11)
COP_srubber6_9umHT5 = 'data/20171113_smallrubber_6.9um_HT_5_vs_COP_657.1g_load_1.xlsx'
COP_srubber6_9umHT5df = data.friction_data(COP_srubber6_9umHT5, load_gram_11)

#19 um PAC on small rubber (2cm*2cm) vs COP, load = 655
COP_srubber19umHT1 = 'data/20171214_smallrubber_19um_HT_1_vs_COP_655g_load_1.xlsx'
COP_srubber19umHT1df = data.friction_data(COP_srubber19umHT1, load_gram_19)
COP_srubber19umHT2 = 'data/20171214_smallrubber_19um_HT_2_vs_COP_655g_load_1.xlsx'
COP_srubber19umHT2df = data.friction_data(COP_srubber19umHT2, load_gram_19)
COP_srubber19umHT3 = 'data/20171214_smallrubber_19um_HT_3_vs_COP_655g_load_1.xlsx'
COP_srubber19umHT3df = data.friction_data(COP_srubber19umHT3, load_gram_19)
COP_srubber19umHT4 = 'data/20171214_smallrubber_19um_HT_4_vs_COP_655g_load_1.xlsx'
COP_srubber19umHT4df = data.friction_data(COP_srubber19umHT4, load_gram_19)

#6.1 um PAHT, SF6 plasma 2 min 50 W 200 mTorr on small rubber (2cm*2cm) vs COP, load =652
COP_srubber6_1umHT_SF61 = 'data/20180214_smallrubber_6.1umHT_SF6_1_vs_COP_652g_.xlsx'
COP_srubber6_1umHT_SF61df = data.friction_data(COP_srubber6_1umHT_SF61, load_gram_25)
COP_srubber6_1umHT_SF62 = 'data/20180214_smallrubber_6.1umHT_SF6_2_vs_COP_652g_.xlsx'
COP_srubber6_1umHT_SF62df = data.friction_data(COP_srubber6_1umHT_SF62, load_gram_25)
COP_srubber6_1umHT_SF63 = 'data/20180214_smallrubber_6.1umHT_SF6_3_vs_COP_652g_.xlsx'
COP_srubber6_1umHT_SF63df = data.friction_data(COP_srubber6_1umHT_SF63, load_gram_25)
COP_srubber6_1umHT_SF64 = 'data/20180214_smallrubber_6.1umHT_SF6_4_vs_COP_652g_.xlsx'
COP_srubber6_1umHT_SF64df = data.friction_data(COP_srubber6_1umHT_SF64, load_gram_25)
COP_srubber6_1umHT_SF65 = 'data/20180214_smallrubber_6.1umHT_SF6_5_vs_COP_652g_.xlsx'
COP_srubber6_1umHT_SF65df = data.friction_data(COP_srubber6_1umHT_SF65, load_gram_25)


## white rubber
#sample: white rubber pieces (small), substrate: COP
#0um on white rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 205.9
COP_wrubber0um1 = 'data/20171211_smallrubber_white_0um_1_vs_old-COP#2_205.9g_load_1.xlsx'
COP_wrubber0um1df = data.friction_data(COP_wrubber0um1, load_gram_15)

#0.25 um PAC on white rubber (2cm*2cm) vs COP, load = 205.4
COP_wrubber0_25um1 = 'data/20180124_smallrubber_white_0.25um_1_vs_COP_205.4g_.xlsx'
COP_wrubber0_25um1df = data.friction_data(COP_wrubber0_25um1, load_gram_22)
COP_wrubber0_25um2 = 'data/20180124_smallrubber_white_0.25um_2_vs_COP_205.4g_.xlsx'
COP_wrubber0_25um2df = data.friction_data(COP_wrubber0_25um2, load_gram_22)
COP_wrubber0_25um3 = 'data/20180124_smallrubber_white_0.25um_3_vs_COP_205.4g_.xlsx'
COP_wrubber0_25um3df = data.friction_data(COP_wrubber0_25um3, load_gram_22)
COP_wrubber0_25um4 = 'data/20180124_smallrubber_white_0.25um_4_vs_COP_205.4g_.xlsx'
COP_wrubber0_25um4df = data.friction_data(COP_wrubber0_25um4, load_gram_22)
COP_wrubber0_25um5 = 'data/20180124_smallrubber_white_0.25um_5_vs_COP_205.4g_.xlsx'
COP_wrubber0_25um5df = data.friction_data(COP_wrubber0_25um5, load_gram_22)

#0.7 um PAC on white rubber (2cm*2cm) vs COP, load = 205.4
COP_wrubber0_7um1 = 'data/20180124_smallrubber_white_0.7um_1_vs_COP_205.4g_.xlsx'
COP_wrubber0_7um1df = data.friction_data(COP_wrubber0_7um1, load_gram_22)
COP_wrubber0_7um2 = 'data/20180124_smallrubber_white_0.7um_2_vs_COP_205.4g_.xlsx'
COP_wrubber0_7um2df = data.friction_data(COP_wrubber0_7um2, load_gram_22)
COP_wrubber0_7um3 = 'data/20180124_smallrubber_white_0.7um_3_vs_COP_205.4g_.xlsx'
COP_wrubber0_7um3df = data.friction_data(COP_wrubber0_7um3, load_gram_22)
COP_wrubber0_7um4 = 'data/20180124_smallrubber_white_0.7um_4_vs_COP_205.4g_.xlsx'
COP_wrubber0_7um4df = data.friction_data(COP_wrubber0_7um4, load_gram_22)
COP_wrubber0_7um5 = 'data/20180124_smallrubber_white_0.7um_5_vs_COP_205.4g_.xlsx'
COP_wrubber0_7um5df = data.friction_data(COP_wrubber0_7um5, load_gram_22)

#1.2 um PAC on white rubber (2cm*2cm) vs COP, load = 652.5
COP_wrubber1_2um1 = 'data/20180201_smallrubber_white_1.2um_1_vs_COP_652.5g_.xlsx'
COP_wrubber1_2um1df = data.friction_data(COP_wrubber1_2um1, load_gram_24)
COP_wrubber1_2um2 = 'data/20180201_smallrubber_white_1.2um_2_vs_COP_652.5g_.xlsx'
COP_wrubber1_2um2df = data.friction_data(COP_wrubber1_2um2, load_gram_24)
COP_wrubber1_2um3 = 'data/20180201_smallrubber_white_1.2um_3_vs_COP_652.5g_.xlsx'
COP_wrubber1_2um3df = data.friction_data(COP_wrubber1_2um3, load_gram_24)
COP_wrubber1_2um4 = 'data/20180201_smallrubber_white_1.2um_4_vs_COP_652.5g_.xlsx'
COP_wrubber1_2um4df = data.friction_data(COP_wrubber1_2um4, load_gram_24)
COP_wrubber1_2um5 = 'data/20180201_smallrubber_white_1.2um_5_vs_COP_652.5g_.xlsx'
COP_wrubber1_2um5df = data.friction_data(COP_wrubber1_2um5, load_gram_24)


#3.6 um PAC on white rubber (2cm*2cm) vs COP, load = 655
COP_wrubber3_6um1 = 'data/20171214_smallrubber_white_3.6um_1_vs_COP_655g_load_1.xlsx'
COP_wrubber3_6um1df = data.friction_data(COP_wrubber3_6um1, load_gram_19)
COP_wrubber3_6um2 = 'data/20171214_smallrubber_white_3.6um_2_vs_COP_655g_load_1.xlsx'
COP_wrubber3_6um2df = data.friction_data(COP_wrubber3_6um2, load_gram_19)
COP_wrubber3_6um3 = 'data/20171214_smallrubber_white_3.6um_3_vs_COP_655g_load_1.xlsx'
COP_wrubber3_6um3df = data.friction_data(COP_wrubber3_6um3, load_gram_19)
COP_wrubber3_6um4 = 'data/20171214_smallrubber_white_3.6um_4_vs_COP_655g_load_1.xlsx'
COP_wrubber3_6um4df = data.friction_data(COP_wrubber3_6um4, load_gram_19)
COP_wrubber3_6um5 = 'data/20171214_smallrubber_white_3.6um_5_vs_COP_655g_load_1.xlsx'
COP_wrubber3_6um5df = data.friction_data(COP_wrubber3_6um5, load_gram_19)


#5 um PAC on white rubber (2cm*2cm) vs COP, load = 655.5
COP_wrubber5um1 = 'data/20171211_smallrubber_white_5um_1_vs_old-COP#2_655.5g_load_1.xlsx'
COP_wrubber5um1df = data.friction_data(COP_wrubber5um1, load_gram_18)
COP_wrubber5um2 = 'data/20171211_smallrubber_white_5um_2_vs_old-COP#2_655.5g_load_1.xlsx'
COP_wrubber5um2df = data.friction_data(COP_wrubber5um2, load_gram_18)
COP_wrubber5um3 = 'data/20171211_smallrubber_white_5um_3_vs_old-COP#2_655.5g_load_1.xlsx'
COP_wrubber5um3df = data.friction_data(COP_wrubber5um3, load_gram_18)
COP_wrubber5um4 = 'data/20171211_smallrubber_white_5um_4_vs_old-COP#2_655.5g_load_1.xlsx'
COP_wrubber5um4df = data.friction_data(COP_wrubber5um4, load_gram_18)
COP_wrubber5um5 = 'data/20171211_smallrubber_white_5um_5_vs_old-COP#2_655.5g_load_1.xlsx'
COP_wrubber5um5df = data.friction_data(COP_wrubber5um5, load_gram_18)

#8.2 um PAC on white rubber (2cm*2cm) vs COP, load = 652.7
COP_wrubber8_2um1 = 'data/20180130_smallrubber_white_8.2um_1_vs_COP_652.7g_.xlsx'
COP_wrubber8_2um1df = data.friction_data(COP_wrubber8_2um1, load_gram_23)
COP_wrubber8_2um2 = 'data/20180130_smallrubber_white_8.2um_2_vs_COP_652.7g_.xlsx'
COP_wrubber8_2um2df = data.friction_data(COP_wrubber8_2um2, load_gram_23)
COP_wrubber8_2um3 = 'data/20180130_smallrubber_white_8.2um_3_vs_COP_652.7g_.xlsx'
COP_wrubber8_2um3df = data.friction_data(COP_wrubber8_2um3, load_gram_23)
COP_wrubber8_2um4 = 'data/20180130_smallrubber_white_8.2um_4_vs_COP_652.7g_.xlsx'
COP_wrubber8_2um4df = data.friction_data(COP_wrubber8_2um4, load_gram_23)
COP_wrubber8_2um5 = 'data/20180130_smallrubber_white_8.2um_5_vs_COP_652.7g_.xlsx'
COP_wrubber8_2um5df = data.friction_data(COP_wrubber8_2um5, load_gram_23)

#15 um PAC on white rubber (2cm*2cm) vs COP, load = 655
COP_wrubber15um1 = 'data/20171214_smallrubber_white_15um_1_vs_COP_655g_load_1.xlsx'
COP_wrubber15um1df = data.friction_data(COP_wrubber15um1, load_gram_19)
COP_wrubber15um2 = 'data/20171214_smallrubber_white_15um_2_vs_COP_655g_load_1.xlsx'
COP_wrubber15um2df = data.friction_data(COP_wrubber15um2, load_gram_19)
COP_wrubber15um3 = 'data/20171214_smallrubber_white_15um_3_vs_COP_655g_load_1.xlsx'
COP_wrubber15um3df = data.friction_data(COP_wrubber15um3, load_gram_19)
COP_wrubber15um4 = 'data/20171214_smallrubber_white_15um_4_vs_COP_655g_load_1.xlsx'
COP_wrubber15um4df = data.friction_data(COP_wrubber15um4, load_gram_19)
COP_wrubber15um5 = 'data/20171214_smallrubber_white_15um_5_vs_COP_655g_load_1.xlsx'
COP_wrubber15um5df = data.friction_data(COP_wrubber15um5, load_gram_19)

#0.26 um PAHT on small rubber (2cm*2cm) vs COP, load =205.9
COP_wrubber0_26umHT1 = 'data/20171211_smallrubber_white_0.26um_HT_1_vs_old-COP#2-left_205.9g_load_1.xlsx'
COP_wrubber0_26umHT1df = data.friction_data(COP_wrubber0_26umHT1, load_gram_15)
COP_wrubber0_26umHT2 = 'data/20171211_smallrubber_white_0.26um_HT_2_vs_old-COP#2-left_205.9g_load_1.xlsx'
COP_wrubber0_26umHT2df = data.friction_data(COP_wrubber0_26umHT2, load_gram_15)
COP_wrubber0_26umHT3 = 'data/20171211_smallrubber_white_0.26um_HT_3_vs_old-COP#2-left_205.9g_load_1.xlsx'
COP_wrubber0_26umHT3df = data.friction_data(COP_wrubber0_26umHT3, load_gram_15)
COP_wrubber0_26umHT4 = 'data/20171211_smallrubber_white_0.26um_HT_4_vs_old-COP#2-left_205.9g_load_1.xlsx'
COP_wrubber0_26umHT4df = data.friction_data(COP_wrubber0_26umHT4, load_gram_15)
COP_wrubber0_26umHT5 = 'data/20171211_smallrubber_white_0.26um_HT_5_vs_old-COP#2-left_205.9g_load_1.xlsx'
COP_wrubber0_26umHT5df = data.friction_data(COP_wrubber0_26umHT5, load_gram_15)

#0.64 um PAHT on small rubber (2cm*2cm) vs COP, load =205.9
COP_wrubber0_64umHT1 = 'data/20171211_smallrubber_white_0.64um_HT_1_vs_old-COP#2-middle_205.9g_load_1.xlsx'
COP_wrubber0_64umHT1df = data.friction_data(COP_wrubber0_64umHT1, load_gram_15)
COP_wrubber0_64umHT2 = 'data/20171211_smallrubber_white_0.64um_HT_2_vs_old-COP#2-middle_205.9g_load_1.xlsx'
COP_wrubber0_64umHT2df = data.friction_data(COP_wrubber0_64umHT2, load_gram_15)
COP_wrubber0_64umHT3 = 'data/20171211_smallrubber_white_0.64um_HT_3_vs_old-COP#2-middle_205.9g_load_1.xlsx'
COP_wrubber0_64umHT3df = data.friction_data(COP_wrubber0_64umHT3, load_gram_15)
COP_wrubber0_64umHT4 = 'data/20171211_smallrubber_white_0.64um_HT_4_vs_old-COP#2-middle_205.9g_load_1.xlsx'
COP_wrubber0_64umHT4df = data.friction_data(COP_wrubber0_64umHT4, load_gram_15)
COP_wrubber0_64umHT5 = 'data/20171211_smallrubber_white_0.64um_HT_5_vs_old-COP#2-middle_205.9g_load_1.xlsx'
COP_wrubber0_64umHT5df = data.friction_data(COP_wrubber0_64umHT5, load_gram_15)

#1.1 um PAHT on small rubber (2cm*2cm) vs COP, load =654
COP_wrubber1_1umHT1 = 'data/20180109_smallrubber_white_1.1um_HT_1_vs_COP_654.7g_.xlsx'
COP_wrubber1_1umHT1df = data.friction_data(COP_wrubber1_1umHT1, load_gram_21)
COP_wrubber1_1umHT2 = 'data/20180109_smallrubber_white_1.1um_HT_2_vs_COP_654.7g_.xlsx'
COP_wrubber1_1umHT2df = data.friction_data(COP_wrubber1_1umHT2, load_gram_21)
COP_wrubber1_1umHT3 = 'data/20180109_smallrubber_white_1.1um_HT_3_vs_COP_654.7g_.xlsx'
COP_wrubber1_1umHT3df = data.friction_data(COP_wrubber1_1umHT3, load_gram_21)
COP_wrubber1_1umHT4 = 'data/20180109_smallrubber_white_1.1um_HT_4_vs_COP_654.7g_.xlsx'
COP_wrubber1_1umHT4df = data.friction_data(COP_wrubber1_1umHT4, load_gram_21)
COP_wrubber1_1umHT5 = 'data/20180109_smallrubber_white_1.1um_HT_5_vs_COP_654.7g_.xlsx'
COP_wrubber1_1umHT5df = data.friction_data(COP_wrubber1_1umHT5, load_gram_21)

#5.3 um PAHT on small rubber (2cm*2cm) vs COP, load =654
COP_wrubber5_3umHT1 = 'data/20180109_smallrubber_white_5.3um_HT_1_vs_COP_654.7g_.xlsx'
COP_wrubber5_3umHT1df = data.friction_data(COP_wrubber5_3umHT1, load_gram_21)
COP_wrubber5_3umHT2 = 'data/20180109_smallrubber_white_5.3um_HT_2_vs_COP_654.7g_.xlsx'
COP_wrubber5_3umHT2df = data.friction_data(COP_wrubber5_3umHT2, load_gram_21)
COP_wrubber5_3umHT3 = 'data/20180109_smallrubber_white_5.3um_HT_3_vs_COP_654.7g_.xlsx'
COP_wrubber5_3umHT3df = data.friction_data(COP_wrubber5_3umHT3, load_gram_21)
COP_wrubber5_3umHT4 = 'data/20180109_smallrubber_white_5.3um_HT_4_vs_COP_654.7g_.xlsx'
COP_wrubber5_3umHT4df = data.friction_data(COP_wrubber5_3umHT4, load_gram_21)
COP_wrubber5_3umHT5 = 'data/20180109_smallrubber_white_5.3um_HT_5_vs_COP_654.7g_.xlsx'
COP_wrubber5_3umHT5df = data.friction_data(COP_wrubber5_3umHT5, load_gram_21)

#6.1 um PAHT on small rubber (2cm*2cm) vs COP, load =652
COP_wrubber6_1umHT1 = 'data/20180213_smallrubber_white_6.1umHT_1_vs_COP_652g_.xlsx'
COP_wrubber6_1umHT1df = data.friction_data(COP_wrubber6_1umHT1, load_gram_25)
COP_wrubber6_1umHT2 = 'data/20180213_smallrubber_white_6.1umHT_2_vs_COP_652g_.xlsx'
COP_wrubber6_1umHT2df = data.friction_data(COP_wrubber6_1umHT2, load_gram_25)
COP_wrubber6_1umHT3 = 'data/20180213_smallrubber_white_6.1umHT_3_vs_COP_652g_.xlsx'
COP_wrubber6_1umHT3df = data.friction_data(COP_wrubber6_1umHT3, load_gram_25)
COP_wrubber6_1umHT4 = 'data/20180213_smallrubber_white_6.1umHT_4_vs_COP_652g_.xlsx'
COP_wrubber6_1umHT4df = data.friction_data(COP_wrubber6_1umHT4, load_gram_25)
COP_wrubber6_1umHT5 = 'data/20180213_smallrubber_white_6.1umHT_5_vs_COP_652g_.xlsx'
COP_wrubber6_1umHT5df = data.friction_data(COP_wrubber6_1umHT5, load_gram_25)

#7.5 um PAHT on small rubber (2cm*2cm) vs COP, load =654
COP_wrubber7_5umHT1 = 'data/20180109_smallrubber_white_7.5um_HT_1_vs_COP_654.7g_.xlsx'
COP_wrubber7_5umHT1df = data.friction_data(COP_wrubber7_5umHT1, load_gram_21)
COP_wrubber7_5umHT2 = 'data/20180109_smallrubber_white_7.5um_HT_2_vs_COP_654.7g_.xlsx'
COP_wrubber7_5umHT2df = data.friction_data(COP_wrubber7_5umHT2, load_gram_21)
COP_wrubber7_5umHT3 = 'data/20180109_smallrubber_white_7.5um_HT_3_vs_COP_654.7g_.xlsx'
COP_wrubber7_5umHT3df = data.friction_data(COP_wrubber7_5umHT3, load_gram_21)
COP_wrubber7_5umHT4 = 'data/20180109_smallrubber_white_7.5um_HT_4_vs_COP_654.7g_.xlsx'
COP_wrubber7_5umHT4df = data.friction_data(COP_wrubber7_5umHT4, load_gram_21)
COP_wrubber7_5umHT5 = 'data/20180109_smallrubber_white_7.5um_HT_5_vs_COP_654.7g_.xlsx'
COP_wrubber7_5umHT5df = data.friction_data(COP_wrubber7_5umHT5, load_gram_21)


#19 um PAHT on white rubber (2cm*2cm) vs COP, load = 655
COP_wrubber19umHT1 = 'data/20171214_smallrubber_white_19um_HT_1_vs_COP_655g_load_1.xlsx'
COP_wrubber19umHT1df = data.friction_data(COP_wrubber19umHT1, load_gram_19)
COP_wrubber19umHT2 = 'data/20171214_smallrubber_white_19um_HT_2_vs_COP_655g_load_1.xlsx'
COP_wrubber19umHT2df = data.friction_data(COP_wrubber19umHT2, load_gram_19)
COP_wrubber19umHT3 = 'data/20171214_smallrubber_white_19um_HT_3_vs_COP_655g_load_1.xlsx'
COP_wrubber19umHT3df = data.friction_data(COP_wrubber19umHT3, load_gram_19)
COP_wrubber19umHT4 = 'data/20171214_smallrubber_white_19um_HT_4_vs_COP_655g_load_1.xlsx'
COP_wrubber19umHT4df = data.friction_data(COP_wrubber19umHT4, load_gram_19)


#sample: rubber pieces (small), substrate: soda lime wafer
#0 um PAC on small rubber(2cm*2cm) vs soda lime wafer, load = 205.5
soda_srubber0um1 = 'data/20171024_smallrubber_1_vs_sodalime_205.5g_load_1.xlsx'
soda_srubber0um1df = data.friction_data(soda_srubber0um1, load_gram_8)

#0.2 um PAC on small rubber (2cm*2cm) vs COP, load = 205.7
soda_srubber0_2um1 = 'data/20171127_smallrubber_0.2um_1_vs_sodalime_#1_205.7g_load_1.xlsx'
soda_srubber0_2um1df = data.friction_data(soda_srubber0_2um1, load_gram_16)
soda_srubber0_2um2 = 'data/20171127_smallrubber_0.2um_2_vs_sodalime_#1_205.7g_load_1.xlsx'
soda_srubber0_2um2df = data.friction_data(soda_srubber0_2um2, load_gram_16)
soda_srubber0_2um3 = 'data/20171127_smallrubber_0.2um_3_vs_sodalime_#1_205.7g_load_1.xlsx'
soda_srubber0_2um3df = data.friction_data(soda_srubber0_2um3, load_gram_16)
soda_srubber0_2um4 = 'data/20171127_smallrubber_0.2um_4_vs_sodalime_#1_205.7g_load_1.xlsx'
soda_srubber0_2um4df = data.friction_data(soda_srubber0_2um4, load_gram_16)

#0.6 um PAC on small rubber (2cm*2cm) vs COP, load = 205.7
soda_srubber0_6um1 = 'data/20171127_smallrubber_0.6um_1_vs_sodalime_#2_205.7g_load_1.xlsx'
soda_srubber0_6um1df = data.friction_data(soda_srubber0_6um1, load_gram_16)
soda_srubber0_6um2 = 'data/20171127_smallrubber_0.6um_2_vs_sodalime_#2_205.7g_load_1.xlsx'
soda_srubber0_6um2df = data.friction_data(soda_srubber0_6um2, load_gram_16)
soda_srubber0_6um3 = 'data/20171127_smallrubber_0.6um_3_vs_sodalime_#2_205.7g_load_1.xlsx'
soda_srubber0_6um3df = data.friction_data(soda_srubber0_6um3, load_gram_16)
soda_srubber0_6um4 = 'data/20171127_smallrubber_0.6um_4_vs_sodalime_#2_205.7g_load_1.xlsx'
soda_srubber0_6um4df = data.friction_data(soda_srubber0_6um4, load_gram_16)

#1.1 um PAC on small rubber (2cm*2cm) vs soda lime wafer, load = 205.8
# soda_srubber1_1um1 = 'data/20171113_smallrubber_1.1um_1_vs_sodalime_#1_205.8g_load_1.xlsx'
# soda_srubber1_1um1df = data.friction_data(soda_srubber1_1um1, load_gram_12)
# soda_srubber1_1um2 = 'data/20171113_smallrubber_1.1um_2_vs_sodalime_#1_205.8g_load_1.xlsx'
# soda_srubber1_1um2df = data.friction_data(soda_srubber1_1um2, load_gram_12)
# soda_srubber1_1um3 = 'data/20171113_smallrubber_1.1um_3_vs_sodalime_#1_205.8g_load_1.xlsx'
# soda_srubber1_1um3df = data.friction_data(soda_srubber1_1um3, load_gram_12)
# soda_srubber1_1um4 = 'data/20171113_smallrubber_1.1um_4_vs_sodalime_#1_205.8g_load_1.xlsx'
# soda_srubber1_1um4df = data.friction_data(soda_srubber1_1um4, load_gram_12)
# soda_srubber1_1um5 = 'data/20171113_smallrubber_1.1um_5_vs_sodalime_#1_205.8g_load_1.xlsx'
# soda_srubber1_1um5df = data.friction_data(soda_srubber1_1um5, load_gram_12)
soda_srubber1_1um1 = 'data/20171127_smallrubber_1.1um_1_vs_sodalime_#1_205.7g_load_1.xlsx'
soda_srubber1_1um1df = data.friction_data(soda_srubber1_1um1, load_gram_16)
soda_srubber1_1um2 = 'data/20171127_smallrubber_1.1um_2_vs_sodalime_#1_205.7g_load_1.xlsx'
soda_srubber1_1um2df = data.friction_data(soda_srubber1_1um2, load_gram_16)
soda_srubber1_1um3 = 'data/20171127_smallrubber_1.1um_3_vs_sodalime_#1_205.7g_load_1.xlsx'
soda_srubber1_1um3df = data.friction_data(soda_srubber1_1um3, load_gram_16)
soda_srubber1_1um4 = 'data/20171127_smallrubber_1.1um_4_vs_sodalime_#1_205.7g_load_1.xlsx'
soda_srubber1_1um4df = data.friction_data(soda_srubber1_1um4, load_gram_16)
soda_srubber1_1um5 = 'data/20171127_smallrubber_1.1um_5_vs_sodalime_#1_205.7g_load_1.xlsx'
soda_srubber1_1um5df = data.friction_data(soda_srubber1_1um5, load_gram_16)

#3.6 um PAC on samll rubber(2cm*2cm) vs soda lime wafer, load = 200.7
soda_srubber3_6um1 = 'data/20171019_smallrubber_3.6um_1_vs_sodalime_200.7g_load_1.xlsx'
soda_srubber3_6um1df = data.friction_data(soda_srubber3_6um1, load_gram_6)
soda_srubber3_6um2 = 'data/20171019_smallrubber_3.6um_2_vs_sodalime_200.7g_load_1.xlsx'
soda_srubber3_6um2df = data.friction_data(soda_srubber3_6um2, load_gram_6)
soda_srubber3_6um3 = 'data/20171019_smallrubber_3.6um_3_vs_sodalime_200.7g_load_1.xlsx'
soda_srubber3_6um3df = data.friction_data(soda_srubber3_6um3, load_gram_6)
soda_srubber3_6um4 = 'data/20171019_smallrubber_3.6um_4_vs_sodalime_200.7g_load_1.xlsx'
soda_srubber3_6um4df = data.friction_data(soda_srubber3_6um4, load_gram_6)
soda_srubber3_6um5 = 'data/20171019_smallrubber_3.6um_5_vs_sodalime_200.7g_load_1.xlsx'
soda_srubber3_6um5df = data.friction_data(soda_srubber3_6um5, load_gram_6)

#3.6 um PAC on small rubber (2cm*2cm) vs soda lime wafer, load = 205.6
soda_srubber3_6um6 = 'data/20171214_smallrubber_3.6um_1_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_srubber3_6um6df = data.friction_data(soda_srubber3_6um6, load_gram_20)
soda_srubber3_6um7 = 'data/20171214_smallrubber_3.6um_2_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_srubber3_6um7df = data.friction_data(soda_srubber3_6um7, load_gram_20)
soda_srubber3_6um8 = 'data/20171214_smallrubber_3.6um_3_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_srubber3_6um8df = data.friction_data(soda_srubber3_6um8, load_gram_20)
soda_srubber3_6um9 = 'data/20171214_smallrubber_3.6um_4_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_srubber3_6um9df = data.friction_data(soda_srubber3_6um9, load_gram_20)

#5 um PAC on samll rubber(2cm*2cm) vs soda lime wafer, load = 205.9
soda_srubber5um1 = 'data/20171211_smallrubber_5um_1_vs_sodalime_#5_205.9g_load_1.xlsx'
soda_srubber5um1df = data.friction_data(soda_srubber5um1, load_gram_15)
soda_srubber5um2 = 'data/20171211_smallrubber_5um_2_vs_sodalime_#5_205.9g_load_1.xlsx'
soda_srubber5um2df = data.friction_data(soda_srubber5um2, load_gram_15)
soda_srubber5um3 = 'data/20171211_smallrubber_5um_3_vs_sodalime_#5_205.9g_load_1.xlsx'
soda_srubber5um3df = data.friction_data(soda_srubber5um3, load_gram_15)
soda_srubber5um4 = 'data/20171211_smallrubber_5um_4_vs_sodalime_#5_205.9g_load_1.xlsx'
soda_srubber5um4df = data.friction_data(soda_srubber5um4, load_gram_15)

#7.3 um PAC on small rubber (2cm*2cm) vs soda lime wafer, load = 205.7
soda_srubber7_3um1 = 'data/20171127_smallrubber_7.3um_1_vs_sodalime_#2_205.7g_load_1.xlsx'
soda_srubber7_3um1df = data.friction_data(soda_srubber7_3um1, load_gram_16)
soda_srubber7_3um2 = 'data/20171127_smallrubber_7.3um_2_vs_sodalime_#2_205.7g_load_1.xlsx'
soda_srubber7_3um2df = data.friction_data(soda_srubber7_3um2, load_gram_16)
soda_srubber7_3um3 = 'data/20171127_smallrubber_7.3um_3_vs_sodalime_#2_205.7g_load_1.xlsx'
soda_srubber7_3um3df = data.friction_data(soda_srubber7_3um3, load_gram_16)
soda_srubber7_3um4 = 'data/20171127_smallrubber_7.3um_4_vs_sodalime_#2_205.7g_load_1.xlsx'
soda_srubber7_3um4df = data.friction_data(soda_srubber7_3um4, load_gram_16)
soda_srubber7_3um5 = 'data/20171127_smallrubber_7.3um_5_vs_sodalime_#2_205.7g_load_1.xlsx'
soda_srubber7_3um5df = data.friction_data(soda_srubber7_3um5, load_gram_16)

#8.9 um PAC on small rubber (2cm*2cm) vs soda lime wafer, load = 205.8
# soda_srubber8_9um1 = 'data/20171113_smallrubber_8.9um_1_vs_sodalime_#1_205.8g_load_1.xlsx'
# soda_srubber8_9um1df = data.friction_data(soda_srubber8_9um1, load_gram_12)
# soda_srubber8_9um2 = 'data/20171113_smallrubber_8.9um_2_vs_sodalime_#1_205.8g_load_1.xlsx'
# soda_srubber8_9um2df = data.friction_data(soda_srubber8_9um2, load_gram_12)
# soda_srubber8_9um3 = 'data/20171113_smallrubber_8.9um_3_vs_sodalime_#1_205.8g_load_1.xlsx'
# soda_srubber8_9um3df = data.friction_data(soda_srubber8_9um3, load_gram_12)
# soda_srubber8_9um4 = 'data/20171113_smallrubber_8.9um_4_vs_sodalime_#1_205.8g_load_1.xlsx'
# soda_srubber8_9um4df = data.friction_data(soda_srubber8_9um4, load_gram_12)
# soda_srubber8_9um5 = 'data/20171113_smallrubber_8.9um_5_vs_sodalime_#1_205.8g_load_1.xlsx'
# soda_srubber8_9um5df = data.friction_data(soda_srubber8_9um5, load_gram_12)
soda_srubber8_9um1 = 'data/20171127_smallrubber_8.9um_1_vs_sodalime_#2_205.7g_load_1.xlsx'
soda_srubber8_9um1df = data.friction_data(soda_srubber8_9um1, load_gram_16)
soda_srubber8_9um2 = 'data/20171127_smallrubber_8.9um_2_vs_sodalime_#2_205.7g_load_1.xlsx'
soda_srubber8_9um2df = data.friction_data(soda_srubber8_9um2, load_gram_16)
soda_srubber8_9um3 = 'data/20171127_smallrubber_8.9um_3_vs_sodalime_#2_205.7g_load_1.xlsx'
soda_srubber8_9um3df = data.friction_data(soda_srubber8_9um3, load_gram_16)
soda_srubber8_9um4 = 'data/20171127_smallrubber_8.9um_4_vs_sodalime_#2_205.7g_load_1.xlsx'
soda_srubber8_9um4df = data.friction_data(soda_srubber8_9um4, load_gram_16)
soda_srubber8_9um5 = 'data/20171127_smallrubber_8.9um_5_vs_sodalime_#2_205.7g_load_1.xlsx'
soda_srubber8_9um5df = data.friction_data(soda_srubber8_9um5, load_gram_16)

soda_1_srubber8_9um5 = 'data/20171127_smallrubber_8.9um_5_vs_sodalime_#1_205.7g_load_1.xlsx'
soda_1_srubber8_9um5df = data.friction_data(soda_1_srubber8_9um5, load_gram_16)
soda_3_srubber8_9um5 = 'data/20171127_smallrubber_8.9um_5_vs_sodalime_#3_205.7g_load_1.xlsx'
soda_3_srubber8_9um5df = data.friction_data(soda_3_srubber8_9um5, load_gram_16)
soda_4_srubber8_9um5 = 'data/20171127_smallrubber_8.9um_5_vs_sodalime_#4_205.7g_load_1.xlsx'
soda_4_srubber8_9um5df = data.friction_data(soda_4_srubber8_9um5, load_gram_16)
soda_5_srubber8_9um5 = 'data/20171127_smallrubber_8.9um_5_vs_sodalime_#5_205.7g_load_1.xlsx'
soda_5_srubber8_9um5df = data.friction_data(soda_5_srubber8_9um5, load_gram_16)

#15 um PAC on small rubber (2cm*2cm) vs soda lime wafer, load = 205.6
soda_srubber15um1 = 'data/20171214_smallrubber_15um_1_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_srubber15um1df = data.friction_data(soda_srubber15um1, load_gram_20)
soda_srubber15um2 = 'data/20171214_smallrubber_15um_2_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_srubber15um2df = data.friction_data(soda_srubber15um2, load_gram_20)
soda_srubber15um3 = 'data/20171214_smallrubber_15um_3_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_srubber15um3df = data.friction_data(soda_srubber15um3, load_gram_20)
soda_srubber15um4 = 'data/20171214_smallrubber_15um_4_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_srubber15um4df = data.friction_data(soda_srubber15um4, load_gram_20)

#16 um PAC on small rubber (2cm*2cm) vs soda lime wafer, load = 205.8
soda_srubber16um1 = 'data/20171108_smallrubber_16um_1_vs_newly_washed_sodalime_#1_205.9g_load_1.xlsx'
soda_srubber16um1df = data.friction_data(soda_srubber16um1, load_gram_12)
soda_srubber16um2 = 'data/20171108_smallrubber_16um_1_vs_newly_washed_sodalime_#2_205.9g_load_1.xlsx'
soda_srubber16um2df = data.friction_data(soda_srubber16um2, load_gram_12)
soda_srubber16um3 = 'data/20171108_smallrubber_16um_1_vs_newly_washed_sodalime_#3_205.9g_load_1.xlsx'
soda_srubber16um3df = data.friction_data(soda_srubber16um3, load_gram_12)
soda_srubber16um4 = 'data/20171108_smallrubber_16um_1_vs_newly_washed_sodalime_#4_205.9g_load_1.xlsx'
soda_srubber16um4df = data.friction_data(soda_srubber16um4, load_gram_12)

#0.26 um PAHT on small rubber (2cm*2cm) vs soda lime wafer, load =205.9
soda_srubber0_26umHT1 = 'data/20171211_smallrubber_0.26um_HT_1_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_srubber0_26umHT1df = data.friction_data(soda_srubber0_26umHT1, load_gram_15)
soda_srubber0_26umHT2 = 'data/20171211_smallrubber_0.26um_HT_2_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_srubber0_26umHT2df = data.friction_data(soda_srubber0_26umHT2, load_gram_15)
soda_srubber0_26umHT3 = 'data/20171211_smallrubber_0.26um_HT_3_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_srubber0_26umHT3df = data.friction_data(soda_srubber0_26umHT3, load_gram_15)
soda_srubber0_26umHT4 = 'data/20171211_smallrubber_0.26um_HT_4_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_srubber0_26umHT4df = data.friction_data(soda_srubber0_26umHT4, load_gram_15)

#0.64 um PAHT on small rubber (2cm*2cm) vs soda, load =205.9
soda_srubber0_64umHT1 = 'data/20171211_smallrubber_0.64um_HT_1_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_srubber0_64umHT1df = data.friction_data(soda_srubber0_64umHT1, load_gram_15)
soda_srubber0_64umHT2 = 'data/20171211_smallrubber_0.64um_HT_2_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_srubber0_64umHT2df = data.friction_data(soda_srubber0_64umHT2, load_gram_15)
soda_srubber0_64umHT3 = 'data/20171211_smallrubber_0.64um_HT_3_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_srubber0_64umHT3df = data.friction_data(soda_srubber0_64umHT3, load_gram_15)
soda_srubber0_64umHT4 = 'data/20171211_smallrubber_0.64um_HT_4_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_srubber0_64umHT4df = data.friction_data(soda_srubber0_64umHT4, load_gram_15)

#1.1 um PAHT on small rubber (2cm*2cm) vs soda lime wafer, load = 205.7
soda_srubber1_1umHT1 = 'data/20171101_smallrubber_1.1um_HT_1_vs_newly_washed_sodalime_205.7g_load_1.xlsx'
soda_srubber1_1umHT1df = data.friction_data(soda_srubber1_1umHT1, load_gram_10)
soda_srubber1_1umHT2 = 'data/20171101_smallrubber_1.1um_HT_2_vs_newly_washed_sodalime_205.7g_load_1.xlsx'
soda_srubber1_1umHT2df = data.friction_data(soda_srubber1_1umHT2, load_gram_10)
soda_srubber1_1umHT3 = 'data/20171101_smallrubber_1.1um_HT_3_vs_newly_washed_sodalime_205.7g_load_1.xlsx'
soda_srubber1_1umHT3df = data.friction_data(soda_srubber1_1umHT3, load_gram_10)
soda_srubber1_1umHT4 = 'data/20171101_smallrubber_1.1um_HT_4_vs_newly_washed_sodalime_205.7g_load_1.xlsx'
soda_srubber1_1umHT4df = data.friction_data(soda_srubber1_1umHT4, load_gram_10)
soda_srubber1_1umHT5 = 'data/20171101_smallrubber_1.1um_HT_5_vs_newly_washed_sodalime_205.7g_load_1.xlsx'
soda_srubber1_1umHT5df = data.friction_data(soda_srubber1_1umHT5, load_gram_10)

#4.5 um PAHT on small rubber (2cm*2cm) vs soda lime wafer, load = 205.8
# soda_srubber4_5umHT1 = 'data/20171113_smallrubber_4.5um_HT_1_vs_sodalime_#1_205.8g_load_1.xlsx'
# soda_srubber4_5umHT1df = data.friction_data(soda_srubber4_5umHT1, load_gram_12)
# soda_srubber4_5umHT2 = 'data/20171113_smallrubber_4.5um_HT_2_vs_sodalime_#1_205.8g_load_1.xlsx'
# soda_srubber4_5umHT2df = data.friction_data(soda_srubber4_5umHT2, load_gram_12)
# soda_srubber4_5umHT3 = 'data/20171113_smallrubber_4.5um_HT_3_vs_sodalime_#1_205.8g_load_1.xlsx'
# soda_srubber4_5umHT3df = data.friction_data(soda_srubber4_5umHT3, load_gram_12)
# soda_srubber4_5umHT4 = 'data/20171113_smallrubber_4.5um_HT_4_vs_sodalime_#1_205.8g_load_1.xlsx'
# soda_srubber4_5umHT4df = data.friction_data(soda_srubber4_5umHT4, load_gram_12)
# soda_srubber4_5umHT5 = 'data/20171113_smallrubber_4.5um_HT_5_vs_sodalime_#1_205.8g_load_1.xlsx'
# soda_srubber4_5umHT5df = data.friction_data(soda_srubber4_5umHT5, load_gram_12)
soda_srubber4_5umHT1 = 'data/20171127_smallrubber_4.5um_HT_1_vs_sodalime_#1_205.7g_load_1.xlsx'
soda_srubber4_5umHT1df = data.friction_data(soda_srubber4_5umHT1, load_gram_16)
soda_srubber4_5umHT2 = 'data/20171127_smallrubber_4.5um_HT_2_vs_sodalime_#1_205.7g_load_1.xlsx'
soda_srubber4_5umHT2df = data.friction_data(soda_srubber4_5umHT2, load_gram_16)
soda_srubber4_5umHT3 = 'data/20171127_smallrubber_4.5um_HT_3_vs_sodalime_#1_205.7g_load_1.xlsx'
soda_srubber4_5umHT3df = data.friction_data(soda_srubber4_5umHT3, load_gram_16)
soda_srubber4_5umHT4 = 'data/20171127_smallrubber_4.5um_HT_4_vs_sodalime_#1_205.7g_load_1.xlsx'
soda_srubber4_5umHT4df = data.friction_data(soda_srubber4_5umHT4, load_gram_16)
soda_srubber4_5umHT5 = 'data/20171127_smallrubber_4.5um_HT_5_vs_sodalime_#1_205.7g_load_1.xlsx'
soda_srubber4_5umHT5df = data.friction_data(soda_srubber4_5umHT5, load_gram_16)

#6.9 um PAHT on small rubber (2cm*2cm) vs soda lime wafer, load = 205.8
# soda_srubber6_9umHT1 = 'data/20171113_smallrubber_6.9um_HT_1_vs_sodalime_#1_205.8g_load_1.xlsx'
# soda_srubber6_9umHT1df = data.friction_data(soda_srubber6_9umHT1, load_gram_12)
# soda_srubber6_9umHT2 = 'data/20171113_smallrubber_6.9um_HT_2_vs_sodalime_#1_205.8g_load_1.xlsx'
# soda_srubber6_9umHT2df = data.friction_data(soda_srubber6_9umHT2, load_gram_12)
# soda_srubber6_9umHT3 = 'data/20171113_smallrubber_6.9um_HT_3_vs_sodalime_#1_205.8g_load_1.xlsx'
# soda_srubber6_9umHT3df = data.friction_data(soda_srubber6_9umHT3, load_gram_12)
# soda_srubber6_9umHT4 = 'data/20171113_smallrubber_6.9um_HT_4_vs_sodalime_#1_205.8g_load_1.xlsx'
# soda_srubber6_9umHT4df = data.friction_data(soda_srubber6_9umHT4, load_gram_12)
# soda_srubber6_9umHT5 = 'data/20171113_smallrubber_6.9um_HT_5_vs_sodalime_#1_205.8g_load_1.xlsx'
# soda_srubber6_9umHT5df = data.friction_data(soda_srubber6_9umHT5, load_gram_12)
soda_srubber6_9umHT1 = 'data/20171127_smallrubber_6.9um_HT_1_vs_sodalime_#1_205.7g_load_1.xlsx'
soda_srubber6_9umHT1df = data.friction_data(soda_srubber6_9umHT1, load_gram_16)
soda_srubber6_9umHT2 = 'data/20171127_smallrubber_6.9um_HT_2_vs_sodalime_#1_205.7g_load_1.xlsx'
soda_srubber6_9umHT2df = data.friction_data(soda_srubber6_9umHT2, load_gram_16)
soda_srubber6_9umHT3 = 'data/20171127_smallrubber_6.9um_HT_3_vs_sodalime_#1_205.7g_load_1.xlsx'
soda_srubber6_9umHT3df = data.friction_data(soda_srubber6_9umHT3, load_gram_16)
soda_srubber6_9umHT4 = 'data/20171127_smallrubber_6.9um_HT_4_vs_sodalime_#1_205.7g_load_1.xlsx'
soda_srubber6_9umHT4df = data.friction_data(soda_srubber6_9umHT4, load_gram_16)
soda_srubber6_9umHT5 = 'data/20171127_smallrubber_6.9um_HT_5_vs_sodalime_#1_205.7g_load_1.xlsx'
soda_srubber6_9umHT5df = data.friction_data(soda_srubber6_9umHT5, load_gram_16)

#19 um PAHT on small rubber (2cm*2cm) vs soda lime wafer, load = 205.6
soda_srubber19umHT1 = 'data/20171214_smallrubber_19um_HT_1_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_srubber19umHT1df = data.friction_data(soda_srubber19umHT1, load_gram_20)
soda_srubber19umHT2 = 'data/20171214_smallrubber_19um_HT_2_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_srubber19umHT2df = data.friction_data(soda_srubber19umHT2, load_gram_20)
soda_srubber19umHT3 = 'data/20171214_smallrubber_19um_HT_3_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_srubber19umHT3df = data.friction_data(soda_srubber19umHT3, load_gram_20)
soda_srubber19umHT4 = 'data/20171214_smallrubber_19um_HT_4_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_srubber19umHT4df = data.friction_data(soda_srubber19umHT4, load_gram_20)

#6.1 um PAHT, SF6 plasma 2 min 50 W 200 mTorr on small rubber (2cm*2cm) vs soda lime wafer, load =205.5
soda_srubber6_1umHT_SF61 = 'data/20180214_smallrubber_6.1umHT_SF6_1_vs_sodalime_205.5g_.xlsx'
soda_srubber6_1umHT_SF61df = data.friction_data(soda_srubber6_1umHT_SF61, load_gram_8)
soda_srubber6_1umHT_SF62 = 'data/20180214_smallrubber_6.1umHT_SF6_2_vs_sodalime_205.5g_.xlsx'
soda_srubber6_1umHT_SF62df = data.friction_data(soda_srubber6_1umHT_SF62, load_gram_8)
soda_srubber6_1umHT_SF63 = 'data/20180214_smallrubber_6.1umHT_SF6_3_vs_sodalime_205.5g_.xlsx'
soda_srubber6_1umHT_SF63df = data.friction_data(soda_srubber6_1umHT_SF63, load_gram_8)
soda_srubber6_1umHT_SF64 = 'data/20180214_smallrubber_6.1umHT_SF6_4_vs_sodalime_205.5g_.xlsx'
soda_srubber6_1umHT_SF64df = data.friction_data(soda_srubber6_1umHT_SF64, load_gram_8)
soda_srubber6_1umHT_SF65 = 'data/20180214_smallrubber_6.1umHT_SF6_5_vs_sodalime_205.5g_.xlsx'
soda_srubber6_1umHT_SF65df = data.friction_data(soda_srubber6_1umHT_SF65, load_gram_8)

## white rubber
#sample: white rubber pieces (small), substrate: soda lime wafer
#0um on white rubber (2cm*2cm) vs soda lime wafer, load = 205.9
soda_wrubber0um1 = 'data/20171211_smallrubber_white_0um_1_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_wrubber0um1df = data.friction_data(soda_wrubber0um1, load_gram_15)

#0.25 um PAC on white rubber (2cm*2cm) vs soda lime wafer, load = 205.4
soda_wrubber0_25um1 = 'data/20180124_smallrubber_white_0.25um_1_vs_sodalime_205.4g_.xlsx'
soda_wrubber0_25um1df = data.friction_data(soda_wrubber0_25um1, load_gram_22)
soda_wrubber0_25um2 = 'data/20180124_smallrubber_white_0.25um_2_vs_sodalime_205.4g_.xlsx'
soda_wrubber0_25um2df = data.friction_data(soda_wrubber0_25um2, load_gram_22)
soda_wrubber0_25um3 = 'data/20180124_smallrubber_white_0.25um_3_vs_sodalime_205.4g_.xlsx'
soda_wrubber0_25um3df = data.friction_data(soda_wrubber0_25um3, load_gram_22)
soda_wrubber0_25um4 = 'data/20180124_smallrubber_white_0.25um_4_vs_sodalime_205.4g_.xlsx'
soda_wrubber0_25um4df = data.friction_data(soda_wrubber0_25um4, load_gram_22)
soda_wrubber0_25um5 = 'data/20180124_smallrubber_white_0.25um_5_vs_sodalime_205.4g_.xlsx'
soda_wrubber0_25um5df = data.friction_data(soda_wrubber0_25um5, load_gram_22)

#0.7 um PAC on white rubber (2cm*2cm) vs soda lime wafer, load = 205.4
soda_wrubber0_7um1 = 'data/20180124_smallrubber_white_0.7um_1_vs_sodalime_205.4g_.xlsx'
soda_wrubber0_7um1df = data.friction_data(soda_wrubber0_7um1, load_gram_22)
soda_wrubber0_7um2 = 'data/20180124_smallrubber_white_0.7um_2_vs_sodalime_205.4g_.xlsx'
soda_wrubber0_7um2df = data.friction_data(soda_wrubber0_7um2, load_gram_22)
soda_wrubber0_7um3 = 'data/20180124_smallrubber_white_0.7um_3_vs_sodalime_205.4g_.xlsx'
soda_wrubber0_7um3df = data.friction_data(soda_wrubber0_7um3, load_gram_22)
soda_wrubber0_7um4 = 'data/20180124_smallrubber_white_0.7um_4_vs_sodalime_205.4g_.xlsx'
soda_wrubber0_7um4df = data.friction_data(soda_wrubber0_7um4, load_gram_22)
soda_wrubber0_7um5 = 'data/20180124_smallrubber_white_0.7um_5_vs_sodalime_205.4g_.xlsx'
soda_wrubber0_7um5df = data.friction_data(soda_wrubber0_7um5, load_gram_22)

#1.2 um PAC on white rubber (2cm*2cm) vs soda lime wafer, load = 205.4
soda_wrubber1_2um1 = 'data/20180201_smallrubber_white_1.2um_1_vs_sodalime_205.4g_.xlsx'
soda_wrubber1_2um1df = data.friction_data(soda_wrubber1_2um1, load_gram_22)
soda_wrubber1_2um2 = 'data/20180201_smallrubber_white_1.2um_2_vs_sodalime_205.4g_.xlsx'
soda_wrubber1_2um2df = data.friction_data(soda_wrubber1_2um2, load_gram_22)
soda_wrubber1_2um3 = 'data/20180201_smallrubber_white_1.2um_3_vs_sodalime_205.4g_.xlsx'
soda_wrubber1_2um3df = data.friction_data(soda_wrubber1_2um3, load_gram_22)
soda_wrubber1_2um4 = 'data/20180201_smallrubber_white_1.2um_4_vs_sodalime_205.4g_.xlsx'
soda_wrubber1_2um4df = data.friction_data(soda_wrubber1_2um4, load_gram_22)
soda_wrubber1_2um5 = 'data/20180201_smallrubber_white_1.2um_5_vs_sodalime_205.4g_.xlsx'
soda_wrubber1_2um5df = data.friction_data(soda_wrubber1_2um5, load_gram_22)

#3.6 um PAC on white rubber (2cm*2cm) vs soda, load = 205.6
soda_wrubber3_6um1 = 'data/20171214_smallrubber_white_3.6um_1_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_wrubber3_6um1df = data.friction_data(soda_wrubber3_6um1, load_gram_20)
soda_wrubber3_6um2 = 'data/20171214_smallrubber_white_3.6um_2_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_wrubber3_6um2df = data.friction_data(soda_wrubber3_6um2, load_gram_20)
soda_wrubber3_6um3 = 'data/20171214_smallrubber_white_3.6um_3_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_wrubber3_6um3df = data.friction_data(soda_wrubber3_6um3, load_gram_20)
soda_wrubber3_6um4 = 'data/20171214_smallrubber_white_3.6um_4_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_wrubber3_6um4df = data.friction_data(soda_wrubber3_6um4, load_gram_20)
soda_wrubber3_6um5 = 'data/20171214_smallrubber_white_3.6um_5_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_wrubber3_6um5df = data.friction_data(soda_wrubber3_6um5, load_gram_20)

#5 um PAC on white rubber (2cm*2cm) vs soda lime wafer, load = 205.9
soda_wrubber5um1 = 'data/20171211_smallrubber_white_5um_1_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_wrubber5um1df = data.friction_data(soda_wrubber5um1, load_gram_15)
soda_wrubber5um2 = 'data/20171211_smallrubber_white_5um_2_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_wrubber5um2df = data.friction_data(soda_wrubber5um2, load_gram_15)
soda_wrubber5um3 = 'data/20171211_smallrubber_white_5um_3_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_wrubber5um3df = data.friction_data(soda_wrubber5um3, load_gram_15)
soda_wrubber5um4 = 'data/20171211_smallrubber_white_5um_4_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_wrubber5um4df = data.friction_data(soda_wrubber5um4, load_gram_15)
soda_wrubber5um5 = 'data/20171211_smallrubber_white_5um_5_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_wrubber5um5df = data.friction_data(soda_wrubber5um5, load_gram_15)

#8.2 um PAC on white rubber (2cm*2cm) vs soda, load = 205.4
soda_wrubber8_2um1 = 'data/20180130_smallrubber_white_8.2um_1_vs_sodalime_205.4g_.xlsx'
soda_wrubber8_2um1df = data.friction_data(soda_wrubber8_2um1, load_gram_22)
soda_wrubber8_2um2 = 'data/20180130_smallrubber_white_8.2um_2_vs_sodalime_205.4g_.xlsx'
soda_wrubber8_2um2df = data.friction_data(soda_wrubber8_2um2, load_gram_22)
soda_wrubber8_2um3 = 'data/20180130_smallrubber_white_8.2um_3_vs_sodalime_205.4g_.xlsx'
soda_wrubber8_2um3df = data.friction_data(soda_wrubber8_2um3, load_gram_22)
soda_wrubber8_2um4 = 'data/20180130_smallrubber_white_8.2um_4_vs_sodalime_205.4g_.xlsx'
soda_wrubber8_2um4df = data.friction_data(soda_wrubber8_2um4, load_gram_22)
soda_wrubber8_2um5 = 'data/20180130_smallrubber_white_8.2um_5_vs_sodalime_205.4g_.xlsx'
soda_wrubber8_2um5df = data.friction_data(soda_wrubber8_2um5, load_gram_22)

#15 um PAC on white rubber (2cm*2cm) vs soda, load = 205.6
soda_wrubber15um1 = 'data/20171214_smallrubber_white_15um_1_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_wrubber15um1df = data.friction_data(soda_wrubber15um1, load_gram_20)
soda_wrubber15um2 = 'data/20171214_smallrubber_white_15um_2_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_wrubber15um2df = data.friction_data(soda_wrubber15um2, load_gram_20)
soda_wrubber15um3 = 'data/20171214_smallrubber_white_15um_3_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_wrubber15um3df = data.friction_data(soda_wrubber15um3, load_gram_20)
soda_wrubber15um4 = 'data/20171214_smallrubber_white_15um_4_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_wrubber15um4df = data.friction_data(soda_wrubber15um4, load_gram_20)
soda_wrubber15um5 = 'data/20171214_smallrubber_white_15um_5_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_wrubber15um5df = data.friction_data(soda_wrubber15um5, load_gram_20)

#0.26 um PAHT on small rubber (2cm*2cm) vs soda lime wafer, load =205.9
soda_wrubber0_26umHT1 = 'data/20171211_smallrubber_white_0.26um_HT_1_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_wrubber0_26umHT1df = data.friction_data(soda_wrubber0_26umHT1, load_gram_15)
soda_wrubber0_26umHT2 = 'data/20171211_smallrubber_white_0.26um_HT_2_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_wrubber0_26umHT2df = data.friction_data(soda_wrubber0_26umHT2, load_gram_15)
soda_wrubber0_26umHT3 = 'data/20171211_smallrubber_white_0.26um_HT_3_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_wrubber0_26umHT3df = data.friction_data(soda_wrubber0_26umHT3, load_gram_15)
soda_wrubber0_26umHT4 = 'data/20171211_smallrubber_white_0.26um_HT_4_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_wrubber0_26umHT4df = data.friction_data(soda_wrubber0_26umHT4, load_gram_15)
soda_wrubber0_26umHT5 = 'data/20171211_smallrubber_white_0.26um_HT_5_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_wrubber0_26umHT5df = data.friction_data(soda_wrubber0_26umHT5, load_gram_15)

#0.64 um PAHT on small rubber (2cm*2cm) vs soda lime wafer, load =205.9
soda_wrubber0_64umHT1 = 'data/20171211_smallrubber_white_0.64um_HT_1_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_wrubber0_64umHT1df = data.friction_data(soda_wrubber0_64umHT1, load_gram_15)
soda_wrubber0_64umHT2 = 'data/20171211_smallrubber_white_0.64um_HT_2_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_wrubber0_64umHT2df = data.friction_data(soda_wrubber0_64umHT2, load_gram_15)
soda_wrubber0_64umHT3 = 'data/20171211_smallrubber_white_0.64um_HT_3_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_wrubber0_64umHT3df = data.friction_data(soda_wrubber0_64umHT3, load_gram_15)
soda_wrubber0_64umHT4 = 'data/20171211_smallrubber_white_0.64um_HT_4_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_wrubber0_64umHT4df = data.friction_data(soda_wrubber0_64umHT4, load_gram_15)
soda_wrubber0_64umHT5 = 'data/20171211_smallrubber_white_0.64um_HT_5_vs_sodalime_#5_205.9g_load_2.xlsx'
soda_wrubber0_64umHT5df = data.friction_data(soda_wrubber0_64umHT5, load_gram_15)

#1.1 um PAHT on small rubber (2cm*2cm) vs soda lime wafer, load =205.6
soda_wrubber1_1umHT1 = 'data/20180109_smallrubber_white_1.1um_HT_1_vs_sodalime_205.6g_.xlsx'
soda_wrubber1_1umHT1df = data.friction_data(soda_wrubber1_1umHT1, load_gram_20)
soda_wrubber1_1umHT2 = 'data/20180109_smallrubber_white_1.1um_HT_2_vs_sodalime_205.6g_.xlsx'
soda_wrubber1_1umHT2df = data.friction_data(soda_wrubber1_1umHT2, load_gram_20)
soda_wrubber1_1umHT3 = 'data/20180109_smallrubber_white_1.1um_HT_3_vs_sodalime_205.6g_.xlsx'
soda_wrubber1_1umHT3df = data.friction_data(soda_wrubber1_1umHT3, load_gram_20)
soda_wrubber1_1umHT4 = 'data/20180109_smallrubber_white_1.1um_HT_4_vs_sodalime_205.6g_.xlsx'
soda_wrubber1_1umHT4df = data.friction_data(soda_wrubber1_1umHT4, load_gram_20)
soda_wrubber1_1umHT5 = 'data/20180109_smallrubber_white_1.1um_HT_5_vs_sodalime_205.6g_.xlsx'
soda_wrubber1_1umHT5df = data.friction_data(soda_wrubber1_1umHT5, load_gram_20)

#5.3 um PAHT on small rubber (2cm*2cm) vs soda lime wafer, load =205.6
soda_wrubber5_3umHT1 = 'data/20180109_smallrubber_white_5.3um_HT_1_vs_sodalime_205.6g_.xlsx'
soda_wrubber5_3umHT1df = data.friction_data(soda_wrubber5_3umHT1, load_gram_20)
soda_wrubber5_3umHT2 = 'data/20180109_smallrubber_white_5.3um_HT_2_vs_sodalime_205.6g_.xlsx'
soda_wrubber5_3umHT2df = data.friction_data(soda_wrubber5_3umHT2,load_gram_20)
soda_wrubber5_3umHT3 = 'data/20180109_smallrubber_white_5.3um_HT_3_vs_sodalime_205.6g_.xlsx'
soda_wrubber5_3umHT3df = data.friction_data(soda_wrubber5_3umHT3, load_gram_20)
soda_wrubber5_3umHT4 = 'data/20180109_smallrubber_white_5.3um_HT_4_vs_sodalime_205.6g_.xlsx'
soda_wrubber5_3umHT4df = data.friction_data(soda_wrubber5_3umHT4, load_gram_20)
soda_wrubber5_3umHT5 = 'data/20180109_smallrubber_white_5.3um_HT_5_vs_sodalime_205.6g_.xlsx'
soda_wrubber5_3umHT5df = data.friction_data(soda_wrubber5_3umHT5, load_gram_20)

#6.1 um PAHT on small rubber (2cm*2cm) vs soda lime wafer, load =205.3
soda_wrubber6_1umHT1 = 'data/20180213_smallrubber_white_6.1umHT_1_vs_sodalime_205.3g_.xlsx'
soda_wrubber6_1umHT1df = data.friction_data(soda_wrubber6_1umHT1, load_gram_26)
soda_wrubber6_1umHT2 = 'data/20180213_smallrubber_white_6.1umHT_2_vs_sodalime_205.3g_.xlsx'
soda_wrubber6_1umHT2df = data.friction_data(soda_wrubber6_1umHT2, load_gram_26)
soda_wrubber6_1umHT3 = 'data/20180213_smallrubber_white_6.1umHT_3_vs_sodalime_205.3g_.xlsx'
soda_wrubber6_1umHT3df = data.friction_data(soda_wrubber6_1umHT3, load_gram_26)
soda_wrubber6_1umHT4 = 'data/20180213_smallrubber_white_6.1umHT_4_vs_sodalime_205.3g_.xlsx'
soda_wrubber6_1umHT4df = data.friction_data(soda_wrubber6_1umHT4, load_gram_26)
soda_wrubber6_1umHT5 = 'data/20180213_smallrubber_white_6.1umHT_5_vs_sodalime_205.3g_.xlsx'
soda_wrubber6_1umHT5df = data.friction_data(soda_wrubber6_1umHT5, load_gram_26)


#7_5 um PAHT on small rubber (2cm*2cm) vs soda lime wafer, load =205.6
soda_wrubber7_5umHT1 = 'data/20180109_smallrubber_white_7.5um_HT_1_vs_sodalime_205.6g_.xlsx'
soda_wrubber7_5umHT1df = data.friction_data(soda_wrubber7_5umHT1, load_gram_20)
soda_wrubber7_5umHT2 = 'data/20180109_smallrubber_white_7.5um_HT_2_vs_sodalime_205.6g_.xlsx'
soda_wrubber7_5umHT2df = data.friction_data(soda_wrubber7_5umHT2, load_gram_20)
soda_wrubber7_5umHT3 = 'data/20180109_smallrubber_white_7.5um_HT_3_vs_sodalime_205.6g_.xlsx'
soda_wrubber7_5umHT3df = data.friction_data(soda_wrubber7_5umHT3, load_gram_20)
soda_wrubber7_5umHT4 = 'data/20180109_smallrubber_white_7.5um_HT_4_vs_sodalime_205.6g_.xlsx'
soda_wrubber7_5umHT4df = data.friction_data(soda_wrubber7_5umHT4, load_gram_20)
soda_wrubber7_5umHT5 = 'data/20180109_smallrubber_white_7.5um_HT_5_vs_sodalime_205.6g_.xlsx'
soda_wrubber7_5umHT5df = data.friction_data(soda_wrubber7_5umHT5, load_gram_20)


#19 um PAHT on white rubber (2cm*2cm) vs soda, load = 205.6
soda_wrubber19umHT1 = 'data/20171214_smallrubber_white_19um_HT_1_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_wrubber19umHT1df = data.friction_data(soda_wrubber19umHT1, load_gram_20)
soda_wrubber19umHT2 = 'data/20171214_smallrubber_white_19um_HT_2_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_wrubber19umHT2df = data.friction_data(soda_wrubber19umHT2, load_gram_20)
soda_wrubber19umHT3 = 'data/20171214_smallrubber_white_19um_HT_3_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_wrubber19umHT3df = data.friction_data(soda_wrubber19umHT3, load_gram_20)
soda_wrubber19umHT4 = 'data/20171214_smallrubber_white_19um_HT_4_vs_sodalime_#6_205.6g_load_1.xlsx'
soda_wrubber19umHT4df = data.friction_data(soda_wrubber19umHT4, load_gram_20)

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

#0.6 um PAC on small rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 205.9
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

#3.6 um PAC on small rubber (2cm*2cm) vs soda lime wafer, load = 205.6
soda3_6um_srubber3_6um6 = 'data/20171214_smallrubber_3.6um_1_vs_sodalime_3,6UM_205.6g_load_1.xlsx'
soda3_6um_srubber3_6um6df = data.friction_data(soda3_6um_srubber3_6um6, load_gram_20)
soda3_6um_srubber3_6um7 = 'data/20171214_smallrubber_3.6um_2_vs_sodalime_3,6UM_205.6g_load_1.xlsx'
soda3_6um_srubber3_6um7df = data.friction_data(soda3_6um_srubber3_6um7, load_gram_20)
soda3_6um_srubber3_6um8 = 'data/20171214_smallrubber_3.6um_3_vs_sodalime_3,6UM_205.6g_load_1.xlsx'
soda3_6um_srubber3_6um8df = data.friction_data(soda3_6um_srubber3_6um8, load_gram_20)
soda3_6um_srubber3_6um9 = 'data/20171214_smallrubber_3.6um_4_vs_sodalime_3,6UM_205.6g_load_1.xlsx'
soda3_6um_srubber3_6um9df = data.friction_data(soda3_6um_srubber3_6um9, load_gram_20)


#5 um PAC on samll rubber(2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 205.9
soda3_6um_srubber5um1 = 'data/20171211_smallrubber_5um_1_vs_sodalime_3.6um_205.9g_load_1.xlsx'
soda3_6um_srubber5um1df = data.friction_data(soda3_6um_srubber5um1, load_gram_15)
soda3_6um_srubber5um2 = 'data/20171211_smallrubber_5um_2_vs_sodalime_3.6um_205.9g_load_1.xlsx'
soda3_6um_srubber5um2df = data.friction_data(soda3_6um_srubber5um2, load_gram_15)
soda3_6um_srubber5um3 = 'data/20171211_smallrubber_5um_3_vs_sodalime_3.6um_205.9g_load_1.xlsx'
soda3_6um_srubber5um3df = data.friction_data(soda3_6um_srubber5um3, load_gram_15)
soda3_6um_srubber5um4 = 'data/20171211_smallrubber_5um_4_vs_sodalime_3.6um_205.9g_load_1.xlsx'
soda3_6um_srubber5um4df = data.friction_data(soda3_6um_srubber5um4, load_gram_15)

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

#15 um PAC on small rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 205.6
soda3_6um_srubber15um1 = 'data/20171214_smallrubber_15um_1_vs_sodalime_3.6um_205.6g_load_1.xlsx'
soda3_6um_srubber15um1df = data.friction_data(soda3_6um_srubber15um1, load_gram_20)
soda3_6um_srubber15um2 = 'data/20171214_smallrubber_15um_2_vs_sodalime_3.6um_205.6g_load_1.xlsx'
soda3_6um_srubber15um2df = data.friction_data(soda3_6um_srubber15um2, load_gram_20)
soda3_6um_srubber15um3 = 'data/20171214_smallrubber_15um_3_vs_sodalime_3.6um_205.6g_load_1.xlsx'
soda3_6um_srubber15um3df = data.friction_data(soda3_6um_srubber15um3, load_gram_20)
soda3_6um_srubber15um4 = 'data/20171214_smallrubber_15um_4_vs_new_sodalime_3.6um_205.6g_load_1.xlsx'
soda3_6um_srubber15um4df = data.friction_data(soda3_6um_srubber15um4, load_gram_20)

#0.26 um PAHT on small rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load =205.9
soda3_6um_srubber0_26umHT1 = 'data/20171211_smallrubber_0.26um_HT_1_vs_sodalime_3.6um_205.9g_load_2.xlsx'
soda3_6um_srubber0_26umHT1df = data.friction_data(soda3_6um_srubber0_26umHT1, load_gram_15)
soda3_6um_srubber0_26umHT2 = 'data/20171211_smallrubber_0.26um_HT_2_vs_sodalime_3.6um_205.9g_load_2.xlsx'
soda3_6um_srubber0_26umHT2df = data.friction_data(soda3_6um_srubber0_26umHT2, load_gram_15)
soda3_6um_srubber0_26umHT3 = 'data/20171211_smallrubber_0.26um_HT_3_vs_sodalime_3.6um_205.9g_load_2.xlsx'
soda3_6um_srubber0_26umHT3df = data.friction_data(soda3_6um_srubber0_26umHT3, load_gram_15)
soda3_6um_srubber0_26umHT4 = 'data/20171211_smallrubber_0.26um_HT_4_vs_sodalime_3.6um_205.9g_load_2.xlsx'
soda3_6um_srubber0_26umHT4df = data.friction_data(soda3_6um_srubber0_26umHT4, load_gram_15)

#0.64 um PAHT on small rubber (2cm*2cm) vs soda, load =205.9
soda3_6um_srubber0_64umHT1 = 'data/20171211_smallrubber_0.64um_HT_1_vs_sodalime_3.6um_205.9g_load_2.xlsx'
soda3_6um_srubber0_64umHT1df = data.friction_data(soda3_6um_srubber0_64umHT1, load_gram_15)
soda3_6um_srubber0_64umHT2 = 'data/20171211_smallrubber_0.64um_HT_2_vs_sodalime_3.6um_205.9g_load_2.xlsx'
soda3_6um_srubber0_64umHT2df = data.friction_data(soda3_6um_srubber0_64umHT2, load_gram_15)
soda3_6um_srubber0_64umHT3 = 'data/20171211_smallrubber_0.64um_HT_3_vs_sodalime_3.6um_205.9g_load_2.xlsx'
soda3_6um_srubber0_64umHT3df = data.friction_data(soda3_6um_srubber0_64umHT3, load_gram_15)
soda3_6um_srubber0_64umHT4 = 'data/20171211_smallrubber_0.64um_HT_4_vs_sodalime_3.6um_205.9g_load_2.xlsx'
soda3_6um_srubber0_64umHT4df = data.friction_data(soda3_6um_srubber0_64umHT4, load_gram_15)

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

#19 um PAHT on small rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 205.6
soda3_6um_srubber19umHT1 = 'data/20171214_smallrubber_19um_HT_1_vs_sodalime_3,6UM_205.6g_load_1.xlsx'
soda3_6um_srubber19umHT1df = data.friction_data(soda3_6um_srubber19umHT1, load_gram_20)
soda3_6um_srubber19umHT2 = 'data/20171214_smallrubber_19um_HT_2_vs_sodalime_3,6UM_205.6g_load_1.xlsx'
soda3_6um_srubber19umHT2df = data.friction_data(soda3_6um_srubber19umHT2, load_gram_20)
soda3_6um_srubber19umHT3 = 'data/20171214_smallrubber_19um_HT_3_vs_sodalime_3,6UM_205.6g_load_1.xlsx'
soda3_6um_srubber19umHT3df = data.friction_data(soda3_6um_srubber19umHT3, load_gram_20)
soda3_6um_srubber19umHT4 = 'data/20171214_smallrubber_19um_HT_4_vs_sodalime_3,6UM_205.6g_load_1.xlsx'
soda3_6um_srubber19umHT4df = data.friction_data(soda3_6um_srubber19umHT4, load_gram_20)

#6.1 um PAHT, SF6 plasma 2 min 50 W 200 mTorr on small rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load =205.5
soda3_6um_srubber6_1umHT_SF61 = 'data/20180214_smallrubber_6.1umHT_SF6_1_vs_sodalime_3.6um_205.5g_.xlsx'
soda3_6um_srubber6_1umHT_SF61df = data.friction_data(soda3_6um_srubber6_1umHT_SF61, load_gram_8)
soda3_6um_srubber6_1umHT_SF62 = 'data/20180214_smallrubber_6.1umHT_SF6_2_vs_sodalime_3.6um_205.5g_.xlsx'
soda3_6um_srubber6_1umHT_SF62df = data.friction_data(soda3_6um_srubber6_1umHT_SF62, load_gram_8)
soda3_6um_srubber6_1umHT_SF63 = 'data/20180214_smallrubber_6.1umHT_SF6_3_vs_sodalime_3.6um_205.5g_.xlsx'
soda3_6um_srubber6_1umHT_SF63df = data.friction_data(soda3_6um_srubber6_1umHT_SF63, load_gram_8)
soda3_6um_srubber6_1umHT_SF64 = 'data/20180214_smallrubber_6.1umHT_SF6_4_vs_sodalime_3.6um_205.5g_.xlsx'
soda3_6um_srubber6_1umHT_SF64df = data.friction_data(soda3_6um_srubber6_1umHT_SF64, load_gram_8)
soda3_6um_srubber6_1umHT_SF65 = 'data/20180214_smallrubber_6.1umHT_SF6_5_vs_sodalime_3.6um_205.5g_.xlsx'
soda3_6um_srubber6_1umHT_SF65df = data.friction_data(soda3_6um_srubber6_1umHT_SF65, load_gram_8)

## white rubber
#sample: white rubber pieces (small), substrate: ssoda lime wafer with 3.6 um PAC
#0um on white rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 205.9
soda3_6um_wrubber0um1 = 'data/20171211_smallrubber_white_0um_1_vs_sodalime_3.6um_205.9g_load_2.xlsx'
soda3_6um_wrubber0um1df = data.friction_data(soda3_6um_wrubber0um1, load_gram_15)

#0.25 um PAC on white rubber (2cm*2cm) vs soda lime waferwith 3.6 um PAC, load = 205.4
soda3_6um_wrubber0_25um1 = 'data/20180124_smallrubber_white_0.25um_1_vs_sodalime_3.6um_205.4g_.xlsx'
soda3_6um_wrubber0_25um1df = data.friction_data(soda3_6um_wrubber0_25um1, load_gram_22)
soda3_6um_wrubber0_25um2 = 'data/20180124_smallrubber_white_0.25um_2_vs_sodalime_3.6um_205.4g_.xlsx'
soda3_6um_wrubber0_25um2df = data.friction_data(soda3_6um_wrubber0_25um2, load_gram_22)
soda3_6um_wrubber0_25um3 = 'data/20180124_smallrubber_white_0.25um_3_vs_sodalime_3.6um_205.4g_.xlsx'
soda3_6um_wrubber0_25um3df = data.friction_data(soda3_6um_wrubber0_25um3, load_gram_22)
soda3_6um_wrubber0_25um4 = 'data/20180124_smallrubber_white_0.25um_4_vs_sodalime_3.6um_205.4g_.xlsx'
soda3_6um_wrubber0_25um4df = data.friction_data(soda3_6um_wrubber0_25um4, load_gram_22)
soda3_6um_wrubber0_25um5 = 'data/20180124_smallrubber_white_0.25um_5_vs_sodalime_3.6um_205.4g_.xlsx'
soda3_6um_wrubber0_25um5df = data.friction_data(soda3_6um_wrubber0_25um5, load_gram_22)

#0.7 um PAC on white rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 205.4
soda3_6um_wrubber0_7um1 = 'data/20180124_smallrubber_white_0.7um_1_vs_sodalime_3.6um_205.4g_.xlsx'
soda3_6um_wrubber0_7um1df = data.friction_data(soda3_6um_wrubber0_7um1, load_gram_22)
soda3_6um_wrubber0_7um2 = 'data/20180124_smallrubber_white_0.7um_2_vs_sodalime_3.6um_205.4g_.xlsx'
soda3_6um_wrubber0_7um2df = data.friction_data(soda3_6um_wrubber0_7um2, load_gram_22)
soda3_6um_wrubber0_7um3 = 'data/20180124_smallrubber_white_0.7um_3_vs_sodalime_3.6um_205.4g_.xlsx'
soda3_6um_wrubber0_7um3df = data.friction_data(soda3_6um_wrubber0_7um3, load_gram_22)
soda3_6um_wrubber0_7um4 = 'data/20180124_smallrubber_white_0.7um_4_vs_sodalime_3.6um_205.4g_.xlsx'
soda3_6um_wrubber0_7um4df = data.friction_data(soda3_6um_wrubber0_7um4, load_gram_22)
soda3_6um_wrubber0_7um5 = 'data/20180124_smallrubber_white_0.7um_5_vs_sodalime_3.6um_205.4g_.xlsx'
soda3_6um_wrubber0_7um5df = data.friction_data(soda3_6um_wrubber0_7um5, load_gram_22)

#1.2 um PAC on white rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 205.4
soda3_6um_wrubber1_2um1 = 'data/20180201_smallrubber_white_1.2um_1_vs_sodalime_3.6um_205.4g_.xlsx'
soda3_6um_wrubber1_2um1df = data.friction_data(soda3_6um_wrubber1_2um1, load_gram_22)
soda3_6um_wrubber1_2um2 = 'data/20180201_smallrubber_white_1.2um_2_vs_sodalime_3.6um_205.4g_.xlsx'
soda3_6um_wrubber1_2um2df = data.friction_data(soda3_6um_wrubber1_2um2, load_gram_22)
soda3_6um_wrubber1_2um3 = 'data/20180201_smallrubber_white_1.2um_3_vs_sodalime_3.6um_205.4g_.xlsx'
soda3_6um_wrubber1_2um3df = data.friction_data(soda3_6um_wrubber1_2um3, load_gram_22)
soda3_6um_wrubber1_2um4 = 'data/20180201_smallrubber_white_1.2um_4_vs_sodalime_3.6um_205.4g_.xlsx'
soda3_6um_wrubber1_2um4df = data.friction_data(soda3_6um_wrubber1_2um4, load_gram_22)
soda3_6um_wrubber1_2um5 = 'data/20180201_smallrubber_white_1.2um_5_vs_sodalime_3.6um_205.4g_.xlsx'
soda3_6um_wrubber1_2um5df = data.friction_data(soda3_6um_wrubber1_2um5, load_gram_22)

#3.6 um PAC on white rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 205.6
soda3_6um_wrubber3_6um1 = 'data/20171214_smallrubber_white_3.6um_1_vs_sodalime_3.6um_205.6g_load_1.xlsx'
soda3_6um_wrubber3_6um1df = data.friction_data(soda3_6um_wrubber3_6um1, load_gram_20)
soda3_6um_wrubber3_6um2 = 'data/20171214_smallrubber_white_3.6um_2_vs_sodalime_3.6um_205.6g_load_1.xlsx'
soda3_6um_wrubber3_6um2df = data.friction_data(soda3_6um_wrubber3_6um2, load_gram_20)
soda3_6um_wrubber3_6um3 = 'data/20171214_smallrubber_white_3.6um_3_vs_sodalime_3.6um_205.6g_load_1.xlsx'
soda3_6um_wrubber3_6um3df = data.friction_data(soda3_6um_wrubber3_6um3, load_gram_20)
soda3_6um_wrubber3_6um4 = 'data/20171214_smallrubber_white_3.6um_4_vs_sodalime_3.6um_205.6g_load_1.xlsx'
soda3_6um_wrubber3_6um4df = data.friction_data(soda3_6um_wrubber3_6um4, load_gram_20)
soda3_6um_wrubber3_6um5 = 'data/20171214_smallrubber_white_3.6um_5_vs_sodalime_3.6um_205.6g_load_1.xlsx'
soda3_6um_wrubber3_6um5df = data.friction_data(soda3_6um_wrubber3_6um5, load_gram_20)

#5 um PAC on white rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 205.9
soda3_6um_wrubber5um1 = 'data/20171211_smallrubber_white_5um_1_vs_sodalime_3.6um_205.9g_load_1.xlsx'
soda3_6um_wrubber5um1df = data.friction_data(soda3_6um_wrubber5um1, load_gram_15)
soda3_6um_wrubber5um2 = 'data/20171211_smallrubber_white_5um_2_vs_sodalime_3.6um_205.9g_load_1.xlsx'
soda3_6um_wrubber5um2df = data.friction_data(soda3_6um_wrubber5um2, load_gram_15)
soda3_6um_wrubber5um3 = 'data/20171211_smallrubber_white_5um_3_vs_sodalime_3.6um_205.9g_load_1.xlsx'
soda3_6um_wrubber5um3df = data.friction_data(soda3_6um_wrubber5um3, load_gram_15)
soda3_6um_wrubber5um4 = 'data/20171211_smallrubber_white_5um_4_vs_sodalime_3.6um_205.9g_load_1.xlsx'
soda3_6um_wrubber5um4df = data.friction_data(soda3_6um_wrubber5um4, load_gram_15)
soda3_6um_wrubber5um5 = 'data/20171211_smallrubber_white_5um_5_vs_sodalime_3.6um_205.9g_load_1.xlsx'
soda3_6um_wrubber5um5df = data.friction_data(soda3_6um_wrubber5um5, load_gram_15)

#8.2 um PAC on white rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 205.4
soda3_6um_wrubber8_2um1 = 'data/20180130_smallrubber_white_8.2um_1_vs_sodalime_3.6um_205.4g_.xlsx'
soda3_6um_wrubber8_2um1df = data.friction_data(soda3_6um_wrubber8_2um1, load_gram_22)
soda3_6um_wrubber8_2um2 = 'data/20180130_smallrubber_white_8.2um_2_vs_sodalime_3.6um_205.4g_.xlsx'
soda3_6um_wrubber8_2um2df = data.friction_data(soda3_6um_wrubber8_2um2, load_gram_22)
soda3_6um_wrubber8_2um3 = 'data/20180130_smallrubber_white_8.2um_3_vs_sodalime_3.6um_205.4g_.xlsx'
soda3_6um_wrubber8_2um3df = data.friction_data(soda3_6um_wrubber8_2um3, load_gram_22)
soda3_6um_wrubber8_2um4 = 'data/20180130_smallrubber_white_8.2um_4_vs_sodalime_3.6um_205.4g_.xlsx'
soda3_6um_wrubber8_2um4df = data.friction_data(soda3_6um_wrubber8_2um4, load_gram_22)
soda3_6um_wrubber8_2um5 = 'data/20180130_smallrubber_white_8.2um_5_vs_sodalime_3.6um_205.4g_.xlsx'
soda3_6um_wrubber8_2um5df = data.friction_data(soda3_6um_wrubber8_2um5, load_gram_22)

#15 um PAC on white rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 205.6
soda3_6um_wrubber15um1 = 'data/20171214_smallrubber_white_15um_1_vs_sodalime_3.6um_205.6g_load_1.xlsx'
soda3_6um_wrubber15um1df = data.friction_data(soda3_6um_wrubber15um1, load_gram_20)
soda3_6um_wrubber15um2 = 'data/20171214_smallrubber_white_15um_2_vs_sodalime_3.6um_205.6g_load_1.xlsx'
soda3_6um_wrubber15um2df = data.friction_data(soda3_6um_wrubber15um2, load_gram_20)
soda3_6um_wrubber15um3 = 'data/20171214_smallrubber_white_15um_3_vs_sodalime_3.6um_205.6g_load_1.xlsx'
soda3_6um_wrubber15um3df = data.friction_data(soda3_6um_wrubber15um3, load_gram_20)
soda3_6um_wrubber15um4 = 'data/20171214_smallrubber_white_15um_4_vs_sodalime_3.6um_205.6g_load_1.xlsx'
soda3_6um_wrubber15um4df = data.friction_data(soda3_6um_wrubber15um4, load_gram_20)
soda3_6um_wrubber15um5 = 'data/20171214_smallrubber_white_15um_5_vs_sodalime_3.6um_205.6g_load_1.xlsx'
soda3_6um_wrubber15um5df = data.friction_data(soda3_6um_wrubber15um5, load_gram_20)

#0.26 um PAHT on small rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load =205.9
soda3_6um_wrubber0_26umHT1 = 'data/20171211_smallrubber_white_0.26um_HT_1_vs_sodalime_3.6um_205.9g_load_2.xlsx'
soda3_6um_wrubber0_26umHT1df = data.friction_data(soda3_6um_wrubber0_26umHT1, load_gram_15)
soda3_6um_wrubber0_26umHT2 = 'data/20171211_smallrubber_white_0.26um_HT_2_vs_sodalime_3.6um_205.9g_load_2.xlsx'
soda3_6um_wrubber0_26umHT2df = data.friction_data(soda3_6um_wrubber0_26umHT2, load_gram_15)
soda3_6um_wrubber0_26umHT3 = 'data/20171211_smallrubber_white_0.26um_HT_3_vs_sodalime_3.6um_205.9g_load_2.xlsx'
soda3_6um_wrubber0_26umHT3df = data.friction_data(soda3_6um_wrubber0_26umHT3, load_gram_15)
soda3_6um_wrubber0_26umHT4 = 'data/20171211_smallrubber_white_0.26um_HT_4_vs_sodalime_3.6um_205.9g_load_2.xlsx'
soda3_6um_wrubber0_26umHT4df = data.friction_data(soda3_6um_wrubber0_26umHT4, load_gram_15)
soda3_6um_wrubber0_26umHT5 = 'data/20171211_smallrubber_white_0.26um_HT_5_vs_sodalime_3.6um_205.9g_load_2.xlsx'
soda3_6um_wrubber0_26umHT5df = data.friction_data(soda3_6um_wrubber0_26umHT5, load_gram_15)

#0.64 um PAHT on small rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load =205.9
soda3_6um_wrubber0_64umHT1 = 'data/20171211_smallrubber_white_0.64um_HT_1_vs_sodalime_3.6um_205.9g_load_2.xlsx'
soda3_6um_wrubber0_64umHT1df = data.friction_data(soda3_6um_wrubber0_64umHT1, load_gram_15)
soda3_6um_wrubber0_64umHT2 = 'data/20171211_smallrubber_white_0.64um_HT_2_vs_sodalime_3.6um_205.9g_load_2.xlsx'
soda3_6um_wrubber0_64umHT2df = data.friction_data(soda3_6um_wrubber0_64umHT2, load_gram_15)
soda3_6um_wrubber0_64umHT3 = 'data/20171211_smallrubber_white_0.64um_HT_3_vs_sodalime_3.6um_205.9g_load_2.xlsx'
soda3_6um_wrubber0_64umHT3df = data.friction_data(soda3_6um_wrubber0_64umHT3, load_gram_15)
soda3_6um_wrubber0_64umHT4 = 'data/20171211_smallrubber_white_0.64um_HT_4_vs_sodalime_3.6um_205.9g_load_2.xlsx'
soda3_6um_wrubber0_64umHT4df = data.friction_data(soda3_6um_wrubber0_64umHT4, load_gram_15)
soda3_6um_wrubber0_64umHT5 = 'data/20171211_smallrubber_white_0.64um_HT_5_vs_sodalime_3.6um_205.9g_load_2.xlsx'
soda3_6um_wrubber0_64umHT5df = data.friction_data(soda3_6um_wrubber0_64umHT5, load_gram_15)

#1.1 um PAHT on small rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load =206
soda3_6um_wrubber1_1umHT1 = 'data/20180109_smallrubber_white_1.1um_HT_1_vs_sodalime_3.6um_205.6g_.xlsx'
soda3_6um_wrubber1_1umHT1df = data.friction_data(soda3_6um_wrubber1_1umHT1, load_gram_13)
soda3_6um_wrubber1_1umHT2 = 'data/20180109_smallrubber_white_1.1um_HT_2_vs_sodalime_3.6um_205.6g_.xlsx'
soda3_6um_wrubber1_1umHT2df = data.friction_data(soda3_6um_wrubber1_1umHT2, load_gram_13)
soda3_6um_wrubber1_1umHT3 = 'data/20180109_smallrubber_white_1.1um_HT_3_vs_sodalime_3.6um_205.6g_.xlsx'
soda3_6um_wrubber1_1umHT3df = data.friction_data(soda3_6um_wrubber1_1umHT3, load_gram_13)
soda3_6um_wrubber1_1umHT4 = 'data/20180109_smallrubber_white_1.1um_HT_4_vs_sodalime_3.6um_205.6g_.xlsx'
soda3_6um_wrubber1_1umHT4df = data.friction_data(soda3_6um_wrubber1_1umHT4, load_gram_13)
soda3_6um_wrubber1_1umHT5 = 'data/20180109_smallrubber_white_1.1um_HT_5_vs_sodalime_3.6um_205.6g_.xlsx'
soda3_6um_wrubber1_1umHT5df = data.friction_data(soda3_6um_wrubber1_1umHT5, load_gram_13)

#5.3 um PAHT on small rubber (2cm*2cm) vs soda3_6um lime wafer with 3.6 um PAC, load =206
soda3_6um_wrubber5_3umHT1 = 'data/20180109_smallrubber_white_5.3um_HT_1_vs_sodalime_3.6um_205.6g_.xlsx'
soda3_6um_wrubber5_3umHT1df = data.friction_data(soda3_6um_wrubber5_3umHT1, load_gram_13)
soda3_6um_wrubber5_3umHT2 = 'data/20180109_smallrubber_white_5.3um_HT_2_vs_sodalime_3.6um_205.6g_.xlsx'
soda3_6um_wrubber5_3umHT2df = data.friction_data(soda3_6um_wrubber5_3umHT2, load_gram_13)
soda3_6um_wrubber5_3umHT3 = 'data/20180109_smallrubber_white_5.3um_HT_3_vs_sodalime_3.6um_205.6g_.xlsx'
soda3_6um_wrubber5_3umHT3df = data.friction_data(soda3_6um_wrubber5_3umHT3, load_gram_13)
soda3_6um_wrubber5_3umHT4 = 'data/20180109_smallrubber_white_5.3um_HT_4_vs_sodalime_3.6um_205.6g_.xlsx'
soda3_6um_wrubber5_3umHT4df = data.friction_data(soda3_6um_wrubber5_3umHT4, load_gram_13)
soda3_6um_wrubber5_3umHT5 = 'data/20180109_smallrubber_white_5.3um_HT_5_vs_sodalime_3.6um_205.6g_.xlsx'
soda3_6um_wrubber5_3umHT5df = data.friction_data(soda3_6um_wrubber5_3umHT5, load_gram_13)

#6.1 um PAHT on small rubber (2cm*2cm) vs soda3_6um lime wafer with 3.6 um PAC,, load =205.3
soda3_6um_wrubber6_1umHT1 = 'data/20180213_smallrubber_white_6.1umHT_1_vs_sodalime_3.6um_205.3g_.xlsx'
soda3_6um_wrubber6_1umHT1df = data.friction_data(soda3_6um_wrubber6_1umHT1, load_gram_26)
soda3_6um_wrubber6_1umHT2 = 'data/20180213_smallrubber_white_6.1umHT_2_vs_sodalime_3.6um_205.3g_.xlsx'
soda3_6um_wrubber6_1umHT2df = data.friction_data(soda3_6um_wrubber6_1umHT2, load_gram_26)
soda3_6um_wrubber6_1umHT3 = 'data/20180213_smallrubber_white_6.1umHT_3_vs_sodalime_3.6um_205.3g_.xlsx'
soda3_6um_wrubber6_1umHT3df = data.friction_data(soda3_6um_wrubber6_1umHT3, load_gram_26)
soda3_6um_wrubber6_1umHT4 = 'data/20180213_smallrubber_white_6.1umHT_4_vs_sodalime_3.6um_205.3g_.xlsx'
soda3_6um_wrubber6_1umHT4df = data.friction_data(soda3_6um_wrubber6_1umHT4, load_gram_26)
soda3_6um_wrubber6_1umHT5 = 'data/20180213_smallrubber_white_6.1umHT_5_vs_sodalime_3.6um_205.3g_.xlsx'
soda3_6um_wrubber6_1umHT5df = data.friction_data(soda3_6um_wrubber6_1umHT5, load_gram_26)


#7_5 um PAHT on small rubber (2cm*2cm) vs soda3_6um lime wafer with 3.6 um PAC, load =206
soda3_6um_wrubber7_5umHT1 = 'data/20180109_smallrubber_white_7.5um_HT_1_vs_sodalime_3.6um_205.6g_.xlsx'
soda3_6um_wrubber7_5umHT1df = data.friction_data(soda3_6um_wrubber7_5umHT1, load_gram_13)
soda3_6um_wrubber7_5umHT2 = 'data/20180109_smallrubber_white_7.5um_HT_2_vs_sodalime_3.6um_205.6g_.xlsx'
soda3_6um_wrubber7_5umHT2df = data.friction_data(soda3_6um_wrubber7_5umHT2, load_gram_13)
soda3_6um_wrubber7_5umHT3 = 'data/20180109_smallrubber_white_7.5um_HT_3_vs_sodalime_3.6um_205.6g_.xlsx'
soda3_6um_wrubber7_5umHT3df = data.friction_data(soda3_6um_wrubber7_5umHT3, load_gram_13)
soda3_6um_wrubber7_5umHT4 = 'data/20180109_smallrubber_white_7.5um_HT_4_vs_sodalime_3.6um_205.6g_.xlsx'
soda3_6um_wrubber7_5umHT4df = data.friction_data(soda3_6um_wrubber7_5umHT4, load_gram_13)
soda3_6um_wrubber7_5umHT5 = 'data/20180109_smallrubber_white_7.5um_HT_5_vs_sodalime_3.6um_205.6g_.xlsx'
soda3_6um_wrubber7_5umHT5df = data.friction_data(soda3_6um_wrubber7_5umHT5, load_gram_13)

#19 um PAHT on white rubber (2cm*2cm) vs soda lime wafer with 3.6 um PAC, load = 205.6
soda3_6um_wrubber19umHT1 = 'data/20171214_smallrubber_white_19um_HT_1_vs_sodalime_3.6um_205.6g_load_1.xlsx'
soda3_6um_wrubber19umHT1df = data.friction_data(soda3_6um_wrubber19umHT1, load_gram_20)
soda3_6um_wrubber19umHT2 = 'data/20171214_smallrubber_white_19um_HT_2_vs_sodalime_3.6um_205.6g_load_1.xlsx'
soda3_6um_wrubber19umHT2df = data.friction_data(soda3_6um_wrubber19umHT2, load_gram_20)
soda3_6um_wrubber19umHT3 = 'data/20171214_smallrubber_white_19um_HT_3_vs_sodalime_3.6um_205.6g_load_1.xlsx'
soda3_6um_wrubber19umHT3df = data.friction_data(soda3_6um_wrubber19umHT3, load_gram_20)
soda3_6um_wrubber19umHT4 = 'data/20171214_smallrubber_white_19um_HT_4_vs_sodalime_3.6um_205.6g_load_1.xlsx'
soda3_6um_wrubber19umHT4df = data.friction_data(soda3_6um_wrubber19umHT4, load_gram_20)

#sample: white rubber piece(small), substrate soda lime wafer with medical fluid 360
#0 um PA on small rubber(2cm*2cm) vs soda lime wafer with oil, load = 652
soda_oil_srubber0um1 = 'data/20180214_smallrubber_oil_1_vs_sodalime_oil_652g_.xlsx'
soda_oil_srubber0um1df = data.friction_data(soda_oil_srubber0um1, load_gram_25)
soda_oil_srubber0um2 = 'data/20180214_smallrubber_oil_2_vs_sodalime_oil_652g_.xlsx'
soda_oil_srubber0um2df = data.friction_data(soda_oil_srubber0um2, load_gram_25)

#0 um PA on white rubber(2cm*2cm) vs soda lime wafer with oil, load = 652
soda_oil_wrubber0um1 = 'data/20180214_smallrubber_white_oil_1_vs_sodalime_oil_652g_.xlsx'
soda_oil_wrubber0um1df = data.friction_data(soda_oil_wrubber0um1, load_gram_25)
soda_oil_wrubber0um2 = 'data/20180214_smallrubber_white_oil_2_vs_sodalime_oil_652g_.xlsx'
soda_oil_wrubber0um2df = data.friction_data(soda_oil_wrubber0um2, load_gram_25)

#6.1 um PAHT on white rubber (2cm*2cm) vs soda lime wafer with oil, load =652
soda_oil_wrubber6_1umHT1 = 'data/20180213_smallrubber_white_6.1umHT_1_vs_sodalime_oil_652g_.xlsx'
soda_oil_wrubber6_1umHT1df = data.friction_data(soda_oil_wrubber6_1umHT1, load_gram_25)
soda_oil_wrubber6_1umHT2 = 'data/20180213_smallrubber_white_6.1umHT_2_vs_sodalime_oil_652g_.xlsx'
soda_oil_wrubber6_1umHT2df = data.friction_data(soda_oil_wrubber6_1umHT2, load_gram_25)
soda_oil_wrubber6_1umHT3 = 'data/20180213_smallrubber_white_6.1umHT_3_vs_sodalime_oil_652g_.xlsx'
soda_oil_wrubber6_1umHT3df = data.friction_data(soda_oil_wrubber6_1umHT3, load_gram_25)
soda_oil_wrubber6_1umHT4 = 'data/20180213_smallrubber_white_6.1umHT_4_vs_sodalime_oil_652g_.xlsx'
soda_oil_wrubber6_1umHT4df = data.friction_data(soda_oil_wrubber6_1umHT4, load_gram_25)
soda_oil_wrubber6_1umHT5 = 'data/20180213_smallrubber_white_6.1umHT_5_vs_sodalime_oil_652g_.xlsx'
soda_oil_wrubber6_1umHT5df = data.friction_data(soda_oil_wrubber6_1umHT5, load_gram_25)


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

plt.plot(glass1um1df['travel'], glass1um1df['load'], marker='.', linestyle='-', label = '1.1 um PAC on glass vs glass', color = '#1f77b4ff')
plt.plot(glass1um2df['travel'], glass1um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')
plt.plot(glass1um3df['travel'], glass1um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')
plt.plot(glass1um4df['travel'], glass1um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')
plt.plot(glass1um5df['travel'], glass1um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#1f77b4ff')

plt.plot(glass3um1df['travel'], glass3um1df['load'], marker='.', linestyle='-', label = '3.3 um PAC on glass vs glass', color = '#ff7f0eff')
plt.plot(glass3um2df['travel'], glass3um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')
plt.plot(glass3um3df['travel'], glass3um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')
plt.plot(glass3um4df['travel'], glass3um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')
plt.plot(glass3um5df['travel'], glass3um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#ff7f0eff')

plt.plot(COP1um1df['travel'], COP1um1df['load'], marker='.', linestyle='-', label = '1.1 um PAC on glass vs COP', color = '#2ca02cff')
plt.plot(COP1um2df['travel'], COP1um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
plt.plot(COP1um3df['travel'], COP1um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
plt.plot(COP1um4df['travel'], COP1um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')
plt.plot(COP1um5df['travel'], COP1um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#2ca02cff')

plt.plot(COP3um1df['travel'], COP3um1df['load'], marker='.', linestyle='-', label = '3.3 um PAC on glass vs COP', color = '#d62728ff')
plt.plot(COP3um2df['travel'], COP3um2df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#d62728ff')
plt.plot(COP3um3df['travel'], COP3um3df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#d62728ff')
plt.plot(COP3um4df['travel'], COP3um4df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#d62728ff')
plt.plot(COP3um5df['travel'], COP3um5df['load'], marker='.', linestyle='-', label = '_nolegend_', color = '#d62728ff')

plt.ylim(-0.2, 2.2)
plt.xlim(-2, 110)
plt.margins(0.2)
plt.xlabel('Travel Distance (mm)', fontsize=20)#
plt.ylabel('Load (N)', fontsize=20)
plt.legend(loc = 'upper right' ,prop={'size':10})
plt.tick_params(axis='both', which='major', labelsize=16)#
#plt.title('friction measurement', fontsize=24)#

plt.show()
