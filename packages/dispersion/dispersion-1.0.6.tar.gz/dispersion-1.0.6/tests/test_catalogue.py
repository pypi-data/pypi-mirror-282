import pytest
import numpy as np
import shutil
import os
from copy import copy
from dispersion import Catalogue
from dispersion import Spectrum
from dispersion.config import default_config
from dispersion.scripts.setup_dispersion import (install_userdata, install_rii)


@pytest.fixture(scope="session")
def spectrum():
    spectrum = Spectrum(0.5, unit='um')
    yield spectrum

@pytest.fixture(scope="session")
def config():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.join(this_dir,"test_data")
    config = default_config()
    config['Path'] = root_path
    yield config

@pytest.fixture(scope="session")
def catalogue(config):
    user_dir = os.path.join(config['Path'], 'UserData')
    if not os.path.isdir(user_dir):
        os.mkdir(user_dir)
    install_userdata(user_dir)
    rii_dir = os.path.join(config['Path'], 'RefractiveIndexInfo')
    if not os.path.isdir(rii_dir):
        os.mkdir(rii_dir)
    install_rii(rii_dir, ask_confirm=False)
    cat = Catalogue(config=config, rebuild= 'All')
    df = cat.get_database()
    row = df.loc[df.Name=="example_file"]
    cat.register_alias(row, 'TestMat')
    cat.save_to_file()
    yield cat
    for item in os.listdir(config['Path']):
        full_path = os.path.join(config['Path'], item)
        if os.path.isdir(full_path):
            shutil.rmtree(full_path)
        else:
            os.remove(full_path)

def test_mdb_init(config, catalogue):
    mdb = Catalogue(config=config)

def test_get_mat(config, catalogue, spectrum):
    mat = catalogue.get_material("TestMat")
    nk = mat.get_nk_data(spectrum)
    assert np.isclose(np.real(nk), 1.6)
    assert np.isclose(np.imag(nk), 0.05)

def test_edit_cat(catalogue):
    df = catalogue.get_database()
    for row in range(df.shape[0]):
        if df.iloc[row,:].Alias == 'TestMat':
            continue
        catalogue.register_alias(row, "{:06d}".format(row))
    catalogue.save_to_file()

if __name__ == "__main__":
    pass
