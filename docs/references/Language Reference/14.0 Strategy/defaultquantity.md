---
title: DefaultQuantity
pathName: defaultquantity
parent: strategy
section: references
status: imported
---

## Definition

An order size variable that can be set either programmatically or overridden via the Strategy that determines the quantity of an entry order.

## Property Value

An **int** value represents the number of contracts or shares to enter a position with. Default value is 1.

{% callout type="warning" %}

This property should ONLY be set from the **OnStateChange()** method during **State.SetDefaults** or **State.Configure**.

{% /callout %}

## Syntax

**DefaultQuantity**

## Examples

```csharp
protected override void OnStateChange() 
{
    if (State == State.SetDefaults)
    {
        DefaultQuantity = 1;
    }
}
```
