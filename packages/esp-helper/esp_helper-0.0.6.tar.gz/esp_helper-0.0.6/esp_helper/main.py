from pathlib import Path
import click


def validate_serial_port(ctx, param, value):
    if not value:
        raise click.BadParameter('Serial port is required as first argument.')
    return value


@click.command()
@click.argument('serial-port', callback=validate_serial_port)
@click.option('--baud-rate', default=115200, help='Baud rate for the serial communication (default: 115200)')
@click.option('--scripts-path', help='Absolute path to the directory that holds the scripts to flash.', default="./scripts")
@click.option('--chip', required=True, type=click.Choice(['ESP32', 'ESP8266']), help='Specify the chip type (ESP32 or ESP8266)')
@click.option('--new-firmware', is_flag=True, default=False, help='Erase and flash firmware. If --firmware-file is not specified, this script will attempt to download the latest firmware from micropython.org')
@click.option('--firmware-file', default=None, help='Path to Micropython firmware bin to flash')
@click.option('--write-env-vars', is_flag=True, default=False, help='Overwrite environment variables in the script (os.environ[\'ENV_VAR\']) with local environment variables')
def main(serial_port, baud_rate, scripts_path, chip, new_firmware, firmware_file, write_env_vars):
    from esp_helper import firmware
    from esp_helper import scripts

    if new_firmware:
        firmware.erase_and_flash_firmware(chip, serial_port, firmware_file, baud_rate)

    scripts_directory = Path(scripts_path)

    if not scripts_directory.exists() or not scripts_directory.is_dir():
        raise FileNotFoundError(f"The directory '{scripts_directory}' does not exist or is not a directory.")

    if write_env_vars:
        scripts.substitute_and_flash(scripts_directory, serial_port, baud_rate)

    else:
        scripts.flash_to_esp(scripts_directory, serial_port, baud_rate)


if __name__ == "__main__":
    main()
