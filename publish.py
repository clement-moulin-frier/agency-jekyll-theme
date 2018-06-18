import os
import shutil
import argparse
import subprocess
import string


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--dontclone", help="don't clone the repository")
    # parser.add_argument("--submodules", help="init the submodules")
    args = parser.parse_args()

    name = 'clement-moulin-frier.github.io.git'
    git_url = 'git@github.com:clement-moulin-frier/clement-moulin-frier.github.io'

    tmp_dir = '/tmp/' + name
    if not args.dontclone:
        subprocess.call(['rm', '-rf', tmp_dir])
        subprocess.call(["git", "clone", "-b", "source", git_url, tmp_dir])
    else:
        os.chdir(tmp_dir)
        subprocess.call(["git", "pull"])

    os.chdir(tmp_dir)
    subprocess.call(["git", "config", "user.email", '"clement.moulinfrier@gmail.com"'])
    subprocess.call(["git", "config", "user.name", '"Clement Moulin-Frier"'])
    # if args.submodules:
    subprocess.call(["git", "submodule", "update", "--init"])
    # os.chdir(os.path.join(tmp_dir, 'media', 'pycon_presentation'))
    # subprocess.call(["git", "submodule", "update", "--init"])
    # os.chdir(tmp_dir)
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
