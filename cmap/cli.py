from __future__ import print_function
import click
import cmap.core as core
import cmap.constants as c
import cmap.config as cfig




#
# PUBLIC
#
@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj={}




""" ADD """
@click.command(help='create geotiff with color-table for a single file')
@click.argument('src')
@click.argument('cmap',default=None,required=False)
@click.option(
    '--band',
    default=None,
    help='band index: if None use all bands',
    type=int)
@click.option(
    '--folder',
    default=None,
    help='destination directory: if None use current directory')
@click.option(
    '--ident',
    default=None,
    help='clr ident: filename.tif => filename.<ident>.tif')
@click.option(
    '--dst',
    default=None,
    help='destination path: empty create name from src path')
@click.pass_context
def add(ctx,src,cmap=None,band=None,folder=None,ident=None,dst=None):
    core.add(src,cmap=cmap,band=band,folder=folder,ident=ident,dst=dst)




""" ADD DIR """
@click.command(help='create geotiffs with color-table for all geotiffs in a directory')
@click.argument('dir_path')
@click.argument('cmap',default=None,required=False)
@click.option(
    '--ext',
    default=None,
    help='extension: defaluts to tif: use  "*.<ext>" to find files')
@click.option(
    '--band',
    default=None,
    help='band index: if None use all bands',
    type=int)
@click.option(
    '--folder',
    default=None,
    help='destination directory: if None use current directory')
@click.option(
    '--ident',
    default=None,
    help='clr ident: filename.tif => filename.<ident>.tif')
@click.option(
    '--dst',
    default=None,
    help='destination path: empty create name from src path')
@click.pass_context
def add_dir(
        ctx,
        dir_path,
        cmap=None,
        ext=None,
        band=None,
        folder=None,
        ident=None,
        dst=None):
    core.add_dir(dir_path,cmap=cmap,band=band,folder=folder,ident=ident,dst=dst)




""" GENERATE CONFIG """
@click.command(name='config',help='generate local or global config file')
@click.option(
    '--force',
    default=False,
    help='if true overwrite existing config',
    type=bool)
@click.option(
    '--global_config',
    help='if true create global config otherwise local. defaults to False',
    default=False,
    type=bool)
@click.option(
    '--ext',
    help='default ext: config default is "{}"'.format(c.EXT),
    default=c.EXT)
@click.option(
    '--band',
    default=c.BAND,
    help='default band: config default is {}'.format(c.BAND),
    type=int)
@click.option(
    '--ident',
    help='default ident: config default is "{}"'.format(c.IDENT),
    default=c.IDENT)
@click.option(
    '--folder',
    help='default folder: config default is "{}"'.format(c.FOLDER),
    default=c.FOLDER)
def generate_config(
        folder=None,
        ident=None,
        band=None,
        ext=None,
        global_config=False,
        force=False):
    cfig.generate(
        folder=folder,
        ident=ident,
        band=band,
        ext=ext,
        global_config=global_config,
        force=force)



#
# MAIN
#
cli.add_command(add)
cli.add_command(add_dir)
cli.add_command(generate_config)

if __name__ == '__main__':
    cli()


