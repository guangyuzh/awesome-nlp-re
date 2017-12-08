#!/bin/bash
#SBATCH --nodes=1
#SBATCH --cpus-per-task=20
#SBATCH --time=48:00:00
#SBATCH --mem=256GB
#SBATCH --job-name=Init_data
#SBATCH --mail-type=END
#SBATCH --mail-user=gz612@nyu.edu
#SBATCH --output=logs/Init_data.out

module purge
module load python3/intel/3.5.3

python3 -u initial.py > logs/Init_data.log
