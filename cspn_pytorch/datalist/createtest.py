import os
import random

with open('/content/CSPN/cspn_pytorch/datalist/png_train_test.csv','w') as file:
    file.write("Name\n")
    for name in random.shuffle(os.listdir('/content/drive/MyDrive/Colab Notebooks/data/kitti/2011_10_03_drive_0027_sync/output_CREStereo')):
        file.write(f"{name}\n")

with open('/content/CSPN/cspn_pytorch/datalist/png_val_test.csv','w') as file:
    file.write("Name\n")
    for name in os.listdir('/content/drive/MyDrive/Colab Notebooks/data/kitti/2011_10_03_drive_0027_sync/output_CREStereo'):
        file.write(f"{name}\n")
