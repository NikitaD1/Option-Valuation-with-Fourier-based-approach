def integration_function(u, S0, K, T, r, sigma, lamb, mu, delta):

    JDCF = characteristic_function(u - 0.5 * 1j, T, r,
    sigma, lamb, mu, delta)
    value = 1 / (u ** 2 + 0.25) * (np.exp(1j * u * math.log(S0 / K))* JDCF).real
    return value