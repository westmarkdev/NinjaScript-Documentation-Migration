---
title: IsFillLimitOnTouch
pathName: isfilllimitontouch
parent: strategy
section: references
status: imported
---

## Definition

Determines if the strategy will use a more liberal fill algorithm for back-testing purposes only. The default behavior of the strategy's fill algorithm is to fill a limit order once price has penetrated the limit price. However, this behavior can be changed by setting **IsFillLimitOnTouch** to true, in which case the strategy's fill algorithm will consider a limit order filled once price has reached the limit price, but does not necessarily need to trade through the limit price.

## Property Value

This property returns true if the strategy will fill limit orders when touched; otherwise, false. Default is set to false.

{% callout type="warning" %}

This property should ONLY be set from the **OnStateChange()** method during State.SetDefaults or State.Configure.

{% /callout %}

## Syntax

**IsFillLimitOnTouch**

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        IsFillLimitOnTouch = true;
    }
}
```
