def to_hereditary_base(n, base):
    if n == 0:
        return []
    e = 0
    power = 1
    next_power = power * base
    while next_power <= n:
        e += 1
        power = next_power
        next_power = power * base
    c = n // power
    remainder = n % power
    rep_e = to_hereditary_base(e, base)
    rep_rem = to_hereditary_base(remainder, base)
    return [(c, rep_e)] + rep_rem

def eval_hereditary(rep, base):
    total = 0
    for coef, exp_rep in rep:
        exp_val = eval_hereditary(exp_rep, base)
        total += coef * (base ** exp_val)
    return total

def goodstein_sequence(start, max_terms=1000):
    if start == 0:
        return [0]
    sequence = [start]
    current = start
    b = 2
    while current > 0 and len(sequence) < max_terms:
        rep = to_hereditary_base(current, b)
        next_val = eval_hereditary(rep, b + 1)
        current = next_val - 1
        sequence.append(current)
        b += 1
    return sequence

if __name__ == "__main__":
    print(goodstein_sequence(4,200))