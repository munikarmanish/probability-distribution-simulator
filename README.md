# Probability distribution simulator

This is a program that can generate samples from the following probability
distributions:

* Discrete distributions:
  - Bernoulli(p)
  - Binomial(n, p)
  - Geometric(p)
  - NegativeBinomial(k, p)
  - Arbitrary(p1, p2, ...)

* Continuous distributions:
  - Uniform(a, b)
  - Normal(µ, σ)
  - Poisson(λ)
  - Exponential(λ)
  - Gamma(α, λ)

## Software requirements

- Python >= 3.6

## Usage

    $ python3 simulate_dist.py <count> <distribution> <parameters>...

Some examples:

    $ python3 simulate_dist.py 30 bernoulli 0.5
    $ python3 simulate_dist.py 30 binomial 10 0.5
    $ python3 simulate_dist.py 30 geometric 0.5
    $ python3 simulate_dist.py 30 neg-binomial 5 0.5
    $ python3 simulate_dist.py 30 arb-discrete 0.1 0.5 0.4
    $ python3 simulate_dist.py 30 uniform 0 10
    $ python3 simulate_dist.py 30 normal 50 10
    $ python3 simulate_dist.py 30 poisson 5
    $ python3 simulate_dist.py 30 exponential 5
    $ python3 simulate_dist.py 30 gamma 3 5

## Author

- Manish Munikar &lt;manish.munikar@mavs.uta.edu&gt;
