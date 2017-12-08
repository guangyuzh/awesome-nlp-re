#!/bin/bash
#SBATCH --nodes=1
#SBATCH --cpus-per-task=20
#SBATCH --time=48:00:00
#SBATCH --mem=32GB
#SBATCH --job-name=NRE_train
#SBATCH --mail-type=END
#SBATCH --mail-user=gz612@nyu.edu
#SBATCH --output=logs/NRE_train.out

module purge
module load python3/intel/3.5.3
module load tensorflow/python3.5/1.0.1 cuda/8.0.44

python3 -u train_GRU.py > logs/NRE_train.log
