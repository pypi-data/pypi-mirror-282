import pytest
import numpy as np
import os
from dispersion import Material
from dispersion import Spectrum

@pytest.fixture
def spectrum():
    spectrum = Spectrum(0.5, unit='um')
    yield spectrum

@pytest.fixture
def root_path():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.join(this_dir,"..","data")
    yield root_path

def test_mat_init(spectrum):
    md = Material(fixed_n=1.0)
    n = md.get_nk_data(spectrum)
    assert np.isclose(np.real(n), 1.0)
    assert np.isclose(np.imag(n), 0.0)

def test_from_yml_file(spectrum, root_path):
    relpath = os.path.join('RefractiveIndexInfo',
                           'data', 'main', 'Ag',
                           'Hagemann.yml')
    filepath = os.path.join(root_path,relpath)
    md = Material(file_path=filepath,
                  spectrum_type='wavelength',
                  unit='micrometer')
    n = md.get_nk_data(spectrum)
    assert np.isclose(np.real(n), 0.23805806451612901)
    assert np.isclose(np.imag(n), 3.126040322580645)

def test_from_txt_file(spectrum, root_path):
    relpath = os.path.join('UserData','AlSb.txt')
    filepath = os.path.join(root_path,relpath)
    md = Material(file_path=filepath,
                  spectrum_type='wavelength',
                  unit='micrometer')
    n = md.get_nk_data(spectrum)
    assert np.isclose(np.real(n), 4.574074754901961)
    assert np.isclose(np.imag(n), 0.4318627450980393)

def test_from_nk_file(spectrum, root_path):
    relpath = os.path.join('Palik','Ag.nk')
    filepath = os.path.join(root_path,relpath)
    md = Material(file_path=filepath,
                  spectrum_type='wavelength',
                  unit='angstrom')
    n = md.get_nk_data(spectrum)
    assert np.isclose(np.real(n), 0.13)
    assert np.isclose(np.imag(n), 2.917632850241546)


def test_from_model(spectrum):
    wp = 8.55 # eV
    loss = 18.4e-3 #eV
    model_kw = {'name':'Drude','parameters':[wp, loss],
                'valid_range':[0.0, np.inf],
                'spectrum_type':'energy', 'unit':'ev'}
    md = Material(model_kw=model_kw)
    n = md.get_nk_data(spectrum)

    assert np.isclose(np.real(n), 0.013366748652710245)
    assert np.isclose(np.imag(n), 3.2997524521729824)

if __name__ == "__main__":
    pass
