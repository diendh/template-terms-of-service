# -*- coding: utf-8 -*-
"""
"""

import requests
import pathlib
import time

for x in range(1000):

    CURRENT_PATH = pathlib.Path(__file__).parent.absolute()
    URL = "https://lh3.googleusercontent.com/proxy/lNLJCzO17HO_zyBXU1n2-S5EV1FCSh-sOOiL_GBFPzXGEWYXHRfX8srHvX3gPENbLEfbLPEJgyDebliTDZfQh5PjiQnSAu6YECdsjIUIHUeeP_y5P5Bx02LKUet8tKZfAfEJSvf-8pxVLmLpMVOHApsD3YTemk_Wr4bsCH0FlLfOJIvwphPL=s0"

    r = requests.get(url = URL, stream=True)

    if r.status_code == 200:
        print("done")
        with open('{}/img.png'.format(CURRENT_PATH), 'wb') as f:
            for chunk in r:
                f.write(chunk)
    else:
        print(r.status_code)
        with open('{}/err.log'.format(CURRENT_PATH), 'wb') as f:
            for chunk in r:
                f.write(chunk)
    
    time.sleep(1)
