from options import *

test_monomial_constant_1d = { INPUT : 'monomial-const-1d.i',
                  EXODIFF : ['monomial-const-1d_out.e']
                  }

test_monomial_constant_2d = { INPUT : 'monomial-const-2d.i',
                  EXODIFF : ['monomial-const-2d_out.e'],
                  ABS_ZERO : 1e-9
                  }

test_monomial_constant_3d = { INPUT : 'monomial-const-3d.i',
                  EXODIFF : ['monomial-const-3d_out.e'],
                  MAX_PARALLEL : 1
                  }
