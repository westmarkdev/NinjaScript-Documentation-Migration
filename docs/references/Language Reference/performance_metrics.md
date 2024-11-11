---
title: Performance Metrics
pathName: performance_metrics
parent: language_reference
status: imported
order: 12
section: references
---

Custom Performance Metrics can be used when generating Trade Performance statistics.

Once custom performance metrics are created be sure to enable their usage in [Tools > Options > General](general_section) or else they will not be available in the [Strategy Analyzer](strategy_analyzer) or [Trade Performance](trade_performance) windows.

## In this section

{% table %}

* Method
* Description

---

* [Format()](format)
* This method allows you to customize the rendering of the performance value on the Summary grid.

---

* [OnAddTrade()](onaddtrade)
* This method is called as each trade is added.

---

* [OnCopyTo()](oncopyto)
* Called as the values of a trade metric are saved.

---

* [OnMergePerformanceMetric()](onmergeperformancemetric)
* This method is called when the Performance Metric would be aggregated and merged together.

---

* [PerformanceUnit](performanceunit)
* Enumeration defining each type of PerformanceUnit calculated by NinjaTrader. Used to store a value for this performance type in PerformanceMetrics.

---

* [Values](values.md)
* The Values array holds an 5 values corresponding to each Cbi.PerformanceUnit.
{% /table %}
