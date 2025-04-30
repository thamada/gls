#!/usr/bin/env python3
import argparse

out = '''
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.124.06             Driver Version: 570.124.06     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 5090        On  |   00000000:02:00.0 Off |                  N/A |
|  0%   25C    P8             24W /  575W |       2MiB /  32607MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
'''

out_a = '''
==============NVSMI LOG==============

Timestamp                                 : Wed Apr 30 17:22:38 2025
Driver Version                            : 570.124.06
CUDA Version                              : 12.8

Attached GPUs                             : 1
GPU 00000000:02:00.0
    Product Name                          : NVIDIA GeForce RTX 5090
    Product Brand                         : GeForce
    Product Architecture                  : Blackwell
    Display Mode                          : Disabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : HMM
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 0
    GPU UUID                              : GPU-ea2294a3-4d61-1757-8aed-f91723f16ad2
    Minor Number                          : 1
    VBIOS Version                         : 98.02.2E.40.61
    MultiGPU Board                        : No
    Board ID                              : 0x200
    Board Part Number                     : N/A
    GPU Part Number                       : 2B85-300-A1
    FRU Part Number                       : N/A
    Platform Info
        Chassis Serial Number             : 
        Slot Number                       : 0
        Tray Index                        : 0
        Host ID                           : 1
        Peer Type                         : Direct Connected
        Module Id                         : 1
        GPU Fabric GUID                   : 0x0
    Inforom Version
        Image Version                     : G005.0000.98.01
        OEM Object                        : 2.1
        ECC Object                        : N/A
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : N/A
        Latest Duration                   : N/A
    GPU Operation Mode
        Current                           : N/A
        Pending                           : N/A
    GPU C2C Mode                          : Disabled
    GPU Virtualization Mode
        Virtualization Mode               : None
        Host VGPU Mode                    : N/A
        vGPU Heterogeneous Mode           : N/A
    GPU Reset Status
        Reset Required                    : Requested functionality has been deprecated
        Drain and Reset Recommended       : Requested functionality has been deprecated
    GPU Recovery Action                   : None
    GSP Firmware Version                  : 570.124.06
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x02
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x0
        Device Id                         : 0x2B8510DE
        Bus Id                            : 00000000:02:00.0
        Sub System Id                     : 0xF3181569
        GPU Link Info
            PCIe Generation
                Max                       : 5
                Current                   : 1
                Device Current            : 1
                Device Max                : 5
                Host Max                  : 5
            Link Width
                Max                       : 16x
                Current                   : 8x
        Bridge Chip
            Type                          : N/A
            Firmware                      : N/A
        Replays Since Reset               : 0
        Replay Number Rollovers           : 0
        Tx Throughput                     : 483 KB/s
        Rx Throughput                     : 387 KB/s
        Atomic Caps Outbound              : N/A
        Atomic Caps Inbound               : N/A
    Fan Speed                             : 0 %
    Performance State                     : P8
    Clocks Event Reasons
        Idle                              : Not Active
        Applications Clocks Setting       : Not Active
        SW Power Cap                      : Active
        HW Slowdown                       : Not Active
            HW Thermal Slowdown           : Not Active
            HW Power Brake Slowdown       : Not Active
        Sync Boost                        : Not Active
        SW Thermal Slowdown               : Not Active
        Display Clock Setting             : Not Active
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 32607 MiB
        Reserved                          : 487 MiB
        Used                              : 2 MiB
        Free                              : 32119 MiB
    BAR1 Memory Usage
        Total                             : 32768 MiB
        Used                              : 2 MiB
        Free                              : 32766 MiB
    Conf Compute Protected Memory Usage
        Total                             : 0 MiB
        Used                              : 0 MiB
        Free                              : 0 MiB
    Compute Mode                          : Default
    Utilization
        GPU                               : 0 %
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
    DRAM Encryption Mode
        Current                           : Disabled
        Pending                           : Disabled
    ECC Mode
        Current                           : N/A
        Pending                           : N/A
    ECC Errors
        Volatile
            SRAM Correctable              : N/A
            SRAM Uncorrectable Parity     : N/A
            SRAM Uncorrectable SEC-DED    : N/A
            DRAM Correctable              : N/A
            DRAM Uncorrectable            : N/A
        Aggregate
            SRAM Correctable              : N/A
            SRAM Uncorrectable Parity     : N/A
            SRAM Uncorrectable SEC-DED    : N/A
            DRAM Correctable              : N/A
            DRAM Uncorrectable            : N/A
            SRAM Threshold Exceeded       : N/A
        Aggregate Uncorrectable SRAM Sources
            SRAM L2                       : N/A
            SRAM SM                       : N/A
            SRAM Microcontroller          : N/A
            SRAM PCIE                     : N/A
            SRAM Other                    : N/A
    Retired Pages
        Single Bit ECC                    : N/A
        Double Bit ECC                    : N/A
        Pending Page Blacklist            : N/A
    Remapped Rows                         : N/A
    Temperature
        GPU Current Temp                  : 25 C
        GPU T.Limit Temp                  : 65 C
        GPU Shutdown T.Limit Temp         : -5 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : N/A
        Memory Max Operating T.Limit Temp : N/A
    GPU Power Readings
        Average Power Draw                : 24.05 W
        Instantaneous Power Draw          : 23.78 W
        Current Power Limit               : 575.00 W
        Requested Power Limit             : 575.00 W
        Default Power Limit               : 575.00 W
        Min Power Limit                   : 400.00 W
        Max Power Limit                   : 575.00 W
    GPU Memory Power Readings 
        Average Power Draw                : N/A
        Instantaneous Power Draw          : N/A
    Module Power Readings
        Average Power Draw                : N/A
        Instantaneous Power Draw          : N/A
        Current Power Limit               : N/A
        Requested Power Limit             : N/A
        Default Power Limit               : N/A
        Min Power Limit                   : N/A
        Max Power Limit                   : N/A
    Power Smoothing                       : N/A
    Workload Power Profiles
        Requested Profiles                : N/A
        Enforced Profiles                 : N/A
    Clocks
        Graphics                          : 22 MHz
        SM                                : 22 MHz
        Memory                            : 405 MHz
        Video                             : 600 MHz
    Applications Clocks
        Graphics                          : N/A
        Memory                            : N/A
    Default Applications Clocks
        Graphics                          : N/A
        Memory                            : N/A
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 3090 MHz
        SM                                : 3090 MHz
        Memory                            : 14001 MHz
        Video                             : 3090 MHz
    Max Customer Boost Clocks
        Graphics                          : N/A
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : N/A
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
            Route Recovery in progress    : N/A
            Route Unhealthy               : N/A
            Access Timeout Recovery       : N/A
    Processes                             : None
    Capabilities
        EGM                               : disabled
'''

def main():
    parser = argparse.ArgumentParser(description="nvidia-smi simulator")
    parser.add_argument('-a', action='store_true', help="simulate nvidia-smi -a")
    args = parser.parse_args()

    if args.a:
        print(out_a)
    else:
        print(out)

