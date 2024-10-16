---
title: "PerformanceMetrics"
pathName: /docs/desktop/strategy_performancemetrics
---

## Definition

Holds an array of [PerformanceMetrics](/docs/desktop/performancemetrics) objects that represent custom metrics that can be used for strategy calculations.

Index value is based on the the array of Bars objects added via the [AddPerformanceMetric](/docs/desktop/addperformancemetric) method.

## Property Value

An array of [PerformanceMetrics](/docs/desktop/performancemetrics) objects.

## Syntax

```csharp
## PerformanceMetrics[int index]
```

## Examples

```csharp
// Define a new SampleCumProfit object
NinjaTrader.NinjaScript.PerformanceMetrics.SampleCumProfit myProfit;

protected override void OnStateChange()
{
    if (State == State.Configure)
    {
        // Instantiate myProfit to a new instance of SampleCumProfit
        myProfit = new NinjaTrader.NinjaScript.PerformanceMetrics.SampleCumProfit();
        // Use AddPerformanceMetric to add myProfit to the strategy
        AddPerformanceMetric(myProfit);
    }
}

protected override void OnBarUpdate()
{
    // Print a string representing the Type of the performance metric at Index 0 of the PerformanceMetrics collection
    Print(PerformanceMetrics[0]);
}
```
