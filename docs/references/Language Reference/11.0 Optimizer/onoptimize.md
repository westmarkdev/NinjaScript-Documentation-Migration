---
title: OnOptimize()
pathName: onoptimize
parent: optimizer
status: imported
section: references
---

## Definition

This method must be overridden in order to optimize a strategy. This method is called once per optimization run (not once per iteration).

## Method Return Value

This method does not return a value.

## Syntax

You must override the method in your Optimizer with the following syntax.

**protected override void OnOptimize()**

## Examples

```csharp

protected override void OnOptimize()
{
     // If there is no optimization objective, return
     if (Strategies[0].OptimizationParameters.Count == 0)
         return;

     // Optimizer logic
}
```
