---
title: "CrossAbove()"
pathName: /docs/desktop/crossabove
---

## Definition

Evaluates a cross above condition over the specified bar look-back period.

{% callout type="note" %}
This method does not return true if both series being compared have equal values on the current or previous bar with a lookbackPeriod of 1.
{% /callout %}

## Method Return Value

This method returns true if a cross above condition occurred; otherwise, false.

## Syntax

```csharp
CrossAbove(ISeries<double> series1, ISeries<double> series2, int lookBackPeriod)
```

## CrossAbove(ISeries<double> series1, double value, int lookBackPeriod)

## Parameters

|  |  |
| --- | --- |
| lookBackPeriod | Number of bars back to check the cross above condition |
| series1 & series2 | Any Series<double> type object such as an indicator, Close, High, Low, etc... |
| value | Any double value |

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Go short if CCI crossed above 250 within the last bar
    if (CrossAbove(CCI(14), 250, 1))
        EnterShort();
    // Go long if 10 EMA crosses above 20 EMA within the last bar
    if (CrossAbove(EMA(10), EMA(20), 1))
        EnterLong();
    // Go long if we have an up bar and the 10 EMA crosses above 20 EMA within the last 5 bars
    if (Close[0] > Open[0] && CrossAbove(EMA(10), EMA(20), 5))
        EnterLong();
}
```
