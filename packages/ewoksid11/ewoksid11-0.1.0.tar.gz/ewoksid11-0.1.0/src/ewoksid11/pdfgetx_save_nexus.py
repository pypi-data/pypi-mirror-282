import h5py
import os.path
import json

from silx.io.dictdump import dicttonx
from ewoksxrpd.tasks.data_access import TaskWithDataAccess

from .constants import SIGNAL_TYPES


try:
    from diffpy import pdfgetx

    VERSION = pdfgetx.__version__
except ImportError:
    VERSION = None


class PdfGetXSaveNexus(
    TaskWithDataAccess,
    input_names=[
        "output_filename",
        "scan",
        "detector_name",
        "result",
        "pdfgetx_options",
    ],
    optional_input_names=["subscan"],
    output_names=["output_url"],
):
    """Saves the PDF result (iq, sq, fq, gr) in a NeXus file

    Inputs:
        - output_filename: h5file name where the data must be saved
        - scan: scan number
        - detector name: name of the detector
        - result: PDFGetter object with attributes defined by outputtype. Attributes are tuples with [0] X (radial) and [1] Y (intensity)
    Outputs:
        - output_url: URL of the NXprocess containing the saved data
    """

    def run(self):
        scan = self.inputs.scan
        subscan = self.get_input_value("subscan", 1)
        detector_name = self.inputs.detector_name
        output_filename = self.inputs.output_filename
        output_url = f"silx://{output_filename}?path=/{scan}.{subscan}"
        result = self.inputs.result
        info = pdfgetx_config_as_nxdict(self.inputs.pdfgetx_options)

        with self.open_h5item(output_url, mode="a", create=True) as data_parent:
            assert isinstance(data_parent, h5py.Group)
            nxprocess = data_parent.create_group(f"{detector_name}_PDF")
            nxprocess.attrs["NX_class"] = "NXprocess"

            dicttonx(
                info, data_parent.file, h5path=f"{nxprocess.name}", update_mode="modify"
            )
            for signal_type, signal_quantities in SIGNAL_TYPES.items():
                nxdata = nxprocess.create_group(signal_type)
                nxdata.attrs["NX_class"] = "NXdata"

                axis, signal = getattr(result, signal_type)
                signal_dset = nxdata.create_dataset(signal_type, data=signal)
                nxdata.attrs["signal"] = signal_type

                signal_dset.attrs["long_name"] = signal_quantities["y"].name
                signal_dset.attrs["units"] = signal_quantities["y"].unit

                axis_name, axis_unit = signal_quantities["x"]
                axis_dset = nxdata.create_dataset(axis_name, data=axis)
                axis_dset.attrs["unit"] = axis_unit

                nxdata.attrs["axes"] = axis_name

                nxprocess.attrs["default"] = signal_type

            nxprocess.parent.attrs["default"] = os.path.basename(nxprocess.name)
            self.outputs.output_url = f"silx://{output_filename}?path={nxprocess.name}"


def pdfgetx_config_as_nxdict(pdfgetx_config: dict) -> dict:
    """Convert pdfgetx config to a Nexus dictionary. Add keys and units when appropriate."""
    nxtree_dict = {
        "@NX_class": "NXprocess",
        "program": "pdfgetx",
        "version": VERSION,
    }
    nxtree_dict["configuration"] = {
        "@NX_class": "NXnote",
        "type": "application/json",
        "data": json.dumps(pdfgetx_config),
    }
    return nxtree_dict
