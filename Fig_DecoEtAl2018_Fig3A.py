# ==========================================================================
# ==========================================================================
#  Computes the Functional Connectivity Dynamics (FCD)
#
#  From the original code:
# --------------------------------------------------------------------------
#
#  Computes simulations with the Dynamic Mean Field Model (DMF) using
#  Feedback Inhibitory Control (FIC) and Regional Drug Receptor Modulation (RDRM):
#
#  - the optimal coupling (we=2.1) for fitting the placebo condition
#  - the optimal neuromodulator gain for fitting the LSD condition (wge=0.2)
#
#  Taken from the code (FCD_LSD_simulated.m) from:
#  [DecoEtAl_2018] Deco,G., Cruzat,J., Cabral, J., Knudsen,G.M., Carhart-Harris,R.L., Whybrow,P.C.,
#       Whole-brain multimodal neuroimaging model using serotonin receptor maps explain non-linear functional effects of LSD
#       Logothetis,N.K. & Kringelbach,M.L. (2018) Current Biology
#       https://www.cell.com/current-biology/pdfExtended/S0960-9822(18)31045-5
#
#  Code written by Josephine Cruzat josephine.cruzat@upf.edu
#
#  Translated to Python by Gustavo Patow
# ==========================================================================
# ==========================================================================
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt

from pathlib import Path

filePath = 'Data_Produced/DecoEtAl2018_fneuro_NEW.mat'
if not Path(filePath).is_file():
    import Prepro_DecoEtAl2018_fgain_Neuro as prepro
    prepro.prepro_Fig3()

print('Loading {}'.format(filePath))
fNeuro = sio.loadmat(filePath)
WEs = fNeuro['we'].flatten()
fitting2 = fNeuro['fitting2'].flatten()
fitting5 = fNeuro['fitting5'].flatten()
FCDfitt2 = fNeuro['FCDfitt2'].flatten()
FCDfitt5 = fNeuro['FCDfitt5'].flatten()

# mFCDfitt5   = np.mean(FCDfitt5,2);
# stdFCDfitt5 = np.std(FCDfitt5,[],2);
# mfitting5   = np.mean(fitting5,2);
# stdfitting5 = np.std(fitting5,[],2);

maxFC = WEs[np.argmax(fitting5)]
minFCD = WEs[np.argmin(FCDfitt5)]
print("\n\n#####################################################################################################")
print(f"# Max FC({maxFC}) = {np.max(fitting5)}             ** Min FCD({minFCD}) = {np.min(FCDfitt5)} **")
print("#####################################################################################################\n\n")

plt.rcParams.update({'font.size': 15})
plotFCDpla, = plt.plot(WEs, FCDfitt5)
plotFCDpla.set_label("FCD placebo")
plotFCpla, = plt.plot(WEs, fitting5)
plotFCpla.set_label("FC placebo")
plt.title("Whole-brain fitting")
plt.ylabel("Fitting")
plt.xlabel("Global Coupling (G = we)")
plt.legend()
plt.show()


# ================================================================================================================
# ================================================================================================================
# ================================================================================================================EOF
