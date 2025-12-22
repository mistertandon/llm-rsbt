How to run ipynb in VS Code

http://localhost:8888/lab?token=0ec5c12b0f34bb90dce6932d0aa8637f895cbd5a0635f662

### Install conda and run below command to set up environment

> conda env create -f conda_env.yml
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126

---

## VAE
https://github.com/pytorch/examples/blob/main/vae/main.py

---

### Confirm that an NVIDIA GPU exists

lspci | grep -i nvidia