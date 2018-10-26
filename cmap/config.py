import os.path
from os.path import expanduser
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
_GLOBAL_CONFIG_PATH="{}/{}/{}".format(
        expanduser("~"),
        c.GLOBAL_CONFIG_DIR,
        c.CONFIG_PATH )

#
# LOAD CONFIG
#
try:
    _CONFIG=yaml.safe_load(open(c.CONFIG_PATH))
except:
    try:
        _CONFIG=yaml.safe_load(open(_GLOBAL_CONFIG_PATH))
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
        global_config=False,
        force=False):
    """ generate config file
    """
    config={
        'folder': c.FOLDER,
        'ident': c.IDENT,
        'band': c.BAND,
        'ext': c.EXT }
    if global_config:
        path=_GLOBAL_CONFIG_PATH
    else:
        path=c.CONFIG_PATH
    if not force and os.path.exists(path):
        utils.log(c.CONFIG_EXISTS,level="ERROR")
    else:
        os.makedirs(os.path.dirname(path),exist_ok=True)
        with open(path,'w+') as file:
            file.write("#\n")
            file.write("# {}\n".format(c.CONFIG_OPTIONS_COMMENT))
            file.write("#\n")
            file.write(yaml.safe_dump(config, default_flow_style=False))
            file.write("\n\n\n\n#\n")
            file.write("# {}\n".format(c.CONFIG_CMAPS_COMMENT))
            file.write("#\n\n\n\n")
        utils.log(c.CONFIG_CREATED)


