#mock up prototype version, going to rewrite in C when im not on vacation

import os

def obfus(file, message):
    content = ''
    vars = []

    with open(file, 'r') as f:
        content = f.read()
    for line in content.split('\n'):
        if '=' in line:
            var = line.split('=')[0].strip()
            vars.append(var)
    for var in vars:
        content = content.replace(var, str(hash(var)))
    with open("ob" + file, "w") as f:
        f.write(content)
    os.system("git add ob" + file)
    os.system("git commit -m '" + message + "'")
    os.system("git push")

