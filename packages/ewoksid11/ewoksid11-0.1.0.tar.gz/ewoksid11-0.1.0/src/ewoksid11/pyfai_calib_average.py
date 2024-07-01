import numpy as np
import hdf5plugin  # noqa F401
from ewokscore import Task
from silx.io.url import DataUrl
from silx.io import h5py_utils


class CalibAverage(
    Task,
    input_names=[
        "bliss_data_url",
    ],
    output_names=[
        "image",
    ],
):
    """Average a list of 2D images from bliss data url

    Inputs:
        - bliss_data_url: format like /data/visitor/maXXXX/idXX/20240101/sample/dataset/dataset.h5::1.1/measurement/detector
    Outputs:
        - image: 2D image averaged from list of 2D images
    """

    def run(self):
        bliss_data_url = DataUrl(self.inputs.bliss_data_url)
        with h5py_utils.open_item(
            bliss_data_url.file_path(), bliss_data_url.data_path()
        ) as NXIn:
            image = np.average(NXIn[:], axis=0)
        self.outputs.image = image
