from logic import calc_CSP, determine_nuclei_types


def test_determine_nuclei_types_nh_hsqc():
    result = determine_nuclei_types(1)

    assert result == ("1H", "15N", 1, 0.2)


def test_determine_nuclei_types_methyl():
    result = determine_nuclei_types(2)

    assert result == ("1H", "13C", 1, 5)


def test_calc_csp_zero_shift():
    result = calc_CSP(
        nuc1_f1=8.0,
        nuc1_f2=8.0,
        nuc2_f1=120.0,
        nuc2_f2=120.0,
        a=1,
        b=0.2
    )

    assert result == 0


def test_calc_csp_basic_case():
    result = calc_CSP(
        nuc1_f1=8.5,
        nuc1_f2=8.0,
        nuc2_f1=121.0,
        nuc2_f2=120.0,
        a=1,
        b=0.2
    )

    expected = (((0.5 ** 2) + (0.2 ** 2)) ** 0.5) / 2

    assert result == expected


def test_calc_csp_negative_difference():
    result = calc_CSP(
        nuc1_f1=8.0,
        nuc1_f2=8.5,
        nuc2_f1=120.0,
        nuc2_f2=121.0,
        a=1,
        b=0.2
    )

    expected = (((-0.5 ** 2) + (-0.2 ** 2)) ** 0.5) / 2

    assert abs(result - expected) < 1e-9