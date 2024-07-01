import numpy as np
import json
from ewokscore import Task
from silx.io.url import DataUrl
from silx.io import h5py_utils


class PdfGetXAverage(
    Task,
    input_names=[
        "nxdata_url",
    ],
    output_names=[
        "radial",
        "intensity",
        "info",
    ],
):
    """Average a list of 1D XRPD patterns from provided output of IntegrateBlissScan

    Inputs:
        - nxdata_url: .h5 path with NXData url
    Outputs:
        - radial: 1D array
        - intensity: 1D array
        - info: dict with radial_units and wavelength
    """

    def run(self):
        nxdata_url = DataUrl(self.inputs.nxdata_url)
        with h5py_utils.open_item(
            nxdata_url.file_path(), nxdata_url.data_path()
        ) as NXIn:
            intensity = NXIn[NXIn.attrs["signal"]][:]
            radial = NXIn[NXIn.attrs["axes"][1]][:]
            info = json.loads(NXIn.parent["configuration/data"][()])
        if intensity.ndim == 1:
            pass
        elif intensity.ndim == 2:
            intensity = np.average(intensity, axis=0)
        else:
            raise ValueError("intensity dimension %s not supported" % intensity.ndim)
        self.outputs.intensity = intensity
        self.outputs.radial = radial
        self.outputs.info = info
