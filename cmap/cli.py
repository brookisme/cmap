from __future__ import print_function
import re
import click
import rasterio
import numpy as np





#
# PUBLIC
#
@click.group()
@click.pass_context
def cli(ctx,noisy):
    ctx.obj={}



@click.command(help='add colormap to geotiff')
@click.argument('src')
@click.argument('cmap',default=None,required=False)
@click.option('--dst',default=None,help='destination')
@click.option('--band',default=None,help='band index',type=int)
@click.option('--folder',default=None,help='directory')
def add(ctx,src,cmap=None,band=None,folder=None,ident=None,dst=None):
    core.add(src,cmap=cmap,band=band,folder=folder,ident=ident,dst=dst)




@click.command(help='add colormap to geotiff')
@click.argument('dir_path')
@click.argument('cmap',default=None,required=False)
@click.option('--dst',default=None,help='destination')
@click.option('--band',default=None,help='band index',type=int)
@click.option('--folder',default=None,help='directory')
def add(ctx,dir_path,cmap=None,band=None,folder=None,ident=None,dst=None):
    core.add_dir(dir_path,cmap=cmap,band=band,folder=folder,ident=ident,dst=dst)



