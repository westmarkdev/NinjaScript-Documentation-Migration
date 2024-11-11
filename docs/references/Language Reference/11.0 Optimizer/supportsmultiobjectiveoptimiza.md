---
title: SupportsMultiObjectiveOptimization
pathName: supportsmultiobjectiveoptimization
parent: optimizer
status: imported
section: references
---

## Definition

Informs the Strategy Analyzer if this Optimizer can do multi-objective optimizations.

## Property Value

A bool value.

## Syntax

**SupportsMultiObjectiveOptimization**

## Examples

```csharp
protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
          Name = "MyOptimizer";
          SupportsMultiObjectiveOptimization = true;
     }
}
```
