import gzip
import shutil

with open('JHUdata.csv','rb') as f_input:
    with gzip.open('JHUdata.csv.gz','wb') as f_output:
        shutil.copyfileobj(f_input,f_output)