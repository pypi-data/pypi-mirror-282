import os
import pytest
import numpy as np

from ..pdfgetx_config import PdfGetXConfig
from ..pdfgetx_processor import PdfGetXProcessor


@pytest.fixture()
def setup_data(requires_diffpy):
    # Define file paths
    datadir = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "data", "pdfexample"
    )
    config_file = os.path.join(datadir, "config.cfg")
    data_file = os.path.join(datadir, "CeO2.dat")

    # Configuration inputs
    config_inputs = {"filename": config_file}

    # Load data
    data = np.genfromtxt(data_file, delimiter="")

    # Create PdfGetXConfig instance and execute
    get_config = PdfGetXConfig(inputs=config_inputs)
    get_config.execute()
    config = get_config.get_output_values()

    # Extract data columns
    radial = data[:, 0]
    intensity = data[:, 1]

    # Processor inputs
    processor_inputs = {
        "radial": radial,
        "intensity": intensity,
        "info": {"unit": "q_A^-1"},
        "pdfgetx_options": config["pdfgetx_options"],
    }

    # Create PdfGetXProcessor instance and execute
    pdf_processor = PdfGetXProcessor(inputs=processor_inputs)
    pdf_processor.execute()
    outputs = pdf_processor.get_output_values()

    # Load true data
    true_iq = np.genfromtxt(
        os.path.join(datadir, "CeO2.iq"), delimiter="", skip_header=27
    )
    true_sq = np.genfromtxt(
        os.path.join(datadir, "CeO2.sq"), delimiter="", skip_header=27
    )
    true_fq = np.genfromtxt(
        os.path.join(datadir, "CeO2.fq"), delimiter="", skip_header=27
    )
    true_gr = np.genfromtxt(
        os.path.join(datadir, "CeO2.gr"), delimiter="", skip_header=27
    )

    return outputs, true_iq, true_sq, true_fq, true_gr


def test_data(setup_data):
    outputs, true_iq, true_sq, true_fq, true_gr = setup_data

    # Define a function for testing data
    def assert_data_close(data_key, true_data, atol_multiplier=1e-5):
        atol = true_data[:, 1].max() * atol_multiplier
        computed_data = getattr(outputs["result"], data_key)
        np.testing.assert_allclose(computed_data[0], true_data[:, 0], rtol=1e-6)
        np.testing.assert_allclose(computed_data[1], true_data[:, 1], atol=atol)

    # Testing iq, sq, fq, and gr
    assert_data_close("iq", true_iq)
    assert_data_close("sq", true_sq)
    assert_data_close("fq", true_fq)
    assert_data_close("gr", true_gr)
