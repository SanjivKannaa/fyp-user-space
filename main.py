import os
from scapy.all import *
from netfilterqueue import NetfilterQueue
import netifaces
QUEUE_NUM = 69  # NFQUEUE number


f = open("output.txt", "w")
# Function to process each packet in the NFQUEUE
def process_packet(packet):
    try:
        temp = ARP(packet.get_payload()).mysummary()
        # temp = ARP_am(packet)
        f.writelines("\n"+str(temp))
        print(temp)
        # scapy_packet = Ether(packet.get_payload())  # Convert raw packet to Scapy packet
        # packet_buffer.append(scapy_packet)  # Save packet in buffer
        # wrpcap(pcap_filename, [scapy_packet], append=True)  # Append to pcap file
        # print(f"Packet captured: {scapy_packet.summary()}")  # Print a summary
        # packet.accept()  # Forward the packet
        packet.accept()
    except Exception as e:
        print(f"Error processing packet: {e}")
        packet.drop()  # Drop the packet in case of errors

# Main function
try:
    interfaces = netifaces.interfaces()  # Get all network interfaces
    host_ips = []
    for interface in interfaces:
        addrs = netifaces.ifaddresses(interface)  # Get interface details
        if netifaces.AF_INET in addrs:
            for addr in addrs[netifaces.AF_INET]:
                host_ips.append(addr['addr'])  # Add IP address to the list

    nfqueue = NetfilterQueue()
    nfqueue.bind(QUEUE_NUM, process_packet)
    nfqueue.run()  # Start capturing packets
except KeyboardInterrupt:
    print("\nKeyboard interrupt detected! Stopping packet capture.")
    print("Execution completed.")
    nfqueue.unbind()  # Unbind the NFQUEUE before exiting
except Exception as e:
    print(f"Unexpected error: {e}")
    nfqueue.unbind()
    f.close()