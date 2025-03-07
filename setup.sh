# setup.sh - Script to install dependencies and configure environment
#!/bin/bash

echo "Setting up Dark Web Monitoring Environment..."

# Update system
echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install required packages
echo "Installing required packages..."
sudo apt install -y tor proxychains python3 python3-pip mongodb

# Configure ProxyChains
echo "Configuring ProxyChains..."
sudo sed -i 's/#dynamic_chain/dynamic_chain/' /etc/proxychains.conf
sudo sed -i 's/#strict_chain/strict_chain/' /etc/proxychains.conf
sudo sed -i 's/#socks4 127.0.0.1 9050/socks5 127.0.0.1 9050/' /etc/proxychains.conf

# Start Tor service
echo "Starting Tor service..."
sudo systemctl start tor
sudo systemctl enable tor

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

# Start MongoDB service
echo "Starting MongoDB..."
sudo systemctl start mongod
sudo systemctl enable mongod

echo "Setup complete! Run the scripts to start monitoring."
