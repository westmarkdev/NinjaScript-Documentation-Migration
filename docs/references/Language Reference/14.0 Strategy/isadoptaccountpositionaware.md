---
title: IsAdoptAccountPositionAware
pathName: isadoptaccountpositionaware
parent: strategy
section: references
status: imported
---

## Definition

Determines if the strategy is programmed in a manner capable of handling real-world account positions. Once set to true, your strategy's **Start behavior** options will include an additional parameter named **Adopt account position** which can be set at run-time. Only set to true if you have specifically programmed your strategy to be able to adopt account positions.

## Property Value

This property returns true if the strategy can adopt account positions; otherwise, false. Default is set to false.

{% callout type="note" %}

This property should ONLY be set from the **OnStateChange()** method during State.SetDefaults.

{% /callout %}

## Syntax

**IsAdoptAccountPositionAware**

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        IsAdoptAccountPositionAware = true;
    }
}
```
