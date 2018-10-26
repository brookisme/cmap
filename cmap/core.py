from __future__ import print_function
import os
import re
from glob import glob
from pprint import pprint
import click
import rasterio
import cmap.config as cfig
import cmap.utils as utils
import cmap.constants as c


def add(src,cmap=None,band=None,folder=None,ident=None,dst=None):
    # initialize params
    if cmap is None:
        cmap=cfig.get('default')
    if band is None:
        band=cfig.get('band')
    if folder is None:
        folder=cfig.get('folder')
    if ident is None:
        ident=cfig.get('ident')
    # get destination
    if not dst:
        if ident:
            dst=re.sub('.tif','.{}.tif'.format(ident),src)
        else:
            dst=src
    if folder:
        dst="{}/{}".format(folder,dst)
    os.makedirs(os.path.dirname(dst),exist_ok=True)
    # add colormap
    if cmap:
        colormap=cfig.get(cmap)
        utils.log('read {}, cmap {}'.format(src,cmap))
        with rasterio.open(src) as src:
                meta = src.meta
                if band is not None:
                    im=np.expand_dims(src.read(band),axis=0)
                    meta['count']=1
                else:
                    im=src.read()
                utils.log("output_file - {}".format(dst))
                utils.log("output_shape - {}".format(im.shape))
                utils.log("output_meta:")
                print()
                pprint(meta)
                print()
        with rasterio.open(dst, 'w', **meta) as dst:
                dst.write(im)
                dst.write_colormap(1, colormap)
    else:
        raise ValueError(c.CMAP_REQUIRED)



def add_dir(
        dir_path,
        ext=None,
        cmap=None,
        band=None,
        folder=None,
        ident=None,
        dst=None):
    if ext is None:
        ext=cfig.get('ext')
    selector='{}/*.{}'.format(dir_path,ext)
    srcs=glob(selector)
    utils.log("add_dir: {}".format(selector))
    for src in srcs:
        print(c.DIVIDER)
        utils.log("src: {}".format(src))
        add(src,cmap=cmap,band=band,folder=folder,ident=ident,dst=dst)


