
import core
from algorithms import bisection, secant, regula_falsi, newton, combined
from functions import f1, g1, f2, g2, fc, gc

def reset():
    core.f_eval=0
    core.g_eval=0

f = fc
g = gc

print(f'Method       Estimate     Value       Iterations  Func Evals  Deriv Evals  Exit Flag')
print('-------------------------------------------------------------------------------------------------')
reset()
x,iter,exit_flag = bisection(f,0,2,100,0.0001)
print(f'Bisection   {x[-1]: 1.8f}  {f(x[-1]): 1.4e}  {iter:10d}  {core.f_eval-1:10d}  {0:11d}  {exit_flag}')
reset()
x,iter,exit_flag = secant(f,0,2,100,0.0001)
print(f'Secant      {x[-1]: 1.8f}  {f(x[-1]): 1.4e}  {iter:10d}  {core.f_eval-1:10d}  {0:11d}  {exit_flag}')
reset()
x,iter,exit_flag = regula_falsi(f,0,2,100,0.0001)
print(f'RegulaFalsi {x[-1]: 1.8f}  {f(x[-1]): 1.4e}  {iter:10d}  {core.f_eval-1:10d}  {0:11d}  {exit_flag}')
reset()
x,iter,exit_flag = newton(f,g,1,100,0.0001)
print(f'Newton      {x[-1]: 1.8f}  {f(x[-1]): 1.4e}  {iter:10d}  {core.f_eval-1:10d}  {core.g_eval:11d}  {exit_flag}')
reset()
x,iter,exit_flag = combined(f,g,0,2,100,0.0001)
print(f'Combined    {x[-1]: 1.8f}  {f(x[-1]): 1.4e}  {iter:10d}  {core.f_eval-1:10d}  {core.g_eval:11d}  {exit_flag}')
print('')