---
title: IsWaitUntilFlat
pathName: iswaituntilflat
parent: strategy
section: references
status: imported
---

## Definition

Indicates the strategy is currently waiting until a flat position is detected before submitting live orders.

{% callout type="note" %}

This property would only apply if the strategy **StartBehavior** was set to **StartBehavior.WaitUntilFlat** or **StartBehavior.WaitUntilFlatSynchronizeAccount**.

{% /callout %}

## Property Value

This property returns true if the strategy has detected it is either in a long or short position during **State.Transition**; otherwise false. Default value is set to false.

## Syntax

**IsWaitUntilFlat**

## Examples

```csharp
// If a strategy is waiting for a flat position, return and print a message
if (!IsWaitUntilFlat)
{ 
   Print("This strategy is currently waiting for a flat account position to begin placing trades");
   return;
}
```
