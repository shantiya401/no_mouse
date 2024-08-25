import speech_recognition as sr
import os
import subprocess
import pyautogui
import screen_brightness_control as sbc
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
import re
import psutil  # برای بستن برنامه‌ها

def adjust_brightness(increase=None, level=None):
    if level is not None:
        new_brightness = min(100, max(0, level))
        sbc.set_brightness(new_brightness)
        print(f"Brightness set to {new_brightness}%")
    else:
        current_brightness = sbc.get_brightness()[0]
        if increase is not None:
            if increase:
                new_brightness = min(100, current_brightness + 10)
            else:
                new_brightness = max(0, current_brightness - 10)
            sbc.set_brightness(new_brightness)
            print(f"Brightness set to {new_brightness}%")

def adjust_volume(increase=None, mute=None):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    if mute is not None:
        volume.SetMute(mute, None)
        print("Volume muted" if mute else "Volume unmuted")
    else:
        current_volume = volume.GetMasterVolumeLevelScalar()

        if increase is not None:
            if increase:
                new_volume = min(1.0, current_volume + 0.1)
            else:
                new_volume = max(0.0, current_volume - 0.1)

            volume.SetMasterVolumeLevelScalar(new_volume, None)
            print(f"Volume set to {new_volume * 100}%")

def execute_system_command(command):
    if command == 'shutdown':
        os.system("shutdown /s /t 1")
    elif command == 'restart':
        os.system("shutdown /r /t 1")
    elif command == 'device_manager':
        os.system("devmgmt.msc")
    elif command == 'run':
        pyautogui.hotkey('win', 'r')
    elif command == 'cmd':
        os.system("start cmd")
    elif command == 'desktop':
        pyautogui.hotkey('win', 'd')
    elif command == 'vscode':
        try:
            subprocess.Popen("code")
        except FileNotFoundError:
            print("VSCode not found. Make sure it's installed and added to PATH.")
    elif command == 'chrome':
        try:
            subprocess.Popen("chrome")
        except FileNotFoundError:
            print("Chrome not found. Make sure it's installed and added to PATH.")
    elif command == 'control_panel':
        os.system("control")
    elif command == 'wifi_off':
        os.system("netsh interface set interface 'Wi-Fi' admin=disable")
    elif command == 'wifi_on':
        os.system("netsh interface set interface 'Wi-Fi' admin=enable")
    elif command == 'recycle_bin':
        os.system("start shell:RecycleBinFolder")
    elif command == 'empty_recycle_bin':
        os.system("rd /s /q %systemdrive%\\$Recycle.bin")
    elif command == 'screen_off':
        # استفاده از روش SendMessage برای خاموش کردن صفحه نمایش
        import ctypes
        ctypes.windll.user32.SendMessageW(0xFFFF, 0x0112, 0xF170, 2)
        print("Screen turned off.")
    elif command == 'screen_on':
        pyautogui.press('enter')  # Wakes up the screen if it's off
    elif command == 'switch_to_persian':
        pyautogui.hotkey('alt', 'shift')
    elif command == 'switch_to_english':
        pyautogui.hotkey('alt', 'shift')
    elif 'close' in command:
        # بستن برنامه با نام فایل اجرایی
        process_name = command.split('_')[1] + '.exe'
        os.system(f"taskkill /IM {process_name} /F")
    else:
        print(f"Unknown command: {command}")

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language='fa-IR')
        print(f"Command received (FA): {command}")
        return command.lower(), 'fa'
    except sr.UnknownValueError:
        try:
            command = recognizer.recognize_google(audio, language='en-US')
            print(f"Command received (EN): {command}")
            return command.lower(), 'en'
        except sr.UnknownValueError:
            print("Sorry, I did not understand the command.")
            return None, None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None, None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None, None

def find_closest_command(command, commands_dict):
    from difflib import get_close_matches
    matches = get_close_matches(command, commands_dict.keys(), n=1, cutoff=0.6)
    if matches:
        return commands_dict[matches[0]]
    else:
        return None

def execute_command(command, lang):
    commands_dict = {
        'نور کم': 'dim',
        'dim': 'dim',
        'نور زیاد': 'brighten',
        'brighten': 'brighten',
        'روشنایی': 'brightness',
        'brightness': 'brightness',
        'روشنایی کامل': 'full_brightness',
        'full brightness': 'full_brightness',
        'صدا کم': 'volume_down',
        'volume down': 'volume_down',
        'صدا زیاد': 'volume_up',
        'volume up': 'volume_up',
        'صدا قطع': 'mute',
        'mute': 'mute',
        'صدا وصل': 'unmute',
        'unmute': 'unmute',
        'ویندوز خاموش': 'shutdown',
        'shutdown': 'shutdown',
        'ویندوز ری استارت': 'restart',
        'restart': 'restart',
        'دیوایس منیجر': 'device_manager',
        'device manager': 'device_manager',
        'اجرای ران': 'run',
        'run': 'run',
        'اجرای سی ام دی': 'cmd',
        'cmd': 'cmd',
        'دسک تاپ': 'desktop',
        'desktop': 'desktop',
        'اجرای vscode': 'vscode',
        'vscode': 'vscode',
        'اجرای chrome': 'chrome',
        'chrome': 'chrome',
        'کنترل پنل': 'control_panel',
        'control panel': 'control_panel',
        'وای فای خاموش': 'wifi_off',
        'wifi off': 'wifi_off',
        'وای فای روشن': 'wifi_on',
        'wifi on': 'wifi_on',
        'زبان فارسی': 'switch_to_persian',
        'switch to persian': 'switch_to_persian',
        'زبان انگلیسی': 'switch_to_english',
        'switch to english': 'switch_to_english',
        'سطل آشغال': 'recycle_bin',
        'recycle bin': 'recycle_bin',
        'سطل آشغال تخلیه': 'empty_recycle_bin',
        'empty recycle bin': 'empty_recycle_bin',
        'صفحه خاموش': 'screen_off',
        'screen off': 'screen_off',
        'صفحه روشن': 'screen_on',
        'screen on': 'screen_on'
    }

    command_key = find_closest_command(command, commands_dict)
    if command_key:
        if 'dim' in command_key:
            adjust_brightness(increase=False)
        elif 'brighten' in command_key:
            adjust_brightness(increase=True)
        elif 'brightness' in command_key:
            match = re.search(r'(روشنایی|brightness) (\d+)', command)
            if match:
                brightness_level = int(match.group(2))
                adjust_brightness(level=brightness_level)
            elif 'روشنایی کامل' in command or 'full_brightness' in command:
                adjust_brightness(level=100)
        elif command_key in ['volume_down', 'volume_up', 'mute', 'unmute']:
            adjust_volume(increase=(command_key in ['volume_up', 'brighten']), mute=(command_key == 'mute'))
        elif command_key in ['shutdown', 'restart', 'device_manager', 'run', 'cmd', 'desktop', 'vscode', 'chrome', 'control_panel', 'wifi_off', 'wifi_on', 'recycle_bin', 'empty_recycle_bin', 'switch_to_persian', 'switch_to_english']:
            execute_system_command(command_key)
        elif command_key == 'screen_off':
            execute_system_command('screen_off')
        elif command_key == 'screen_on':
            execute_system_command('screen_on')
        else:
            print("Command not recognized.")
    else:
        print("Command not recognized.")

while True:
    command, lang = listen_for_command()
    if command:
        execute_command(command, lang)
