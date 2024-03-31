import os
from pathlib import Path
import requests

base_url='http://datasets.lids.mit.edu/nyudepthv2/nyudepthv2_noskip/val_full/'

old_file_path=Path(__file__).parent/'nyudepth_hdf5_train_test.csv'
new_file_path=Path(__file__).parent/'nyudepth_hdf5_train_new.csv'

total=len(open(old_file_path,'r').readlines())-1
def check_if_dataset_file_exists_online(filepath):
    count=0
    with open(filepath,'r') as file:
        next(file)
        for line in file:
            link=base_url+line.strip().split('/')[-2]+'/'+line.strip().split('/')[-1]
            response=requests.head(link)
            if response.status_code!=200:
                print(f"{count}/{total}:{line.strip()},False        ",end='\r')
                continue
            else:
                count+=1
                print(f"{count}/{total}:{line.strip()},True        ",end='\r')
    print(f'\n{count}')

check_if_dataset_file_exists_online(new_file_path)