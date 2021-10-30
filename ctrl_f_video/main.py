import random 
import youtube_dl
import argparse


if __name__ == "__main__":
    # main mehthod of python

    # Input Parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('-url', action='store', dest='url', help='Parse the URL you want to analyse', required=True)

    # Get Input
    results = parser.parse_args()
    if results.url is not None:
        url = str(results.url)    

