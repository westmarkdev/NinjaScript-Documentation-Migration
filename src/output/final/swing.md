---
title: "Swing"
pathName: /docs/desktop/swing
---

## Description

The Swing indicator will plot lines that represent the swing points based on the strength (number of bars to the left and right of the swing point) parameter provided. It's mostly a visual tool and not meant to be predictive in nature. Only after the strength number of bars has passed since the extreme point, the swing return value could be definitely set. Thus, the indicator updates its calculations as new incoming data warrants so.

You can access methods within this indicator to determine the number of bars ago a swing point occurred or the current swing value.

{% callout type="tip" %}
To work around the situation where the indicator has to recalculate, you could only access the SwingHigh / Low values from the number of swing strength bars ago - those values are calculated in their final state.
{% /callout %}

## Syntax - Bars Ago

### High Bar

```csharp
Swing(int strength).SwingHighBar(int barsAgo, int instance, int lookBackPeriod)
Swing(ISeries<double> input, int strength).SwingHighBar(int barsAgo, int instance, int lookBackPeriod)
```

### Low Bar

```csharp
Swing(int strength).SwingLowBar(int barsAgo, int instance, int lookBackPeriod)
Swing(ISeries<double> input, int strength).SwingLowBar(int barsAgo, int instance, int lookBackPeriod)
```

## Return Value

An `int` value representing the number of bars ago. Returns a value of -1 if a swing point is not found within the look back period.

## Syntax - Value

### High Value

```csharp
Swing(int strength).SwingHigh[int barsAgo]
Swing(ISeries<double> input, int strength).SwingHigh[int barsAgo]
```

### Low Value

```csharp
Swing(int strength).SwingLow[int barsAgo]
Swing(ISeries<double> input, int strength).SwingLow[int barsAgo]
```

## Return Value

`double`; Accessing this method via an index value `[int barsAgo]` returns the indicator value of the referenced bar.

- A return value of 0 (zero) will be returned if the CurrentBar number is less than the "strength" value or a swing pivot has not yet been found.

## Parameters

|  |  |
| --- | --- |
| barsAgo | The number of bars ago that serves as the starting bar from which to work backwards |
| input | Indicator source data ([Valid Input Data for Indicator](/docs/desktop/valid_input_data_for_indicator)) |
| instance | The occurrence to check for (1 is the most recent, 2 is the 2nd most recent, etc...) |
| lookBackPeriod | Number of bars to look back to check for the test condition, which is evaluated on the current bar and the bars in the look back period. |
| strength | The number of required bars to the left and right of the swing point |

## Example

```csharp
// Prints the high price of the most recent swing high
Print("The high of the swing bar is " + High[Math.Max(0, Swing(5).SwingHighBar(0, 1, 10))]);
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.

