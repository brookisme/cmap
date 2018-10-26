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



@click.command(help='add colormap to geotiff')
@click.argument('src')
@click.argument('cmap',default=None,required=False)
@click.option('--dst',default=None,help='destination')
@click.option('--band',default=None,help='band index',type=int)
@click.option('--folder',default=None,help='directory')
@click.pass_context
def add(ctx,src,cmap=None,band=None,folder=None,ident=None,dst=None):
    core.add(src,cmap=cmap,band=band,folder=folder,ident=ident,dst=dst)




@click.command(help='add colormap to geotiffs in dir')
@click.argument('dir_path')
@click.argument('cmap',default=None,required=False)
@click.option('--ext',default=None,help='extension: defaluts to tif')
@click.option('--dst',default=None,help='destination')
@click.option('--band',default=None,help='band index',type=int)
@click.option('--folder',default=None,help='directory')
@click.pass_context
def add_dir(ctx,dir_path,ext=None,cmap=None,band=None,folder=None,ident=None,dst=None):
    core.add_dir(dir_path,cmap=cmap,band=band,folder=folder,ident=ident,dst=dst)




@click.command(name='config',help='generate config file')
@click.option('--folder',default=c.FOLDER)
@click.option('--ident',default=c.IDENT)
@click.option('--band',default=c.BAND)
@click.option('--ext',default=c.EXT)
@click.option(
    '--force',
    default=False,
    help='if true overwrite existing config',
    type=bool)
def generate_config(
        folder=None,
        ident=None,
        band=None,
        ext=None,
        force=False):
    cfig.generate(
        folder=folder,
        ident=ident,
        band=band,
        ext=ext,
        force=force)



#
# MAIN
#
cli.add_command(add)
cli.add_command(add_dir)
cli.add_command(generate_config)

if __name__ == '__main__':
    cli()


