"""Code from https://vhernando.github.io/calculate-pi-digits-python-high-precision"""

from decimal import getcontext, Decimal


def calculate_pi(precision: int) -> Decimal:

    excess_prec = 2

    prec_cur = 100 if precision > 100 else precision

    getcontext().prec = prec_cur + excess_prec

    second = Decimal(3)  # Current element for PI
    queue_cur = [Decimal(0), Decimal(0), Decimal(0), second]

    qq_append = queue_cur.append
    qq_pop = queue_cur.pop

    limit = Decimal(10) ** (-prec_cur - excess_prec)

    while True:

        sec_sq = second * second
        term = second
        acc = second + term
        count = Decimal(1)

        while term > limit:

            term *= sec_sq / ((count + 1) * (count + 2))
            acc -= term

            term *= sec_sq / ((count + 3) * (count + 4))
            acc += term

            count += 4

        if acc in queue_cur:
            if prec_cur < precision:
                prec_cur += prec_cur
                if prec_cur > precision:
                    prec_cur = precision
                limit = Decimal(10) ** (-prec_cur - excess_prec)
                getcontext().prec = prec_cur + excess_prec

            else:
                second = acc
                break

        qq_append(acc)
        qq_pop(0)
        second = acc
        # print ('second: {}'.format(second))

    getcontext().prec = precision
    return +second


if __name__ == "__main__":
    print(calculate_pi(10000))
