from urllib.request import urlretrieve
import lzma
from asthook.conf import PACKAGE_PATH
import tempfile
import pkg_resources
import os
from git import Repo, exc  # pip install gitpython



def main():
    os.makedirs(f"{PACKAGE_PATH}/submodule/", exist_ok=True)
    print("clone apkx")
    try:
        Repo.clone_from("https://github.com/b-mueller/apkx.git", f"{PACKAGE_PATH}/submodule/apkx")
    except exc.GitCommandError:
        pass
    print("clone jadx")
    try:
        Repo.clone_from("https://github.com/skylot/jadx.git", f"{PACKAGE_PATH}/submodule/jadx")
    except exc.GitCommandError:
        pass
    env = dict(tuple(str(ws).split()) for ws in pkg_resources.working_set)
    with tempfile.TemporaryDirectory() as tmpdirname:
        os.makedirs(f"{PACKAGE_PATH}/bin/", exist_ok=True)
        for _type, _ext in [("server", ""), ("gadget", ".so")]:
            for abi in ["x86", "x86_64", "arm", "arm64"]:
                print(f"Install frida {_type} for {abi}")
                url = f"https://github.com/frida/frida/releases/download/{env['frida']}/frida-{_type}-{env['frida']}-android-{abi}{_ext}.xz"
                urlretrieve(url, f"{tmpdirname}/frida-{_type}{_ext}.xz")
                with open(f"{PACKAGE_PATH}/bin/frida-{_type}_{abi}{_ext}", "wb") as fw:
                    with lzma.open(f"{tmpdirname}/frida-{_type}{_ext}.xz") as fr:
                        fw.write(fr.read())

if __name__ == "__main__":
    main()
