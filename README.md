#### CMAP: a simple cli for adding color-tables to geotiffs

---

###### INSTALL

```bash
git clone https://github.com/brookisme/cmap.git
cd sublr
pip install -e .
```

###### USAGE

**NOTE**: Before using `cmap` you must [generate a config file](#config). 

1. [add](#add): create geotiff with color-table for a single file
2. [add_dir](#add_dir): create geotiffs with color-table for all geotiffs in a directory
3. [config](#config): generate cmap config file 

```
Usage: cmap [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add      add color-table to geotiff
  add_dir  add color-table to geotiffs in dir
  config   generate config file
```

---

<a name='add'></a>

##### ADD

```
Usage: cmap add [OPTIONS] [CMAP] SRC

  create tif with color map for a single file

Options:
  --dst TEXT      destination path: empty create name from src path
  --ident TEXT    clr ident: filename.tif => filename.<ident>.tif
  --folder TEXT   destination directory: if None use current directory
  --band INTEGER  band index: if None use all bands
  --help          Show this message and exit.
```


---

<a name='add_dir'></a>

##### ADD DIR

```
Usage: cmap add_dir [OPTIONS] [CMAP] DIR_PATH

  create geotiffs with color-table for all geotiffs in a directory

Options:
  --dst TEXT      destination path: empty create name from src path
  --ident TEXT    clr ident: filename.tif => filename.<ident>.tif
  --folder TEXT   destination directory: if None use current directory
  --band INTEGER  band index: if None use all bands
  --ext TEXT      extension: defaluts to tif: use  "*.<ext>" to find files
  --help          Show this message and exit.
```

---

<a name='config'></a>

##### CONFIG

NOTES:

* config file(s) must be generated before using other `cmap` methods
* the config file contains:
  - color-tables and default: added after generation (see [example](https://github.com/brookisme/cmap/blob/master/example.cmap.config.yaml)).
  - option defaults
* if a local config file is not present the `cmap` will use the global config.

```
Usage: cmap config [OPTIONS]

  generate local or global config file

Options:
  --force BOOLEAN          if true overwrite existing config
  --global_config BOOLEAN  if true create global config otherwise local.
                           defaults to False
  --ext TEXT               default ext: config default is "tif"
  --band INTEGER           default band: config default is None
  --ident TEXT             default ident: config default is "clr"
  --folder TEXT            default folder: config default is "clr"
  --help                   Show this message and exit.
```


