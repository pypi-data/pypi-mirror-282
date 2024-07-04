import os
import re
import shutil
from pathlib import Path
import time


def create_temp_dir(name):
    tmp_dir = Path.cwd() / name
    if tmp_dir.exists():
        shutil.rmtree(tmp_dir)
    tmp_dir.mkdir()
    return tmp_dir


def substitute_env_variables(file_path, tmp_dir):
    with open(file_path, 'r') as file:
        script_content = file.read()

    pattern = r"os\.environ\['(\w+)'\]"

    def replace_with_env_value(match):
        env_var = match.group(1)
        env_value = os.getenv(env_var)
        if env_value is None:
            raise ValueError(f"Environment variable '{env_var}' not found.")
        return repr(env_value)

    modified_script_content = re.sub(pattern, replace_with_env_value, script_content)

    original_filename = Path(file_path).name
    modified_file_path = tmp_dir / original_filename

    with open(modified_file_path, 'w') as modified_file:
        modified_file.write(modified_script_content)

    print(f"Modified script saved as {modified_file_path}")

    relative_path = modified_file_path.relative_to(Path.cwd())
    return relative_path


def flash_to_esp(src_dir, serial_port, baud_rate):
    for file_path in src_dir.glob('*'):
        file_path_str = str(file_path).replace('\\', '/')
        rshell_command = f'rshell -p {serial_port} --baud {baud_rate} cp "{file_path_str}" /pyboard'

        try:
            exit_code = os.system(rshell_command)
            if exit_code == 0:
                print(f"Successfully flashed {file_path_str} to ESP32.")
            else:
                print(f"Failed to flash {file_path_str} with exit code {exit_code}.")
        except Exception as e:
            print(f"An error occurred while flashing {file_path_str}: {e}")
        time.sleep(2)  # Flashing too fast seems to cause errors


def substitute_and_flash(scripts_directory, serial_port, baud_rate):
    tmp_dir = create_temp_dir("temp")

    try:
        for script_file in scripts_directory.glob('*.py'):
            substitute_env_variables(script_file, tmp_dir)

        relative_dir = tmp_dir.relative_to(Path.cwd())
        flash_to_esp(relative_dir, serial_port, baud_rate)
    finally:
        shutil.rmtree(tmp_dir)
