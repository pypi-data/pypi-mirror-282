import os
import sys
import random
import shutil
import subprocess

TMPDIR = os.path.abspath(os.environ.get("SUBMIT_TOOL_TMPDIR", os.path.expanduser("~/.submit_tool")))

SUPPORT_EXTS = [".json", ".yaml", ".yml", ".toml", ".ini"]


def random_str(length=8):
    return ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(length))


def check_config_file(path):
    return any(path.endswith(ext) for ext in SUPPORT_EXTS)


def submit():
    print("[Original Command] " + " ".join(sys.argv[1:]))

    tag = random_str()
    while os.path.exists(os.path.join(TMPDIR, tag)):
        tag = random_str()

    # detect config files
    for idx, arg in enumerate(sys.argv[1:]):
        if check_config_file(arg):
            print("\t[Detected Config File] " + arg)
            if not os.path.exists(TMPDIR):
                os.makedirs(TMPDIR, exist_ok=True)
            if not os.path.exists(os.path.join(TMPDIR, tag)):
                os.makedirs(os.path.join(TMPDIR, tag), exist_ok=True)
            # copy to tmpdir
            shutil.copy(arg, os.path.join(TMPDIR, tag))
            # replace with new path
            sys.argv[1+idx] = os.path.join(TMPDIR, tag, os.path.basename(arg))
            print("\t[Replaced Config File] " + sys.argv[1+idx])

    print("[Modified Command] " + " ".join(sys.argv[1:]))
    # run command
    subprocess.run(sys.argv[1:])
