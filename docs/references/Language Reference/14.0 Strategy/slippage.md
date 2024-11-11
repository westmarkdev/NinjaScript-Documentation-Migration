---
title: Slippage
pathName: slippage
parent: strategy
section: references
status: imported
---

## Definition

Sets the amount of slippage in ticks per execution used in performance calculations during backtests.

## Property Value

An **int** value representing the number ticks. Default value is set to 0.

## Syntax

**Slippage**

## Examples

```csharp
protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         **Slippage** = 2; 
     }
}
```
