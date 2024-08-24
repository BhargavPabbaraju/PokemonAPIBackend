from django.core.management.base import BaseCommand, CommandError

from api.models import GrowthRate

DEFAULT_GROWTH_RATES = [
    {
        'name': 'Slow',
        'latex': '\\frac{5x^3}{4}',
        'python': 'lambda x: (5 * x**3) / 4'
    },
    {
        'name': 'Medium',
        'latex': 'x^3',
        'python': 'lambda x: x**3'
    },
    {
        'name': 'Fast',
        'latex': '\\frac{4x^3}{5}',
        'python': 'lambda x: (4 * x**3) / 5'
    },
    {
        'name': 'Medium Slow',
        'latex': '\\frac{6x^3}{5} - 15x^2 + 100x - 140',
        'python': 'lambda x: (6 * x**3) / 5 - 15 * x**2 + 100 * x - 140'
    },
    {
        'name': 'Erratic',
        'latex': '\\begin{cases}\n\\frac{ x^3 \\left( 100 - x \\right) }{50},    & \\text{if } x \\leq 50  \\\\\n\\frac{ x^3 \\left( 150 - x \\right) }{100},   & \\text{if } 50 < x \\leq 68  \\\\\n\\frac{ x^3 \\left( 1274 + (x \\bmod 3)^2 - 9 (x \\bmod 3) - 20 \\left\\lfloor \\frac{x}{3} \\right\\rfloor \\right) }{1000}, & \\text{if } 68 < x \\leq 98  \\\\\n\\frac{ x^3 \\left( 160 - x \\right) }{100},   & \\text{if } x > 98  \\\\\n\\end{cases}',
        'python': 'lambda x: ((x**3 * (100 - x) / 50) if x <= 50 else \
            (x**3 * (150 - x) / 100) if 50 < x <= 68 else \
            (x**3 * (1274 + (x % 3)**2 - 9 * (x % 3) - 20 * (x // 3)) / 1000) if 68 < x <= 98 else \
            (x**3 * (160 - x) / 100))'
    },
    {
        'name': 'Fluctuating',
        'latex': '\\begin{cases}\n\\frac{ x^3 \\left( 24 + \\left\\lfloor \\frac{x+1}{3} \\right\\rfloor \\right) }{50},  & \\text{if } x \\leq 15  \\\\\n\\frac{ x^3 \\left( 14 + x \\right) }{50},     & \\text{if } 15 < x \\leq 35  \\\\\n\\frac{ x^3 \\left( 32 + \\left\\lfloor \\frac{x}{2} \\right\\rfloor \\right ) }{50},   & \\text{if } x > 35  \\\\\n\\end{cases}',
        'python': 'lambda x: ((x**3 * (24 + (x + 1) // 3) / 50) if x <= 15 else \
            (x**3 * (14 + x) / 50) if 15 < x <= 35 else \
            (x**3 * (32 + x // 2) / 50))'
    }
]

class Command(BaseCommand):
    help = "Initializes default Pokemon Growth rates"

    def handle(self,*args,**options):
        for growth_rate in DEFAULT_GROWTH_RATES:
            try:
                growth_rate_obj = GrowthRate(name = growth_rate['name'],
                latex_formula=growth_rate['latex'],
                python_formula=growth_rate['python'])
            
            except Exception as e:
                raise CommandError(e)
            
            growth_rate_obj.save()
        
        self.stdout.write(
            self.style.SUCCESS('Successfully initialized %d growth rates' % len(DEFAULT_GROWTH_RATES))
        )
