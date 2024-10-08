# No Mouse

**No Mouse** is a voice-controlled tool for managing system settings such as volume and screen brightness, as well as executing various system commands. This project allows you to control your system effortlessly using voice commands, without needing a mouse.

## Features

- **Brightness Control**: Increase, decrease, and set the screen brightness to a specific percentage.
- **Volume Control**: Increase, decrease, mute, and unmute the system volume.
- **System Commands**: Shut down and restart the system, open various applications and windows, and manage Wi-Fi.

## Requirements

To use this project, you need to install the following dependencies:

- Python 3.x
- `speech_recognition` for recognizing voice commands
- `pyautogui` for simulating mouse and keyboard activities
- `screen_brightness_control` for adjusting screen brightness
- `pycaw` for controlling audio volume
- `psutil` for managing processes

You can install these dependencies using pip:

```bash
pip install speech_recognition pyautogui screen_brightness_control pycaw psutil
```

#
To install and use No Mouse, follow these steps:

Clone the repository from GitHub or download the project files.

```bash
git clone https://github.com/shantiya401/no_mouse.git
```

Navigate to the project directory:

```bash
cd no_mouse
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Usage
To run No Mouse, execute the no_mouse.py file using Python:

```bash
python no_mouse.py
```

The program continuously listens for voice commands and performs the corresponding action based on the received command. Voice commands may include the following:

dim to decrease brightness
brighten to increase brightness
brightness [percentage] to set the brightness to a specified percentage
volume down to decrease volume
volume up to increase volume
mute to mute the volume
unmute to unmute the volume
shutdown to shut down the system
restart to restart the system
and other commands for managing applications and windows
Contributing
If you wish to contribute to this project, please submit a pull request. Feedback and suggestions are also welcome!

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
For any questions or issues, please feel free to reach out.

You can follow me on GitHub
