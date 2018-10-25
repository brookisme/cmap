from __future__ import print_function
import re
import click
import rasterio
import numpy as np
import cmap.config as cfig
import cmap.utils as utils
from glob import glob



def add(src,cmap=None,band=None,folder=None,ident=None,dst=None):
    # initialize params
    if cmap is None:
        cmap=cfig.get('defalut')
        colormap=cfig.get(cmap)
    if band is None:
        band=cfig.get('band')
    if folder is None:
        folder=cfig.get('folder')
    if ident is None:
        ident=cfig.get('ident')
    if not dst:
        dst=re.sub('.tif','.{}.tif'.format(CLR_IDENT),src)
    # add colormap
    utils.print('read {}, cmap {}'.format(src,cmap))
    with rasterio.open(src) as src:
            meta = src.meta
            if band is not None:
                im=np.expand_dims(src.read(band),axis=0)
                meta['count']=1
            else:
                im=src.read()
            print()
            utils.print("\toutput_file:",dst)
            utils.print("\toutput_shape:",im.shape)
            utils.print("\toutput_meta:",meta)
            print()
    with rasterio.open(dst, 'w', **meta) as dst:
            dst.write(im)
            dst.write_colormap(1, colormap)



def add_dir(dir_path,cmap=None,band=None,folder=None,ident=None,dst=None):
    print("TODO: add all files in a directory")
    pass
