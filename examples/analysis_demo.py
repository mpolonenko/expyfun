# -*- coding: utf-8 -*-
"""
=============
Analysis demo
=============

This example simulates some 2AFC data and demonstrates the analysis
functions dprime_2afc() and barplot().
"""
# Author: Dan McCloy <drmccloy@uw.edu>
#
# License: BSD (3-clause)

print __doc__

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import expyfun.analyze as ea

# simulate some 2AFC data
trials = 100
c_prob = 0.9
t_prob = 0.6
subjs = ['a', 'b', 'c', 'd', 'e']
ctrl = np.random.binomial(trials, c_prob, len(subjs))
test = np.random.binomial(trials, t_prob, len(subjs))
ctrl_miss = trials - ctrl
test_miss = trials - test
data = pd.DataFrame(dict(ctrl_hit=ctrl, ctrl_miss=ctrl_miss,
                         test_hit=test, test_miss=test_miss), index=subjs)
# calculate dprimes
ctrl_dprime = ea.dprime_2afc(data[['ctrl_hit', 'ctrl_miss']])
test_dprime = ea.dprime_2afc(data[['test_hit', 'test_miss']])
results = dict(ctrl=ctrl_dprime, test=test_dprime)
# plot
plt.ion()
bp = ea.barplot(results, err_bars='sd', bar_kwargs=dict(color='Gray'),
                lines=True, err_kwargs=dict(ecolor='Black'))
bp.ylabel(u'd-prime ± 1 s.d.')
bp.title('Each colored line represents a different subject')