# Stateful Address Resolution Protocol

This repository contains the user-space components of the Final Year Project (FYP) by Sanjiv Kannaa J, Bhoopesh M, Sri Vignesh, a B.Tech CSE student at NIT Trichy.

## Project Overview

Address Resolution Protocol (ARP) is a crucial networking protocol that resolves IP addresses to MAC addresses. However, ARP is inherently **stateless**, making it vulnerable to **ARP poisoning attacks**. 

#### **How ARP Poisoning Works**
1. Attackers send **spoofed ARP replies** to a target device, associating their MAC address with the IP of a legitimate device (e.g., a router).
2. The victim updates its ARP table with the attacker's MAC address, unknowingly sending traffic to the attacker's machine.
3. The attacker can then intercept, modify, or drop the victim’s network traffic (Man-in-the-Middle attack).

#### **Mitigating ARP Poisoning with Stateful ARP**
To prevent ARP poisoning, this project introduces a **stateful approach** to ARP management:
- **Persistent ARP Entries**: Maintains a verified ARP cache that is resistant to spoofed updates.
- **Validation Mechanisms**: Tracks ARP requests and responses over time to detect anomalies.
- **Rate Limiting**: Restricts the frequency of ARP table updates to prevent abuse.
- **Logging and Alerts**: Monitors suspicious ARP activity and triggers alerts when inconsistencies are detected.

By making ARP **stateful**, the system ensures that only trusted mappings are maintained, significantly improving network security against ARP spoofing attacks.



## Prerequisites

- **Python**: Ensure Python is installed on your system.
- **Docker**: Install Docker to run containerized applications.
- **Docker Compose**: Install Docker Compose for managing multi-container applications.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SanjivKannaa/fyp-user-space.git
   cd fyp-user-space
