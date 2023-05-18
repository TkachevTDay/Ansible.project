import os
import getpass
import funcs

def main():
    cmd = ''
    while cmd != 'exit':
        cmd = input("=>> ")
        if cmd == "help":
            funcs.help()
        elif cmd == "create-base":
            with open("inventory.txt", "w") as inventory_open:
                funcs.inventory_write(inventory_open)
            print("files created")
        elif cmd == "add_ip":
            funcs.add_to_inventory()
            print("new ip added")
        elif cmd == "delete_ip":
            target_ip = input("print ip to remove: =>> ")
            funcs.delete_ip(target_ip)
            print("{} deleted".format(target_ip))
        elif cmd == "display_config":
            funcs.print_ips()
        elif cmd == "ping":
            funcs.ping()
        elif cmd == "start-install":
            funcs.yaml_start("0")
        elif cmd == "start-remove":
            funcs.yaml_start("2")

if __name__ == '__main__':
    main()