import os
import shutil
import platform

print("ThunderFucker 1.0.0 - https://github.com/Shinryin/thunderfucker")

def thunder_fucker():
    profile_paths = {
        'Windows': os.path.expandvars(r'%APPDATA%\Thunderbird'),
        'Darwin': os.path.expanduser('~/Library/Thunderbird'),
        'Linux': os.path.expanduser('~/.thunderbird')
    }
    current_os = platform.system()
    if current_os not in profile_paths: return
    profile_path = profile_paths[current_os]
    profiles_ini_path = os.path.join(profile_path, 'profiles.ini')
    if os.path.exists(profiles_ini_path): os.remove(profiles_ini_path)
    for item in os.listdir(profile_path):
        item_path = os.path.join(profile_path, item)
        if os.path.isdir(item_path) and (item.startswith("default-release") or item.startswith("default")):
            shutil.rmtree(item_path)
    print("Thunderbird profiles removed.")
    input("Press any key to close.")

if __name__ == "__main__":
    thunder_fucker()