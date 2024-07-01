yum groupinstall "Development Tools"
yum install bison flex

cd ext/verilator
autoconf
./configure
make -j `nproc`
cd ../../
