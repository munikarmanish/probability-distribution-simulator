#!/bin/bash

commands=('python3 simulate_dist.py 30 bernoulli 0.5'
          'python3 simulate_dist.py 30 binomial 10 0.5'
          'python3 simulate_dist.py 30 geometric 0.5'
          'python3 simulate_dist.py 30 neg-binomial 5 0.5'
          'python3 simulate_dist.py 30 arb-discrete 0.1 0.5 0.4'
          'python3 simulate_dist.py 30 uniform 0 10'
          'python3 simulate_dist.py 30 normal 50 10'
          'python3 simulate_dist.py 30 poisson 5'
          'python3 simulate_dist.py 30 exponential 5'
          'python3 simulate_dist.py 30 gamma 3 5')

for command in "${commands[@]}"; do
    eval "$command" 1>/dev/null
    if (( $? != 0 )); then
        echo "Error in '$command'" 1>&2
        exit 1
    fi
done

echo "Test successful."
