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

## 2025 checkpoint

You can download the historical checkpoint from [checkpoints/ours2025.pth](checkpoints/ours2025.pth).

If you already have the original 2025 inference code, place this file at the checkpoint path used by your inference script. The matching model is constructed as follows:

```python
import torch
from archs import UKAN

model = UKAN(1, 3, False, embed_dims=[128, 160, 256])
state = torch.load("checkpoints/ours2025.pth", map_location="cpu", weights_only=True)
model.load_state_dict(state, strict=True)
model.eval()
```

This loads the checkpoint with its original architecture. Running image inference also requires the matching preprocessing and model code.

Model code, inference notebook, dataset setup instructions, and further documentation: **Coming soon**.

