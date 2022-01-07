import os
from os import listdir
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pydicom

def getDcms(patient):
    image_dir = 'train/'+patient

    fig=plt.figure(figsize=(10,10))
    columns = 5
    rows = 6
    image_list = os.listdir(image_dir)
    for i in range(1, columns*rows +1):
        filename = image_dir + "/" + str(i) + ".dcm"
        ds = pydicom.dcmread(filename)
        fig.add_subplot(rows, columns, i)
        plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
    return image_list