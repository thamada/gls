#!/usr/bin/env python3
import argparse

out = '''
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.127.05             Driver Version: 550.127.05     CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA L40S                    On  |   00000000:A1:00.0 Off |                    0 |
| N/A   31C    P8             33W /  350W |       1MiB /  46068MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
'''

out_a = '''
==============NVSMI LOG==============

Timestamp                                 : Tue Nov 12 07:19:22 2024
Driver Version                            : 550.127.05
CUDA Version                              : 12.4

Attached GPUs                             : 1
GPU 00000000:A1:00.0
    Product Name                          : NVIDIA L40S
    Product Brand                         : NVIDIA
    Product Architecture                  : Ada Lovelace
    Display Mode                          : Enabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : None
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 1323623029179
    GPU UUID                              : GPU-1db6b1cf-de5e-b497-caca-1a027578d587
    Minor Number                          : 6
    VBIOS Version                         : 95.02.66.00.02
    MultiGPU Board                        : No
    Board ID                              : 0xa100
    Board Part Number                     : 900-2G133-0080-000
    GPU Part Number                       : 26B9-896-A1
    FRU Part Number                       : N/A
    Module ID                             : 1
    Inforom Version
        Image Version                     : G133.0242.00.03
        OEM Object                        : 2.1
        ECC Object                        : 6.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : N/A
        Latest Duration                   : N/A
    GPU Operation Mode
        Current                           : N/A
        Pending                           : N/A
    GPU C2C Mode                          : N/A
    GPU Virtualization Mode
        Virtualization Mode               : None
        Host VGPU Mode                    : N/A
        vGPU Heterogeneous Mode           : N/A
    GPU Reset Status
        Reset Required                    : No
        Drain and Reset Recommended       : No
    GSP Firmware Version                  : N/A
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0xA1
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x26B910DE
        Bus Id                            : 00000000:A1:00.0
        Sub System Id                     : 0x185110DE
        GPU Link Info
            PCIe Generation
                Max                       : 4
                Current                   : 1
                Device Current            : 1
                Device Max                : 4
                Host Max                  : 4
            Link Width
                Max                       : 16x
                Current                   : 16x
        Bridge Chip
            Type                          : N/A
            Firmware                      : N/A
        Replays Since Reset               : 0
        Replay Number Rollovers           : 0
        Tx Throughput                     : 50 KB/s
        Rx Throughput                     : 0 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : N/A
    Performance State                     : P8
    Clocks Event Reasons
        Idle                              : Active
        Applications Clocks Setting       : Not Active
        SW Power Cap                      : Not Active
        HW Slowdown                       : Not Active
            HW Thermal Slowdown           : Not Active
            HW Power Brake Slowdown       : Not Active
        Sync Boost                        : Not Active
        SW Thermal Slowdown               : Not Active
        Display Clock Setting             : Not Active
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 46068 MiB
        Reserved                          : 479 MiB
        Used                              : 1 MiB
        Free                              : 45589 MiB
    BAR1 Memory Usage
        Total                             : 65536 MiB
        Used                              : 1 MiB
        Free                              : 65535 MiB
    Conf Compute Protected Memory Usage
        Total                             : 0 MiB
        Used                              : 0 MiB
        Free                              : 0 MiB
    Compute Mode                          : Default
    Utilization
        Gpu                               : 0 %
        Memory                            : 0 %
        Encoder                           : 0 %
        Decoder                           : 0 %
        JPEG                              : 0 %
        OFA                               : 0 %
    Encoder Stats
        Active Sessions                   : 0
        Average FPS                       : 0
        Average Latency                   : 0
    FBC Stats
        Active Sessions                   : 0
        Average FPS                       : 0
        Average Latency                   : 0
    ECC Mode
        Current                           : Enabled
        Pending                           : Enabled
    ECC Errors
        Volatile
            SRAM Correctable              : 0
            SRAM Uncorrectable Parity     : 0
            SRAM Uncorrectable SEC-DED    : 0
            DRAM Correctable              : 0
            DRAM Uncorrectable            : 0
        Aggregate
            SRAM Correctable              : 0
            SRAM Uncorrectable Parity     : 0
            SRAM Uncorrectable SEC-DED    : 0
            DRAM Correctable              : 0
            DRAM Uncorrectable            : 0
            SRAM Threshold Exceeded       : No
        Aggregate Uncorrectable SRAM Sources
            SRAM L2                       : 0
            SRAM SM                       : 0
            SRAM Microcontroller          : 0
            SRAM PCIE                     : 0
            SRAM Other                    : 0
    Retired Pages
        Single Bit ECC                    : N/A
        Double Bit ECC                    : N/A
        Pending Page Blacklist            : N/A
    Remapped Rows
        Correctable Error                 : 0
        Uncorrectable Error               : 0
        Pending                           : No
        Remapping Failure Occurred        : No
        Bank Remap Availability Histogram
            Max                           : 192 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 30 C
        GPU T.Limit Temp                  : 57 C
        GPU Shutdown T.Limit Temp         : -5 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : N/A
        Memory Max Operating T.Limit Temp : N/A
    GPU Power Readings
        Power Draw                        : 33.44 W
        Current Power Limit               : 350.00 W
        Requested Power Limit             : 350.00 W
        Default Power Limit               : 350.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 350.00 W
    GPU Memory Power Readings 
        Power Draw                        : N/A
    Module Power Readings
        Power Draw                        : N/A
        Current Power Limit               : N/A
        Requested Power Limit             : N/A
        Default Power Limit               : N/A
        Min Power Limit                   : N/A
        Max Power Limit                   : N/A
    Clocks
        Graphics                          : 210 MHz
        SM                                : 210 MHz
        Memory                            : 405 MHz
        Video                             : 1185 MHz
    Applications Clocks
        Graphics                          : 2520 MHz
        Memory                            : 9001 MHz
    Default Applications Clocks
        Graphics                          : 2520 MHz
        Memory                            : 9001 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 2520 MHz
        SM                                : 2520 MHz
        Memory                            : 9001 MHz
        Video                             : 1965 MHz
    Max Customer Boost Clocks
        Graphics                          : 2520 MHz
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 875.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None
'''

def main():
    parser = argparse.ArgumentParser(description="nvidia-smi simulator")
    parser.add_argument('-a', action='store_true', help="simulate nvidia-smi -a")
    args = parser.parse_args()

    if args.a:
        print(out_a)
    else:
        print(out)

