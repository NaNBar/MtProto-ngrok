import os
import random

os.chdir(os.path.dirname(__file__))

PORT = 4443
USERS = {
    "tg": open("secret", "r").read() if os.path.exists("secret") else "",
}

MODES = {
    "classic": False,
    "secure": True,
    "tls": True,
}

TLS_DOMAIN = random.choice(
    [
        "www.ngrok.com",

    ]
)
AUTHTOKEN = "2JCQ06Dx8HJiMZu4vUAfWyHTdHr_2k8zVcMbazjNELg7LM39x"
AD_TAG = "6a121ef8cb42a837e4d3a6670dd19f3e"
