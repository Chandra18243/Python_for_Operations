import subprocess

def run_cmd(cmd):
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
        exit(1)
    return result.stdout.strip()

def main():
    lv_name = input("Enter Logical Volume name (lv_name): ").strip()
    vg_name = input("Enter Volume Group name (vg_name): ").strip()
    lv_size = input("Enter Logical Volume size (e.g. 10G, 500M): ").strip()
    mount_point = input("Enter mount point (e.g. /mnt/data): ").strip()

    # Create the logical volume
    run_cmd(['lvcreate', '-L', lv_size, '-n', lv_name, vg_name])

    lv_path = f"/dev/{vg_name}/{lv_name}"

    # Format the LV with XFS
    run_cmd(['mkfs.xfs', lv_path])

    # Create mount point directory if it doesn't exist
    run_cmd(['mkdir', '-p', mount_point])

    # Mount the LV
    run_cmd(['mount', lv_path, mount_point])

    print(f"Logical Volume {lv_path} created, formatted with XFS and mounted at {mount_point}")

if __name__ == "__main__":
    main()
