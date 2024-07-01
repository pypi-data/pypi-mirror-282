import os

from ..pyfai_calib_save import CalibSave


def test_pyfai_calib_save(tmpdir):
    datadir = os.path.abspath(os.path.dirname(__file__))
    spline_path = os.path.join(datadir, "data", "frelon.spline")
    detector_config = {
        "pixel1": 47e-6,
        "pixel2": 47e-6,
        "splineFile": spline_path,
        "max_shape": (2048, 2048),
    }
    geometry = {
        "dist": 0.2,
        "poni1": 0.046,
        "poni2": 0.05,
        "rot1": 0,
        "rot2": 0,
        "rot3": 0,
    }
    save_inputs = {
        "geometry": geometry,
        "calibrant": "CeO2",
        "detector": "Detector",
        "detector_config": detector_config,
        "output_path": [tmpdir],
        "energy": 43.5689,
    }
    save = CalibSave(inputs=save_inputs)
    save.execute()
    output_poni_paths = save.get_output_value("output_path")
    for output_poni_path in output_poni_paths:
        assert os.path.exists(output_poni_path)
