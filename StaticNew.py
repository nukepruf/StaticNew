
import subprocess
sites = {}


def main():  # main loop for the program, currently no exit condition.
    load_sites()
    print("Starting...")
    while True:
        action = input("Hello, what would you like to do?")
        if action == "?":
            print("available commands are: new, set, query, dhcp ")
        elif action == "new":
            new_site()
        elif action == "set":
            set_static()
        elif action == "dhcp":
            dhcp()
        else:
            print("I'm sorry Dave, I can't do that.")


def set_static():  # modifies the network interface parameters based on user input
    print("Please refer to the Systems spread sheet for site names")
    site_name = input("What site are you at?").lower()
    site_name_map = {
        'site 1': ['192.168.1.2', '255.255.255.0', '192.168.1.1'],
        'site 2': ['192.168.1.3', '255.255.255.0', '192.168.1.1'],
        'site 3': ['192.168.1.4', '255.255.255.0', '192.168.1.1'],
        'site 4': ['192.168.1.5', '255.255.255.0', '192.168.1.1'],
        'New': ['192.168.42.1', '255.255.255.0', '192.168.1.1']
    }

    static_ip = site_name_map[site_name]

    # print(f'{sitename.capatalize()}, okay great! Setting your static IP address to {static_ip}')
    command = f'''netsh interface ip set address name= "Ethernet" static {static_ip}'''.split()
    subprocess.run(command)


def dhcp():  # Function sets network interface back to dhcp mode
    print("Okay, setting the adapter back to dhcp! ")
    dhcp_command = '''netsh interface ip set address name= "Ethernet 3" dhcp'''
    command = dhcp_command.split()
    subprocess.run(command)


def load_sites():  # function opens txt or csv and writes contents to dictionary.
    print("loading site information... ")
    f = open("sites.txt", "r")
    print(f.read())
    sites = f.read()


def new_site():  # function updates the 'sites' dictionary from user input
    new = {}
    new_name = input("Please enter the site name ")
    new_ip = input("Please enter the ip address ")
    new_mask = input("Please enter netmask ")
    new_gateway = input("Please enter the gateway ")
    new.update({new_name: [new_name, new_ip, new_mask, new_gateway]})
    sites.update(new)
    save_sites(new)


def save_sites(write_to_file):  # function writes to txt or csv with the dictionary contents
    print("writing new site to file... ")
    f = open("sites.txt", "w")  #a appends to end of file, w overwrites file, will need to expermiment more.
    ## w is probably better but will need to save and load information back into the "sites" dictionary each time.
    f.write('\n')
    f.write(str(sites))
    f.close()

    load_sites()


main()


