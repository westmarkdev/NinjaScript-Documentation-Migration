---
title: PerformanceMetrics
pathName: performancemetrics
parent: tradecollection
section: references
status: imported
---

## Definition

Returns a collection of custom **Performance Metrics**. These need to have been enabled in [Tools > Options > General](general_section) to be able to use them.

## Syntax

<`tradecollection`>.TradesPerformance.**PerformanceMetrics**

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Print out the number of enabled custom Performance Metrics
     Print("Number of Performance Metrics: "
         + SystemPerformance.AllTrades.TradesPerformance.PerformanceMetrics.Length);
 
     // Find a the value of a specific custom Performance Metric named "MyPerformanceMetric"
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
