import subprocess
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
wifi_list = []
for profile in profiles:
    wifi_profile = {}
    profile_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile]).decode('utf-8', errors="backslashreplace").split('\n')
    if "Security key           : Absent" in profile_info:
        continue
    wifi_profile["ssid"] = profile
    profile_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
    for i in profile_info:
        if "Key Content            :" in i:
            wifi_profile["password"] = i.split(":")[1][1:-1]
    if "password" not in wifi_profile:
        wifi_profile["password"] = "N/A"
    wifi_list.append(wifi_profile)
for x in range(len(wifi_list)):
    print(f"SSID: {wifi_list[x]['ssid']}, Password: {wifi_list[x]['password']}")