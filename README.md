# coffee-leaves-classification

![](./docs/src/images/coffee_beans.png)

A Digital Image Processing project to detect coffee leaves infected by rust and their level of affectation. The state of the coffee leaves is classified as *healthy* or *unhealthy*, and a category is given for the latter: *rust_level_1*, *rust_level_2*, *rust_level_3* or *rust_level_4*. The algorithm implements color segmentation leveraging on the Hue channel from the [HSV color space](https://en.wikipedia.org/wiki/HSL_and_HSV).

This project is based on the work made by [Jorge Parraga-Alava](mailto:jorge.parraga@usach.cl), Kevin Cusme, Angélica Loor and Esneider Santander, published in [RoCoLe: A robusta coffee leaf images dataset for evaluation of machine learning based methods in plant diseases recognition](https://doi.org/10.1016/j.dib.2019.104414), publicly available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

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
