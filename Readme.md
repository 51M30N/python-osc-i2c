# python-osc-i2c
 OSC_to_I2C
 
pour ONAVIO KLD

ecoute un port OSC avec puredata
puredata envoie des messages OSC aux patchs python
les patchs pytgons envoient les ordres via I2C aux Arduino

 
## basé sur
https://github.com/attwad/python-osc
<https://pypi.org/project/python-osc/>




## installation 
```
cd /Mon/Dossier
git clone https://github.com/51M30N/python-osc-i2c.git
```
## creer lien librairie pythonosc
```
cd ~/Mon/Dossier/python-osc-i2c/
ln -rs python-osc-1.7.4/pythonosc/
```
## rendre executable le script main
```
cd ~/Mon/Dossier/python-osc-i2c/
sudo chmod +x main_OSC_to_Pd_to_python_to_i2c
```
## executer le script
```
cd ~/Mon/Dossier/python-osc-i2c/
./main_OSC_to_Pd_to_python_to_i2c
```








#### test d'un autre oscsender python a faire
```
git clone https://github.com/Qux/quxpy.git
```


""" I2C baudrate
```
sudo nano /boot/config.txt
dtparam=i2c_arm=on,i2c_arm_baudrate=40000
```
