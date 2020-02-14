# -*- coding: utf-8 -*-
# flake8: noqa
import os
import pytest
from cordex import ESGF

__author__ = "Lars Buntemeyer"
__copyright__ = "Lars Buntemeyer"
__license__ = "mit"

root = '/pool/data/cordex'
cordex_path = 'output/EUR-11/GERICS/MPI-M-MPI-ESM-LR/' \
        'historical/r3i1p1/GERICS-REMO2015/v1/day/tas/v20190925'
cordex_filename = 'tas_EUR-11_MPI-M-MPI-ESM-LR_historical_r3i1p1_GERICS-REMO2015_v1_day_19500102-19501231.nc'


def test_convs():
    for conv_name in ['CMIP5', 'CORDEX']:
        assert conv_name in (ESGF.conventions())


def test_cordex():
    cordex = ESGF.get_convention('CORDEX')
    filename = os.path.join(cordex_path, cordex_filename)
    # get attributes from filename 
    attrs = cordex.parse(filename)
    print(attrs)
    # test if filename is reconstructed correctly
    assert cordex.pattern(**attrs) == filename



if __name__ == '__main__':
    test_convs()
    test_cordex()
