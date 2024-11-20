#!/usr/bin/env python3

out = '''
deviceQuery Starting...

 CUDA Device Query (Runtime API) version (CUDART static linking)

Detected 9 CUDA Capable device(s)

Device 0: "NVIDIA RTX A6000"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    8.6
  Total amount of global memory:                 45619 MBytes (47834660864 bytes)
  (084) Multiprocessors, (128) CUDA Cores/MP:    10752 CUDA Cores
  GPU Max Clock rate:                            1800 MHz (1.80 GHz)
  Memory Clock rate:                             8001 Mhz
  Memory Bus Width:                              384-bit
  L2 Cache Size:                                 6291456 bytes
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
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 79 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 1: "NVIDIA RTX A6000"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    8.6
  Total amount of global memory:                 45619 MBytes (47834660864 bytes)
  (084) Multiprocessors, (128) CUDA Cores/MP:    10752 CUDA Cores
  GPU Max Clock rate:                            1800 MHz (1.80 GHz)
  Memory Clock rate:                             8001 Mhz
  Memory Bus Width:                              384-bit
  L2 Cache Size:                                 6291456 bytes
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
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 82 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 2: "NVIDIA RTX A6000"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    8.6
  Total amount of global memory:                 45619 MBytes (47834660864 bytes)
  (084) Multiprocessors, (128) CUDA Cores/MP:    10752 CUDA Cores
  GPU Max Clock rate:                            1800 MHz (1.80 GHz)
  Memory Clock rate:                             8001 Mhz
  Memory Bus Width:                              384-bit
  L2 Cache Size:                                 6291456 bytes
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
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 83 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 3: "NVIDIA RTX A6000"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    8.6
  Total amount of global memory:                 45619 MBytes (47834660864 bytes)
  (084) Multiprocessors, (128) CUDA Cores/MP:    10752 CUDA Cores
  GPU Max Clock rate:                            1800 MHz (1.80 GHz)
  Memory Clock rate:                             8001 Mhz
  Memory Bus Width:                              384-bit
  L2 Cache Size:                                 6291456 bytes
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
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 87 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 4: "NVIDIA RTX A6000"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    8.6
  Total amount of global memory:                 45619 MBytes (47834660864 bytes)
  (084) Multiprocessors, (128) CUDA Cores/MP:    10752 CUDA Cores
  GPU Max Clock rate:                            1800 MHz (1.80 GHz)
  Memory Clock rate:                             8001 Mhz
  Memory Bus Width:                              384-bit
  L2 Cache Size:                                 6291456 bytes
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
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 206 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 5: "NVIDIA RTX A6000"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    8.6
  Total amount of global memory:                 45619 MBytes (47834660864 bytes)
  (084) Multiprocessors, (128) CUDA Cores/MP:    10752 CUDA Cores
  GPU Max Clock rate:                            1800 MHz (1.80 GHz)
  Memory Clock rate:                             8001 Mhz
  Memory Bus Width:                              384-bit
  L2 Cache Size:                                 6291456 bytes
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
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 209 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 6: "NVIDIA RTX A6000"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    8.6
  Total amount of global memory:                 45619 MBytes (47834660864 bytes)
  (084) Multiprocessors, (128) CUDA Cores/MP:    10752 CUDA Cores
  GPU Max Clock rate:                            1800 MHz (1.80 GHz)
  Memory Clock rate:                             8001 Mhz
  Memory Bus Width:                              384-bit
  L2 Cache Size:                                 6291456 bytes
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
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 210 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 7: "NVIDIA RTX A6000"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    8.6
  Total amount of global memory:                 45619 MBytes (47834660864 bytes)
  (084) Multiprocessors, (128) CUDA Cores/MP:    10752 CUDA Cores
  GPU Max Clock rate:                            1800 MHz (1.80 GHz)
  Memory Clock rate:                             8001 Mhz
  Memory Bus Width:                              384-bit
  L2 Cache Size:                                 6291456 bytes
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
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 213 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

Device 8: "NVIDIA RTX A6000"
  CUDA Driver Version / Runtime Version          12.4 / 12.4
  CUDA Capability Major/Minor version number:    8.6
  Total amount of global memory:                 45619 MBytes (47834660864 bytes)
  (084) Multiprocessors, (128) CUDA Cores/MP:    10752 CUDA Cores
  GPU Max Clock rate:                            1800 MHz (1.80 GHz)
  Memory Clock rate:                             8001 Mhz
  Memory Bus Width:                              384-bit
  L2 Cache Size:                                 6291456 bytes
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
  Device has ECC support:                        Enabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 214 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >
> Peer access from NVIDIA RTX A6000 (GPU0) -> NVIDIA RTX A6000 (GPU1) : Yes
> Peer access from NVIDIA RTX A6000 (GPU0) -> NVIDIA RTX A6000 (GPU2) : Yes
> Peer access from NVIDIA RTX A6000 (GPU0) -> NVIDIA RTX A6000 (GPU3) : Yes
> Peer access from NVIDIA RTX A6000 (GPU0) -> NVIDIA RTX A6000 (GPU4) : Yes
> Peer access from NVIDIA RTX A6000 (GPU0) -> NVIDIA RTX A6000 (GPU5) : Yes
> Peer access from NVIDIA RTX A6000 (GPU0) -> NVIDIA RTX A6000 (GPU6) : Yes
> Peer access from NVIDIA RTX A6000 (GPU0) -> NVIDIA RTX A6000 (GPU7) : Yes
> Peer access from NVIDIA RTX A6000 (GPU0) -> NVIDIA RTX A6000 (GPU8) : Yes
> Peer access from NVIDIA RTX A6000 (GPU1) -> NVIDIA RTX A6000 (GPU0) : Yes
> Peer access from NVIDIA RTX A6000 (GPU1) -> NVIDIA RTX A6000 (GPU2) : Yes
> Peer access from NVIDIA RTX A6000 (GPU1) -> NVIDIA RTX A6000 (GPU3) : Yes
> Peer access from NVIDIA RTX A6000 (GPU1) -> NVIDIA RTX A6000 (GPU4) : Yes
> Peer access from NVIDIA RTX A6000 (GPU1) -> NVIDIA RTX A6000 (GPU5) : Yes
> Peer access from NVIDIA RTX A6000 (GPU1) -> NVIDIA RTX A6000 (GPU6) : Yes
> Peer access from NVIDIA RTX A6000 (GPU1) -> NVIDIA RTX A6000 (GPU7) : Yes
> Peer access from NVIDIA RTX A6000 (GPU1) -> NVIDIA RTX A6000 (GPU8) : Yes
> Peer access from NVIDIA RTX A6000 (GPU2) -> NVIDIA RTX A6000 (GPU0) : Yes
> Peer access from NVIDIA RTX A6000 (GPU2) -> NVIDIA RTX A6000 (GPU1) : Yes
> Peer access from NVIDIA RTX A6000 (GPU2) -> NVIDIA RTX A6000 (GPU3) : Yes
> Peer access from NVIDIA RTX A6000 (GPU2) -> NVIDIA RTX A6000 (GPU4) : Yes
> Peer access from NVIDIA RTX A6000 (GPU2) -> NVIDIA RTX A6000 (GPU5) : Yes
> Peer access from NVIDIA RTX A6000 (GPU2) -> NVIDIA RTX A6000 (GPU6) : Yes
> Peer access from NVIDIA RTX A6000 (GPU2) -> NVIDIA RTX A6000 (GPU7) : Yes
> Peer access from NVIDIA RTX A6000 (GPU2) -> NVIDIA RTX A6000 (GPU8) : Yes
> Peer access from NVIDIA RTX A6000 (GPU3) -> NVIDIA RTX A6000 (GPU0) : Yes
> Peer access from NVIDIA RTX A6000 (GPU3) -> NVIDIA RTX A6000 (GPU1) : Yes
> Peer access from NVIDIA RTX A6000 (GPU3) -> NVIDIA RTX A6000 (GPU2) : Yes
> Peer access from NVIDIA RTX A6000 (GPU3) -> NVIDIA RTX A6000 (GPU4) : Yes
> Peer access from NVIDIA RTX A6000 (GPU3) -> NVIDIA RTX A6000 (GPU5) : Yes
> Peer access from NVIDIA RTX A6000 (GPU3) -> NVIDIA RTX A6000 (GPU6) : Yes
> Peer access from NVIDIA RTX A6000 (GPU3) -> NVIDIA RTX A6000 (GPU7) : Yes
> Peer access from NVIDIA RTX A6000 (GPU3) -> NVIDIA RTX A6000 (GPU8) : Yes
> Peer access from NVIDIA RTX A6000 (GPU4) -> NVIDIA RTX A6000 (GPU0) : Yes
> Peer access from NVIDIA RTX A6000 (GPU4) -> NVIDIA RTX A6000 (GPU1) : Yes
> Peer access from NVIDIA RTX A6000 (GPU4) -> NVIDIA RTX A6000 (GPU2) : Yes
> Peer access from NVIDIA RTX A6000 (GPU4) -> NVIDIA RTX A6000 (GPU3) : Yes
> Peer access from NVIDIA RTX A6000 (GPU4) -> NVIDIA RTX A6000 (GPU5) : Yes
> Peer access from NVIDIA RTX A6000 (GPU4) -> NVIDIA RTX A6000 (GPU6) : Yes
> Peer access from NVIDIA RTX A6000 (GPU4) -> NVIDIA RTX A6000 (GPU7) : Yes
> Peer access from NVIDIA RTX A6000 (GPU4) -> NVIDIA RTX A6000 (GPU8) : Yes
> Peer access from NVIDIA RTX A6000 (GPU5) -> NVIDIA RTX A6000 (GPU0) : Yes
> Peer access from NVIDIA RTX A6000 (GPU5) -> NVIDIA RTX A6000 (GPU1) : Yes
> Peer access from NVIDIA RTX A6000 (GPU5) -> NVIDIA RTX A6000 (GPU2) : Yes
> Peer access from NVIDIA RTX A6000 (GPU5) -> NVIDIA RTX A6000 (GPU3) : Yes
> Peer access from NVIDIA RTX A6000 (GPU5) -> NVIDIA RTX A6000 (GPU4) : Yes
> Peer access from NVIDIA RTX A6000 (GPU5) -> NVIDIA RTX A6000 (GPU6) : Yes
> Peer access from NVIDIA RTX A6000 (GPU5) -> NVIDIA RTX A6000 (GPU7) : Yes
> Peer access from NVIDIA RTX A6000 (GPU5) -> NVIDIA RTX A6000 (GPU8) : Yes
> Peer access from NVIDIA RTX A6000 (GPU6) -> NVIDIA RTX A6000 (GPU0) : Yes
> Peer access from NVIDIA RTX A6000 (GPU6) -> NVIDIA RTX A6000 (GPU1) : Yes
> Peer access from NVIDIA RTX A6000 (GPU6) -> NVIDIA RTX A6000 (GPU2) : Yes
> Peer access from NVIDIA RTX A6000 (GPU6) -> NVIDIA RTX A6000 (GPU3) : Yes
> Peer access from NVIDIA RTX A6000 (GPU6) -> NVIDIA RTX A6000 (GPU4) : Yes
> Peer access from NVIDIA RTX A6000 (GPU6) -> NVIDIA RTX A6000 (GPU5) : Yes
> Peer access from NVIDIA RTX A6000 (GPU6) -> NVIDIA RTX A6000 (GPU7) : Yes
> Peer access from NVIDIA RTX A6000 (GPU6) -> NVIDIA RTX A6000 (GPU8) : Yes
> Peer access from NVIDIA RTX A6000 (GPU7) -> NVIDIA RTX A6000 (GPU0) : Yes
> Peer access from NVIDIA RTX A6000 (GPU7) -> NVIDIA RTX A6000 (GPU1) : Yes
> Peer access from NVIDIA RTX A6000 (GPU7) -> NVIDIA RTX A6000 (GPU2) : Yes
> Peer access from NVIDIA RTX A6000 (GPU7) -> NVIDIA RTX A6000 (GPU3) : Yes
> Peer access from NVIDIA RTX A6000 (GPU7) -> NVIDIA RTX A6000 (GPU4) : Yes
> Peer access from NVIDIA RTX A6000 (GPU7) -> NVIDIA RTX A6000 (GPU5) : Yes
> Peer access from NVIDIA RTX A6000 (GPU7) -> NVIDIA RTX A6000 (GPU6) : Yes
> Peer access from NVIDIA RTX A6000 (GPU7) -> NVIDIA RTX A6000 (GPU8) : Yes
> Peer access from NVIDIA RTX A6000 (GPU8) -> NVIDIA RTX A6000 (GPU0) : Yes
> Peer access from NVIDIA RTX A6000 (GPU8) -> NVIDIA RTX A6000 (GPU1) : Yes
> Peer access from NVIDIA RTX A6000 (GPU8) -> NVIDIA RTX A6000 (GPU2) : Yes
> Peer access from NVIDIA RTX A6000 (GPU8) -> NVIDIA RTX A6000 (GPU3) : Yes
> Peer access from NVIDIA RTX A6000 (GPU8) -> NVIDIA RTX A6000 (GPU4) : Yes
> Peer access from NVIDIA RTX A6000 (GPU8) -> NVIDIA RTX A6000 (GPU5) : Yes
> Peer access from NVIDIA RTX A6000 (GPU8) -> NVIDIA RTX A6000 (GPU6) : Yes
> Peer access from NVIDIA RTX A6000 (GPU8) -> NVIDIA RTX A6000 (GPU7) : Yes

deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 12.4, CUDA Runtime Version = 12.4, NumDevs = 9
Result = PASS
'''

def main():
    print(out)

