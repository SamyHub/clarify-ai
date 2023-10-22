#############################################################################
# Code description
"""Global variables for the scripts."""

#############################################################################
#############################################################################
# Modules & libraries
import os

#############################################################################
#############################################################################
# Location where the code is executed
__location__ = os.path.dirname(os.path.realpath(__file__))

#############################################################################
#############################################################################
# Different variables classes
class OpenAIkey:
    OPENAI_API_KEY = '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'

class Icons:
    iconsPath = os.path.join(__location__,'icons')
    banner = str(os.path.join(iconsPath,'banner.tiff'))