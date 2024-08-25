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
Installation
To install and use No Mouse, follow these steps:

Clone the repository from GitHub or download the project files.


git clone https://github.com/shantiya401/no_mouse.git
Navigate to the project directory:


cd no_mouse
Install the required dependencies:


pip install -r requirements.txt
Usage
To run No Mouse, execute the no_mouse.py file using Python:


python no_mouse.py
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


### Key Points:

- **General Description**: The `README.md` should provide a general overview of what the project is about and its main features.
- **Requirements**: List the software requirements and provide installation instructions.
- **Installation**: Provide clear instructions on how to install and set up the project.
- **Usage**: Explain how to run the project and include examples of voice commands.
- **Contributing and License**: Provide guidelines for contributing and information about the project's license.
- **Contact Information**: Offer a way for users to get in touch with you for questions or issues.

Feel free to modify or expand upon this template as needed for your project!
