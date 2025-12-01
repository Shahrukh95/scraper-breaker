from selenium import webdriver
import tempfile
import os

class Selenium():
    """Selenium class to handle selenium webdriver with custom download directory"""
    
    def __init__(self, download_dir=None):
        unique_dir = tempfile.mkdtemp()
        # Set download directory
        if download_dir is None:
            download_dir = os.path.join(os.getcwd(), "downloads")
        os.makedirs(download_dir, exist_ok=True)
        self.download_dir = download_dir


        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument(f"user-data-dir={unique_dir}")
        # chrome_options.add_argument("profile-directory=Default")
        
        # Reuqired for running in docker
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues. Also required in docker because shared memory is 64mb only in docker.

        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

        chrome_options.add_argument('--window-size=1920,1080')
        # chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--log-level=3")

        # Disable GPU
        # chrome_options.add_argument("--disable-gpu")  # Disables GPU acceleration
        # chrome_options.add_argument("--disable-software-rasterizer")  # Further prevents GPU issues
        chrome_options.add_argument("--enable-webgl")


        # Ignore SSL warnings
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--allow-insecure-localhost")

        # PDF download preferences
        prefs = {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally": True
        }
        chrome_options.add_experimental_option("prefs", prefs)


        self.__driver = webdriver.Chrome(options=chrome_options)



    def get(self, url):
        """Open the URL in selenium"""
        return self.__driver.get(url)
    
    def quit(self):
        """Quit the selenium driver"""
        self.__driver.quit()
   