---
title: PerformanceUnit
pathName: performanceunit
parent: performance_metrics
status: imported
section: references
---

## Definition

Enumeration defining each type of **PerformanceUnit** calculated by **NinjaTrader**. Used to store a value for this performance type in **PerformanceMetrics**.

## Syntax

**PerformanceUnit.Currency**

**PerformanceUnit.Percent**

**PerformanceUnit.Pips**

**PerformanceUnit.Points**

**PerformanceUnit.Ticks**

## Examples

```csharp
//Prints unrealized PnL in ticks at the close of each bar
Print(Position.GetUnrealizedProfitLoss(PerformanceUnit.Ticks, Close[0]));
```
