import unittest
from unittest.mock import patch, Mock
from esp_helper.firmware import get_latest_micropython_download_link


class TestFirmware(unittest.TestCase):
    @patch('esp_helper.firmware.requests.get')
    def test_get_latest_micropython_download_link(self, mock_get):
        html_content = '''
                <strong>
                <a href="/resources/firmware/ESP32_GENERIC-20240602-v1.23.0.bin">v1.23.0 (2024-06-02) .bin</a>
                </strong>
                / <a href="/resources/firmware/ESP32_GENERIC-20240602-v1.23.0.app-bin">[.app-bin]</a>
                / <a href="/resources/firmware/ESP32_GENERIC-20240602-v1.23.0.elf">[.elf]</a>
                / <a href="/resources/firmware/ESP32_GENERIC-20240602-v1.23.0.map">[.map]</a>
                / <a href="https://github.com/micropython/micropython/releases/tag/v1.23.0">[Release notes]</a>
                (latest)
        '''

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = html_content
        mock_get.return_value = mock_response

        url = 'http://micropython.org'
        expected_link = 'https://micropython.org/resources/firmware/ESP32_GENERIC-20240602-v1.23.0.bin'
        result = get_latest_micropython_download_link(url)
        self.assertEqual(result, expected_link)

    @patch('esp_helper.firmware.requests.get')
    def test_get_latest_micropython_download_link_no_bin(self, mock_get):
        html_content = '''
        <html>
        <body>
            <a href="/resources/firmware/">Download Latest</a>
            <a href="/resources/firmware/">(latest)</a>
        </body>
        </html>
        '''
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = html_content
        mock_get.return_value = mock_response

        url = 'http://example.com'
        with self.assertRaises(ValueError) as context:
            get_latest_micropython_download_link(url)
        self.assertEqual(str(context.exception), "No '.bin' file found on the page before '(latest)'")

    def test_get_latest_micropython_download_link_live_esp32(self):
        url = 'https://micropython.org/download/ESP32_GENERIC/'
        result = get_latest_micropython_download_link(url)
        self.assertTrue(result.startswith('https://micropython.org/resources/firmware'))

    def test_get_latest_micropython_download_link_live_esp8266(self):
        url = 'https://micropython.org/download/ESP8266_GENERIC/'
        result = get_latest_micropython_download_link(url)
        self.assertTrue(result.startswith('https://micropython.org/resources/firmware'))


if __name__ == '__main__':
    unittest.main()
