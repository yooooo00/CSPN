import os
from pathlib import Path

# print(os.getcwd())
# print(Path(__file__).parent)

import requests
from concurrent.futures import ThreadPoolExecutor

def download_file(link, save_dir):
    filename = link.split('/')[-1]
    filepath = os.path.join(save_dir, filename)
    response = requests.get(link)
    if response.status_code == 200:
        with open(filepath, 'wb') as f:
            f.write(response.content)

def download_files(links, save_dir):
    if not os.path.exists(save_dir):
        print('路径不对')
        return
    with ThreadPoolExecutor(max_workers=10) as executor:  # 控制同时进行下载的线程数
        for link in links:
            executor.submit(download_file, link, save_dir)

base_url='http://datasets.lids.mit.edu/nyudepthv2/nyudepthv2_noskip/val_full/'

with open(Path(__file__).parent/'nyudepth_hdf5_train.csv','r') as file:
    next(file)
    links=[]
    count=0
    for line in file:
        links.append(base_url+line.strip().split('/')[-2]+'/'+line.strip().split('/')[-1])
        count+=1
        if count>=1000:
            download_files(links=links,save_dir=Path(__file__).parent.parent/'data')
            print(count,end=' ')
            count=0
            links=[]
            pass
    download_files(links=links,save_dir=Path(__file__).parent.parent/'data')
    print(count,end=' ')

    


