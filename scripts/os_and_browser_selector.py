import platform

def get_os():
    return platform.system()

def select_web_browser():
    os_ = get_os()
    if 'win' in get_os().lower():
        return 'Firefox'
    else:
        return 'Firefox'

