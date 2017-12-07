#!/bin/bash
#SBATCH --nodes=1
#SBATCH --cpus-per-task=20
#SBATCH --time=48:00:00
#SBATCH --mem=128GB
#SBATCH --job-name=NRE_train
#SBATCH --mail-type=END
#SBATCH --mail-user=gz612@nyu.edu
#SBATCH --output=NRE_train.out

module purge
module load python3/intel/3.5.3
#module load numpy/intel/1.13.1
module load tensorflow/python3.5/1.4.0 cudnn/8.0v6.0 cuda/8.0.44

python3 train_GRU.py
