
bank = {}
itrue = [
    "A PID controller is an example of a closed-loop controller",
    "PID controllers are relatively simple to implement compared to other approaches",
    "A PID controller can, for certain problems, be optimal or near-optimal",
    "It is generally advisable to tune the $K_P$ parameter before the $K_D$ parameter in a PID controller",
    'We can build a PID controller without specifying a cost-function',
]
ifalse = ["A PID controller is not appropriate for stochastic environments."]
for name in ['proportionality', 'integral', 'derivative']:
    for sgn in ['negative', 'positive']:
        ss = '\\geq' if sgn == 'positive' else '\\leq'
        ifalse += [f"The {name} parameter $K_{name[0]}$ must always be {sgn} $K_{name[0]} {ss} 0$"]
ifalse += ['A PID controller is an example of an open-loop controller']
ifalse += ['A PID controller is a model-based control method']
ifalse += ['PID control requires a differential equation describing the system dynamics',
           'A model of the environment cannot be used to set the parameters in a PID controller',
           'In a PID controller, the $K_D$ (derivative) parameter is multiplied to the derivative of the system dynamics',
           'In a PID controller, the $K_I$ (integral) parameter is multiplied to the integral of the cost function',
           ]
           # 'If the discretization time $\Delta$ is doubled, we should expect that the parameters $K_p, K_d$ and $K_I$ are doubled as well']

bank['pid'] = {'true': itrue, 'false': ifalse}
