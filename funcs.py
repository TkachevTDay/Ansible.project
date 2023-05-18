import getpass
import subprocess
import os
INVENTORY_FILE = "inventory.txt"
PLAYBOOK_FILE = "ping.yaml"

def help():
    print("create-base     : creating base files needed to work with ansible ")
    print("add_ip          : add new ip to config file")
    print("delete_ip       : delete target ip from config file")
    print("display_config  : display a config file")
    print("ping            : pings added hosts")
    print("start-install   : start ansible scenario")
    print("start-remove    : remove installed features")
    print("exit            : close program")

def inventory_write(obj):
    obj.write("[targets]\n")
    ips = int(input("number of ips =>> "))
    for i in range(ips):
        ip = input("enter ip =>> ")
        user = input("(root default) enter user =>> ")
        user = "root" if user == "" else user
        passwd = getpass.getpass("user password: ")
        text = f"{ip} ansible_user={user} ansible_password={passwd} ansible_python_interpreter=/usr/bin/python3 ansible_become_password=school1516 \n"
        obj.write(text)

def add_to_inventory():
    with open(INVENTORY_FILE, "a") as inventory_append:
        ips = int(input("number of ips you want to add =>> "))
        for i in range(ips):
            ip = input("enter ip =>> ")
            user = input("(root default) enter user =>> ")
            user = "root" if user == "" else user
            passwd = getpass.getpass("user password: ")
            text = f"{ip} ansible_user={user} ansible_password={passwd} ansible_python_interpreter=/usr/bin/python3 ansible_become_password=school1516 \n"
            inventory_append.write(text)

def delete_ip(target):
    with open(INVENTORY_FILE, "r") as input_file, open("temp.txt", "w") as output_file:
        for line in input_file:
            if target not in line.strip("\n"):
                output_file.write(line)
    os.replace("temp.txt", INVENTORY_FILE)

def print_ips():
    with open(INVENTORY_FILE, "r") as input_file:
        for line in input_file:
            print(line)

def ping():
    ansible_command = f"ansible-playbook -i {INVENTORY_FILE} {PLAYBOOK_FILE}"
    result = subprocess.run(ansible_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode == 0:
        print("Successfully executed playbook")
        print(result.stdout.decode("utf-8"))
    else:
        print("Failed to execute playbook")
        print(result.stderr.decode("utf-8"))

def yaml_start(argx):
    const_mode = "install.yaml" if argx == "0" else "upgrade.yaml" if argx == "1" else "remove.yaml"
    ansible_command = f"ansible-playbook -i {INVENTORY_FILE} {const_mode}"
    result = subprocess.run(ansible_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode == 0:
        print("Successfully executed playbook")
        print(result.stdout.decode("utf-8"))
    else:
        print("Failed to execute playbook")
        print(result.stderr.decode("utf-8"))

