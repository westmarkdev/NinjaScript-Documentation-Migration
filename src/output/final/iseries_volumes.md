---
title: "Volumes"
pathName: /docs/desktop/iseries_volumes
---

## Definition

Holds an array of `ISeries<double>` objects holding historical bar volumes. An `ISeries<double>` object is added to this array when calling the [AddDataSeries()](/docs/desktop/adddataseries) method. Its purpose is to provide access to the volumes of all Bars objects in a multi-instrument or multi-time frame script.

{% callout type="note" %}
For working with [Cryptocurrency instruments](/docs/desktop/instrumenttype) which report volume fractional, please use the [VOL()](/docs/desktop/volume) indicator series, or store the volume for your script in a custom variable and convert alongside our [VOL()](/docs/desktop/volume) indicator (Instrument.MasterInstrument.InstrumentType == InstrumentType.CryptoCurrency ? Core.Globals.ToCryptocurrencyVolume((long)Volume[0]) : Volume[0]).
{% /callout %}

## Property Value

An array of `ISeries<double>` objects.

### Syntax

```csharp
Volumes[int barSeriesIndex][int barsAgo]
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
    // Compares the primary bar's volume to the 5-minute bar's volume
    if (Volumes[0][0] > Volumes[1][0])
        Print("The primary bar's volume is greater");
}
```
