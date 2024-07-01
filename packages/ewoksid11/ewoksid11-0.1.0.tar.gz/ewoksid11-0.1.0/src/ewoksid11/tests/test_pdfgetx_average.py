import os

from ..pdfgetx_average import PdfGetXAverage


def test_pdfgetx_average():
    datadir = os.path.abspath(os.path.dirname(__file__))
    data_path = os.path.join(
        datadir,
        "data",
        "pdfexample",
        "CeO2_processed.h5::1.1/frelon6_integrate/integrated",
    )

    average_inputs2D = {"nxdata_url": data_path}

    get_average2D = PdfGetXAverage(inputs=average_inputs2D)
    get_average2D.execute()
    average2D = get_average2D.get_output_values()

    assert average2D["intensity"].ndim == 1
