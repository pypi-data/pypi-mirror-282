
bank = {}
itrue = [
    'Euler-discretization can be applied to time-dependent control problems',
    ]
ifalse = [
    'Euler-discretization is exact when both the dynamics and cost-function for the continuous-time control problem are linear',
    'Euler-discretization is necesary if we want to apply LQR to a general continuous-time control problem.',
    'To apply Exponential integration to a control problem of the form $\cdot x = A x + B u$, it is necesary that $A$ is invertible',
      ]

bank['discretization'] = {'true': itrue, 'false': ifalse}