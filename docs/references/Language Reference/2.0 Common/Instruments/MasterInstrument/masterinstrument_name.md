---
title: Name
pathName: masterinstrument
parent: masterinstrument
section: references
status: review
---

## Definition

Indicates the NinjaTrader database name of an instrument. For example, "MSFT", "ES", "NQ" etc...

## Property Value

A string representing the name of the instrument.

## Syntax

**Instrument.MasterInstrument.Name**

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Displays the master instrument's name at the bottom right of the chart**
    Draw.TextFixed(this, "tag1", Bars.Instrument.MasterInstrument.Name, TextPosition.BottomRight);
}
```

## Additional Access Information

This property can be accessed without a null reference check in the **OnBarUpdate()** event handler. When the **OnBarUpdate()** event is triggered, there will always be an **Instrument** object. Should you wish to access this property elsewhere, check for null reference first. e.g. **if (Instrument != null)**