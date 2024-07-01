import os
import numpy as np

from ewoksid11.constants import SIGNAL_TYPES
from ewoksid11.pdfgetx_save_ascii import PdfGetXSaveAscii


def assert_data_close(outputs, data_key, true_data, atol_multiplier=1e-5):
    atol = true_data[:, 1].max() * atol_multiplier
    computed_data = getattr(outputs, data_key)
    np.testing.assert_allclose(computed_data[0], true_data[:, 0], rtol=1e-6)
    np.testing.assert_allclose(computed_data[1], true_data[:, 1], atol=atol)


def test_assert_save_ascii(setup_save_data, tmpdir):
    save_result_input = setup_save_data
    dsetname = "CeO2.h5"
    save_inputs = {
        "filename": os.path.join(tmpdir, dsetname),
        "result": save_result_input,
    }
    save = PdfGetXSaveAscii(inputs=save_inputs)
    save.execute()

    for signal_type in SIGNAL_TYPES:
        with open(save_inputs["filename"].replace("h5", signal_type), "r") as f_in:
            cfg_lines = f_in.readlines()[10:27]  # Skip header to calculation setup
        for i, line in enumerate(cfg_lines):
            cfg_parts = line.split("=")
            if len(cfg_parts) == 2:
                key = cfg_parts[0].strip()
                value = cfg_parts[1].strip()
                expected_value = getattr(save_result_input.config, key)
                if isinstance(expected_value, str) or isinstance(expected_value, float):
                    assert value == str(expected_value)
                if isinstance(expected_value, list):
                    assert value == str(expected_value[0])
        data = np.genfromtxt(
            save_inputs["filename"].replace("h5", signal_type), skip_header=27
        )
        assert_data_close(save_result_input, signal_type, data)
