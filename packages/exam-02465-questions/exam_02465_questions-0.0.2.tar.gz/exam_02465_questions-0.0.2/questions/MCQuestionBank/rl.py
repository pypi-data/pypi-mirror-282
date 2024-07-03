

bank = {}
itrue = [
    # 'Dynamical programming is more remeniscent of $Q$-learning than policy evaluation',
    'The optimal policy for a MDP may change if $\\gamma$ is changed',
    'The value function associated with the optimal policy can be computed from the $Q$-function associated with the optimal policy',
    # 'Assume the maximal reward of a MDP is bounded by one, i.e. that $|R_{t+1}| \\leq 1$. In this case, it can still be the case that $Q$-learning finds a value $Q(s,a) > 2$?'
]
ifalse = ["In order for $Q$-learning to find the optimal policy, the exploration parameter must converge to $0$ over time",
          'Sarsa cannot be used to find the optimal policy',
          'Sarsa learning cannot be used to find the $Q$-function associated with the random policy',
          '$Q$-learning will find an open-loop controller',
          'Sarsa will find an open-loop controller',
          '$Q$-learning can only be applied to problems where the discount factor satisfies $\\gamma < 0$',
          'If $\\lambda>0$, then over time TD(0) will tend to find lower values of the value-function $V$ than $TD(\\lambda)$',
          'TD(0) requires that the value-function is initialized to 0, and will not work if the value-function is initialized randomly',
          'If $a_1 \\neq a_2$, we can conclude that $Q(s,a_1) \\neq Q(s,a_2)$ assuming $Q$ is the $Q$-function associated with the optimal policy of an MDP',
            ]

bank['tabular_rl'] = {'true': itrue, 'false': ifalse}