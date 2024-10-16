---
title: "Volume"
pathName: /docs/desktop/iseries_volume
---

## Definition

A collection of historical bar volume values.

{% callout type="note" %}
For working with [Cryptocurrency instruments](/docs/desktop/instrumenttype) which report volume fractional, please use the [VOL()](/docs/desktop/volume) indicator series, or store the volume for your script in a custom variable and convert alongside our [VOL()](/docs/desktop/volume) indicator (Instrument.MasterInstrument.InstrumentType == InstrumentType.CryptoCurrency ? Core.Globals.ToCryptocurrencyVolume((long)Volume[0]) : Volume[0]).
{% /callout %}

## Property Value

An `ISeries<double>` object. Accessing this property via an index `int barsAgo` returns a double value representing the volume of the referenced bar.

## Syntax

```csharp
Volume
Volume[int barsAgo]
```

## Examples

```csharp
// OnBarUpdate method
protected override void OnBarUpdate()
{
    // Is current volume greater than twice the prior bar's volume
    if (Volume[0] > Volume[1] * 2)
        Print("We have increased volume");
    
    // Is the current volume greater than the 20 period moving average of volume
    if (Volume[0] > SMA(Volume, 20)[0])
        Print("Increasing volume");
}
```
