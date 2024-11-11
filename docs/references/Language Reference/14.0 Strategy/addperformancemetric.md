---
section: references
status: imported
parent: strategy
title: AddPerformanceMetric()
pathName: addperformancemetric
---

## Definition

Adds an instance of custom **Performance Metric** to a strategy used in strategy calculations.

## Method Return Value

This method does not return a value.

## Syntax

**AddPerformanceMetric(PerformanceMetricBase performanceMetric)**

{% callout type="warning" %}

This method should ONLY be called from the **OnStateChange()** method during State.Configure

{% /callout %}

## Parameters

{% table %}

* performanceMetric

---

* The performance metric object to be added
{% /table %}

## Examples

```csharp
protected override void OnStateChange()
{
     if (State == State.Configure)
     {
         AddPerformanceMetric(new NinjaTrader.NinjaScript.PerformanceMetrics.SampleCumProfit());
     }
}
```
