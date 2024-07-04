import requests
from bs4 import BeautifulSoup
import subprocess
import urllib.request
import os


def erase_firmware(chip, port, baud_rate):
    try:
        # Construct the command
        command = f"esptool --port {port} --baud {baud_rate} --chip {chip} erase_flash"

        # Run the command using subprocess
        subprocess.run(command, shell=True, check=True)

        print("Firmware erased successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while erasing firmware: {e}")


def flash_firmware(chip, port, firmware_file, baud_rate):
    if chip == "ESP32":
        command = f"esptool --port {port} --baud {baud_rate} --chip {chip} write_flash --flash_size detect --flash_mode dio -z 0x1000 {firmware_file}"

    if chip == "ESP8266":
        command = f"esptool --port {port} --baud {baud_rate} --chip {chip} write_flash --flash_size=detect -fm dout 0 {firmware_file}"

    try:
        subprocess.run(command, shell=True, check=True)
        print("Firmware flashed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while flashing firmware: {e}")


def get_latest_micropython_download_link(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        links = soup.find_all('a')

        latest_version_link = None
        for link in links:
            href = link.get('href')
            if href and href.endswith('.bin'):
                if link.find_previous(string=lambda text: '(latest)' in text):
                    continue

                latest_version_link = f"https://micropython.org{href}"
                break

        if not latest_version_link:
            raise ValueError("No '.bin' file found on the page before '(latest)'")

        return latest_version_link

    except IndexError as e:
        print("Error: Index out of range. Make sure the website structure has not changed.")
        raise e
    except Exception as e:
        print(f"An error occurred: {e}")
        raise


def erase_and_flash_firmware(chip, port, firmware_file, baud_rate):
    if not firmware_file:
        if chip == "ESP32":
            download_page = "https://micropython.org/download/ESP32_GENERIC/"

        if chip == "ESP8266":
            download_page = "https://micropython.org/download/ESP8266_GENERIC/"

        firmware_bin_download_link = get_latest_micropython_download_link(download_page)
        urllib.request.urlretrieve(firmware_bin_download_link, "latest.bin")
        firmware_file = "latest.bin"
    erase_firmware(chip, port, baud_rate)
    flash_firmware(chip, port, firmware_file, baud_rate)
    if firmware_file == "latest.bin":
        os.remove("latest.bin")
    exit(0)
