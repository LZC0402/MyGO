🧠 MyGO: Make Your Goals Obvious

MyGO is a deep learning model for prostate cancer MRI segmentation that avoids semantic confusion by selectively modeling key global features. It introduces a novel Pixel Fulcrum Module and integrates self-attention with Top-k selection to enhance feature interpretation while reducing computational redundancy. The architecture is built upon a U-KAN backbone and leverages KAN Layers for nonlinear semantic learning.

🎯 Highlights

Pixel Anchor Module: Learns sparse anchors to capture semantic context.

Top-k Attention: Selects the most relevant anchor features.

Focal Loss Integration: Addresses class imbalance in small lesion regions.

U-KAN Framework: Strong modeling for high-order nonlinear features.

SOTA Performance: Achieved 69.73% mIoU and 74.32% Dice on the PI-CAI dataset.

![Model Architecture](fig2.png)
![Model Architecture](fig3.jpg)

| Method       | mIoU (%) | Dice (%) | Specificity (%) | FPR (%) |
|--------------|----------|----------|-----------------|---------|
| U-Net        | 24.00    | 35.64    | 99.57           | 0.43    |
| RollingUnet  | 43.31    | 54.65    | 99.66           | 0.21    |
| U-KAN        | 66.82    | 72.94    | 99.66           | 0.21    |
| MyGO         | 69.73    | 74.32    | 99.87           | 0.13    |

## Checkpoint and matching test data

Use these files together to run the supplied example:

- [Checkpoint: ours.pth](checkpoints/ours.pth)
- [Matching test data: checkpoint_test_data.zip](data/checkpoint_test_data.zip)
- [Inference notebook](inference.ipynb)

The test archive contains **46 prepared T2W MRI slices and 46 corresponding lesion masks**, each 256 by 256 pixels, from PI-CAI patients 11256 (19 slices) and 11382 (27 slices). Use **checkpoint_test_data.zip** with **ours.pth** to reproduce the notebook's example evaluation.

Data source: [PI-CAI](https://pi-cai.grand-challenge.org/). The original public image collection is available in the [Dataset repository](https://github.com/LZC0402/Dataset).

## Run the notebook

1. Download or clone this repository and open **inference.ipynb** in VS Code or Jupyter.
2. Select a **Python 3.12** kernel. Install the dependencies listed in the first code cell, then restart the kernel.
3. Set **ROOT** to your MyGO folder. Leave **DATA_ROOT** at its default, **ROOT / "data/mri"**.
4. Select **Run All**. The notebook downloads missing files, verifies the checkpoint and archive, extracts the matching test images and masks, and runs CPU inference.
5. View the prediction in the final cell. The CSV and JSON results are saved in **local_results/**.

If you prefer to extract the archive yourself, extract **checkpoint_test_data.zip** into **data/**. The resulting folders should be:

    data/mri/images/
    data/mri/masks/0/

The notebook includes the model definitions needed to load this checkpoint and has been executed successfully on the server.

Further code and documentation: **Coming soon**.
