import os
from scapy.all import ARP, Ether
from netfilterqueue import NetfilterQueue, Packet
import netifaces
QUEUE_NUM = 2  # NFQUEUE number

q = set()
# Function to process each packet in the NFQUEUE
def process_packet(packet):
    try:
        inbound = ARP(packet.get_payload())#.mysummary() # for inbound
        outbound = Ether(packet.get_payload()) # for outbound
        print(outbound)
        packet.accept()
        return
    except Exception as e:
        print(f"Error processing packet: {e}")
        packet.drop()  # Drop the packet in case of errors
'''
        if inbound.op == 1: # inbound req
            inbound = inbound.mysummary().split(" ")
            src = inbound[5]
            dst = inbound[3]
            # in_req.writelines(f"for:{_for} from:{_from} \n")
            print(f"in req -> src:{src} dst:{dst}", end="\t")
            if dst in host_ips:
                print("packet accepted")
                packet.accept()
            else:
                print("packet dropped")
                packet.drop()
        elif inbound.op == 2: # inbound reply
            inbound = inbound.mysummary()#.split(" ")
            print(inbound)
            # _at = inbound[3]
            # _from = inbound[5]
            # in_res.writelines(f"at:{_at} from:{_from} \n")
            # print(f"at:{_at} from:{_from} \n")
            # if _from in q:
            #     q.remove(_from)
            #     print("accepted")
            #     allowed.writelines(f"\ninbound arp reply at:{_at} from:{_from}")
            # else:
            #     print("rejected")
            #     blocked.writelines(f"\ninbound arp reply at:{_at} from:{_from}")
            packet.accept()
        elif outbound.op == 1: # outbound req
            # yet to be implemented
            outbound = str(outbound)#.split(" ")
            print(outbound)
            # _for = outbound[5]
            # _from = outbound[7]
            # in_req.writelines(f"for:{_for} from:{_from} \n")
            # print(f"for:{_for} from:{_from} \n")
            # if _from == "192.168.1.8":
            #     print("accepted")
            #     allowed.writelines(f"\noutbound arp request for:{_for} from:{_from}")
            #     q.add(_for)
            # else:
            #     print("rejected")
            #     blocked.writelines(f"\noutbound arp request for:{_for} from:{_from}")
            packet.accept()
        elif outbound.op == 2: # outbound reply
            outbound = str(outbound)#.split(" ")
            print("monitoring: ", end="\t")
            print(outbound)
            # _at = outbound[5]
            # _from = outbound[7]
            # in_res.writelines(f"at:{_at} from:{_from} \n")
            # print(f"at:{_at} from:{_from} \n")
            # if _from == "192.168.1.8":
            #     print("accepted")
            #     allowed.writelines(f"\noutbound arp reply at:{_at} from:{_from}")
            # else:
            #     print("rejected")
            #     blocked.writelines(f"\noutbound arp reply at:{_at} from:{_from}")
            packet.accept()
        else:
            print(f"Unexpected op in:{inbound.op} out:{outbound.op}!!")
            packet.accept()
        # print(str(inbound.op)+" => "+str(inbound.mysummary().split()))
        # scapy_packet = Ether(packet.get_payload())  # Convert raw packet to Scapy packet
        # packet_buffer.append(scapy_packet)  # Save packet in buffer
        # wrpcap(pcap_filename, [scapy_packet], append=True)  # Append to pcap file
        # print(f"Packet captured: {scapy_packet.summary()}")  # Print a summary
        # packet.accept()  # Forward the packet
'''

# Main function
try:
    interfaces = netifaces.interfaces()  # Get all network interfaces
    host_ips = []
    for interface in interfaces:
        addrs = netifaces.ifaddresses(interface)  # Get interface details
        if netifaces.AF_INET in addrs:
            for addr in addrs[netifaces.AF_INET]:
                host_ips.append(addr['addr'])  # Add IP address to the list
    print("host ips = ", host_ips)
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