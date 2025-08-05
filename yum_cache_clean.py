import subprocess

def clear_yum_cache():
    try:
        # Run the yum clean all command
        subprocess.run(['yum', 'clean', 'all'], check=True)
        print("YUM cache cleared successfully.") 
    except subprocess.CalledProcessError as e:
        print(f"Failed to clear YUM cache. Error: {e}") 

if __name__ == '__main__':
    clear_yum_cache()
