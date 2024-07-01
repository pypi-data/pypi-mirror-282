import os
from datetime import datetime
from pyFAI.io import ponifile
from pyFAI.units import hc

from ewokscore import Task


class CalibSave(
    Task,
    input_names=[
        "geometry",
        "calibrant",
        "detector",
        "detector_config",
        "output_path",
        "energy",
    ],
    output_names=[
        "output_path",
    ],
):
    """Saves the geometry from calibration result in output_path. By default, the geometry file will be: {calibrant}_YYYYMMDD_hhmm.poni

    Inputs:
        - geometry: dictionnary, result of CalibrateSingle
        - calibrant: string with calibrant name used in CalibrateSingle
        - detector: string, default is detector
        - detector_config: dict with key splineFile
        - output_path: list of strings, where the poni will be saved
        - energy: float, in keV

    Outputs:
        - output_path: list of strings, path of the poni files saved
    """

    def run(self):
        now = datetime.now()
        dt_string = now.strftime("%Y%m%d_%H%M")
        poni_paths = []
        poni_pars = {
            "poni_version": 2,
            "detector": self.inputs.detector,
            "detector_config": self.inputs.detector_config,
            **self.inputs.geometry,
            "wavelength": (1e-10 * hc) / self.inputs.energy,
        }
        poni_obj = ponifile.PoniFile(poni_pars)
        for path in self.inputs.output_path:
            if not os.path.exists(path):
                os.makedirs(path)
            poni_path = os.path.join(path, f"{self.inputs.calibrant}_{dt_string}.poni")
            with open(poni_path, "w") as poniFile:
                poni_obj.write(poniFile)
            poni_paths.append(poni_path)
        self.outputs.output_path = poni_paths
