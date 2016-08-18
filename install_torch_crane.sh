#!/bin/bash

# fix the maxmin problem

cd ~

# part 001  Install original torch

if [-d 'torch' ]; then
    rm -rf torch
fi

git clone https://github.com/torch/distro.git ~/torch --recursive
cd ~/torch
./install.sh

luarocks install loadcaffe

git clone https://github.com/torch/nn.git
cd nn
luarocks make rocks/nn-scm-1.rockspec

source .bashrc

#################################

#if [ -d "cutorch"]; then
#    rm -rf cutorch
#fi

# part 002 install older version of cutorch

#git clone https://github.com/torch/cutorch.git
#cd cutorch
#git checkout aa9dd6e08ac3d5aea5643ef26f2fcf10d9b076a6
#luarocks make rocks/cutorch-scm-1.rockspec

## if I use train() here,  undefined symbol: THCuda_Blas_Segmm 





#  curlew-06: 
#  .bashrc_v0.0    using cuda-7.0


#  result of part 001

#  original torch installation succeed
# ========== th -i ~/test_minpooling.lua  
# === error
# invalid arguments: CudaTensor CudaTensor CudaTensor number
# expected arguments: CudaTensor | [*CudaTensor*] [*CudaLongTensor*] CudaTensor index
# ==========

# follow the original torch installation
  
# result of part 002
# older version cutorch installation succeed
# ========== th -i ~/test_minpooling.lua
# === succeed in printing the output

# ========== th -i 9_doall.lua
# === succeed in runing the scripts
# ========== train()                    =====set useGPU=nil will work
# === failed in /home/jielei/torch/install/bin/luajit: symbol lookup error: /home/jielei/torch/install/lib/lua/5.1/libTHCUNN.so: undefined symbol: THCudaBlas_Sgemm


# luarocks install cunn --  ===>  undefined symbol: THCudaBlas_Sgemm
# luarocks install nn
# luarocks install cutorch
# luarocks install cunn
# === works fine
# === has the same problem with the newly installed original torch 


# install older version of cutorch follow part 002
# result is the same with previous installation of old-cutorch





###################################### Try fixed nn (for maxminfix)














































