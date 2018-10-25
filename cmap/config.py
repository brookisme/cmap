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
    'band': c.BAND
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
        cmap_keys=[],
        force=False):
    """ generate config file
    """
    config={
        'folder':folder,
        'ident':ident }
    for cmap_key in cmap_keys:
        config[cmap_key]={ 0: (0,0,0) }
    if not force and os.path.exists(c.CONFIG_PATH):
        utils.print(c.CONFIG_EXISTS,level="ERROR")
    else:
        with open(c.CONFIG_PATH,'w+') as file:
            file.write("# {}\n".format(c.CONFIG_COMMENT))
            file.write(yaml.safe_dump(config, default_flow_style=False))
        utils.print(c.CONFIG_CREATED)


