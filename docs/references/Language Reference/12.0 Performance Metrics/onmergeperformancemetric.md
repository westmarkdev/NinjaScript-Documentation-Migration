---
title: OnMergePerformanceMetric()
pathName: onmergeperformancemetric
parent: performance_metrics
status: imported
section: references
---

## Definition

This method is called when the Performance Metric would be aggregated and merged together (E.g. on the Strategy Analyzer's total row).

## Syntax

**protected override void OnMergePerformanceMetric(PerformanceMetricBase merge)**

## Examples

```csharp
protected override void OnMergePerformanceMetric(PerformanceMetricBase target)
{
   // You need to cast, in order to access the right type
   SampleCumProfit targetMetrics = (target as SampleCumProfit);

   // This is just a simple weighted average sample
   if (targetMetrics != null && TradesPerformance.TradesCount + targetMetrics.TradesPerformance.TradesCount > 0)
     for (int i = 0; i < Values.Length; i++)
         targetMetrics.Values[i] = (targetMetrics.Values[i] *targetMetrics.TradesPerformance.TradesCount + Values[i]* TradesPerformance.TradesCount) / (TradesPerformance.TradesCount + targetMetrics.TradesPerformance.TradesCount);
}
```
