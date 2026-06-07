# ==================================================
# IMPORTS + SETUP
# ==================================================

import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import CSP_calculator as cc


# ==================================================
# determine_nuclei_types
# ==================================================

def test_determine_nuclei_types_hsqc():
    result = cc.determine_nuclei_types(1)

    assert result == ("1H", "15N", 1, 0.2)

def test_determine_nuclei_types_hmqc():
    result = cc.determine_nuclei_types(2)

    assert result == ("13C", "1H", 1, 5)


# ==================================================
# calc_CSP
# ==================================================

def test_calc_csp_hsqc_example():
    result = cc.calc_CSP(
        7.22, 7.556,       # 1H exp1/exp2
        112.64, 117.593,   # 15N exp1/exp2
        1,
        0.2
    )

    assert result == pytest.approx(0.523, abs=0.001)

def test_calc_csp_hmqc_example():
    result = cc.calc_CSP(
        20.328, 20.057,   # 13C exp1/exp2
        0.793, 0.802,     # 1H exp1/exp2
        1,
        5
    )

    assert result == pytest.approx(0.275, abs=0.001)