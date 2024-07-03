
bank_lqr = {}
itrue = [
    'The cost-functions suitable for a linear-quadratic regulator can potentially produce negative values',
#    'The linear-quadratic regulator ',
]
ifalse = []
ifalse += ['The linear-quadratic regulartor is an example of model-free control']
ifalse += ['Control problems where the continuous-time dynamics takes the form $\ddot{x} = a\dot{x} + bx + c + u$ falls outside the scope of the linear quadratic regulator']
ifalse += ['In a linear-quadratic control problem of the form $x_{k+1} = Ax + Bu$, the matrices $A$ and $B$ are both square.']

bank_lqr['lqr'] = {'true': itrue, 'false': ifalse}
