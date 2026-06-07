from streamlit.testing.v1 import AppTest

import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(__file__))
)

def test_app_loads():
    app = AppTest.from_file(
        os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "app.py"
        )
    )

    app.run()

    print(app.button)
    print(app.error)

    assert not app.exception


def test_missing_files_shows_error():
    app = AppTest.from_file(
        os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "app.py"
        )
    ).run()

    # click the button
    app.button[0].click().run()

    # check error appears
    assert len(app.error) > 0
    assert "Please upload both files" in app.error[0].value


def test_full_pipeline_minimal():
    app = AppTest.from_file(
        os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "app.py"
        )
    ).run()

    # --- create fake input files ---
    file1 = (
        "Peak W1 W2\n"
        "A10 7.22 112.64\n"
        "A11 7.95 118.30\n"
    )

    file2 = (
        "Peak W1 W2\n"
        "A10 7.556 117.593\n"
        "A11 8.00 119.00\n"
    )

    # --- upload files ---
    app.file_uploader[0].set_value(
        ("file1.txt", file1.encode("utf-8"), "text/plain")
    )

    app.file_uploader[1].set_value(
        ("file2.txt", file2.encode("utf-8"), "text/plain")
    )

    # --- click process button ---
    app.button[0].click().run()

    # --- verify results exist ---
    assert len(app.dataframe) > 0
    
    # --- verify session state was populated ---
    assert "df" in app.session_state
    assert "fig" in app.session_state