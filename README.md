# coffee-leaves-classification
Digital Image Processing project to classify healthy/unhealthy coffe leaves from RoCoLe dataset

## Installation

### RoCoLe dataset

The *RoCoLe* dataset used in this project is available at [RoCoLe: A robusta coffee leaf images dataset](https://data.mendeley.com/datasets/c5yvn32dzg/2).

Once you have downloaded it, extract the *RoCoLe* photos from `Annotations/RoCoLe-voc.tar.gz/export` in the `rocole_photos` directory at the same level of the cloned repository. You should have something like:

```bash
.
├── coffee-leaves-classification
└── rocole_photos
```

### Python libraries

Create a Python virtual environment and install required packages:

```bash
cd coffee-leaves-classification
python3 -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

On Debian platforms you might need to install the `venv` package at OS level in order to create virtual environments. For Debian 13 Trixie:

```bash
sudo apt install -y python3.13-venv
```

Once the Python requirements are installed, you can launch the Jupyter notebook by running:

```bash
jupyter-notebook coffee-leaves-classification.ipynb
```
