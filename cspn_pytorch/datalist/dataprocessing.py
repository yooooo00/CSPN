import os
from pathlib import Path
import requests

base_url='http://datasets.lids.mit.edu/nyudepthv2/nyudepthv2_noskip/val_full/'

old_file_path=Path(__file__).parent/'nyudepth_hdf5_train_test.csv'
new_file_path=Path(__file__).parent/'nyudepth_hdf5_train_new.csv'

count=0
total=len(open(old_file_path,'r').readlines())-1
with open(old_file_path,'r') as file,open(new_file_path,'w') as newfile:
    next(file)
    for line in file:
        count+=1
        link=base_url+line.strip().split('/')[-2]+'/'+line.strip().split('/')[-1]
        response=requests.get(link)
        if response.status_code!=200:
            print(f"{count}/{total}:{line.strip()},False        ",end='\r')
            continue
        else:
            newfile.write(line)
            print(f"{count}/{total}:{line.strip()},True        ",end='\r')

