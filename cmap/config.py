import os.path
import yaml
import cmap.utils as utils
import cmap.constants as c


#
# DEFAULT CONFIG
#
_DEFAULTS={
    'folder': c.FOLDER,
    'ident': c.IDENT,
    'band': c.BAND,
    'ext': c.EXT
}


#
# LOAD CONFIG
#
try:
    _CONFIG=yaml.safe_load(open(c.CONFIG_PATH))
except:
    _CONFIG=False


def get(key):
    """ get value
    """
    if _CONFIG is False:
        raise ValueError('CMAP: config file required (use generate)')
    return _CONFIG.get(key,_DEFAULTS.get(key))



def generate(
        folder=c.FOLDER,
        ident=c.IDENT,
        band=c.BAND,
        ext=c.EXT,
        force=False):
    """ generate config file
    """
    config={
        'folder': c.FOLDER,
        'ident': c.IDENT,
        'band': c.BAND,
        'ext': c.EXT }
    if not force and os.path.exists(c.CONFIG_PATH):
        utils.log(c.CONFIG_EXISTS,level="ERROR")
    else:
        with open(c.CONFIG_PATH,'w+') as file:
            file.write("# {}\n".format(c.CONFIG_COMMENT))
            file.write(yaml.safe_dump(config, default_flow_style=False))
        utils.log(c.CONFIG_CREATED)


