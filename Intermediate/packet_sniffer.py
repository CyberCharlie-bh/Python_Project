# To use thsi python code scapy needs to be installled
#To install scapy there are 2 ways:

#1. python3 -m pip install scapy
# The method is (sudo python packet_sniffer.py)

#2. pipx install scapy
# To use the second method u need to use pipx list
# The method is (sudo FilePath packet_sniffer.py)

# The file saved file.pcap can be only be used in Wireshark

# To select the required please choose from A/B/C
# To select more than one option just type intials 
# Options are A for just count 
# Options are AB for both Count and Filter
# Options are AC for Count and save file
# Options are ABC for all Count, Filter and save Filter


from scapy.all import *
import os

while True:
    print(f'A = Count only\nAB = Count + Filter\nAC = Count + Save\nABC = Count + Filter + Save')
    options = input("Please choose from the given options:- ").lower()

#-----------------------------COUNT-------------------------------------------

    if options == "a":
        num = int(input("Please state the number of packets to sniff:- "))
        results = sniff(count=num)
        results.show()

#---------------------------COUNT AND FILTER-----------------------------------

    elif options == "ab":
        num = int(input("Please state the number of packets to sniff:- "))
        fil = input("Please state the packet filter (example UDP,TCP,ICMP,Port 80):- ")
        results = sniff(count=num,filter=fil)
        results.show()

#----------------------COUNT FILTER AND SAVE FILTER------------------------------

    elif options == "abc":
        file_name = input("Filename of the new file (Without extension):- ") + ".pcap"
        num = int(input("Please state the number of packets to sniff:- "))
        fil = input("Please state the packet filter (example UDP,TCP,ICMP,Port 80):- ")
        results = sniff(count=num,filter=fil)
        
        if not os.path.exists(file_name):
            wrpcap(file_name, results)
            print(f'{file_name} created')

        elif os.path.exists(file_name):
             append = input(f'File exists do you want to make changes in {file_name}')

             if append == "yes":
                 wrpcap(file_name,results,append=True)
             else:
                 pass

        else:
            print("Error 404")

#-------------------------COUNT AND SAVE CONTENT------------------------

    elif options == "ac":
        file_name = input("Filename of the new file (Without extension):- ") + ".pcap"
        num = int(input("Please state the number of packets to sniff:- "))
        results = sniff(count=num)
        
        if not os.path.exists(file_name):
            wrpcap(file_name, results)
            print(f'{file_name} created')

        elif os.path.exists(file_name):
             append = input(f'File exists do you want to make changes in {file_name}')

             if append == "yes":
                 wrpcap(file_name,results,append=True)
             else:
                 pass

        else:
            print("Error 404")

    else:
        print("Please choose from options that are A, AB, AC, ABC")


    y = input("Do you want to continue yes or no: -  ")

    if y == "yes":
        pass
    else:
        break
print("Thanks for trying my project")
