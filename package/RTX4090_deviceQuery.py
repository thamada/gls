#!/usr/bin/env python3

out = '''
deviceQuery Starting...

 CUDA Device Query (Runtime API) version (CUDART static linking)

Detected 8 CUDA Capable device(s)

Device 0: "NVIDIA GeForce RTX 4090"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    8.9
  Total amount of global memory:                 24210 MBytes (25386352640 bytes)
  (128) Multiprocessors, (128) CUDA Cores/MP:    16384 CUDA Cores
  GPU Max Clock rate:                            2520 MHz (2.52 GHz)
  Memory Clock rate:                             10501 Mhz
  Memory Bus Width:                              384-bit
  L2 Cache Size:                                 75497472 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        102400 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  1536
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 2 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Disabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 1 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 1: "NVIDIA GeForce RTX 4090"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    8.9
  Total amount of global memory:                 24210 MBytes (25386352640 bytes)
  (128) Multiprocessors, (128) CUDA Cores/MP:    16384 CUDA Cores
  GPU Max Clock rate:                            2520 MHz (2.52 GHz)
  Memory Clock rate:                             10501 Mhz
  Memory Bus Width:                              384-bit
  L2 Cache Size:                                 75497472 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        102400 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  1536
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 2 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Disabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 37 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 2: "NVIDIA GeForce RTX 4090"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    8.9
  Total amount of global memory:                 24210 MBytes (25386352640 bytes)
  (128) Multiprocessors, (128) CUDA Cores/MP:    16384 CUDA Cores
  GPU Max Clock rate:                            2520 MHz (2.52 GHz)
  Memory Clock rate:                             10501 Mhz
  Memory Bus Width:                              384-bit
  L2 Cache Size:                                 75497472 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        102400 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  1536
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 2 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Disabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 65 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 3: "NVIDIA GeForce RTX 4090"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    8.9
  Total amount of global memory:                 24210 MBytes (25386352640 bytes)
  (128) Multiprocessors, (128) CUDA Cores/MP:    16384 CUDA Cores
  GPU Max Clock rate:                            2520 MHz (2.52 GHz)
  Memory Clock rate:                             10501 Mhz
  Memory Bus Width:                              384-bit
  L2 Cache Size:                                 75497472 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        102400 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  1536
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 2 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Disabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 97 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 4: "NVIDIA GeForce RTX 4090"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    8.9
  Total amount of global memory:                 24210 MBytes (25386352640 bytes)
  (128) Multiprocessors, (128) CUDA Cores/MP:    16384 CUDA Cores
  GPU Max Clock rate:                            2520 MHz (2.52 GHz)
  Memory Clock rate:                             10501 Mhz
  Memory Bus Width:                              384-bit
  L2 Cache Size:                                 75497472 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        102400 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  1536
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 2 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Disabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 129 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 5: "NVIDIA GeForce RTX 4090"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    8.9
  Total amount of global memory:                 24210 MBytes (25386352640 bytes)
  (128) Multiprocessors, (128) CUDA Cores/MP:    16384 CUDA Cores
  GPU Max Clock rate:                            2520 MHz (2.52 GHz)
  Memory Clock rate:                             10501 Mhz
  Memory Bus Width:                              384-bit
  L2 Cache Size:                                 75497472 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        102400 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  1536
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 2 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Disabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 161 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 6: "NVIDIA GeForce RTX 4090"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    8.9
  Total amount of global memory:                 24210 MBytes (25386352640 bytes)
  (128) Multiprocessors, (128) CUDA Cores/MP:    16384 CUDA Cores
  GPU Max Clock rate:                            2520 MHz (2.52 GHz)
  Memory Clock rate:                             10501 Mhz
  Memory Bus Width:                              384-bit
  L2 Cache Size:                                 75497472 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        102400 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  1536
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 2 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Disabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 193 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 7: "NVIDIA GeForce RTX 4090"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    8.9
  Total amount of global memory:                 24210 MBytes (25386352640 bytes)
  (128) Multiprocessors, (128) CUDA Cores/MP:    16384 CUDA Cores
  GPU Max Clock rate:                            2520 MHz (2.52 GHz)
  Memory Clock rate:                             10501 Mhz
  Memory Bus Width:                              384-bit
  L2 Cache Size:                                 75497472 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        102400 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  1536
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 2 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Disabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 225 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >
> Peer access from NVIDIA GeForce RTX 4090 (GPU0) -> NVIDIA GeForce RTX 4090 (GPU1) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU0) -> NVIDIA GeForce RTX 4090 (GPU2) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU0) -> NVIDIA GeForce RTX 4090 (GPU3) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU0) -> NVIDIA GeForce RTX 4090 (GPU4) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU0) -> NVIDIA GeForce RTX 4090 (GPU5) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU0) -> NVIDIA GeForce RTX 4090 (GPU6) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU0) -> NVIDIA GeForce RTX 4090 (GPU7) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU1) -> NVIDIA GeForce RTX 4090 (GPU0) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU1) -> NVIDIA GeForce RTX 4090 (GPU2) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU1) -> NVIDIA GeForce RTX 4090 (GPU3) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU1) -> NVIDIA GeForce RTX 4090 (GPU4) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU1) -> NVIDIA GeForce RTX 4090 (GPU5) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU1) -> NVIDIA GeForce RTX 4090 (GPU6) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU1) -> NVIDIA GeForce RTX 4090 (GPU7) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU2) -> NVIDIA GeForce RTX 4090 (GPU0) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU2) -> NVIDIA GeForce RTX 4090 (GPU1) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU2) -> NVIDIA GeForce RTX 4090 (GPU3) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU2) -> NVIDIA GeForce RTX 4090 (GPU4) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU2) -> NVIDIA GeForce RTX 4090 (GPU5) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU2) -> NVIDIA GeForce RTX 4090 (GPU6) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU2) -> NVIDIA GeForce RTX 4090 (GPU7) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU3) -> NVIDIA GeForce RTX 4090 (GPU0) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU3) -> NVIDIA GeForce RTX 4090 (GPU1) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU3) -> NVIDIA GeForce RTX 4090 (GPU2) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU3) -> NVIDIA GeForce RTX 4090 (GPU4) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU3) -> NVIDIA GeForce RTX 4090 (GPU5) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU3) -> NVIDIA GeForce RTX 4090 (GPU6) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU3) -> NVIDIA GeForce RTX 4090 (GPU7) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU4) -> NVIDIA GeForce RTX 4090 (GPU0) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU4) -> NVIDIA GeForce RTX 4090 (GPU1) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU4) -> NVIDIA GeForce RTX 4090 (GPU2) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU4) -> NVIDIA GeForce RTX 4090 (GPU3) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU4) -> NVIDIA GeForce RTX 4090 (GPU5) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU4) -> NVIDIA GeForce RTX 4090 (GPU6) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU4) -> NVIDIA GeForce RTX 4090 (GPU7) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU5) -> NVIDIA GeForce RTX 4090 (GPU0) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU5) -> NVIDIA GeForce RTX 4090 (GPU1) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU5) -> NVIDIA GeForce RTX 4090 (GPU2) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU5) -> NVIDIA GeForce RTX 4090 (GPU3) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU5) -> NVIDIA GeForce RTX 4090 (GPU4) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU5) -> NVIDIA GeForce RTX 4090 (GPU6) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU5) -> NVIDIA GeForce RTX 4090 (GPU7) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU6) -> NVIDIA GeForce RTX 4090 (GPU0) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU6) -> NVIDIA GeForce RTX 4090 (GPU1) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU6) -> NVIDIA GeForce RTX 4090 (GPU2) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU6) -> NVIDIA GeForce RTX 4090 (GPU3) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU6) -> NVIDIA GeForce RTX 4090 (GPU4) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU6) -> NVIDIA GeForce RTX 4090 (GPU5) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU6) -> NVIDIA GeForce RTX 4090 (GPU7) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU7) -> NVIDIA GeForce RTX 4090 (GPU0) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU7) -> NVIDIA GeForce RTX 4090 (GPU1) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU7) -> NVIDIA GeForce RTX 4090 (GPU2) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU7) -> NVIDIA GeForce RTX 4090 (GPU3) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU7) -> NVIDIA GeForce RTX 4090 (GPU4) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU7) -> NVIDIA GeForce RTX 4090 (GPU5) : No
> Peer access from NVIDIA GeForce RTX 4090 (GPU7) -> NVIDIA GeForce RTX 4090 (GPU6) : No

deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 12.4, CUDA Runtime Version = 12.4, NumDevs = 8
Result = PASS
'''

def main():
    print(out)

