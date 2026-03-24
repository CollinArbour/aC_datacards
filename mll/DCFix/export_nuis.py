import re
from optparse import OptionParser
import tempfile
import sys
import numpy as np

from HiggsAnalysis.CombinedLimit.DatacardParser import *

from DatacardHelpers import datacardHelper


DC = datacardHelper.loadDatacard("datacard.txt")

# nuisances to be exported from SM to EFT 
nuisances_to_export = ["CMS_SMP24008_ptWWRew_0j_B0", "CMS_SMP24008_ptWWRew_1j_B0", "sm_LO_1j", "sm_LO_0j"]
from__ = "sm"
to__ = [i for i in datacardHelper.getDCEFTsamples(DC) if i != "sm"]

bins = DC.bins 

for nuis in nuisances_to_export:
    for bin in bins:
        datacardHelper.export_nuisance(
            DC=DC,
            base_proc=from__,
            base_bin=bin,
            nuisance_list=[nuis],
            process_list=to__,
            channel_list=[bin],
            debug=False
        )
        
datacardHelper.writeDatacard(DC, "out.txt")
