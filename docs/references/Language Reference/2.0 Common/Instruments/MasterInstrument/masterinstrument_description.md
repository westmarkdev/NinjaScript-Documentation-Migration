---
title: Description
pathName: description
parent: masterinstrument
section: references
status: review
---

## Definition

Indicates the description configured for the **Master Instrument properties**.

## Property Value

A **string** value which is configured for the current master instrument.

## Syntax

**Bars.Instrument.MasterInstrument.Description**

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Displays the master instrument's description at the bottom right of the chart
    Draw.TextFixed(this, "tag1", Bars.Instrument.MasterInstrument.Description, TextPosition.BottomRight);
}
```
