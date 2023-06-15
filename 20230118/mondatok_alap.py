#!/usr/bin/env python3
import random
def névelő(szó):
    magánhangzók = 'aáeéiíoóöőuúüű'
    if szó[0].lower() in magánhangzók:
        return 'az'
    else:
        return 'a'

def jelző():
    return random.choice(['piros', 'nagy', 'könnyed'])

