---
title: "PerformanceMetrics"
pathName: /docs/desktop/performancemetrics
---

## Definition

Returns a collection of custom [Performance Metrics](/docs/desktop/performance_metrics). These need to have been enabled in [Tools > Options > General](/docs/desktop/general_section) to be able to use them.

## Syntax

```plaintext
## <tradecollection>.TradesPerformance.PerformanceMetrics
```

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Print out the number of enabled custom Performance Metrics
    Print("Number of Performance Metrics: "
    + SystemPerformance.AllTrades.TradesPerformance.PerformanceMetrics.Length);
    
    // Find the value of a specific custom Performance Metric named "MyPerformanceMetric"
    for (int i = 0; i < SystemPerformance.AllTrades.TradesPerformance.PerformanceMetrics.Length; i++)
    {
        if (SystemPerformance.AllTrades.TradesPerformance.PerformanceMetrics[i] is
        NinjaTrader.NinjaScript.PerformanceMetrics.MyPerformanceMetric)
        {
            Print((SystemPerformance.AllTrades.TradesPerformance.PerformanceMetrics[i] as
            NinjaTrader.NinjaScript.PerformanceMetrics.MyPerformanceMetric).Values[0]);
        }
    }
}
```
