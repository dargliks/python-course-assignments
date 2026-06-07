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

    assert result == pytest.approx(0.137, abs=0.001)


# ==================================================
# parse_experiment_data
# ==================================================

def test_parse_experiment_data_basic():
    lines = [
        "Peak W1 W2",
        "A10 8.10 120.5",
        "A11 7.95 118.3"
    ]

    result = cc.parse_experiment_data(lines)

    assert result == {
        "A10": (8.10, 120.5),
        "A11": (7.95, 118.3)
    }

def test_parse_experiment_data_extra_columns_ignored():
    lines = [
        "Peak W1 W2 Intensity",
        "A10 8.10 120.5 9999",
        "A11 7.95 118.3 8888"
    ]

    result = cc.parse_experiment_data(lines)

    assert result == {
        "A10": (8.10, 120.5),
        "A11": (7.95, 118.3)
    }

def test_parse_experiment_data_skips_bad_lines():
    lines = [
        "Peak W1 W2",
        "A10 8.10",          # bad line
        "A11 7.95 118.3"
    ]

    result = cc.parse_experiment_data(lines)

    assert result == {
        "A11": (7.95, 118.3)
    }


# ==================================================
# calculate_csp_results
# ==================================================

def test_calculate_csp_results_single_peak():
    exp1 = {
        "A10": (7.22, 112.64)
    }

    exp2 = {
        "A10": (7.556, 117.593)
    }

    df, fig = cc.calculate_csp_results(1, exp1, exp2)

    # structure checks
    assert len(df) == 1
    assert df.iloc[0]["Peak"] == "A10"

    # scientific check
    assert df.iloc[0]["CSP"] == pytest.approx(0.523, abs=0.001)
