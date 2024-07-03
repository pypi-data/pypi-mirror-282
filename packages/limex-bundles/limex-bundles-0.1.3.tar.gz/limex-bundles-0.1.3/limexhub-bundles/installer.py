import logging
import sys
import os
import shutil

def copy(filelist, dest, src, force):
    for f in filelist:
        dstf = os.path.join(dest, f)
        if not force and os.path.exists(dstf):
            logging.error("'{}' already exists.".format(dstf))
            sys.exit(1)
        else:
            srcf = os.path.join(src, f)
            logging.info("copying '{}' to '{}'".format(srcf, dest))
            try:
                shutil.copyfile(srcf, dstf)
            except Exception as exp:
                logging.error("error while copying '{}' to '{}': {}".format(srcf, dest, exp))
                sys.exit(1)

def install_bundle(api_key, force=True):
    ### configure logging
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

    # check if zipline is installed
    try:
        import zipline.data.bundles as bld
    except ImportError:
        logging.error('cannot found zipline. Run the installer in an environment where zipline is installed.')
        sys.exit(1)

    ### source files and directory
    src_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'zipline-bundles')
    src_ext = ['extension.py']
    src_ing = ['ingester.py', 'limex.py']

    ### destination directories
    dst_ext = os.path.join(os.path.expanduser('~'), '.zipline')
    # check the existence of zipline home
    if not os.path.isdir(dst_ext):
        logging.error(f"zipline home ('{dst_ext}') does not exist.")
        sys.exit(1)

    dst_ing = bld.__path__[0]

    # Update configuration with API key
    with open(os.path.join(src_dir, 'limex.py'), 'a') as f:
        f.write(f"\nLIMEX_API_KEY = '{api_key}'\n")

    copy(src_ext, dst_ext, src_dir, force)
    copy(src_ing, dst_ing, src_dir, force)