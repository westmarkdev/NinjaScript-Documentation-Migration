---
title: OnCalculatePerformanceValue()
pathName: oncalculateperformancevalue
parent: optimization_fitness
status: review
section: references
---

## Definition

This method calculates the value for the Optimization Fitness.

## Syntax

**protected override void OnCalculatePerformanceValue(StrategyBase strategy)**

## Examples

```csharp
protected override void OnCalculatePerformanceValue(StrategyBase strategy)
{

     Value = strategy.SystemPerformance.AllTrades.TradesPerformance.Percent.Drawdown;

}
