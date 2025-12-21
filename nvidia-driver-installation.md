> sudo apt purge '^nvidia-.*'
> sudo apt autoremove
> sudo apt autoclean

---

### Find the recommended driver

> ubuntu-drivers devices
> sudo reboot
> sudo apt install nvidia-driver-535
> sudo reboot

---

### Verify NVIDIA driver installation

> nvidia-smi
