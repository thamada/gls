#!/usr/bin/env python3
import argparse

out = '''
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.256.02   Driver Version: 470.256.02   CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  Off  | 00000000:08:00.0 N/A |                  N/A |
| 37%   35C    P0    N/A /  N/A |      0MiB /  2000MiB |     N/A      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
'''

out_a = '''
==============NVSMI LOG==============

Timestamp                                 : Thu Nov 21 18:31:40 2024
Driver Version                            : 470.256.02
CUDA Version                              : 11.4

Attached GPUs                             : 1
GPU 00000000:08:00.0
    Product Name                          : NVIDIA GeForce GTX 680
    Product Brand                         : GeForce
    Display Mode                          : N/A
    Display Active                        : N/A
    Persistence Mode                      : Disabled
    MIG Mode
        Current                           : N/A
        Pending                           : N/A
    Accounting Mode                       : N/A
    Accounting Mode Buffer Size           : N/A
    Driver Model
        Current                           : N/A
        Pending                           : N/A
    Serial Number                         : N/A
    GPU UUID                              : GPU-550139a6-4f96-fb93-dc5c-741f01045b48
    Minor Number                          : 0
    VBIOS Version                         : 80.04.47.00.11
    MultiGPU Board                        : N/A
    Board ID                              : N/A
    GPU Part Number                       : N/A
    Module ID                             : 0
    Inforom Version
        Image Version                     : N/A
        OEM Object                        : N/A
        ECC Object                        : N/A
        Power Management Object           : N/A
    GPU Operation Mode
        Current                           : N/A
        Pending                           : N/A
    GSP Firmware Version                  : N/A
    GPU Virtualization Mode
        Virtualization Mode               : N/A
        Host VGPU Mode                    : N/A
    IBMNPU
        Relaxed Ordering Mode             : N/A
    PCI
        Bus                               : 0x08
        Device                            : 0x00
        Domain                            : 0x0000
        Device Id                         : 0x118010DE
        Bus Id                            : 00000000:08:00.0
        Sub System Id                     : 0x353C1458
        GPU Link Info
            PCIe Generation
                Max                       : N/A
                Current                   : N/A
            Link Width
                Max                       : N/A
                Current                   : N/A
        Bridge Chip
            Type                          : N/A
            Firmware                      : N/A
        Replays Since Reset               : 0
        Replay Number Rollovers           : 0
        Tx Throughput                     : N/A
        Rx Throughput                     : N/A
    Fan Speed                             : 37 %
    Performance State                     : P0
    Clocks Throttle Reasons               : N/A
    FB Memory Usage
        Total                             : 2000 MiB
        Used                              : 0 MiB
        Free                              : 2000 MiB
    BAR1 Memory Usage
        Total                             : N/A
        Used                              : N/A
        Free                              : N/A
    Compute Mode                          : Default
    Utilization
        Gpu                               : N/A
        Memory                            : N/A
        Encoder                           : N/A
        Decoder                           : N/A
    Encoder Stats
        Active Sessions                   : N/A
        Average FPS                       : N/A
        Average Latency                   : N/A
    FBC Stats
        Active Sessions                   : N/A
        Average FPS                       : N/A
        Average Latency                   : N/A
    Ecc Mode
        Current                           : N/A
        Pending                           : N/A
    ECC Errors
        Volatile
            Single Bit            
                Device Memory             : N/A
                Register File             : N/A
                L1 Cache                  : N/A
                L2 Cache                  : N/A
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : N/A
                Total                     : N/A
            Double Bit            
                Device Memory             : N/A
                Register File             : N/A
                L1 Cache                  : N/A
                L2 Cache                  : N/A
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : N/A
                Total                     : N/A
        Aggregate
            Single Bit            
                Device Memory             : N/A
                Register File             : N/A
                L1 Cache                  : N/A
                L2 Cache                  : N/A
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : N/A
                Total                     : N/A
            Double Bit            
                Device Memory             : N/A
                Register File             : N/A
                L1 Cache                  : N/A
                L2 Cache                  : N/A
                Texture Memory            : N/A
                Texture Shared            : N/A
                CBU                       : N/A
                Total                     : N/A
    Retired Pages
        Single Bit ECC                    : N/A
        Double Bit ECC                    : N/A
        Pending Page Blacklist            : N/A
    Remapped Rows                         : N/A
    Temperature
        GPU Current Temp                  : 35 C
        GPU Shutdown Temp                 : N/A
        GPU Slowdown Temp                 : N/A
        GPU Max Operating Temp            : N/A
        GPU Target Temperature            : N/A
        Memory Current Temp               : N/A
        Memory Max Operating Temp         : N/A
    Power Readings
        Power Management                  : N/A
        Power Draw                        : N/A
        Power Limit                       : N/A
        Default Power Limit               : N/A
        Enforced Power Limit              : N/A
        Min Power Limit                   : N/A
        Max Power Limit                   : N/A
    Clocks
        Graphics                          : N/A
        SM                                : N/A
        Memory                            : N/A
        Video                             : N/A
    Applications Clocks
        Graphics                          : N/A
        Memory                            : N/A
    Default Applications Clocks
        Graphics                          : N/A
        Memory                            : N/A
    Max Clocks
        Graphics                          : N/A
        SM                                : N/A
        Memory                            : N/A
        Video                             : N/A
    Max Customer Boost Clocks
        Graphics                          : N/A
    Clock Policy
        Auto Boost                        : N/A
        Auto Boost Default                : N/A
    Voltage
        Graphics                          : N/A
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

