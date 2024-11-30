# gls

gls: gpu list

## Install

```
# (Recommended) Create a new python environment
python3 -m venv /tmp/your_python
source /tmp/your_python/bin/activate
```

```
pip install git+https://github.com/thamada/gls.git
```

## Upgrade

```
gls --upgrade
```


## Uninstall

```
gls --remove
```

## Available Commands

| commands           | variations                 |
|--------------------|----------------------------|
| gls                | --help, --upgrade, --remove, --csv, --version|
| nvidia-smi         | -a, .a40, .a10, .a100, .h200, .gh200, .h100, .h100nvl, .rtx2000ada, .rtx4000ada, .rtx6000ada, .rtxa6000, .rtx4060ti, .rtx4090, .rtx3070, .rtx3090, .gtx1050ti, .l40s, .l4, .v100|
| deviceQuery        | .a40, .a10, .a100, .h200, .gh200, .h100, .h100nvl, .rtx2000ada, .rtx4000ada, .rtx6000ada, .rtxa6000, .rtx4060ti, .rtx4090, .rtx3070, .rtx3090, .gtx1050ti, .l40s, .l4, .v100, .mi300x |
| rocm-smi           | -a                         |
| rocminfo           |                            |
| setDevice          |                            |

## Demo

[![asciicast](https://asciinema.org/a/TXn0LrBbp59YItJhZk87GDcit.svg)](https://asciinema.org/a/TXn0LrBbp59YItJhZk87GDcit)

[![asciicast](https://asciinema.org/a/s6HwspuwfToy6TrlxwsnNNDkS.svg)](https://asciinema.org/a/s6HwspuwfToy6TrlxwsnNNDkS)

Enjoy gls!
