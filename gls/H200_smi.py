#!/usr/bin/env python3
import argparse

out = '''
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.90.12              Driver Version: 550.90.12      CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H200                    On  |   00000000:03:00.0 Off |                    0 |
| N/A   28C    P0             74W /  700W |       1MiB / 143771MiB |      0%      Default |
|                                         |                        |             Disabled |
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

Timestamp                                 : Thu Nov 28 04:03:23 2024
Driver Version                            : 550.90.12
CUDA Version                              : 12.4

Attached GPUs                             : 1
GPU 00000000:03:00.0
    Product Name                          : NVIDIA H200
    Product Brand                         : NVIDIA
    Product Architecture                  : Hopper
    Display Mode                          : Disabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : None
    MIG Mode
        Current                           : Disabled
        Pending                           : Disabled
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 1753724031847
    GPU UUID                              : GPU-cb3dfa52-e2f3-9ca4-a399-7d16041c3732
    Minor Number                          : 0
    VBIOS Version                         : 96.00.A5.00.03
    MultiGPU Board                        : No
    Board ID                              : 0x300
    Board Part Number                     : 695-2G520-0280-000
    GPU Part Number                       : 2335-895-A1
    FRU Part Number                       : N/A
    Module ID                             : 3
    Inforom Version
        Image Version                     : G520.0280.02.02
        OEM Object                        : 2.1
        ECC Object                        : 7.16
        Power Management Object           : N/A
    Inforom BBX Object Flush
        Latest Timestamp                  : N/A
        Latest Duration                   : N/A
    GPU Operation Mode
        Current                           : N/A
        Pending                           : N/A
    GPU C2C Mode                          : Disabled
    GPU Virtualization Mode
        Virtualization Mode               : Pass-Through
        Host VGPU Mode                    : N/A
        vGPU Heterogeneous Mode           : N/A
    GPU Reset Status
        Reset Required                    : No
        Drain and Reset Recommended       : No
    GSP Firmware Version                  : 550.90.12
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x03
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x233510DE
        Bus Id                            : 00000000:03:00.0
        Sub System Id                     : 0x18BE10DE
        GPU Link Info
            PCIe Generation
                Max                       : 5
                Current                   : 5
                Device Current            : 5
                Device Max                : 5
                Host Max                  : N/A
            Link Width
                Max                       : 16x
                Current                   : 16x
        Bridge Chip
            Type                          : N/A
            Firmware                      : N/A
        Replays Since Reset               : 0
        Replay Number Rollovers           : 0
        Tx Throughput                     : 657 KB/s
        Rx Throughput                     : 619 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : N/A
    Performance State                     : P0
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
    Sparse Operation Mode                 : Disabled
    FB Memory Usage
        Total                             : 143771 MiB
        Reserved                          : 700 MiB
        Used                              : 1 MiB
        Free                              : 143072 MiB
    BAR1 Memory Usage
        Total                             : 262144 MiB
        Used                              : 1 MiB
        Free                              : 262143 MiB
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
            Max                           : 3072 bank(s)
            High                          : 0 bank(s)
            Partial                       : 0 bank(s)
            Low                           : 0 bank(s)
            None                          : 0 bank(s)
    Temperature
        GPU Current Temp                  : 28 C
        GPU T.Limit Temp                  : 59 C
        GPU Shutdown T.Limit Temp         : -8 C
        GPU Slowdown T.Limit Temp         : -2 C
        GPU Max Operating T.Limit Temp    : 0 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 25 C
        Memory Max Operating T.Limit Temp : 0 C
    GPU Power Readings
        Power Draw                        : 74.58 W
        Current Power Limit               : 700.00 W
        Requested Power Limit             : 700.00 W
        Default Power Limit               : 700.00 W
        Min Power Limit                   : 200.00 W
        Max Power Limit                   : 700.00 W
    GPU Memory Power Readings 
        Power Draw                        : 41.76 W
    Module Power Readings
        Power Draw                        : N/A
        Current Power Limit               : N/A
        Requested Power Limit             : N/A
        Default Power Limit               : N/A
        Min Power Limit                   : N/A
        Max Power Limit                   : N/A
    Clocks
        Graphics                          : 345 MHz
        SM                                : 345 MHz
        Memory                            : 3199 MHz
        Video                             : 765 MHz
    Applications Clocks
        Graphics                          : 1980 MHz
        Memory                            : 3201 MHz
    Default Applications Clocks
        Graphics                          : 1980 MHz
        Memory                            : 3201 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1980 MHz
        SM                                : 1980 MHz
        Memory                            : 3201 MHz
        Video                             : 1545 MHz
    Max Customer Boost Clocks
        Graphics                          : 1980 MHz
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 685.000 mV
    Fabric
        State                             : Completed
        Status                            : Success
        CliqueId                          : 0
        ClusterUUID                       : 00000000-0000-0000-0000-000000000000
        Health
            Bandwidth                     : N/A
    Processes                             : None
'''

def main():
    # ArgumentParserのインスタンスを作成
    parser = argparse.ArgumentParser(description="nvidia-smi simulator")

    # -a 引数（例: フラグとして使用するオプション）
    parser.add_argument('-a', action='store_true', help="simulate nvidia-smi -a")

    # 引数をパース
    args = parser.parse_args()

    # 引数に基づいた処理
    if args.a:
        print(out_a)
    else:
        print(out)

