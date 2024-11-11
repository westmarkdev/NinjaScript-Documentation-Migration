---
title: Count
pathName: count
parent: onbarupdate
section: references
status: review
---

## Definition

The total number of bars or data points.

## Property Value

An **int** value representing the total number of bars.

## Syntax

**Count**

## Examples

```csharp
//If there are less than 365 bars on the chart, text indicates how many bars are on the chart
if (Count < 365)
{
  Draw.TextFixed(this, "tag1", "There are " + Count + " bars on the chart", TextPosition.BottomRight);
}
```

{ %callout type="note" %}

[CurrentBar](currentbar) value is guaranteed to be <= Count - 1. This is because of the NinjaTrader multi-threaded architecture, the Count value can have additional bars as inflight ticks come in to the system.

{% /callout %}
