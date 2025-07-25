import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
import os




path = "./resampled"

for i in os.listdir('./resampled'):#`.reverse()`:
            print(i)
            
            Im_file = nib.load('./resampled/'+i)
            Im = Im_file.get_fdata()
            Im2 = np.int16(Im)
            
            np.save(f'./npy/{i}',Im2)
            #break
            #print(Im2.shape)
            #input()
            #Im2 = np.load(f'./npy/{f}.npy')




"""

test = np.load('./npy/10000_1000000.nii.gz.npy')
#print(np.shape(test))
for i in range(0,15):
    print(test[:, :, i])
    plt.imshow(test[:, :, i]*100, cmap='gray')
    plt.show()

path = "./Task05_Prostate/labelsTr"
"""


"""
for (root, dirs, file) in os.walk(path):
    for f in file:
        if '.gz' in f:
            Im_file = nib.load(f'./Task05_Prostate/labelsTr/{f}')
            Im = Im_file.get_fdata()
            Im2 = np.int16(Im)
            Im3 = Im2[:, :, :]
            np.save(f'./Task05_Prostate/Limages/{f}',Im2)
            Im2 = np.load(f'./Task05_Prostate/Limages/{f}.npy')
            np.save(f'./Task05_Prostate/Limages/{f}', Im2)

test = np.load('./Task05_Prostate/Limages/prostate_14.nii.gz.npy')
print(np.shape(test))
"""
