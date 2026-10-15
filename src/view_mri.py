import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

base = Path(__file__).resolve().parent.parent / "dataset" / "100005"

# Load MRI
mri = nib.load(base / "100005_time1_t1.nii.gz").get_fdata()

# Load segmentation
seg = nib.load(base / "100005_time1_seg.nii.gz").get_fdata()

labels, counts = np.unique(seg, return_counts=True)

print("\nSegmentation labels:")
for label, count in zip(labels, counts):
    print(f"Label {int(label)}: {count} voxels")
    
# Find the slice containing the most segmentation
seg_counts = np.sum(seg > 0, axis=(0, 1))
z = np.argmax(seg_counts)

print("MRI shape:", mri.shape)
print("Segmentation shape:", seg.shape)
print("Selected slice:", z)

# Display
plt.figure(figsize=(8, 8))

plt.imshow(np.rot90(mri[:, :, z]), cmap="gray")

# Show segmentation transparently
mask = np.ma.masked_where(seg[:, :, z] == 0, seg[:, :, z])
plt.imshow(np.rot90(mask), cmap="jet", alpha=0.5)

plt.title(f"T1 MRI + Segmentation (Slice {z})")
plt.axis("off")

plt.show()