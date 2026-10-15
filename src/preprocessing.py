import nibabel as nib
import numpy as np
from pathlib import Path

base = Path(__file__).resolve().parent.parent / "dataset" / "100001"
file_path = base / "100001_time1_t1.nii.gz"

image = nib.load(file_path).get_fdata()

print("NaN values:", np.isnan(image).sum())
print("Infinite values:", np.isinf(image).sum())
print("Total voxels:", image.size)
print("Invalid values:", (~np.isfinite(image)).sum())