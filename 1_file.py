#  Added comment
# Added another commend
# Added branch as one_branch
# Added jibberish 
import subprocess
import platform

try:
    os_type = platform.system()
    if os_type == 'Windows':
        command = ['cmd', '/c', 'dir']
    else:
        command = ['bash', '-c', 'ls']

    result = subprocess.run(command, capture_output=True, text=True, check=True)
    print(f"Output of the command on {os_type}:")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Command failed with return code {e.returncode}")
    print(f"Error output:\n{e.stderr}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
