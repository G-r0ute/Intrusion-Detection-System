from scapy.all import sniff, wrpcap
import pandas as pd

def packet_handler(packet):
    packet_dict = {
        'time': packet.time,
        'src': packet[0][1].src if packet.haslayer('IP') else 'N/A',
        'dst': packet[0][1].dst if packet.haslayer('IP') else 'N/A',
        'proto': packet.proto if packet.haslayer('IP') else 'N/A',
        'len': len(packet)
    }
    return packet_dict




packets = sniff(count=1000)# Capture 1000 packets

packet_list = [packet_handler(packet) for packet in packets]# Process packets and convert to a list of dictionaries

df = pd.DataFrame(packet_list)  # Convert the list of dictionaries to a DataFrame

df.to_csv('packets.csv', index=False) # Save the DataFrame to a CSV filee

wrpcap('packets.pcap', packets)# Save packets to a pcap file for further analysis