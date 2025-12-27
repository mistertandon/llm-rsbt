How to run ipynb in VS Code

http://localhost:8888/lab?token=f4646a3546c9fa59c84b75c781195b66b05e54d7aabc1014

### Install conda and run below command to set up environment

> conda env create -f conda_env.yml
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126

---

## VAE
https://github.com/pytorch/examples/blob/main/vae/main.py

---

### Confirm that an NVIDIA GPU exists

lspci | grep -i nvidia

---

dim = 0  → operate column-wise (down the rows)
dim = 1  → operate row-wise (across the columns)