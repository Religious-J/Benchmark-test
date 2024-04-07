#!/bash/bin

#sh ./clear.sh

source /opt/intel/oneapi/setvars.sh

# mpirun -np 2 ./xhpl

# mpirun -np 2 ./xhpl

sudo apt update
sudo apt install -y python3
sudo ln -s /usr/bin/python3 /usr/bin/python

sudo apt install -y python3-pip

pip3 --version

pip3 install py-cpuinfo
pip3 install tqdm
pip3 install psutil
pip3 install py-json

sh ./print.sh

chmod 777 xhpl

# mpirun -np 2 ./xhpl

python test.py

python ./py/Gflops.py
