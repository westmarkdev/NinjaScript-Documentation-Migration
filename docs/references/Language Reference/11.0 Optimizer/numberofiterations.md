---
title: NumberOfIterations
pathName: numberofiterations
parent: optimizer
status: imported
section: references
---

## Definition

Informs the Strategy Analyzer how many iterations of optimizing it needs to do.

## Property Value

An **int** value.

## Syntax

**NumberOfIterations**

## Examples

```csharp
protected override void OnStateChange()
{
     if (State == State.SetDefaults)
         Name = "MyOptimizer";
     else if (State == State.Configure && Strategies.Count > 0)
         NumberOfIterations = 1;
}
```
