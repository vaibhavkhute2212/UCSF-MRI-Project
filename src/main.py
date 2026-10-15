from pathlib import Path

# Dataset location
DATASET_PATH = Path(__file__).resolve().parent.parent / "dataset"


def check_dataset():

    patient_folders = [
        folder for folder in DATASET_PATH.iterdir()
        if folder.is_dir()
    ]

    print("===================================")
    print("       UCSF MRI DATASET CHECK")
    print("===================================")

    print("Number of patients:", len(patient_folders))
    print()

    # Check each patient
    for patient in sorted(patient_folders):

        nii_files = list(patient.glob("*.nii")) + list(patient.glob("*.nii.gz"))

        print(f"Patient: {patient.name}")
        print(f"Number of NIfTI files: {len(nii_files)}")

        for file in sorted(nii_files):
            print("   └──", file.name)

        print()


if __name__ == "__main__":
    check_dataset()