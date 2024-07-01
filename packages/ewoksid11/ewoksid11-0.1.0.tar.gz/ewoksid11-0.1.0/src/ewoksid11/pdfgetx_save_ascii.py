import numpy as np
from ewokscore import Task

from .constants import CONFIG_ASCII_HEADER, DATA_ASCII_HEADER, SIGNAL_TYPES


class PdfGetXSaveAscii(
    Task,
    input_names=[
        "filename",
        "result",
    ],
    output_names=["saved", "filenames"],
):
    """Saves the PDF result (iq, sq, fq, gr) in separate ASCII files

    Inputs:
        - filename: h5file name that would have been used to save data from XrpdProcessor
        - result: PDFGetter object with attributes defined by outputtype. Attributes are tuples with [0] X (radial) and [1] Y (intensity)
    Outputs:
        - saved: True if saved
        - filename: list of saved filenames
    """

    def run(self):
        filename = self.inputs.filename
        self.outputs.filenames = []
        result = self.inputs.result
        for signal_type, signal_quantities in SIGNAL_TYPES.items():
            if not hasattr(result, signal_type):
                continue
            signal = getattr(result, signal_type)
            data = np.stack([signal[0], signal[1]], axis=1)
            config_header = self.header_config_writer(signal_type)
            data_header = DATA_ASCII_HEADER.format(
                f"{signal_quantities['x'].name} ({signal_quantities['x'].unit})",
                f"{signal_quantities['y'].name} ({signal_quantities['y'].unit})",
            )
            header = config_header + data_header
            np.savetxt(
                filename.replace("h5", signal_type),
                data,
                fmt="%10.7f",
                header=header,
                comments="",
            )
            self.outputs.filenames.append(filename.replace("h5", signal_type))
        self.outputs.saved = True

    def header_config_writer(self, signal_type: str):
        result = self.inputs.result
        config = result.config
        config.outputtypes = signal_type
        lines = CONFIG_ASCII_HEADER.split("\n")
        for i, line in enumerate(lines):
            parts = line.split("=")
            if len(parts) != 2:
                continue
            key = parts[0].strip()
            if hasattr(config, key):
                attr = getattr(config, key)
                lines[i] = (
                    f"{key} = {attr}".replace("[", "")
                    .replace("'", "")
                    .replace("]", "")
                    .replace("./", "")
                )
        updated_config_header = "\n".join(lines)
        return updated_config_header
