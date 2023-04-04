
import fractions
import decimal

deciamls = [decimal.Decimal('0.2'), decimal.Decimal('0.32'),decimal.Decimal('0.75')]

print([fractions.Fraction(d) for d in deciamls])
