---
title: "Performance Metrics"
pathName: /docs/desktop/performance_metrics
---

Custom Performance Metrics can be used when generating Trade Performance statistics.

Once custom performance metrics are created, be sure to enable their usage in [Tools > Options > General](/docs/desktop/general_section) or else they will not be available in the [Strategy Analyzer](/docs/desktop/strategy_analyzer) or [Trade Performance](/docs/desktop/trade_performance) windows.

## In this section

|  |  |
| --- | --- |
| [Format()](/docs/desktop/format) | This method allows you to customize the rendering of the performance value on the Summary grid. |
| [OnAddTrade()](/docs/desktop/onaddtrade) | This method is called as each trade is added. |
| [OnCopyTo()](/docs/desktop/oncopyto) | Called as the values of a trade metric are saved. |
| [OnMergePerformanceMetric()](/docs/desktop/onmergeperformancemetric) | This method is called when the Performance Metric would be aggregated and merged together. |
| [PerformanceUnit](/docs/desktop/performanceunit) | Enumeration defining each type of PerformanceUnit calculated by NinjaTrader. Used to store a value for this performance type in PerformanceMetrics. |
| [Values](/docs/desktop/performancemetric_values) | The Values array holds five values corresponding to each Cbi.PerformanceUnit. |
