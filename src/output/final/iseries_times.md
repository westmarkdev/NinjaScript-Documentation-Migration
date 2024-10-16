---
title: "Times"
pathName: /docs/desktop/iseries_times
---

## Definition

Holds an array of `ISeries<datetime>` objects holding historical bar times. An `ISeries<datetime>` object is added to this array when calling the [AddDataSeries()](/docs/desktop/adddataseries) method. Its purpose is to provide access to the times of all Bars objects in a multi-instrument or multi-time frame script.

## Property Value

An array of `ISeries<datetime>` objects.

## Syntax

```csharp
Times[int barSeriesIndex][int barsAgo]
```

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.Configure)
    {
        // Adds a 5-minute Bars object to the strategy and is automatically assigned
        // a Bars object index of 1 since the primary data the strategy is run against
        // set by the UI takes the index of 0.
        AddDataSeries("AAPL", BarsPeriodType.Minute, 5);
    }
}

protected override void OnBarUpdate()
{
    // Compares the primary bar's time to the 5-minute bar's time
    if (Times[0][0].Ticks > Times[1][0].Ticks)
        Print("The current bar's time is greater");
}
```

