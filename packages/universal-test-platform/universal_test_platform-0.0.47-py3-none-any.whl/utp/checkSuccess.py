import os
from xml.dom import minidom

from utp.getConfig import getConfig

def checkSuccess():
    config = getConfig()
    
    file = minidom.parse(os.path.join(os.getcwd(), config.get("artifactsDir") ,'output.xml'))

    #use getElementsByTagName() to get tag
    statistics = file.getElementsByTagName('statistics')
    total = statistics[0].getElementsByTagName('total')
    stats = total[0].getElementsByTagName('stat')

    fails = 0
    for stat in stats:
        fail = int(stat.getAttribute('fail'))
        fails += fail
        
    return fails == 0
        