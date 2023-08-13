# Task 1

from golden import golden
from brent import brent
from fullbrent import fullbrent
from functions import task1functions, task1functiontitles, task3functions, task3functiontitles
from testoptimiser import testoptimiser




# initialisation
tol = 10e-4
max_iter = 50
a = 0.0   # a & b define uncertainty interval
b = 1.0
plotleft = 0.0  # plotleft & plotright define the plot range
plotright = 3.0
showlog = True

testoptimiser(golden,"Andrew's Golden", task1functions, task1functiontitles, a, b, max_iter, tol, showlog, plotleft, plotright)
testoptimiser(brent,"Andrew's Brent", task1functions, task1functiontitles, a, b, max_iter, tol, showlog, plotleft, plotright)
testoptimiser(fullbrent,"My FullBrent",  task1functions, task1functiontitles, a, b, max_iter, tol, showlog, plotleft, plotright)
