---
title: "Exchange"
pathName: /docs/desktop/exchange
---

## Definition

Indicates the current exchange of an instrument.

## Property Value

Represents the exchange which is selected for the current instrument.

## Syntax

`Instrument.Exchange`

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Print the exchange of the currently configured instrument
    Print(String.Format("Configured instrument is on the {0} exchange", Instrument.Exchange));
}
```

## Additional Access Information

This property can be accessed without a null reference check in the `OnBarUpdate()` event handler. When the `OnBarUpdate()` event is triggered, there will always be an `Instrument` object. Should you wish to access this property elsewhere, check for null reference first, e.g., `if (Instrument != null)`.
