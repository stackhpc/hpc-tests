#!/bin/bash
#SBATCH --job-name="rfm_Osu_mbw_mr__4_job"
#SBATCH --ntasks=8
#SBATCH --ntasks-per-node=4
#SBATCH --output=rfm_Osu_mbw_mr__4_job.out
#SBATCH --error=rfm_Osu_mbw_mr__4_job.err
#SBATCH --time=0:15:0
#SBATCH --exclusive
module load gcc/9.3.0-5abm3xg
module load intel-mpi/2019.7.217-bzs5ocr
export FI_VERBS_IFACE=ib
module load osu-micro-benchmarks/5.6.2-ppxiddg
mpirun -np 8 osu_mbw_mr
