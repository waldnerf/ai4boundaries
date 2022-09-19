import urllib.error
import urllib.request
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from tqdm import tqdm

# URL of data set
url = 'http://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/DRLL/AI4BOUNDARIES/'


def download_file(url, dst_path):
    """
    Download files to disk

    :param url: URL of the file to download
    :param dst_path: File location on disk after download

    """
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)


def download_ai4boundaries(dir):
    """

    :param dir:

    """
    urls = []
    url_fns = []

    def scrape(site):
        """
        Recursively scrape a website
        :param site:
        :return:
        """

        # getting the request from url
        r = requests.get(site)

        # converting the text
        s = BeautifulSoup(r.text, "html.parser")

        for i in s.find_all("a"):
            href = i.attrs['href']

            if href.endswith("/"):

                subsite = site + href

                if subsite not in urls:
                    urls.append(subsite)

                    # calling it self
                    scrape(subsite)
            if href.endswith("tif"):
                url_fn_ = site + href
                url_fns.append(url_fn_)

    scrape(url)

    if dir.endswith('/'):
        subdirs = [i.replace(url, dir) for i in urls if not i.endswith('DRLL/')]
    else:
        subdirs = [i.replace(url, dir + '/') for i in urls if not i.endswith('DRLL/')]

    subdirs = [subdir.replace('DRLL/', '') for subdir in subdirs if not 'ftp' in subdir]

    for subdir in subdirs:
        Path(subdir).mkdir(parents=True, exist_ok=True)

    for url_fn in tqdm(url_fns):
        if dir.endswith('/'):
            fn = url_fn.replace(url, dir)
        else:
            fn = url_fn.replace(url, dir + '/')

        download_file(url_fn, fn)

    print('Download finished!')


if __name__ == '__main__':
    out_dir = 'C:/Users/franc/Downloads/ai4boundaries'
    download_ai4boundaries(out_dir)
