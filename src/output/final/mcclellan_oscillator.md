---
title: "McClellan Oscillator"
pathName: /docs/desktop/mcclellan_oscillator
---

## Description

McClellan Oscillator is the difference between two exponential moving averages of the NYSE advance decline spread. This indicator requires ADV and DECL index data.

## Syntax

```csharp
McClellanOscillator(int fastPeriod, int slowPeriod)  
```

```csharp
McClellanOscillator(ISeries<double> input, int fastPeriod, int slowPeriod)  
```

## Return Value

`double`; Accessing this method via an index value `[int barsAgo]` returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([Valid Input Data for Indicator](/docs/desktop/valid_input_data_for_indicator)) |
| fastPeriod | Number of bars used in the fast moving average calculation |
| slowPeriod | Number of bars used in the slow moving average calculation |

## Examples

```csharp
// An ADV and DECL data series must be added to OnStateChange()
else if (State == State.Configure)
{
    AddDataSeries("^ADV");
    AddDataSeries("^DECL");
}
// Prints the current value of the McClellan Oscillator with a 19 fast period moving average & 39 slow period
double value = McClellanOscillator(19, 39)[0];
Print("The current McClellan Oscillator value is " + value.ToString());
```
