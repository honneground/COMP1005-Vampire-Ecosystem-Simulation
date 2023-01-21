#!/bin/bash

low_hum=${1:-10}
hi_hum=${2:-40}
low_vam=${3:-1}
hi_vam=${4:-5}
timesteps=${5:-50}
plot_or_not=${6:-"Y"}

echo "Parameters are: "
echo "Population : " $low_hum $hi_hum $low_vam $hi_vam
outfile="simulation"$low_hum"-"$hi_hum"-"$low_vam"-"$hi_vam".csv"
if [ -e $outfile ]; then
  rm $outfile
echo "Initial Human Population,Final Human population,Initial Vampire Population,Final Vampir population" > $outfile
fi
for hum_pop in `seq $low_hum $hi_hum`
do
    for vam_pop in `seq $low_vam $hi_vam`
    do
        echo "Experiment: " $hum_pop-$vam_pop 
        output=$(python3 main.py $hum_pop $vam_pop $timesteps $plot_or_not)
        last_line=$(echo "$output" | tail -n 1)
        echo "$last_line" >> $outfile
    done
done
echo "End of the execution."
echo "Simulation result saved."
