---
title: BarsSinceNewTradingDay
pathName: barssincenewtradingday
parent: bars
section: references
status: review
---

## Definition

Returns the number of bars elapsed since the start of the trading day relative to the current bar processing.

## Property Value

An **int** value representing the number of bars elapsed. This property cannot be set.

## Syntax

**Bars.BarsSinceNewTradingDay**

## Examples

```csharp

// Only process strategy logic after five bars have posted since the start of the trading day
protected override void OnBarUpdate()
{
   if (Bars.BarsSinceNewTradingDay >= 5)
   {
     //Strategy logic here
   }
}
```
