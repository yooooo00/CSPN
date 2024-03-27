import os
from pathlib import Path

# print(os.getcwd())
# print(Path(__file__).parent)

import requests
from concurrent.futures import ThreadPoolExecutor

def download_file(link, save_path):
    filename = link.split('/')[-1]
    response = requests.get(link)
    if not os.path.exists(Path(save_path).parent):
        os.makedirs(Path(save_path).parent)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)

def download_files(links, save_dir):
    if not os.path.exists(save_dir):
        print('路径不对')
        return
    with ThreadPoolExecutor(max_workers=10) as executor:  # 控制同时进行下载的线程数
        for link in links:
            save_path=Path(save_dir)/link.split('/')[-2]/link.split('/')[-1]
            print(link)
            executor.submit(download_file, link, save_path)

base_url='http://datasets.lids.mit.edu/nyudepthv2/nyudepthv2_noskip/val_full/'
print('\n')
with open(Path(__file__).parent/'nyudepth_hdf5_train.csv','r') as file:
    next(file)
    links=[]
    total=len(file.readlines())
    totalcount=0
    count=0
    for line in file:
        links.append(base_url+line.strip().split('/')[-2]+'/'+line.strip().split('/')[-1])
        count+=1
        totalcount+=1
        print(f"\r{(totalcount/total)*100:.2f}%,{totalcount}/{total}",end='')
        if count>=1000:
            download_files(links=links,save_dir=Path(__file__).parent.parent/'data/nyudepth_hdf5/train')
            # print(count,end='\r')
            count=0
            links=[]
            pass
    download_files(links=links,save_dir=Path(__file__).parent.parent/'data/nyudepth_hdf5/train')
    print(f"\n{totalcount}完成")

    



