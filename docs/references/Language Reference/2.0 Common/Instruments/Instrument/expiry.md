---
title: Expiry
pathName: expiry
parent: instrument
section: references
status: review
---

## Definition

Indicates the expiration month of a futures contract.

## Property Value

A **DateTime** structure representing the expiration month of a futures contract.

## Syntax

**Instrument.Expiry**

## Examples

```csharp

protected override void OnBarUpdate()
{
   // Print the expiry of the currently configured futures instrument
   Print(String.Format("You are viewing the {0} contract", Instrument.Expiry));
}
```

## Additional Access Information

This property can be accessed without a null reference check in the **OnBarUpdate()** event handler. When the **OnBarUpdate()** event is triggered, there will always be an **Instrument** object. Should you wish to access this property elsewhere, check for null reference first. e.g. if (**Instrument** != null)
