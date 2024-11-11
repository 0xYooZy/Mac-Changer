# MAC Changer

🔧 **A Simple Python Tool for Changing MAC Addresses**

## Overview
`mac-changer` is a lightweight Python script that allows you to easily change the MAC address of your network interface. This can help you improve your privacy, bypass network restrictions, or test network security.

### Key Features
- **Simple and Easy-to-Use**: Change your MAC address effortlessly using straightforward command-line options.
- **MAC Address Validation**: Ensures the provided MAC address follows the correct format before making any changes.
- **Automated Interface Handling**: Uses ifconfig commands to safely bring the network interface down, change the MAC address, and bring it back up.
- **Error Handling**: Provides clear error messages for invalid inputs or insufficient permissions, ensuring a smooth user experience.
- **Cross-Platform Compatibility**: Compatible with all Linux distributions, making it versatile for any Linux environment.
- **Lightweight & Fast**: Minimal dependencies with quick execution, making it ideal for on-the-go network anonymity tasks.

## Getting Started

### Prerequisites
- **Python 3.x** installed on your system.
- **Root Privileges**: You need to run the script with `sudo` to change the MAC address.

### Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/0xYooZy/mac-changer.git
cd mac-changer
```

### Usage
``` bash
sudo python3 mac_changer.py -i <interface> -m <new_mac_address>
```

### Example
```bash
sudo python3 mac_changer.py -i wlan0 -m 00:11:22:33:44:55
```

## Contributing
Feel free to contribute to this project! You can:

- Open Issues: Report bugs or request new features.
- Submit Pull Requests: If you have improvements or new features.

## License
This project is licensed under the MIT License.

## Disclaimer
This tool is intended for educational purposes only. Use it responsibly!

## Author
Developed by YooZy 💻

## Connect with Me
- **Twitter**: [@yourTwitterHandle](https://twitter.com/0xYooZy/)
- **LinkedIn**: [Your LinkedIn](https://www.linkedin.com/in/reda-selouane-398979333/)