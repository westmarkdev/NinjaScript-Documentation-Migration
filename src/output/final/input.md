---
title: "Input"
pathName: /docs/desktop/input
---

## Definition

The main historical data input. If implemented in the NinjaScript object, it allows for more flexibility as non-bars based series such as plot series could be passed in and drive the calculation outcomes - an example would be a custom moving average that should have the ability to operate on another moving average (i.e. the SMA) as input series.

## Property Value

An `ISeries<double>` type object that implements the `Series<double>` interface. Accessing this property via an index value `int barsAgo` returns a double value representing the price of the referenced bar.

## Syntax

```
Input
Input[int barsAgo]
```

## Examples

```csharp
// Prints the current value of input
Print(Input[0].ToString());
```

```csharp
// Prints the current type of input passed to the object, so we can detect if we're working on a price based series such as OHLCV or a derivative such as an SMA indicator
if (Input is PriceSeries)
    Print("Price Series Input");
if (Input is Indicator)
    Print("Indicator Input");
```

```csharp
// Prints the current selected price type for the input series
else if (State == State.DataLoaded)
{
    PriceSeries priceSeries = Inputs[0] as PriceSeries;
    if (priceSeries != null)
        Print("PriceType selected: " + priceSeries.PriceType);
}
```

{% callout type="tip" %}
When working with multi-series indicators, Input is not guaranteed to reference the primary [BarsInProgress](/docs/desktop/barsinprogress). Please be mindful as to when you access Input[0] as you will only be able to do so after the contextual BarsInProgress has bars. To check to ensure BarsInProgress has some bars you can use [CurrentBars](/docs/desktop/currentbars) to check.
{% /callout %}
