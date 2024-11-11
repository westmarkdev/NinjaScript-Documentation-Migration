---
title: GetInstrument()
pathName: getinstrument
parent: instrument
section: references
status: review
---

## Definition

Returns an **Instrument** object by the master instrument name configured in the database.

{% callout type="note" %}

This method does NOT add additional data for real-time or historical processing. For adding additional data to your script, please see the **AddDataSeries()** method.

{% /callout %}

## Method Return Value

An **Instrument** object

## Syntax

**Instrument.GetInstrument(string instrumentName)**

## Parameters

{% table %}

---

* **instrumentName**
* A **string** value representing a name of an instrument
{% /table %}

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.Historical)
    {
        Instrument myInstrument = Instrument.GetInstrument("AAPL");

        Print("AAPL's tick size is " + myInstrument.MasterInstrument.TickSize.ToString());
    }
}
```
