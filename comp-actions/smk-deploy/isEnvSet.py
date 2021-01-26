'''
Gets an input value from github actions.  If that parameter and returns
prd if that value is either blank, or null
'''
import os, sys
retVal = 'dev'
if len(sys.argv) > 1:
    inputVar = sys.argv[1]
    if inputVar.lower() not in ['null', '', ' ', 'none']:
        retVal = 'prod'
sys.stdout.write(retVal)
