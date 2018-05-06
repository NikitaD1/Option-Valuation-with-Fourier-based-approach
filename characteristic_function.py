def characteristic_function(u, T, r, sigma, lamb, mu, delta):
    ''' Valuation of European call option in M76 model via
    Lewis (2001) Fourier-based approach: characteristic function.
    Parameter definitions see function M76_value_call_INT. '''
    omega = r - 0.5 * sigma ** 2 - lamb * (np.exp(mu + 0.5 * delta ** 2) - 1)
    value = np.exp((1j * u * omega - 0.5 * u ** 2 * sigma ** 2 + lamb * (np.exp(1j * u * mu - u ** 2 * delta ** 2 * 0.5) - 1)) * T)
    return value