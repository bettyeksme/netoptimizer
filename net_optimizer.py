import os
import subprocess
import platform
import ctypes
import socket

class NetOptimizer:
    def __init__(self):
        self.os_name = platform.system()
        if self.os_name != "Windows":
            raise EnvironmentError("NetOptimizer is only compatible with Windows.")
        self.is_admin = self.check_admin()

    def check_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def analyze_connection(self):
        try:
            ping_result = subprocess.check_output(["ping", "8.8.8.8", "-n", "4"], shell=True).decode()
            print("Ping Result:\n", ping_result)
        except subprocess.CalledProcessError as e:
            print("Error during ping test:", e)

    def enhance_settings(self):
        if not self.is_admin:
            print("Administrator privileges required to enhance settings.")
            return

        print("Enhancing TCP/IP settings...")
        try:
            os.system("netsh int tcp set global autotuninglevel=normal")
            os.system("netsh int tcp set heuristics disabled")
            os.system("netsh int tcp set global congestionprovider=ctcp")
            os.system("netsh int tcp set global rss=enabled")
            os.system("netsh int tcp set global chimney=enabled")
            print("Network settings enhanced successfully.")
        except Exception as e:
            print("Failed to enhance network settings:", e)

    def flush_dns(self):
        if not self.is_admin:
            print("Administrator privileges required to flush DNS.")
            return

        print("Flushing DNS resolver cache...")
        try:
            os.system("ipconfig /flushdns")
            print("DNS cache flushed successfully.")
        except Exception as e:
            print("Failed to flush DNS cache:", e)

if __name__ == "__main__":
    optimizer = NetOptimizer()
    optimizer.analyze_connection()
    optimizer.enhance_settings()
    optimizer.flush_dns()