# ==================================================
# IMPORTS + SETUP
# ==================================================

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from CSP_calculator import determine_nuclei_types


# ==================================================
# determine_nuclei_types
# ==================================================

def test_determine_nuclei_types_hsqc():
    result = determine_nuclei_types(1)

    assert result == ("1H", "15N", 1, 0.2)

def test_determine_nuclei_types_hmqc():
    result = determine_nuclei_types(2)

    assert result == ("13C", "1H", 1, 5)


# ==================================================
# calc_CSP
# ==================================================

