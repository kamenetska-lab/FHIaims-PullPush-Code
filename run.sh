#!/bin/bash -l

#$ -P kamenet

#$ -pe omp 16

#$ -l h_rt=12:00:00

ACTIVE=/projectnb/kamenet/Brent/FHIaims/amine_hyroxy_mol/methylaminephenol/deprot/w_2au18/plus/testing/

export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export MKL_DYNAMIC=FALSE

ulimit -s unlimited

module load gcc/5.5.0
module load intel/2019.5
module load openmpi/3.1.4_intel-2019
module load cuda/9.2
module load python3/3.7.7

n=1
for ((n=1; n<=3; n++))
do
nohup mpirun -np 16 /projectnb/kamenet/Programs/FHIaims/fhi-aims.171221/bin/aims.171221_1.scalapack.mpi.x < /dev/null | tee aims.dft.out

mkdir step$n

cp aims.dft.out aimstemp.dft.out
cp aims.dft.out "aims$n.dft.out"

cp geometry.in geometrytemp.in
cp geometry.in geometryinitial$n.in

cp aims$n.dft.out step$n
cp geometryinitial$n.in step$n

rm geometry.in
cp control.in controltemp.in
rm control.in


python aimsconverter.py

nohup mpirun -np 16 /projectnb/kamenet/Programs/FHIaims/fhi-aims.171221/bin/aims.171221_1.scalapack.mpi.x < /dev/null | tee aims.dft.out

cp mos.aims step$n
cp omat.aims step$n
cp basis-indices.out step$n

rm aims.dft.out
cp aimstemp.dft.out aims.dft.out
rm geometry.in

python batch_scriptv2.py

cp geometry.xyz geometryrelaxed$n.xyz
cp geometryrelaxed$n.xyz step$n

rm geometry.xyz
rm geometry$n.xyz
rm mos.aims
rm aims.dft.out
rm geometrytemp.in
rm aimstemp.dft.out
rm omat.aims
rm aims$n.dft.out
rm control.in
cp controltemp.in control.in
rm controltemp.in
rm geometry$n.in
rm basis-indices.out
rm geometry.in.next_step

done