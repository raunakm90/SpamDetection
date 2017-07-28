from urllib.request import urlretrieve
import zipfile
import argparse
import time

extract_path = "./data/"


def sms_spam_data(zip_url):
    zip_fldr = "./data/SMS_Spam_Collection.zip"
    print("Downloading SMS Spam Collection...")
    urlretrieve(zip_url, zip_fldr)
    zip_ref = zipfile.ZipFile(zip_fldr)
    print("\n Extracting Folder Contents...")
    zip_ref.extractall(extract_path)
    zip_ref.close()


if __name__ == '__main__':
    '''Download data for SMS Spam Collection from UCI Machine learning repository'''
    parser = argparse.ArgumentParser(
        description='Download SMS Spam Collection from UCI Machine learning repository')
    parser.add_argument('-zip_url', type=str, help="URL to download dataset",
                        default="https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip")
    args = parser.parse_args()

    start = time.time()
    sms_spam_data(args.zip_url)
    print("It took ", time.time() - start, 'seconds to download and extract SMS Spam Collection.')
