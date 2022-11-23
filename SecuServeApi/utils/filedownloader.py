"""
file downloader for image
"""

import os
import pathlib
from urllib import request

from utils import logger
import os
import requests




# downloader for the avi
def downloadfiles(downloadUrl, location, file):

    try:
        # pulls right info from data
        filename = str(file)
        url = str(downloadUrl)

        logger.info(
            "The file ur downloading is from "
            + str(url)
            + " with the filename "
            + str(file)
            + " to the localtion of "
            + str(location)
        )

        pathlib.Path(location + "/").mkdir(parents=True, exist_ok=True)

        logger.warning(
            "the file location for the downloader is" + str(location) + str(file)
        )

        #! checks for file if it exists and
        if not os.path.exists(location + file):
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
            }
            response = request.get(url, headers=headers)
            logger.Error("RESPONCE OF PAGE IS"+ str(response.status_code))

            #! respoce heasdr
            if(response.status_code == 404):
                logger.Error("cannot download fike does not exists!")
                return -2
                
            else:
                with requests.get(url, headers=headers, stream=True) as r:
                    r.raise_for_status()

                    #! checks  the responce code 
                    if(r.status_code == 404):
                        logger.Error("cannot download fike does not exists!")
                        return -2
                
                    with open(location + file, "wb") as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            # If you have chunk encoded response uncomment if
                            # and set chunk_size parameter to None.
                            # if chunk:
                            f.write(chunk)

                logger.PipeLine_Ok("done downloading  fike....")
    except:
    
        logger.Error("cannot download file")
