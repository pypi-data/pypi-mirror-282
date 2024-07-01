import h5py
import numpy
import os
import json
from silx.io import utils as silx_io_utils


from ewoksid11.constants import SIGNAL_TYPES
from ewoksid11.constants import PDF_CONFIG_PARSED
from ewoksid11.pdfgetx_save_nexus import PdfGetXSaveNexus


def test_assert_save_nexus(setup_save_data, tmpdir):
    output_filename = os.path.join(tmpdir, "CeO2.h5")
    save_inputs = {
        "output_filename": output_filename,
        "scan": 2,
        "detector_name": "detector",
        "result": setup_save_data,
        "subscan": 2,
        "pdfgetx_options": dict(PDF_CONFIG_PARSED),
    }
    save = PdfGetXSaveNexus(inputs=save_inputs)
    save.execute()
    output_url = save.get_output_value("output_url")

    assert output_url == f"silx://{output_filename}?path=/2.2/detector_PDF"

    with silx_io_utils.open(output_url) as nxprocess:
        assert isinstance(nxprocess, h5py.Group)
        assert nxprocess.attrs["NX_class"] == "NXprocess"

        configuration = nxprocess["configuration"]
        assert configuration.attrs["NX_class"] == "NXnote"
        assert json.loads(configuration["data"][()]) == PDF_CONFIG_PARSED

        for signal_type in SIGNAL_TYPES:
            nxdata = nxprocess[signal_type]
            assert isinstance(nxdata, h5py.Group)
            assert nxdata.attrs["NX_class"] == "NXdata"

            expected_data = getattr(setup_save_data, signal_type)
            expected_axes = expected_data[0]
            axes_data = nxdata[nxdata.attrs["axes"]][()]
            numpy.testing.assert_allclose(expected_axes, axes_data)

            expected_signal = expected_data[1]
            signal_data = nxdata[nxdata.attrs["signal"]][()]
            numpy.testing.assert_allclose(expected_signal, signal_data)
