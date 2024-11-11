---
title: OptimizationParameters
pathName: optimizationparameters
parent: optimizer
status: review
section: references
---

## Definition

The optimization parameters selected for the optimization run. (e.g. user parameters or Data Series)

## Property Value

A bool value.

## Syntax

**Strategies[0].OptimizationParameters**

## Examples

```csharp
protected override void OnOptimize()
{
     // If there are no optimization parameters to optimize, return
     if (Strategies[0].OptimizationParameters.Count == 0)
         return;

     // Do something with the optimization parameter
     Parameter parameter = Strategies[0].OptimizationParameters[0];
}
```
