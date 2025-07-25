import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
import os

train_img_dir = './npy/'
train_mask_dir = './npy/'
train_imgs = os.listdir(train_img_dir)
train_masks = os.listdir(train_mask_dir)
train_imgs= sorted([ i for i in train_imgs ])
train_masks= sorted([ i for i in train_masks ])
print(len(train_imgs))
print(len(train_masks))
print(train_imgs[:])
print(train_masks[:])
fin=os.listdir("./label_bingzao")
name=os.listdir(train_img_dir)
print(name)
for f in name:

        try:
            test = np.load(f'./npy/'+f)
            print(f)
            #os.mkdir(f'./bmc_png/'+f.split(".")[0])
        except:
            pass
        for i in range(test.shape[-1]):
            #print(f.split(".")[0]+"_"+str(i)+".png")
            if(f.split(".")[0]+"_"+str(i)+".png" in fin):
                 continue
            try:
                plt.imshow(test[:, :, i], cmap='gray')
                plt.axis('off')
                plt.savefig(f'./label_bingzao/'+f.split(".")[0]+"_"+str(i)+".png")
            except:
                pass
        del test
       