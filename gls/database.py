#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# GPUのデータを辞書リストで定義
gpu_data = [
    {
        'vendor': 'AMD',
        'product': 'MI300X',
        'tdp': 750, # Watt
        'vram_size': 192, # GB
        'vram_bw': 10649.6, # GB/s: (10.4 [GHz])[Gbps]  * 8192-bits / 8.0 [bits/byte]
        'vram_ecc': False, 
        'n_sp_core': 19456,
        'n_mp': 304, # number of MIMD-processors (SM for Nvidia, CU for AMD)
        'gpu_clock': 2100.00, # MHz
        'mem_clock': 10400.0, # MHz (1300 MHz * 8)
        'mem_bus_width': 8192, # Memory Bus Width (bits)
        'n_tensor_core': 1216,
#       'gen_tensor_core': ,
        'tflops_fp16': 653.7216, # TFLOP/s (8:1)
        'tflops_fp32': 81.7152, # TFLOP/s
        'tflops_fp64': 81.7152, # TFLOP/s (1:1)
#       'tflops_fp8_tensor': , # TFLOP/s (Effective FP8 TFLOP/s)
#       'tflops_fp8_tensor_sparse': , # TFLOP/s (Effective FP8 TFLOP/s using the sparsity feature)
        'system_interface': 'PCIe 5.0 x16', 
        'gpu_chip': 'Aqua Vanjaram',
        'gpu_variant': 'gfx940',
        'gpu_arch': 'CDNA 3.0',
        'url': 'https://www.techpowerup.com/gpu-specs/radeon-instinct-mi300x.c4179'
    },
    {
        'vendor': 'AMD',
        'product': 'RX 7900 XTX',
        'tdp': 355, # Watt
        'vram_size': 24, # GB
        'vram_bw': 960.0, # GB/s: (10.0 [GHz] * 2)[Gbps]  * 384-bits / 8.0 [bits/byte]
        'vram_ecc': False, 
        'n_sp_core': 6144,
        'n_mp': 96, # number of MIMD-processors (SM for Nvidia, CU for AMD)
        'gpu_clock': 2482.00, # MHz
        'mem_clock': 10000.0, # MHz (1250 MHz * 8)
        'mem_bus_width': 384, # Memory Bus Width (bits)
#       'n_tensor_core': ,
#       'gen_tensor_core': ,
        'tflops_fp16': 122.8, # TFLOP/s (2:1)
        'tflops_fp32': 61.39, # TFLOP/s
#       'tflops_fp8_tensor': , # TFLOP/s (Effective FP8 TFLOP/s)
#       'tflops_fp8_tensor_sparse': , # TFLOP/s (Effective FP8 TFLOP/s using the sparsity feature)
        'system_interface': 'PCIe 4.0 x16', 
        'gpu_chip': 'Navi 31 (Plum Bonito)',
        'gpu_variant': 'gfx1100',
        'gpu_arch': 'RDNA 3.0',
        'url': 'https://www.techpowerup.com/gpu-specs/radeon-rx-7900-xtx.c3941'
    },

    {
        'vendor': 'NVIDIA',
        'product': 'L4',
        'tdp': 72, # Watt
        'vram_size': 24, # GB
        'vram_bw': 300.048, # GB/s: (6.251 [GHz] * 2)[Gbps]  * 192-bits / 8.0 [bits/byte]
        'vram_ecc': True,
        'n_sp_core': 7424,
        'n_mp': 58, # number of MIMD-processors (SM for Nvidia, CU for AMD)
        'gpu_clock': 2040, # MHz
        'mem_clock': 6251, # MHz
        'mem_bus_width': 192, # Memory Bus Width (bits)
        'n_tensor_core': 240,
        'gen_tensor_core': 4,
        'tflops_fp16': 30.28992, # TFLOP/s
        'tflops_fp32': 30.28992, # TFLOP/s
        'tflops_fp8_tensor': 242.5, # TFLOP/s (Effective FP8 TFLOP/s)
        'tflops_fp8_tensor_sparse': 485, # TFLOP/s (Effective FP8 TFLOP/s using the sparsity feature)
        'system_interface': 'PCIe 4.0 x16',
        'gpu_chip': 'AD104',
        'gpu_variant': 'AD104-???-A1',
        'gpu_arch': 'Ada Lovelace',
        'url': 'https://www.techpowerup.com/gpu-specs/l4.c4091'
    },

    {
        'vendor': 'NVIDIA',
        'product': 'L40S',
        'tdp': 350, # Watt
        'vram_size': 48, # GB
        'vram_bw': 864.096, # GB/s: (9.001 [GHz] * 2)[Gbps]  * 384-bits / 8.0 [bits/byte]
        'vram_ecc': True,
        'n_sp_core': 18176,
        'n_mp': 142, # number of MIMD-processors (SM for Nvidia, CU for AMD)
        'gpu_clock': 2520, # MHz
        'mem_clock': 9001, # MHz
        'mem_bus_width': 384, # Memory Bus Width (bits)
        'n_tensor_core': 568,
        'gen_tensor_core': 4,
        'tflops_fp16': 91.607, # TFLOP/s
        'tflops_fp32': 91.607, # TFLOP/s
        'tflops_fp8_tensor': 733, # TFLOP/s (Effective FP8 TFLOP/s)
        'tflops_fp8_tensor_sparse': 1466, # TFLOP/s (Effective FP8 TFLOP/s using the sparsity feature)
        'system_interface': 'PCIe 4.0 x16',
        'gpu_chip': 'AD102',
        'gpu_variant': 'AD102-???-A1',
        'gpu_arch': 'Ada Lovelace',
        'url': 'https://www.techpowerup.com/gpu-specs/l40s.c4173'
    },

    {
        'vendor': 'NVIDIA',
        'product': 'H100 NVL',
        'tdp': 310, # Watt
        'vram_size': 94, # GB (95346 MB)
        'vram_bw': 4022.784, # GB/s: (2.619 [GHz] * 2)[Gbps]  * 6144-bits / 8.0 [bits/byte]
        'vram_ecc': True, 
        'n_sp_core': 16896,
        'n_mp': 132, # number of MIMD-processors (SM for Nvidia, CU for AMD)
        'gpu_clock': 1785, # MHz
        'mem_clock': 2619, # MHz
        'mem_bus_width': 6144, # Memory Bus Width (bits)
        'n_tensor_core': 528,
        'gen_tensor_core': 4,
        'tflops_fp16': 241.27488, # TFLOP/s (4:1)
        'tflops_fp32': 60.31872, # TFLOP/s
        'tflops_fp8_tensor': 1979, # TFLOP/s (Effective FP8 TFLOP/s)
        'tflops_fp8_tensor_sparse': 3958, # TFLOP/s (Effective FP8 TFLOP/s using the sparsity feature)
        'system_interface': 'PCIe 5.0 x16', 
        'gpu_chip': 'GH100',
        'gpu_variant': 'GH100 NVL 94GB HBM3',
        'gpu_arch': 'Hopper',
        'url': ''
    },

    {
        'vendor': 'NVIDIA',
        'product': 'H100 SXM',
        'tdp': 700, # Watt
        'vram_size': 80, # GB
        'vram_bw': 3352.32, # GB/s: (2.619 [GHz] * 2)[Gbps]  * 5120-bits / 8.0 [bits/byte]
        'vram_ecc': True, 
        'n_sp_core': 16896,
        'n_mp': 132, # number of MIMD-processors (SM for Nvidia, CU for AMD)
        'gpu_clock': 1980, # MHz
        'mem_clock': 2619, # MHz
        'mem_bus_width': 5120, # Memory Bus Width (bits)
        'n_tensor_core': 528,
        'gen_tensor_core': 4,
        'tflops_fp16': 267.63264, # TFLOP/s (4:1)
        'tflops_fp32': 66.90816, # TFLOP/s
        'tflops_fp8_tensor': 1979, # TFLOP/s (Effective FP8 TFLOP/s)
        'tflops_fp8_tensor_sparse': 3958, # TFLOP/s (Effective FP8 TFLOP/s using the sparsity feature)
        'system_interface': 'PCIe 5.0 x16', 
        'gpu_chip': 'GH100',
        'gpu_variant': 'GH100 80GB HBM3 SXM5',
        'gpu_arch': 'Hopper',
        'url': 'https://www.techpowerup.com/gpu-specs/h100-sxm5-80-gb.c3900'
    },
    {
        'vendor': 'NVIDIA',
        'product': 'GTX 1050 Ti',
        'tdp': 75, # Watt
        'vram_size': 4, # GB
        'vram_bw': 112.128, # GB/s = (3.504 [GHz] * 2)[Gbps]  * 128-bits / 8.0 [bits/byte]
        'vram_ecc': False,
        'n_sp_core': 768,
        'n_mp': 6, # number of MIMD-processors (SM for Nvidia, CU for AMD)
        'gpu_clock': 1392, # MHz
        'mem_clock': 3504, # MHz
        'mem_bus_width': 128, # Memory Bus Width (bits)
        'n_tensor_core': 0,
        'gen_tensor_core': 0,
        'tflops_fp16': 0.033408, # TFLOP/s (1:64!?)
        'tflops_fp32': 2.138112, # TFLOP/s
        'tflops_fp8_tensor': 0, # TFLOP/s (Effective FP8 TFLOP/s)
        'tflops_fp8_tensor_sparse': 0, # TFLOP/s (Effective FP8 TFLOP/s using the sparsity feature)
        'system_interface': 'PCIe 3.0 x16', 
        'gpu_chip': 'GP107',
        'gpu_variant': 'GP107-400-A1',
        'gpu_arch': 'Pascal',
        'url': 'https://www.techpowerup.com/gpu-specs/geforce-gtx-1050-ti.c2885'
    },
    {
        'vendor': 'NVIDIA',
        'product': 'GTX 1080 Ti',
        'tdp': 250, # Watt
        'vram_size': 11, # GB
        'vram_bw': 484.0, # GB/s = (5.5 [GHz] * 2)[Gbps]  * 352-bits / 8.0 [bits/byte]
        'vram_ecc': False,
        'n_sp_core': 3584,
        'n_mp': 28, # number of MIMD-processors (SM for Nvidia, CU for AMD)
        'gpu_clock': 1582, # MHz
        'mem_clock': 5500, # MHz
        'mem_bus_width': 352, # Memory Bus Width (bits)
        'n_tensor_core': 0,
        'gen_tensor_core': 0,
        'tflops_fp16': 0.1171875, # TFLOP/s (1:64!?)
        'tflops_fp32': 11.339776, # TFLOP/s
        'tflops_fp8_tensor': 0, # TFLOP/s (Effective FP8 TFLOP/s)
        'tflops_fp8_tensor_sparse': 0, # TFLOP/s (Effective FP8 TFLOP/s using the sparsity feature)
        'system_interface': 'PCIe 3.0 x16', 
        'gpu_chip': 'GP102',
        'gpu_variant': 'GP102-350-K1-A1',
        'gpu_arch': 'Pascal',
        'url': 'https://www.techpowerup.com/gpu-specs/nvidia-gp102.g798'
    },
    {
        'vendor': 'NVIDIA',
        'product': 'RTX 4090',
        'tdp': 450, # Watt
        'vram_size': 24, # GB
        'vram_bw': 1008.096, # GB/s: (10.501 [GHz] * 2)[Gbps]  * 384-bits / 8.0 [bits/byte]
        'vram_ecc': False, 
        'n_sp_core': 16384,
        'n_mp': 128, # number of MIMD-processors (SM for Nvidia, CU for AMD)
        'gpu_clock': 2520, # MHz
        'mem_clock': 10501, # MHz
        'mem_bus_width': 384, # Memory Bus Width (bits)
        'n_tensor_core': 512,
        'gen_tensor_core': 4,
        'tflops_fp16': 82.57536, # TFLOP/s
        'tflops_fp32': 82.57536, # TFLOP/s
        'tflops_fp8_tensor': 660.5, # TFLOP/s (Effective FP8 TFLOP/s)
        'tflops_fp8_tensor_sparse': 1321, # TFLOP/s (Effective FP8 TFLOP/s using the sparsity feature)
        'system_interface': 'PCIe 4.0 x16', 
        'gpu_chip': 'AD102',
        'gpu_variant': 'AD102-300-A1',
        'gpu_arch': 'Ada Lovelace',
        'url': 'https://www.techpowerup.com/gpu-specs/geforce-rtx-4090.c3889'
    },
    {
        'vendor': 'NVIDIA',
        'product': 'RTX 4060 Ti',
        'tdp': 165, # Watt
        'vram_size': 16, # GB
        'vram_bw': 288.032, # GB/s = (9.001 [GHz] * 2)[Gbps]  * 128-bits / 8.0 [bits/byte]
        'vram_ecc': False, 
        'n_sp_core': 4352,
        'n_mp': 34, # number of MIMD-processors (SM for Nvidia, CU for AMD)
        'gpu_clock': 2610, # MHz
        'mem_clock': 9001, # MHz
        'mem_bus_width': 128, # Memory Bus Width (bits)
        'n_tensor_core': 136,
        'gen_tensor_core': 4,
        'tflops_fp16': 22.71744, # TFLOP/s
        'tflops_fp32': 22.71744, # TFLOP/s
        'tflops_fp8_tensor': 176.5, # TFLOP/s (Effective FP8 TFLOP/s)
        'tflops_fp8_tensor_sparse': 353, # TFLOP/s (Effective FP8 TFLOP/s using the sparsity feature)
        'system_interface': 'PCIe 4.0 x8', 
        'gpu_chip': 'AD106',
        'gpu_variant': 'AD106-351-A1',
        'gpu_arch': 'Ada Lovelace',
        'url': 'https://www.techpowerup.com/308795/nvidia-explains-geforce-rtx-40-series-vram-functionality'
    },
    {
        'vendor': 'NVIDIA',
        'product': 'RTX 2000 Ada',
        'tdp': 70, # Watt
        'vram_size': 16, # GB
        'vram_bw': 224.032, # GB/s = (7.001 [GHz] * 2)[Gbps]  * 128-bits / 8.0 [bits/byte]
        'vram_ecc': False, 
        'n_sp_core': 2816,
        'n_mp': 22, # number of MIMD-processors (SM for Nvidia, CU for AMD)
        'gpu_clock': 2130, # MHz
        'mem_clock': 7001, # MHz
        'mem_bus_width': 128, # Memory Bus Width (bits)
        'n_tensor_core': 88,
        'gen_tensor_core': 4,
        'tflops_fp16': 11.99616, # TFLOP/s
        'tflops_fp32': 11.99616, # TFLOP/s
        'tflops_fp8_tensor': 96.0, # TFLOP/s (Effective FP8 TFLOP/s)
        'tflops_fp8_tensor_sparse': 191.9, # TFLOP/s (Effective FP8 TFLOP/s using the sparsity feature)
        'system_interface': 'PCIe 4.0 x8', 
        'gpu_chip': 'AD107',
        'gpu_variant': 'AD107-???-??',
        'gpu_arch': 'Ada Lovelace',
        'url': 'https://resources.nvidia.com/en-us-briefcase-for-datasheets/proviz-rtx-2000-ada'
    },
    {
        'vendor': 'NVIDIA',
        'product': 'RTX 4000 Ada',
        'tdp': 130, # Watt
        'vram_size': 20, # GB
        'vram_bw': 360.04, # GB/s = (9.001 [GHz] * 2)[Gbps]  * 160-bits / 8.0 [bits/byte]
        'vram_ecc': False,
        'n_sp_core': 6144,
        'n_mp': 48, # number of MIMD-processors (SM for Nvidia, CU for AMD)
        'gpu_clock': 2175, # MHz
        'mem_clock': 9001, # MHz
        'mem_bus_width': 160, # Memory Bus Width (bits)
        'n_tensor_core': 192,
        'gen_tensor_core': 4,
        'tflops_fp16': 26.7264, # TFLOP/s
        'tflops_fp32': 26.7264, # TFLOP/s
        'tflops_fp8_tensor': 153.4, # TFLOP/s (Effective FP8 TFLOP/s)
        'tflops_fp8_tensor_sparse': 306.8, # TFLOP/s (Effective FP8 TFLOP/s using the sparsity feature)
        'system_interface': 'PCIe 4.0 x16', 
        'gpu_chip': 'AD104',
        'gpu_variant': 'AD104-???-??',
        'gpu_arch': 'Ada Lovelace',
        'url': 'https://www.techpowerup.com/gpu-specs/rtx-4000-ada-generation.c4171'
    },
    {
        'vendor': 'NVIDIA',
        'product': 'RTX 6000 Ada',
        'tdp': 300, # Watt
        'vram_size': 48, # GB
        'vram_bw': 960.096, # GB/s = (10.001 [GHz] * 2)[Gbps]  * 384-bits / 8.0 [bits/byte]
        'vram_ecc': False,
        'n_sp_core': 18176,
        'n_mp': 142, # number of MIMD-processors (SM for Nvidia, CU for AMD)
        'gpu_clock': 2505, # MHz
        'mem_clock': 10001, # MHz
        'mem_bus_width': 384, # Memory Bus Width (bits)
        'n_tensor_core': 568,
        'gen_tensor_core': 4,
        'tflops_fp16': 91.06176, # TFLOP/s (1:1)
        'tflops_fp32': 91.06176, # TFLOP/s
        'tflops_fp8_tensor': 728.5, # TFLOP/s (Effective FP8 TFLOP/s) ???
        'tflops_fp8_tensor_sparse': 1457, # TFLOP/s (Effective FP8 TFLOP/s using the sparsity feature) ???
        'system_interface': 'PCIe 4.0 x16', 
        'gpu_chip': 'AD102',
        'gpu_variant': 'AD102',
        'gpu_arch': 'Ada Lovelace',
        'url': 'https://www.techpowerup.com/gpu-specs/rtx-6000-ada-generation.c3933'
    }
]
