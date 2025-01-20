# pdf-summary-watcher

## TL;DR

Watches a directory for new PDF files and generates a TXT summary using `docling` and `textsum`.

## Pre-requisites

Python 3.11:
`sudo dnf install gcc gcc-c++ make git python3.11 python3.11-devel`
`sudo alternatives --install /usr/bin/python python /usr/bin/python3.11 1`
`sudo alternatives --install /usr/bin/python python /usr/bin/python3.12 2`
`sudo alternatives --config python`

CUDA:

`wget https://developer.download.nvidia.com/compute/cuda/12.6.3/local_installers/cuda-repo-fedora39-12-6-local-12.6.3_560.35.05-1.x86_64.rpm`
`sudo rpm -i cuda-repo-fedora39-12-6-local-12.6.3_560.35.05-1.x86_64.rpm`
`sudo dnf clean all`
`sudo dnf -y install cuda-toolkit-12-6`

Python venv:
`python -m venv --upgrade-deps venv`
`source venv/bin/activate`

Python libraries:
`pip install -r requirements.txt`

## Usage

`usage: pdf-summary-watcher.py [-h] --directory DIRECTORY [--model MODEL]`
