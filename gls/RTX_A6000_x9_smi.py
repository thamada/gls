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
|   0  NVIDIA RTX A6000               On  |   00000000:4F:00.0 Off |                    0 |
| 30%   28C    P8             24W /  300W |       1MiB /  46068MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX A6000               On  |   00000000:52:00.0 Off |                    0 |
| 30%   29C    P8             18W /  300W |       1MiB /  46068MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA RTX A6000               On  |   00000000:53:00.0 Off |                    0 |
| 30%   28C    P8             23W /  300W |       1MiB /  46068MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA RTX A6000               On  |   00000000:57:00.0 Off |                    0 |
| 30%   29C    P8             28W /  300W |       1MiB /  46068MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   4  NVIDIA RTX A6000               On  |   00000000:CE:00.0 Off |                    0 |
| 30%   30C    P8             18W /  300W |       1MiB /  46068MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   5  NVIDIA RTX A6000               On  |   00000000:D1:00.0 Off |                    0 |
| 30%   30C    P8             22W /  300W |       1MiB /  46068MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   6  NVIDIA RTX A6000               On  |   00000000:D2:00.0 Off |                    0 |
| 30%   29C    P8             17W /  300W |       1MiB /  46068MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   7  NVIDIA RTX A6000               On  |   00000000:D5:00.0 Off |                    0 |
| 30%   29C    P8             26W /  300W |       1MiB /  46068MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   8  NVIDIA RTX A6000               On  |   00000000:D6:00.0 Off |                    0 |
| 30%   30C    P8             23W /  300W |       1MiB /  46068MiB |      0%      Default |
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

Timestamp                                 : Wed Nov 20 08:14:15 2024
Driver Version                            : 550.127.05
CUDA Version                              : 12.4

Attached GPUs                             : 9
GPU 00000000:4F:00.0
    Product Name                          : NVIDIA RTX A6000
    Product Brand                         : NVIDIA RTX
    Product Architecture                  : Ampere
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
    Serial Number                         : 1562521008218
    GPU UUID                              : GPU-880b8a57-8586-fe40-bec5-fb703f80ffe6
    Minor Number                          : 0
    VBIOS Version                         : 94.02.5C.00.02
    MultiGPU Board                        : No
    Board ID                              : 0x4f00
    Board Part Number                     : 900-5G133-1700-000
    GPU Part Number                       : 2230-875-A1
    FRU Part Number                       : N/A
    Module ID                             : 1
    Inforom Version
        Image Version                     : G133.0500.00.05
        OEM Object                        : 2.0
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
        Bus                               : 0x4F
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x223010DE
        Bus Id                            : 00000000:4F:00.0
        Sub System Id                     : 0x145910DE
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
        Tx Throughput                     : 0 KB/s
        Rx Throughput                     : 150 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : 30 %
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
        Reserved                          : 450 MiB
        Used                              : 1 MiB
        Free                              : 45619 MiB
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
        GPU Current Temp                  : 28 C
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 98 C
        GPU Slowdown Temp                 : 95 C
        GPU Max Operating Temp            : 93 C
        GPU Target Temperature            : 84 C
        Memory Current Temp               : N/A
        Memory Max Operating Temp         : N/A
    GPU Power Readings
        Power Draw                        : 24.69 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 300.00 W
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
        Graphics                          : 0 MHz
        SM                                : 0 MHz
        Memory                            : 405 MHz
        Video                             : 555 MHz
    Applications Clocks
        Graphics                          : 1800 MHz
        Memory                            : 8001 MHz
    Default Applications Clocks
        Graphics                          : 1800 MHz
        Memory                            : 8001 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 2100 MHz
        SM                                : 2100 MHz
        Memory                            : 8001 MHz
        Video                             : 1950 MHz
    Max Customer Boost Clocks
        Graphics                          : N/A
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 0.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None

GPU 00000000:52:00.0
    Product Name                          : NVIDIA RTX A6000
    Product Brand                         : NVIDIA RTX
    Product Architecture                  : Ampere
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
    Serial Number                         : 1562521008167
    GPU UUID                              : GPU-588b70bd-7af1-b8d2-f0a9-d8af8d063f30
    Minor Number                          : 1
    VBIOS Version                         : 94.02.5C.00.02
    MultiGPU Board                        : No
    Board ID                              : 0x5200
    Board Part Number                     : 900-5G133-1700-000
    GPU Part Number                       : 2230-875-A1
    FRU Part Number                       : N/A
    Module ID                             : 1
    Inforom Version
        Image Version                     : G133.0500.00.05
        OEM Object                        : 2.0
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
        Bus                               : 0x52
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x223010DE
        Bus Id                            : 00000000:52:00.0
        Sub System Id                     : 0x145910DE
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
        Tx Throughput                     : 0 KB/s
        Rx Throughput                     : 100 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : 30 %
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
        Reserved                          : 450 MiB
        Used                              : 1 MiB
        Free                              : 45619 MiB
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
        GPU Current Temp                  : 29 C
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 98 C
        GPU Slowdown Temp                 : 95 C
        GPU Max Operating Temp            : 93 C
        GPU Target Temperature            : 84 C
        Memory Current Temp               : N/A
        Memory Max Operating Temp         : N/A
    GPU Power Readings
        Power Draw                        : 18.67 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 300.00 W
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
        Graphics                          : 0 MHz
        SM                                : 0 MHz
        Memory                            : 405 MHz
        Video                             : 555 MHz
    Applications Clocks
        Graphics                          : 1800 MHz
        Memory                            : 8001 MHz
    Default Applications Clocks
        Graphics                          : 1800 MHz
        Memory                            : 8001 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 2100 MHz
        SM                                : 2100 MHz
        Memory                            : 8001 MHz
        Video                             : 1950 MHz
    Max Customer Boost Clocks
        Graphics                          : N/A
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 0.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None

GPU 00000000:53:00.0
    Product Name                          : NVIDIA RTX A6000
    Product Brand                         : NVIDIA RTX
    Product Architecture                  : Ampere
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
    Serial Number                         : 1562521009219
    GPU UUID                              : GPU-9f432315-e4ef-f5e1-ab74-dfd8887bd00c
    Minor Number                          : 2
    VBIOS Version                         : 94.02.5C.00.02
    MultiGPU Board                        : No
    Board ID                              : 0x5300
    Board Part Number                     : 900-5G133-1700-000
    GPU Part Number                       : 2230-875-A1
    FRU Part Number                       : N/A
    Module ID                             : 1
    Inforom Version
        Image Version                     : G133.0500.00.05
        OEM Object                        : 2.0
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
        Bus                               : 0x53
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x223010DE
        Bus Id                            : 00000000:53:00.0
        Sub System Id                     : 0x145910DE
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
        Rx Throughput                     : 50 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : 30 %
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
        Total                             : 46068 MiB
        Reserved                          : 450 MiB
        Used                              : 1 MiB
        Free                              : 45619 MiB
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
        GPU Current Temp                  : 28 C
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 98 C
        GPU Slowdown Temp                 : 95 C
        GPU Max Operating Temp            : 93 C
        GPU Target Temperature            : 84 C
        Memory Current Temp               : N/A
        Memory Max Operating Temp         : N/A
    GPU Power Readings
        Power Draw                        : 23.29 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 300.00 W
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
        Graphics                          : 0 MHz
        SM                                : 0 MHz
        Memory                            : 405 MHz
        Video                             : 555 MHz
    Applications Clocks
        Graphics                          : 1800 MHz
        Memory                            : 8001 MHz
    Default Applications Clocks
        Graphics                          : 1800 MHz
        Memory                            : 8001 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 2100 MHz
        SM                                : 2100 MHz
        Memory                            : 8001 MHz
        Video                             : 1950 MHz
    Max Customer Boost Clocks
        Graphics                          : N/A
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 0.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None

GPU 00000000:57:00.0
    Product Name                          : NVIDIA RTX A6000
    Product Brand                         : NVIDIA RTX
    Product Architecture                  : Ampere
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
    Serial Number                         : 1562521009517
    GPU UUID                              : GPU-0c0867ee-0378-7a41-93f7-0af12ede6ce8
    Minor Number                          : 4
    VBIOS Version                         : 94.02.5C.00.02
    MultiGPU Board                        : No
    Board ID                              : 0x5700
    Board Part Number                     : 900-5G133-1700-000
    GPU Part Number                       : 2230-875-A1
    FRU Part Number                       : N/A
    Module ID                             : 1
    Inforom Version
        Image Version                     : G133.0500.00.05
        OEM Object                        : 2.0
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
        Bus                               : 0x57
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x223010DE
        Bus Id                            : 00000000:57:00.0
        Sub System Id                     : 0x145910DE
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
        Tx Throughput                     : 0 KB/s
        Rx Throughput                     : 0 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : 30 %
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
        Total                             : 46068 MiB
        Reserved                          : 450 MiB
        Used                              : 1 MiB
        Free                              : 45619 MiB
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
        GPU Current Temp                  : 29 C
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 98 C
        GPU Slowdown Temp                 : 95 C
        GPU Max Operating Temp            : 93 C
        GPU Target Temperature            : 84 C
        Memory Current Temp               : N/A
        Memory Max Operating Temp         : N/A
    GPU Power Readings
        Power Draw                        : 28.15 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 300.00 W
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
        Graphics                          : 0 MHz
        SM                                : 0 MHz
        Memory                            : 405 MHz
        Video                             : 555 MHz
    Applications Clocks
        Graphics                          : 1800 MHz
        Memory                            : 8001 MHz
    Default Applications Clocks
        Graphics                          : 1800 MHz
        Memory                            : 8001 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 2100 MHz
        SM                                : 2100 MHz
        Memory                            : 8001 MHz
        Video                             : 1950 MHz
    Max Customer Boost Clocks
        Graphics                          : N/A
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 0.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None

GPU 00000000:CE:00.0
    Product Name                          : NVIDIA RTX A6000
    Product Brand                         : NVIDIA RTX
    Product Architecture                  : Ampere
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
    Serial Number                         : 1562521008526
    GPU UUID                              : GPU-42af5422-772a-4c31-6b42-94abbf346a80
    Minor Number                          : 5
    VBIOS Version                         : 94.02.5C.00.02
    MultiGPU Board                        : No
    Board ID                              : 0xce00
    Board Part Number                     : 900-5G133-1700-000
    GPU Part Number                       : 2230-875-A1
    FRU Part Number                       : N/A
    Module ID                             : 1
    Inforom Version
        Image Version                     : G133.0500.00.05
        OEM Object                        : 2.0
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
        Bus                               : 0xCE
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x223010DE
        Bus Id                            : 00000000:CE:00.0
        Sub System Id                     : 0x145910DE
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
        Tx Throughput                     : 0 KB/s
        Rx Throughput                     : 50 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : 30 %
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
        Reserved                          : 450 MiB
        Used                              : 1 MiB
        Free                              : 45619 MiB
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
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 98 C
        GPU Slowdown Temp                 : 95 C
        GPU Max Operating Temp            : 93 C
        GPU Target Temperature            : 84 C
        Memory Current Temp               : N/A
        Memory Max Operating Temp         : N/A
    GPU Power Readings
        Power Draw                        : 18.67 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 300.00 W
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
        Graphics                          : 0 MHz
        SM                                : 0 MHz
        Memory                            : 405 MHz
        Video                             : 555 MHz
    Applications Clocks
        Graphics                          : 1800 MHz
        Memory                            : 8001 MHz
    Default Applications Clocks
        Graphics                          : 1800 MHz
        Memory                            : 8001 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 2100 MHz
        SM                                : 2100 MHz
        Memory                            : 8001 MHz
        Video                             : 1950 MHz
    Max Customer Boost Clocks
        Graphics                          : N/A
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 0.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None

GPU 00000000:D1:00.0
    Product Name                          : NVIDIA RTX A6000
    Product Brand                         : NVIDIA RTX
    Product Architecture                  : Ampere
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
    Serial Number                         : 1562521008286
    GPU UUID                              : GPU-3e4b79e2-9771-7aba-1766-aaf9bc4acfc4
    Minor Number                          : 6
    VBIOS Version                         : 94.02.5C.00.02
    MultiGPU Board                        : No
    Board ID                              : 0xd100
    Board Part Number                     : 900-5G133-1700-000
    GPU Part Number                       : 2230-875-A1
    FRU Part Number                       : N/A
    Module ID                             : 1
    Inforom Version
        Image Version                     : G133.0500.00.05
        OEM Object                        : 2.0
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
        Bus                               : 0xD1
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x223010DE
        Bus Id                            : 00000000:D1:00.0
        Sub System Id                     : 0x145910DE
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
        Rx Throughput                     : 50 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : 30 %
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
        Reserved                          : 450 MiB
        Used                              : 1 MiB
        Free                              : 45619 MiB
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
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 98 C
        GPU Slowdown Temp                 : 95 C
        GPU Max Operating Temp            : 93 C
        GPU Target Temperature            : 84 C
        Memory Current Temp               : N/A
        Memory Max Operating Temp         : N/A
    GPU Power Readings
        Power Draw                        : 22.28 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 300.00 W
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
        Graphics                          : 0 MHz
        SM                                : 0 MHz
        Memory                            : 405 MHz
        Video                             : 555 MHz
    Applications Clocks
        Graphics                          : 1800 MHz
        Memory                            : 8001 MHz
    Default Applications Clocks
        Graphics                          : 1800 MHz
        Memory                            : 8001 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 2100 MHz
        SM                                : 2100 MHz
        Memory                            : 8001 MHz
        Video                             : 1950 MHz
    Max Customer Boost Clocks
        Graphics                          : N/A
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 0.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None

GPU 00000000:D2:00.0
    Product Name                          : NVIDIA RTX A6000
    Product Brand                         : NVIDIA RTX
    Product Architecture                  : Ampere
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
    Serial Number                         : 1562521009084
    GPU UUID                              : GPU-f6c2d76c-2fc3-2266-ca2a-0794d5ae0153
    Minor Number                          : 7
    VBIOS Version                         : 94.02.5C.00.02
    MultiGPU Board                        : No
    Board ID                              : 0xd200
    Board Part Number                     : 900-5G133-1700-000
    GPU Part Number                       : 2230-875-A1
    FRU Part Number                       : N/A
    Module ID                             : 1
    Inforom Version
        Image Version                     : G133.0500.00.05
        OEM Object                        : 2.0
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
        Bus                               : 0xD2
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x223010DE
        Bus Id                            : 00000000:D2:00.0
        Sub System Id                     : 0x145910DE
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
        Tx Throughput                     : 100 KB/s
        Rx Throughput                     : 50 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : 30 %
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
        Reserved                          : 450 MiB
        Used                              : 1 MiB
        Free                              : 45619 MiB
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
        GPU Current Temp                  : 29 C
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 98 C
        GPU Slowdown Temp                 : 95 C
        GPU Max Operating Temp            : 93 C
        GPU Target Temperature            : 84 C
        Memory Current Temp               : N/A
        Memory Max Operating Temp         : N/A
    GPU Power Readings
        Power Draw                        : 17.85 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 300.00 W
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
        Graphics                          : 0 MHz
        SM                                : 0 MHz
        Memory                            : 405 MHz
        Video                             : 555 MHz
    Applications Clocks
        Graphics                          : 1800 MHz
        Memory                            : 8001 MHz
    Default Applications Clocks
        Graphics                          : 1800 MHz
        Memory                            : 8001 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 2100 MHz
        SM                                : 2100 MHz
        Memory                            : 8001 MHz
        Video                             : 1950 MHz
    Max Customer Boost Clocks
        Graphics                          : N/A
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 0.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None

GPU 00000000:D5:00.0
    Product Name                          : NVIDIA RTX A6000
    Product Brand                         : NVIDIA RTX
    Product Architecture                  : Ampere
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
    Serial Number                         : 1562521008274
    GPU UUID                              : GPU-8ba6181f-9fe7-9eda-3394-4dc1d8a2d854
    Minor Number                          : 8
    VBIOS Version                         : 94.02.5C.00.02
    MultiGPU Board                        : No
    Board ID                              : 0xd500
    Board Part Number                     : 900-5G133-1700-000
    GPU Part Number                       : 2230-875-A1
    FRU Part Number                       : N/A
    Module ID                             : 1
    Inforom Version
        Image Version                     : G133.0500.00.05
        OEM Object                        : 2.0
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
        Bus                               : 0xD5
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x223010DE
        Bus Id                            : 00000000:D5:00.0
        Sub System Id                     : 0x145910DE
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
        Tx Throughput                     : 0 KB/s
        Rx Throughput                     : 50 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : 30 %
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
        Reserved                          : 450 MiB
        Used                              : 1 MiB
        Free                              : 45619 MiB
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
        GPU Current Temp                  : 29 C
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 98 C
        GPU Slowdown Temp                 : 95 C
        GPU Max Operating Temp            : 93 C
        GPU Target Temperature            : 84 C
        Memory Current Temp               : N/A
        Memory Max Operating Temp         : N/A
    GPU Power Readings
        Power Draw                        : 26.77 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 300.00 W
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
        Graphics                          : 0 MHz
        SM                                : 0 MHz
        Memory                            : 405 MHz
        Video                             : 555 MHz
    Applications Clocks
        Graphics                          : 1800 MHz
        Memory                            : 8001 MHz
    Default Applications Clocks
        Graphics                          : 1800 MHz
        Memory                            : 8001 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 2100 MHz
        SM                                : 2100 MHz
        Memory                            : 8001 MHz
        Video                             : 1950 MHz
    Max Customer Boost Clocks
        Graphics                          : N/A
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 0.000 mV
    Fabric
        State                             : N/A
        Status                            : N/A
        CliqueId                          : N/A
        ClusterUUID                       : N/A
        Health
            Bandwidth                     : N/A
    Processes                             : None

GPU 00000000:D6:00.0
    Product Name                          : NVIDIA RTX A6000
    Product Brand                         : NVIDIA RTX
    Product Architecture                  : Ampere
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
    Serial Number                         : 1562521009261
    GPU UUID                              : GPU-ff2fc9a7-8cec-6497-d6af-c4253ff2d4f8
    Minor Number                          : 9
    VBIOS Version                         : 94.02.5C.00.02
    MultiGPU Board                        : No
    Board ID                              : 0xd600
    Board Part Number                     : 900-5G133-1700-000
    GPU Part Number                       : 2230-875-A1
    FRU Part Number                       : N/A
    Module ID                             : 1
    Inforom Version
        Image Version                     : G133.0500.00.05
        OEM Object                        : 2.0
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
        Bus                               : 0xD6
        Device                            : 0x00
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x223010DE
        Bus Id                            : 00000000:D6:00.0
        Sub System Id                     : 0x145910DE
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
        Tx Throughput                     : 0 KB/s
        Rx Throughput                     : 150 KB/s
        Atomic Caps Inbound               : N/A
        Atomic Caps Outbound              : N/A
    Fan Speed                             : 30 %
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
        Total                             : 46068 MiB
        Reserved                          : 450 MiB
        Used                              : 1 MiB
        Free                              : 45619 MiB
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
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 98 C
        GPU Slowdown Temp                 : 95 C
        GPU Max Operating Temp            : 93 C
        GPU Target Temperature            : 84 C
        Memory Current Temp               : N/A
        Memory Max Operating Temp         : N/A
    GPU Power Readings
        Power Draw                        : 23.11 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 100.00 W
        Max Power Limit                   : 300.00 W
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
        Graphics                          : 0 MHz
        SM                                : 0 MHz
        Memory                            : 405 MHz
        Video                             : 555 MHz
    Applications Clocks
        Graphics                          : 1800 MHz
        Memory                            : 8001 MHz
    Default Applications Clocks
        Graphics                          : 1800 MHz
        Memory                            : 8001 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 2100 MHz
        SM                                : 2100 MHz
        Memory                            : 8001 MHz
        Video                             : 1950 MHz
    Max Customer Boost Clocks
        Graphics                          : N/A
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : 0.000 mV
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

