import re
from setuptools import setup, find_packages

'''
# バージョン情報を取得する関数
# === exec()を使用するため廃止 ===
def get_version():
    version = {}

    # exec(fp.read(), version):
    # ファイルから読み込んだコードを実行し、その実行コンテキスト（名前空間）として version 辞書を使用します。
    # これにより、コード内で定義されたすべての変数が version 辞書に格納されます。
    # (ただの小技です)
    with open("gls/__init__.py") as fp:
        exec(fp.read(), version)

    vstr = version['__version__']
    print ('version=', vstr)
    return vstr
'''

# バージョン情報を取得する関数
# === exec()を使用しないバージョン ===
#  (*) コードは読みにくいので、それを避けたい 場合は上記のexec()使用バージョンに変更してください
def get_version():
    with open('gls/__init__.py', 'r') as f:
        content = f.read()
    version_match = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', content, re.MULTILINE)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


setup(
    name="gls",
    version=get_version(),  # バージョン情報をセット
    packages=find_packages(),
    install_requires=[
        # 依存パッケージとそのバージョンを指定
        "pandas>=2.2.3",
        "tabulate>=0.9.0",
        "colorama>=0.4.6",
    ],
    entry_points={
        'console_scripts': [
            'nvidia-smi.gtx1050ti=gls.GTX1050Ti_smi:main',
            'deviceQuery.gtx1050ti=gls.GTX1050Ti_deviceQuery:main',

            'nvidia-smi=gls.H100SXMx8_smi:main',
            'deviceQuery=gls.H100SXMx8_deviceQuery:main',

            'nvidia-smi.h100=gls.H100SXMx8_smi:main',
            'deviceQuery.h100=gls.H100SXMx8_deviceQuery:main',

            'nvidia-smi.h100nvl=gls.H100NVLx2_smi:main', # 2 devices
            'deviceQuery.h100nvl=gls.H100NVLx2_deviceQuery:main', # 2 devices

            'nvidia-smi.rtx2000ada=gls.RTX2000Ada_smi:main',
            'deviceQuery.rtx2000ada=gls.RTX2000Ada_deviceQuery:main',

            'nvidia-smi.rtx4000ada=gls.RTX4000Ada_smi:main',
            'deviceQuery.rtx4000ada=gls.RTX4000Ada_deviceQuery:main',

            'nvidia-smi.rtx6000ada=gls.RTX6000Ada_x8_smi:main', # 8 devices
            'deviceQuery.rtx6000ada=gls.RTX6000Ada_x8_deviceQuery:main', # 8 devices

            'nvidia-smi.rtx4060ti=gls.RTX4060Ti_smi:main',
            'deviceQuery.rtx4060ti=gls.RTX4060Ti_deviceQuery:main',

            'nvidia-smi.rtx4090=gls.RTX4090_smi:main', # 8 devices
            'deviceQuery.rtx4090=gls.RTX4090_deviceQuery:main', # 8 devices

            'nvidia-smi.l40s=gls.L40S_smi:main',
            'deviceQuery.l40s=gls.L40S_deviceQuery:main',

            'nvidia-smi.l4=gls.L4_smi:main',
            'deviceQuery.l4=gls.L4_deviceQuery:main',

            'nvidia-smi.a100=gls.A100SXMx4_smi:main',  # 4 devices
            'deviceQuery.a100=gls.A100SXMx4_deviceQuery:main', # 4 devices

            'nvidia-smi.rtx3090=gls.RTX3090_smi:main',  # 2 devices
            'deviceQuery.rtx3090=gls.RTX3090_deviceQuery:main', # 2 devices

            'nvidia-smi.a40=gls.A40x10_smi:main',  # 10 devices
            'deviceQuery.a40=gls.A40x10_deviceQuery:main', # 10 devices

            'rocm-smi=gls.MI300X_x4_smi:main', # 4 devices
            'rocminfo=gls.MI300X_x4_rocminfo:main', # 4 devices
            'deviceQuery.mi300x=gls.MI300X_x4_deviceQuery:main', # 4 devices

            # gls: gpu list
            'gls=gls.gls:main', 

        ],
    },
)
