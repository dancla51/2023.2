import core
from algorithms import newton, newton_damped
def f1(x):
    core.f_eval += 1
    return 2 * x * x - 8 * x + 4


def g1(x):
    core.g_eval += 1
    return 4 * x - 8


def f2(x):
    return x * x - 1


def g2(x):
    return 2 * x



def reset():
    core.f_eval=0
    core.g_eval=0

j=(-1)**0.5
print(f'Method       Estimate     Value       Iterations  Func Evals  Deriv Evals  Exit Flag')
print('-------------------------------------------------------------------------------------------------')
reset()
x,iter,exit_flag = newton(f1,g1,1,100,0.0001)
print(f'Newton      {x[-1]: 1.8f}  {f1(x[-1]): 1.4e}  {iter:10d}  {core.f_eval-1:10d}  {core.g_eval:11d}  {exit_flag}')
reset()
x,iter,exit_flag = newton_damped(f1,g1,1,100,0.0001, 9)
print(f'Damped    {x[-1]: 1.8f}  {f1(x[-1]): 1.4e}  {iter:10d}  {core.f_eval-1:10d}  {core.g_eval:11d}  {exit_flag}')
print('')