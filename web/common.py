__author__ = 'Administrator'
def intPage(arg,default):
    try:
        arg = int(arg)
    except:
        arg = default
    return arg
