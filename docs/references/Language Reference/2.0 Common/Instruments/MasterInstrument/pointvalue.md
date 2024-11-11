---
title: PointValue
pathName: pointvalue
parent: masterinstrument
section: references
status: review
---

## Definition

Indicates the currency value of 1 full point of movement. For example, 1 point in the **S&P 500 Emini** futures contract (ES) is $50 USD which is equal to $12.50 USD per tick.

## Property Value

A **double** value representing the currency value of 1 point of movement.

## Syntax

**Instrument.MasterInstrument.PointValue**

## Examples

```csharp
// protected override void OnBarUpdate()
{
    // Displays the master instrument's point value at the bottom right of the chart
    Draw.TextFixed(this, "Point value: ", Bars.Instrument.MasterInstrument.PointValue.ToString(), TextPosition.BottomRight);
}
```

## Additional Access Information

This property can be accessed without a null reference check in the **OnBarUpdate()** event handler. When the **OnBarUpdate()** event is triggered, there will always be an **Instrument** object. Should you wish to access this property elsewhere, check for null reference first. e.g. if (**Instrument** != null)
