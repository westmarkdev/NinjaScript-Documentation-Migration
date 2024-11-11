---
title: IgnoreOverfill
pathName: ignoreoverfill
parent: unmanaged_approach
section: references
status: double_check
lg2m: true
---

## Definition

An **unmanaged order property** which defines the behavior of a strategy when an overfill is detected. An overfill is categorized as when an order returns a "Filled" or "PartFilled" state after the order was already marked for cancellation. The cancel request could have been induced by an explicit **CancelOrder()** call, from more implicit cancellations like those that occur when another order sharing the same OCO ID is filled, or from things like order expiration.

{% callout type="critical" %}

* Setting this property value to true can have serious adverse effects on a running strategy unless you have programmed your own overfill handling.
* User defined overfill handling is advanced and should ONLY be addressed by experienced programmers. Additional information can be found on overfills in the [Unmanaged approach](unmanaged_approach).
{% /callout %}

## Property Value

This property returns true if the strategy will ignore overfills; otherwise, false. Default is set to false.

{% callout type="warning" %}

This property should ONLY be set from the **OnStateChange()** method during State.SetDefaults or State.Configure.

{% /callout %}

## Syntax

**IgnoreOverfill**

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        // Allows for custom overfill handling
        IgnoreOverfill = true;
    }
}
```
