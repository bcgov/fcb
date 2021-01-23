'''
super simple, gets a org/repo_name
and returns repo_name
'''
import sys
orgRepo = sys.argv[1]
orgRepoList = orgRepo.split('/')
sys.stdout.write( orgRepoList[1] )