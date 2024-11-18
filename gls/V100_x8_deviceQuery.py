#!/usr/bin/env python3

out = '''
deviceQuery Starting...

 CUDA Device Query (Runtime API) version (CUDART static linking)

Detected 8 CUDA Capable device(s)

Device 0: "Tesla V100-SXM2-16GB"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    7.0
  Total amount of global memory:                 16144 MBytes (16928342016 bytes)
  (080) Multiprocessors, (064) CUDA Cores/MP:    5120 CUDA Cores
  GPU Max Clock rate:                            1530 MHz (1.53 GHz)
  Memory Clock rate:                             877 Mhz
  Memory Bus Width:                              4096-bit
  L2 Cache Size:                                 6291456 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        98304 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 6 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 0 / 4
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 1: "Tesla V100-SXM2-16GB"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    7.0
  Total amount of global memory:                 16144 MBytes (16928342016 bytes)
  (080) Multiprocessors, (064) CUDA Cores/MP:    5120 CUDA Cores
  GPU Max Clock rate:                            1530 MHz (1.53 GHz)
  Memory Clock rate:                             877 Mhz
  Memory Bus Width:                              4096-bit
  L2 Cache Size:                                 6291456 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        98304 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 6 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 0 / 5
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 2: "Tesla V100-SXM2-16GB"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    7.0
  Total amount of global memory:                 16144 MBytes (16928342016 bytes)
  (080) Multiprocessors, (064) CUDA Cores/MP:    5120 CUDA Cores
  GPU Max Clock rate:                            1530 MHz (1.53 GHz)
  Memory Clock rate:                             877 Mhz
  Memory Bus Width:                              4096-bit
  L2 Cache Size:                                 6291456 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        98304 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 6 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 0 / 6
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 3: "Tesla V100-SXM2-16GB"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    7.0
  Total amount of global memory:                 16144 MBytes (16928342016 bytes)
  (080) Multiprocessors, (064) CUDA Cores/MP:    5120 CUDA Cores
  GPU Max Clock rate:                            1530 MHz (1.53 GHz)
  Memory Clock rate:                             877 Mhz
  Memory Bus Width:                              4096-bit
  L2 Cache Size:                                 6291456 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        98304 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 6 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 0 / 7
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 4: "Tesla V100-SXM2-16GB"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    7.0
  Total amount of global memory:                 16144 MBytes (16928342016 bytes)
  (080) Multiprocessors, (064) CUDA Cores/MP:    5120 CUDA Cores
  GPU Max Clock rate:                            1530 MHz (1.53 GHz)
  Memory Clock rate:                             877 Mhz
  Memory Bus Width:                              4096-bit
  L2 Cache Size:                                 6291456 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        98304 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 6 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 0 / 8
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 5: "Tesla V100-SXM2-16GB"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    7.0
  Total amount of global memory:                 16144 MBytes (16928342016 bytes)
  (080) Multiprocessors, (064) CUDA Cores/MP:    5120 CUDA Cores
  GPU Max Clock rate:                            1530 MHz (1.53 GHz)
  Memory Clock rate:                             877 Mhz
  Memory Bus Width:                              4096-bit
  L2 Cache Size:                                 6291456 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        98304 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 6 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 0 / 9
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 6: "Tesla V100-SXM2-16GB"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    7.0
  Total amount of global memory:                 16144 MBytes (16928342016 bytes)
  (080) Multiprocessors, (064) CUDA Cores/MP:    5120 CUDA Cores
  GPU Max Clock rate:                            1530 MHz (1.53 GHz)
  Memory Clock rate:                             877 Mhz
  Memory Bus Width:                              4096-bit
  L2 Cache Size:                                 6291456 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        98304 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 6 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 0 / 10
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 7: "Tesla V100-SXM2-16GB"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    7.0
  Total amount of global memory:                 16144 MBytes (16928342016 bytes)
  (080) Multiprocessors, (064) CUDA Cores/MP:    5120 CUDA Cores
  GPU Max Clock rate:                            1530 MHz (1.53 GHz)
  Memory Clock rate:                             877 Mhz
  Memory Bus Width:                              4096-bit
  L2 Cache Size:                                 6291456 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        98304 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 6 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 0 / 11
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >
> Peer access from Tesla V100-SXM2-16GB (GPU0) -> Tesla V100-SXM2-16GB (GPU1) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU0) -> Tesla V100-SXM2-16GB (GPU2) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU0) -> Tesla V100-SXM2-16GB (GPU3) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU0) -> Tesla V100-SXM2-16GB (GPU4) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU0) -> Tesla V100-SXM2-16GB (GPU5) : No
> Peer access from Tesla V100-SXM2-16GB (GPU0) -> Tesla V100-SXM2-16GB (GPU6) : No
> Peer access from Tesla V100-SXM2-16GB (GPU0) -> Tesla V100-SXM2-16GB (GPU7) : No
> Peer access from Tesla V100-SXM2-16GB (GPU1) -> Tesla V100-SXM2-16GB (GPU0) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU1) -> Tesla V100-SXM2-16GB (GPU2) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU1) -> Tesla V100-SXM2-16GB (GPU3) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU1) -> Tesla V100-SXM2-16GB (GPU4) : No
> Peer access from Tesla V100-SXM2-16GB (GPU1) -> Tesla V100-SXM2-16GB (GPU5) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU1) -> Tesla V100-SXM2-16GB (GPU6) : No
> Peer access from Tesla V100-SXM2-16GB (GPU1) -> Tesla V100-SXM2-16GB (GPU7) : No
> Peer access from Tesla V100-SXM2-16GB (GPU2) -> Tesla V100-SXM2-16GB (GPU0) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU2) -> Tesla V100-SXM2-16GB (GPU1) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU2) -> Tesla V100-SXM2-16GB (GPU3) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU2) -> Tesla V100-SXM2-16GB (GPU4) : No
> Peer access from Tesla V100-SXM2-16GB (GPU2) -> Tesla V100-SXM2-16GB (GPU5) : No
> Peer access from Tesla V100-SXM2-16GB (GPU2) -> Tesla V100-SXM2-16GB (GPU6) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU2) -> Tesla V100-SXM2-16GB (GPU7) : No
> Peer access from Tesla V100-SXM2-16GB (GPU3) -> Tesla V100-SXM2-16GB (GPU0) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU3) -> Tesla V100-SXM2-16GB (GPU1) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU3) -> Tesla V100-SXM2-16GB (GPU2) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU3) -> Tesla V100-SXM2-16GB (GPU4) : No
> Peer access from Tesla V100-SXM2-16GB (GPU3) -> Tesla V100-SXM2-16GB (GPU5) : No
> Peer access from Tesla V100-SXM2-16GB (GPU3) -> Tesla V100-SXM2-16GB (GPU6) : No
> Peer access from Tesla V100-SXM2-16GB (GPU3) -> Tesla V100-SXM2-16GB (GPU7) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU4) -> Tesla V100-SXM2-16GB (GPU0) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU4) -> Tesla V100-SXM2-16GB (GPU1) : No
> Peer access from Tesla V100-SXM2-16GB (GPU4) -> Tesla V100-SXM2-16GB (GPU2) : No
> Peer access from Tesla V100-SXM2-16GB (GPU4) -> Tesla V100-SXM2-16GB (GPU3) : No
> Peer access from Tesla V100-SXM2-16GB (GPU4) -> Tesla V100-SXM2-16GB (GPU5) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU4) -> Tesla V100-SXM2-16GB (GPU6) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU4) -> Tesla V100-SXM2-16GB (GPU7) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU5) -> Tesla V100-SXM2-16GB (GPU0) : No
> Peer access from Tesla V100-SXM2-16GB (GPU5) -> Tesla V100-SXM2-16GB (GPU1) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU5) -> Tesla V100-SXM2-16GB (GPU2) : No
> Peer access from Tesla V100-SXM2-16GB (GPU5) -> Tesla V100-SXM2-16GB (GPU3) : No
> Peer access from Tesla V100-SXM2-16GB (GPU5) -> Tesla V100-SXM2-16GB (GPU4) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU5) -> Tesla V100-SXM2-16GB (GPU6) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU5) -> Tesla V100-SXM2-16GB (GPU7) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU6) -> Tesla V100-SXM2-16GB (GPU0) : No
> Peer access from Tesla V100-SXM2-16GB (GPU6) -> Tesla V100-SXM2-16GB (GPU1) : No
> Peer access from Tesla V100-SXM2-16GB (GPU6) -> Tesla V100-SXM2-16GB (GPU2) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU6) -> Tesla V100-SXM2-16GB (GPU3) : No
> Peer access from Tesla V100-SXM2-16GB (GPU6) -> Tesla V100-SXM2-16GB (GPU4) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU6) -> Tesla V100-SXM2-16GB (GPU5) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU6) -> Tesla V100-SXM2-16GB (GPU7) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU7) -> Tesla V100-SXM2-16GB (GPU0) : No
> Peer access from Tesla V100-SXM2-16GB (GPU7) -> Tesla V100-SXM2-16GB (GPU1) : No
> Peer access from Tesla V100-SXM2-16GB (GPU7) -> Tesla V100-SXM2-16GB (GPU2) : No
> Peer access from Tesla V100-SXM2-16GB (GPU7) -> Tesla V100-SXM2-16GB (GPU3) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU7) -> Tesla V100-SXM2-16GB (GPU4) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU7) -> Tesla V100-SXM2-16GB (GPU5) : Yes
> Peer access from Tesla V100-SXM2-16GB (GPU7) -> Tesla V100-SXM2-16GB (GPU6) : Yes

deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 12.4, CUDA Runtime Version = 12.4, NumDevs = 8
Result = PASS
'''

def main():
    print(out)

