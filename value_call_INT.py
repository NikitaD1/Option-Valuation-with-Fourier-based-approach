S0 = 100.0 # initial index level
K = 100.0 # strike level
T = 1.0 # call option maturity
r = 0.05 # constant short rate
sigma = 0.4 # constant volatility of diffusion
lamb = 1.0 # jump frequency p.a.
mu = -0.2 # expected jump size
delta = 0.1 # jump size volatility
int_value = quad(lambda u: integration_function(u, S0, K, T, r, sigma, lamb, mu, delta), 0, 50, limit=250)[0]
call_value = S0 - np.exp(-r * T) * math.sqrt(S0 * K) / math.pi * int_value
rint("The value of call option is %8.3f" %call_value)
