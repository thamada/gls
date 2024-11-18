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
|   0  Tesla V100-SXM2-16GB           On  |   00000000:00:04.0 Off |                    0 |
| N/A   37C    P0             45W /  300W |       1MiB /  16384MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  Tesla V100-SXM2-16GB           On  |   00000000:00:05.0 Off |                    0 |
| N/A   40C    P0             40W /  300W |       1MiB /  16384MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   2  Tesla V100-SXM2-16GB           On  |   00000000:00:06.0 Off |                    0 |
| N/A   39C    P0             39W /  300W |       1MiB /  16384MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   3  Tesla V100-SXM2-16GB           On  |   00000000:00:07.0 Off |                    0 |
| N/A   36C    P0             39W /  300W |       1MiB /  16384MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   4  Tesla V100-SXM2-16GB           On  |   00000000:00:08.0 Off |                    0 |
| N/A   37C    P0             44W /  300W |       1MiB /  16384MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   5  Tesla V100-SXM2-16GB           On  |   00000000:00:09.0 Off |                    0 |
| N/A   39C    P0             41W /  300W |       1MiB /  16384MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   6  Tesla V100-SXM2-16GB           On  |   00000000:00:0A.0 Off |                    0 |
| N/A   38C    P0             45W /  300W |       1MiB /  16384MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   7  Tesla V100-SXM2-16GB           On  |   00000000:00:0B.0 Off |                    0 |
| N/A   36C    P0             44W /  300W |       1MiB /  16384MiB |      0%      Default |
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

Timestamp                                 : Mon Nov 18 12:16:13 2024
Driver Version                            : 550.127.05
CUDA Version                              : 12.4

Attached GPUs                             : 8
GPU 00000000:00:04.0
    Product Name                          : Tesla V100-SXM2-16GB
    Product Brand                         : Tesla
    Product Architecture                  : Volta
    Display Mode                          : Enabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : N/A
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 0324218203972
    GPU UUID                              : GPU-f3bbf1a0-ec50-caa0-d5ab-180afe8207e3
    Minor Number                          : 0
    VBIOS Version                         : 88.00.4F.00.09
    MultiGPU Board                        : No
    Board ID                              : 0x4
    Board Part Number                     : 900-2G503-0300-000
    GPU Part Number                       : 1DB1-895-A1
    FRU Part Number                       : N/A
    Module ID                             : 4
    Inforom Version
        Image Version                     : G503.0201.00.03
        OEM Object                        : 1.1
        ECC Object                        : 5.0
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
        Drain and Reset Recommended       : N/A
    GSP Firmware Version                  : N/A
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x00
        Device                            : 0x04
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x1DB110DE
        Bus Id                            : 00000000:00:04.0
        Sub System Id                     : 0x121210DE
        GPU Link Info
            PCIe Generation
                Max                       : 3
                Current                   : 3
                Device Current            : 3
                Device Max                : 3
                Host Max                  : Unknown Error
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
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 16384 MiB
        Reserved                          : 240 MiB
        Used                              : 1 MiB
        Free                              : 16145 MiB
    BAR1 Memory Usage
        Total                             : 16384 MiB
        Used                              : 2 MiB
        Free                              : 16382 MiB
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
        JPEG                              : N/A
        OFA                               : N/A
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
            Single Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : N/A
                Total                     : 0
            Double Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : 0
                Total                     : 0
        Aggregate
            Single Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : N/A
                Total                     : 0
            Double Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : 0
                Total                     : 0
    Retired Pages
        Single Bit ECC                    : 0
        Double Bit ECC                    : 0
        Pending Page Blacklist            : No
    Remapped Rows                         : N/A
    Temperature
        GPU Current Temp                  : 37 C
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 90 C
        GPU Slowdown Temp                 : 87 C
        GPU Max Operating Temp            : 83 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 33 C
        Memory Max Operating Temp         : 85 C
    GPU Power Readings
        Power Draw                        : 44.50 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 150.00 W
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
        Graphics                          : 135 MHz
        SM                                : 135 MHz
        Memory                            : 877 MHz
        Video                             : 555 MHz
    Applications Clocks
        Graphics                          : 1312 MHz
        Memory                            : 877 MHz
    Default Applications Clocks
        Graphics                          : 1312 MHz
        Memory                            : 877 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1530 MHz
        SM                                : 1530 MHz
        Memory                            : 877 MHz
        Video                             : 1372 MHz
    Max Customer Boost Clocks
        Graphics                          : 1530 MHz
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
    Processes                             : None

GPU 00000000:00:05.0
    Product Name                          : Tesla V100-SXM2-16GB
    Product Brand                         : Tesla
    Product Architecture                  : Volta
    Display Mode                          : Enabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : N/A
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 0324417023159
    GPU UUID                              : GPU-68acf7f1-73a9-a303-c14a-9615d3bd6511
    Minor Number                          : 1
    VBIOS Version                         : 88.00.13.00.02
    MultiGPU Board                        : No
    Board ID                              : 0x5
    Board Part Number                     : 900-2G503-0300-000
    GPU Part Number                       : 1DB1-895-A1
    FRU Part Number                       : N/A
    Module ID                             : 3
    Inforom Version
        Image Version                     : G503.0201.00.03
        OEM Object                        : 1.1
        ECC Object                        : 5.0
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
        Drain and Reset Recommended       : N/A
    GSP Firmware Version                  : N/A
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x00
        Device                            : 0x05
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x1DB110DE
        Bus Id                            : 00000000:00:05.0
        Sub System Id                     : 0x121210DE
        GPU Link Info
            PCIe Generation
                Max                       : 3
                Current                   : 3
                Device Current            : 3
                Device Max                : 3
                Host Max                  : Unknown Error
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
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 16384 MiB
        Reserved                          : 240 MiB
        Used                              : 1 MiB
        Free                              : 16145 MiB
    BAR1 Memory Usage
        Total                             : 16384 MiB
        Used                              : 2 MiB
        Free                              : 16382 MiB
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
        JPEG                              : N/A
        OFA                               : N/A
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
            Single Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : N/A
                Total                     : 0
            Double Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : 0
                Total                     : 0
        Aggregate
            Single Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : N/A
                Total                     : 0
            Double Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : 0
                Total                     : 0
    Retired Pages
        Single Bit ECC                    : 0
        Double Bit ECC                    : 0
        Pending Page Blacklist            : No
    Remapped Rows                         : N/A
    Temperature
        GPU Current Temp                  : 40 C
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 90 C
        GPU Slowdown Temp                 : 87 C
        GPU Max Operating Temp            : 83 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 38 C
        Memory Max Operating Temp         : 85 C
    GPU Power Readings
        Power Draw                        : 40.96 W
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
        Graphics                          : 135 MHz
        SM                                : 135 MHz
        Memory                            : 877 MHz
        Video                             : 555 MHz
    Applications Clocks
        Graphics                          : 1312 MHz
        Memory                            : 877 MHz
    Default Applications Clocks
        Graphics                          : 1312 MHz
        Memory                            : 877 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1530 MHz
        SM                                : 1530 MHz
        Memory                            : 877 MHz
        Video                             : 1372 MHz
    Max Customer Boost Clocks
        Graphics                          : 1530 MHz
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
    Processes                             : None

GPU 00000000:00:06.0
    Product Name                          : Tesla V100-SXM2-16GB
    Product Brand                         : Tesla
    Product Architecture                  : Volta
    Display Mode                          : Enabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : N/A
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 0321518027677
    GPU UUID                              : GPU-e78e5e57-703c-e44c-ede9-fad2adc312f9
    Minor Number                          : 2
    VBIOS Version                         : 88.00.13.00.02
    MultiGPU Board                        : No
    Board ID                              : 0x6
    Board Part Number                     : 900-2G503-0300-000
    GPU Part Number                       : 1DB1-895-A1
    FRU Part Number                       : N/A
    Module ID                             : 4
    Inforom Version
        Image Version                     : G503.0201.00.03
        OEM Object                        : 1.1
        ECC Object                        : 5.0
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
        Drain and Reset Recommended       : N/A
    GSP Firmware Version                  : N/A
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x00
        Device                            : 0x06
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x1DB110DE
        Bus Id                            : 00000000:00:06.0
        Sub System Id                     : 0x121210DE
        GPU Link Info
            PCIe Generation
                Max                       : 3
                Current                   : 3
                Device Current            : 3
                Device Max                : 3
                Host Max                  : Unknown Error
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
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 16384 MiB
        Reserved                          : 240 MiB
        Used                              : 1 MiB
        Free                              : 16145 MiB
    BAR1 Memory Usage
        Total                             : 16384 MiB
        Used                              : 2 MiB
        Free                              : 16382 MiB
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
        JPEG                              : N/A
        OFA                               : N/A
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
            Single Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : N/A
                Total                     : 0
            Double Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : 0
                Total                     : 0
        Aggregate
            Single Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : N/A
                Total                     : 0
            Double Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : 0
                Total                     : 0
    Retired Pages
        Single Bit ECC                    : 0
        Double Bit ECC                    : 0
        Pending Page Blacklist            : No
    Remapped Rows                         : N/A
    Temperature
        GPU Current Temp                  : 39 C
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 90 C
        GPU Slowdown Temp                 : 87 C
        GPU Max Operating Temp            : 83 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 36 C
        Memory Max Operating Temp         : 85 C
    GPU Power Readings
        Power Draw                        : 39.45 W
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
        Graphics                          : 135 MHz
        SM                                : 135 MHz
        Memory                            : 877 MHz
        Video                             : 555 MHz
    Applications Clocks
        Graphics                          : 1312 MHz
        Memory                            : 877 MHz
    Default Applications Clocks
        Graphics                          : 1312 MHz
        Memory                            : 877 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1530 MHz
        SM                                : 1530 MHz
        Memory                            : 877 MHz
        Video                             : 1372 MHz
    Max Customer Boost Clocks
        Graphics                          : 1530 MHz
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
    Processes                             : None

GPU 00000000:00:07.0
    Product Name                          : Tesla V100-SXM2-16GB
    Product Brand                         : Tesla
    Product Architecture                  : Volta
    Display Mode                          : Enabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : N/A
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 0321518027719
    GPU UUID                              : GPU-f641830d-c3e5-bdfb-2412-f9270a5d2928
    Minor Number                          : 3
    VBIOS Version                         : 88.00.13.00.02
    MultiGPU Board                        : No
    Board ID                              : 0x7
    Board Part Number                     : 900-2G503-0300-000
    GPU Part Number                       : 1DB1-895-A1
    FRU Part Number                       : N/A
    Module ID                             : 3
    Inforom Version
        Image Version                     : G503.0201.00.03
        OEM Object                        : 1.1
        ECC Object                        : 5.0
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
        Drain and Reset Recommended       : N/A
    GSP Firmware Version                  : N/A
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x00
        Device                            : 0x07
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x1DB110DE
        Bus Id                            : 00000000:00:07.0
        Sub System Id                     : 0x121210DE
        GPU Link Info
            PCIe Generation
                Max                       : 3
                Current                   : 3
                Device Current            : 3
                Device Max                : 3
                Host Max                  : Unknown Error
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
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 16384 MiB
        Reserved                          : 240 MiB
        Used                              : 1 MiB
        Free                              : 16145 MiB
    BAR1 Memory Usage
        Total                             : 16384 MiB
        Used                              : 2 MiB
        Free                              : 16382 MiB
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
        JPEG                              : N/A
        OFA                               : N/A
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
            Single Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : N/A
                Total                     : 0
            Double Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : 0
                Total                     : 0
        Aggregate
            Single Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : N/A
                Total                     : 0
            Double Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : 0
                Total                     : 0
    Retired Pages
        Single Bit ECC                    : 0
        Double Bit ECC                    : 0
        Pending Page Blacklist            : No
    Remapped Rows                         : N/A
    Temperature
        GPU Current Temp                  : 36 C
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 90 C
        GPU Slowdown Temp                 : 87 C
        GPU Max Operating Temp            : 83 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 34 C
        Memory Max Operating Temp         : 85 C
    GPU Power Readings
        Power Draw                        : 39.97 W
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
        Graphics                          : 135 MHz
        SM                                : 135 MHz
        Memory                            : 877 MHz
        Video                             : 555 MHz
    Applications Clocks
        Graphics                          : 1312 MHz
        Memory                            : 877 MHz
    Default Applications Clocks
        Graphics                          : 1312 MHz
        Memory                            : 877 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1530 MHz
        SM                                : 1530 MHz
        Memory                            : 877 MHz
        Video                             : 1372 MHz
    Max Customer Boost Clocks
        Graphics                          : 1530 MHz
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
    Processes                             : None

GPU 00000000:00:08.0
    Product Name                          : Tesla V100-SXM2-16GB
    Product Brand                         : Tesla
    Product Architecture                  : Volta
    Display Mode                          : Enabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : N/A
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 0324218203971
    GPU UUID                              : GPU-a21b8730-c4b2-027e-a677-8646b707cdbc
    Minor Number                          : 4
    VBIOS Version                         : 88.00.4F.00.09
    MultiGPU Board                        : No
    Board ID                              : 0x8
    Board Part Number                     : 900-2G503-0300-000
    GPU Part Number                       : 1DB1-895-A1
    FRU Part Number                       : N/A
    Module ID                             : 4
    Inforom Version
        Image Version                     : G503.0201.00.03
        OEM Object                        : 1.1
        ECC Object                        : 5.0
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
        Drain and Reset Recommended       : N/A
    GSP Firmware Version                  : N/A
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x00
        Device                            : 0x08
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x1DB110DE
        Bus Id                            : 00000000:00:08.0
        Sub System Id                     : 0x121210DE
        GPU Link Info
            PCIe Generation
                Max                       : 3
                Current                   : 3
                Device Current            : 3
                Device Max                : 3
                Host Max                  : Unknown Error
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
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 16384 MiB
        Reserved                          : 240 MiB
        Used                              : 1 MiB
        Free                              : 16145 MiB
    BAR1 Memory Usage
        Total                             : 16384 MiB
        Used                              : 2 MiB
        Free                              : 16382 MiB
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
        JPEG                              : N/A
        OFA                               : N/A
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
            Single Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : N/A
                Total                     : 0
            Double Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : 0
                Total                     : 0
        Aggregate
            Single Bit            
                Device Memory             : 4
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : N/A
                Total                     : 4
            Double Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : 0
                Total                     : 0
    Retired Pages
        Single Bit ECC                    : 1
        Double Bit ECC                    : 0
        Pending Page Blacklist            : No
    Remapped Rows                         : N/A
    Temperature
        GPU Current Temp                  : 38 C
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 90 C
        GPU Slowdown Temp                 : 87 C
        GPU Max Operating Temp            : 83 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 35 C
        Memory Max Operating Temp         : 85 C
    GPU Power Readings
        Power Draw                        : 44.50 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 150.00 W
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
        Graphics                          : 135 MHz
        SM                                : 135 MHz
        Memory                            : 877 MHz
        Video                             : 555 MHz
    Applications Clocks
        Graphics                          : 1312 MHz
        Memory                            : 877 MHz
    Default Applications Clocks
        Graphics                          : 1312 MHz
        Memory                            : 877 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1530 MHz
        SM                                : 1530 MHz
        Memory                            : 877 MHz
        Video                             : 1372 MHz
    Max Customer Boost Clocks
        Graphics                          : 1530 MHz
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
    Processes                             : None

GPU 00000000:00:09.0
    Product Name                          : Tesla V100-SXM2-16GB
    Product Brand                         : Tesla
    Product Architecture                  : Volta
    Display Mode                          : Enabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : N/A
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 0324517094678
    GPU UUID                              : GPU-0eece41c-628e-9354-635e-d195e9df1d69
    Minor Number                          : 5
    VBIOS Version                         : 88.00.13.00.02
    MultiGPU Board                        : No
    Board ID                              : 0x9
    Board Part Number                     : 900-2G503-0300-000
    GPU Part Number                       : 1DB1-895-A1
    FRU Part Number                       : N/A
    Module ID                             : 3
    Inforom Version
        Image Version                     : G503.0201.00.03
        OEM Object                        : 1.1
        ECC Object                        : 5.0
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
        Drain and Reset Recommended       : N/A
    GSP Firmware Version                  : N/A
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x00
        Device                            : 0x09
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x1DB110DE
        Bus Id                            : 00000000:00:09.0
        Sub System Id                     : 0x121210DE
        GPU Link Info
            PCIe Generation
                Max                       : 3
                Current                   : 3
                Device Current            : 3
                Device Max                : 3
                Host Max                  : Unknown Error
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
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 16384 MiB
        Reserved                          : 240 MiB
        Used                              : 1 MiB
        Free                              : 16145 MiB
    BAR1 Memory Usage
        Total                             : 16384 MiB
        Used                              : 2 MiB
        Free                              : 16382 MiB
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
        JPEG                              : N/A
        OFA                               : N/A
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
            Single Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : N/A
                Total                     : 0
            Double Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : 0
                Total                     : 0
        Aggregate
            Single Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : N/A
                Total                     : 0
            Double Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : 0
                Total                     : 0
    Retired Pages
        Single Bit ECC                    : 0
        Double Bit ECC                    : 0
        Pending Page Blacklist            : No
    Remapped Rows                         : N/A
    Temperature
        GPU Current Temp                  : 39 C
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 90 C
        GPU Slowdown Temp                 : 87 C
        GPU Max Operating Temp            : 83 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 37 C
        Memory Max Operating Temp         : 85 C
    GPU Power Readings
        Power Draw                        : 41.94 W
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
        Graphics                          : 135 MHz
        SM                                : 135 MHz
        Memory                            : 877 MHz
        Video                             : 555 MHz
    Applications Clocks
        Graphics                          : 1312 MHz
        Memory                            : 877 MHz
    Default Applications Clocks
        Graphics                          : 1312 MHz
        Memory                            : 877 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1530 MHz
        SM                                : 1530 MHz
        Memory                            : 877 MHz
        Video                             : 1372 MHz
    Max Customer Boost Clocks
        Graphics                          : 1530 MHz
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
    Processes                             : None

GPU 00000000:00:0A.0
    Product Name                          : Tesla V100-SXM2-16GB
    Product Brand                         : Tesla
    Product Architecture                  : Volta
    Display Mode                          : Enabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : N/A
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 0324218203978
    GPU UUID                              : GPU-cf868a21-d726-de0a-32f0-6b014e8add85
    Minor Number                          : 6
    VBIOS Version                         : 88.00.4F.00.09
    MultiGPU Board                        : No
    Board ID                              : 0xa
    Board Part Number                     : 900-2G503-0300-000
    GPU Part Number                       : 1DB1-895-A1
    FRU Part Number                       : N/A
    Module ID                             : 4
    Inforom Version
        Image Version                     : G503.0201.00.03
        OEM Object                        : 1.1
        ECC Object                        : 5.0
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
        Drain and Reset Recommended       : N/A
    GSP Firmware Version                  : N/A
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x00
        Device                            : 0x0A
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x1DB110DE
        Bus Id                            : 00000000:00:0A.0
        Sub System Id                     : 0x121210DE
        GPU Link Info
            PCIe Generation
                Max                       : 3
                Current                   : 3
                Device Current            : 3
                Device Max                : 3
                Host Max                  : Unknown Error
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
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 16384 MiB
        Reserved                          : 240 MiB
        Used                              : 1 MiB
        Free                              : 16145 MiB
    BAR1 Memory Usage
        Total                             : 16384 MiB
        Used                              : 2 MiB
        Free                              : 16382 MiB
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
        JPEG                              : N/A
        OFA                               : N/A
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
            Single Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : N/A
                Total                     : 0
            Double Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : 0
                Total                     : 0
        Aggregate
            Single Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : N/A
                Total                     : 0
            Double Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : 0
                Total                     : 0
    Retired Pages
        Single Bit ECC                    : 0
        Double Bit ECC                    : 0
        Pending Page Blacklist            : No
    Remapped Rows                         : N/A
    Temperature
        GPU Current Temp                  : 38 C
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 90 C
        GPU Slowdown Temp                 : 87 C
        GPU Max Operating Temp            : 83 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 37 C
        Memory Max Operating Temp         : 85 C
    GPU Power Readings
        Power Draw                        : 45.00 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 150.00 W
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
        Graphics                          : 135 MHz
        SM                                : 135 MHz
        Memory                            : 877 MHz
        Video                             : 555 MHz
    Applications Clocks
        Graphics                          : 1312 MHz
        Memory                            : 877 MHz
    Default Applications Clocks
        Graphics                          : 1312 MHz
        Memory                            : 877 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1530 MHz
        SM                                : 1530 MHz
        Memory                            : 877 MHz
        Video                             : 1372 MHz
    Max Customer Boost Clocks
        Graphics                          : 1530 MHz
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
    Processes                             : None

GPU 00000000:00:0B.0
    Product Name                          : Tesla V100-SXM2-16GB
    Product Brand                         : Tesla
    Product Architecture                  : Volta
    Display Mode                          : Enabled
    Display Active                        : Disabled
    Persistence Mode                      : Enabled
    Addressing Mode                       : N/A
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : Disabled
    Accounting Mode Buffer Size           : 4000
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : 0324218203610
    GPU UUID                              : GPU-0af026bd-e04b-42f9-5b83-f1c2badf58ca
    Minor Number                          : 7
    VBIOS Version                         : 88.00.4F.00.09
    MultiGPU Board                        : No
    Board ID                              : 0xb
    Board Part Number                     : 900-2G503-0300-000
    GPU Part Number                       : 1DB1-895-A1
    FRU Part Number                       : N/A
    Module ID                             : 3
    Inforom Version
        Image Version                     : G503.0201.00.03
        OEM Object                        : 1.1
        ECC Object                        : 5.0
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
        Drain and Reset Recommended       : N/A
    GSP Firmware Version                  : N/A
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x00
        Device                            : 0x0B
        Domain                            : 0x0000
        Base Classcode                    : 0x3
        Sub Classcode                     : 0x2
        Device Id                         : 0x1DB110DE
        Bus Id                            : 00000000:00:0B.0
        Sub System Id                     : 0x121210DE
        GPU Link Info
            PCIe Generation
                Max                       : 3
                Current                   : 3
                Device Current            : 3
                Device Max                : 3
                Host Max                  : Unknown Error
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
    Sparse Operation Mode                 : N/A
    FB Memory Usage
        Total                             : 16384 MiB
        Reserved                          : 240 MiB
        Used                              : 1 MiB
        Free                              : 16145 MiB
    BAR1 Memory Usage
        Total                             : 16384 MiB
        Used                              : 2 MiB
        Free                              : 16382 MiB
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
        JPEG                              : N/A
        OFA                               : N/A
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
            Single Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : N/A
                Total                     : 0
            Double Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : 0
                Total                     : 0
        Aggregate
            Single Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : N/A
                Total                     : 0
            Double Bit            
                Device Memory             : 0
                Register File             : 0
                L1 Cache                  : 0
                L2 Cache                  : 0
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : 0
                Total                     : 0
    Retired Pages
        Single Bit ECC                    : 0
        Double Bit ECC                    : 0
        Pending Page Blacklist            : No
    Remapped Rows                         : N/A
    Temperature
        GPU Current Temp                  : 36 C
        GPU T.Limit Temp                  : N/A
        GPU Shutdown Temp                 : 90 C
        GPU Slowdown Temp                 : 87 C
        GPU Max Operating Temp            : 83 C
        GPU Target Temperature            : N/A
        Memory Current Temp               : 35 C
        Memory Max Operating Temp         : 85 C
    GPU Power Readings
        Power Draw                        : 44.53 W
        Current Power Limit               : 300.00 W
        Requested Power Limit             : 300.00 W
        Default Power Limit               : 300.00 W
        Min Power Limit                   : 150.00 W
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
        Graphics                          : 135 MHz
        SM                                : 135 MHz
        Memory                            : 877 MHz
        Video                             : 555 MHz
    Applications Clocks
        Graphics                          : 1312 MHz
        Memory                            : 877 MHz
    Default Applications Clocks
        Graphics                          : 1312 MHz
        Memory                            : 877 MHz
    Deferred Clocks
        Memory                            : N/A
    Max Clocks
        Graphics                          : 1530 MHz
        SM                                : 1530 MHz
        Memory                            : 877 MHz
        Video                             : 1372 MHz
    Max Customer Boost Clocks
        Graphics                          : 1530 MHz
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

