yum groupinstall -y "Development Tools"
yum install -y bison flex help2man

git clone --branch v5.026 https://github.com/verilator/verilator
cd verilator
autoconf
./configure
make -j `nproc`
make install
