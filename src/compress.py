import gzip
import shutil


def compress (filename):
    """
    Takes in a filename and uses GZIP to compress it
    """
    gzipped = filename + ".gz"
    with open(filename, 'rb') as f_in:
        with gzip.open(gzipped, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
