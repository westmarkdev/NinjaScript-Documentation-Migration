---
title: Optimizer
pathName: optimizer
parent: language_reference
order: 11
status: imported
section: references
---

Custom Optimizers can be used to optimize your Strategy through different algorithms. These may allow you to make trade offs like being able to find adequate results quickly as opposed to trying to find the absolute best result but through a time consuming process. The methods and properties covered in this section are unique to custom Optimizer development.

## In this section

{% table %}

---

* [NumberOfIterations](numberofiterations)
* Informs the Strategy Analyzer how many iterations of optimizing it needs to do.

---

* [OnOptimize()](onoptimize)
* This method must be overridden in order to optimize a strategy.

---

* [OptimizationParameters](optimizationparameters)
* The optimization parameters selected for the optimization run.

---

* [RunIteration()](runiteration)
* Runs an iteration of backtesting for the optimizer.

---

* [SupportsMultiObjectiveOptimization](supportsmultiobjectiveoptimiza)
* Informs the Strategy Analyzer if this Optimizer can do multi-objective optimizations.
{% /table %}
