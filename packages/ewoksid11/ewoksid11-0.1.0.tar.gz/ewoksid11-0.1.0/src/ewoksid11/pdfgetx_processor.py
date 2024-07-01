from ewokscore import Task

try:
    from diffpy import pdfgetx
except ImportError:
    pdfgetx = None


class PdfGetXProcessor(
    Task,
    input_names=[
        "radial",
        "intensity",
        "info",
        "pdfgetx_options",
    ],
    output_names=[
        "result",
        "pdfgetx_options",
    ],
):
    """Extracts the PDF signal from provided intensities and radial

    Inputs:
        - radial: 1D array
        - intensity: 1D array
        - info: dict with unit and wavelength
        - pdfgetx_options: PDFConfig object
    Outputs:
        - result: PDFGetter object with attributes defined by outputtype. Attributes are tuples with [0] X (radial) and [1] Y (intensity)
        - pdfgetx_options: PDFConfig object
    """

    def run(self):
        cfg = self.inputs.pdfgetx_options
        if pdfgetx is None:
            raise ImportError("diffpy couldn't be imported")
        worker = pdfgetx.PDFGetter(cfg)
        worker(self.inputs.radial, self.inputs.intensity)
        self.outputs.result = worker
        self.outputs.pdfgetx_options = cfg
