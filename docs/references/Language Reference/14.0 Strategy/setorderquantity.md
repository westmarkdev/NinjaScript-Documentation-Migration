---
title: SetOrderQuantity
pathName: setorderquantity
parent: strategy
section: references
status: imported
---

## Definition

Determines how order sizes are calculated for a given strategy.

## Property Value

An enum determining how order quantities are set. Default value is set to **SetOrderQuantity.Strategy**.

Possible values are:

{% table %}

---

* **SetOrderQuantity.DefaultQuantity** | User defined order size based on the [DefaultQuantity](defaultquantity) property
* **SetOrderQuantity.Strategy** | Takes the order size specified programmatically within the strategy
{% /table %}

{% callout type="warning" %}

This property should ONLY be set from the **OnStateChange()** method during State.SetDefaults or State.Configure.

{% /callout %}

## Syntax

**SetOrderQuantity**

## Examples

```csharp
protected override void OnStateChange()
{
     if (State == State.Configure)
     {
         SetOrderQuantity = SetOrderQuantity.DefaultQuantity; // calculate orders based off default size
     }
}
```
