import os
import shutil
import argparse
import subprocess
import string
 
 
if __name__ == '__main__':

    name = 'clement-moulin-frier.github.io.git'
    git_url = 'git@github.com:clement-moulin-frier/clement-moulin-frier.github.io'

    tmp_dir = '/tmp/' + name
    subprocess.call(['rm', '-rf', tmp_dir])  
    subprocess.call(["git", "clone", "-b", "source", git_url, tmp_dir])
    os.chdir(tmp_dir)
    subprocess.call(["git", "submodule", "update", "--init"])
    subprocess.call(["bundle", "install"])
    subprocess.call(["bundle", "exec", "jekyll", "build"])
    sub = subprocess.Popen(["git", "ls-files"], stdout=subprocess.PIPE)
    for file_name in string.split(sub.communicate()[0][:-1], '\n'):
        subprocess.call(["git", "rm", file_name])
    subprocess.call(['mv _site/* .'], shell=True)
    subprocess.call(['rmdir _site'], shell=True)
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", "to be published"])
    subprocess.call(["git", "push", "origin", "source:master"])
