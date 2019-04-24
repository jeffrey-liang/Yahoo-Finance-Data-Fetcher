#!/usr/bin/env python
# -*- coding: utf-8 -*-

import arrow
from get_yahoo_finance import get_data
from pandas.testing import assert_frame_equal
import pandas as pd

start_period = 1546300800  # 2019-01-01
end_period = 1546905600  # 2019-01-08

spy = pd.read_csv('SPY.csv', index_col=0, header=0)

data = get_data('SPY', start_period, end_period)

assert_frame_equal(spy, data['SPY'])
