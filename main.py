# Standard Library
import os
import time

# Local Imports
from Classes.Selenium import Selenium

# DEVELOPMENT ONLY

def get_downloaded_filename(download_dir):
    """Return the most recently added file in the download directory, or None if not found."""
    files = [
        f for f in os.listdir(download_dir)
        if not f.startswith('.')
    ]
    if not files:
        return None
    files = sorted(
        files,
        key=lambda f: os.path.getmtime(os.path.join(download_dir, f)),
        reverse=True
    )
    return files[0]


def download_file(url, driver):
    """*ONLY FOR TESTING PURPOSES* Download a file from a URL using the selenium driver. The download path should be set in the Selenium class."""
    # THE TRICK IS HERE :)
    for i in range(4):
        driver.get(url)
        time.sleep(5)
        
        filename = get_downloaded_filename(driver.download_dir)
        if filename:
            break
    print(f"File downloaded to: {driver.download_dir}")
    


def main():
    driver = Selenium()

    download_file("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12659923/pdf/TPJ-124-0.pdf", driver)
    download_file("https://link.springer.com/content/pdf/10.1007/s10444-024-10186-9.pdf", driver)
    driver.quit()


if __name__ == "__main__":
    main()
