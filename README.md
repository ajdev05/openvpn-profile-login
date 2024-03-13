# OPENVPN PROFILE LOGIN ALERT SYSTEM
<h3>
This program written in Python allows users to track client logins on a server that is running OpenVPN. This program uses Discord Webhooks to send alerts when an OpenVPN Client profile is activated. When a profile establishes a successful connection to the OpenVPN server it sends the profile name and the IP Address associated with it to the webhook and it will also log all the information into a .txt file.
</h3>
<h2>
OpenVPN Server: https://github.com/angristan/openvpn-install

  Install

  ```
  curl -O https://raw.githubusercontent.com/angristan/openvpn-install/master/openvpn-install.sh
  chmod +x openvpn-install.sh
  ./openvpn-install.sh
  ```

Start the program:
  ```
  python3 ovpnLogin.py
  ```

  To run this program in the background:
  ```
  screen python3 ovpnLogin.py
  ```

  To let the program run in the background press **CTRL+AD**
  
</h2>



