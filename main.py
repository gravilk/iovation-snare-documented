import execjs
import datetime
import requests

# pip install pyexecjs
helper = execjs.compile(open("helper.js").read())
website_url = "https://poshmark.com/login"
script_url = "https://poshmark.com/snare.js"


def generate_snare_token():
    r = requests.get(script_url)
    iggy = r.text.split("\"IGGY\",\"")[1].split("\"")[0]
    flrtd = r.text.split('"FLRTD","')[1].split("\"")[0]
    svrtime = r.text.split('"SVRTIME","')[1].split("\"")[0]
    jssrc = r.text.split('"JSSRC",_i_o.__if_ap("')[1].split("\"")[0]
    jssrc = helper.call("decode", jssrc)
    _if_gs = datetime.datetime.utcnow()
    js_time = (
            str(_if_gs.year)
            + "/"
            + _if_gs.strftime("%m")
            + "/"
            + _if_gs.strftime("%d")
            + " "
            + _if_gs.strftime("%H")
            + ":"
            + _if_gs.strftime("%M")
            + ":"
            + _if_gs.strftime("%S")
    )
    fp_object = {
        "APNAM": "Netscape",  # navigator.appName
        "APVER": "5.0 (X11)",  # navigator.appVersion
        "FLRTD": flrtd,  # string from script (dynamic)
        "IGGY": iggy,  # string from script (dynamic)
        "INTLOC": website_url,  # document.documentURI.split("?")[0]
        "JBRCM": "rv:109.0",  # parsed from ???
        "JBRNM": "Firefox",  # parsed from user agent
        "JBROS": "Linux x86_64",  # navigator.platform
        "JBRVR": "111.0",  # parsed from user agent
        "JDIFF": "1",  # 1 if user agent isn't == "Amazon Cloudfront"
        "JENBL": "1",  # always 1
        "JINT": "function",  # always function
        "JLANG": "en-US",  # navigator.language
        "JPLGNS": "internal-pdf-viewer;internal-pdf-viewer;internal-pdf-viewer;internal-pdf-viewer;internal-pdf-viewer;",  # plugin names lowercase separated by ;
        "JRES": "1440x2560",  # screen resolution
        "JSSRC": jssrc,  # src name (parsed from script)
        "JSTIME": js_time,  # execution time
        "JSVER": "3.1.3",  # version of script
        "NPLAT": "Linux x86_64",  # navigator.platform
        "OSCPU": "Linux x86_64",  # navigator.oscpu
        "SUAGT": "Amazon CloudFront",  # exists if user agent isn't == "Amazon Cloudfront"
        "SVRTIME": svrtime,  # script response type (parsed from script)
        "TZON": "-60",  # timezone offset
        "UAGT": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0"  # user agent
    }

    return "0400" + helper.call("encode", helper.call("stringify_fp", fp_object))


print(generate_snare_token())
