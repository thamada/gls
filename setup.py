from setuptools import setup, find_packages

setup(
    name="nvidia-smi-simulator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # 依存パッケージをここに記述
    ],
    entry_points={
        'console_scripts': [
            'nvidia-smi=package.H100SXMx8_smi:main',
            'deviceQuery=package.H100SXMx8_deviceQuery:main',

            'nvidia-smi.h100x8=package.H100SXMx8_smi:main',
            'deviceQuery.h100x8=package.H100SXMx8_deviceQuery:main',

            'nvidia-smi.rtx2000ada=package.RTX2000Ada_smi:main',
            'deviceQuery.rtx2000ada=package.RTX2000Ada_deviceQuery:main',

            'nvidia-smi.rtx4000ada=package.RTX4000Ada_smi:main',
            'deviceQuery.rtx4000ada=package.RTX4000Ada_deviceQuery:main',

            'nvidia-smi.rtx4060ti=package.RTX4060Ti_smi:main',
            'deviceQuery.rtx4060ti=package.RTX4060Ti_deviceQuery:main',

            'nvidia-smi.rtx4090=package.RTX4090_smi:main',  # 8 devices
            'deviceQuery.rtx4090=package.RTX4090_deviceQuery:main', # 8 devices

            'rocm-smi=package.MI300X_smi:main',
            'deviceQuery.mi300x=package.MI300X_deviceQuery:main',
        ],
    },
)
