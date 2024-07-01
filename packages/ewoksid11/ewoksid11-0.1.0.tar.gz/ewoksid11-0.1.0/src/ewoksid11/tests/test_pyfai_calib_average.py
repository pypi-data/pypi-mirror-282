import os

from ..pyfai_calib_average import CalibAverage


def test_pyfai_calib_average():
    datadir = os.path.abspath(os.path.dirname(__file__))
    data_path = os.path.join(
        datadir, "data", "pdfexample", "CeO2.h5" + "::entry_0000/measurement/data"
    )

    average_inputs2D = {"bliss_data_url": data_path}

    get_average2D = CalibAverage(inputs=average_inputs2D)
    get_average2D.execute()
    average2D = get_average2D.get_output_values()

    assert average2D["image"].ndim == 2
