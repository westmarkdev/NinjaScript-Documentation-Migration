---
title: IsFirstBarOfSessionByIndex()
pathName: isfirstbarofsessionbyindex
parent: bars
section: references
status: review
---

## Definition

Indicates if the selected bar index value is the first bar of a trading session.

## Property Value

This property returns true if the bar is the first bar of a session; otherwise, false. This property is read-only.

## Syntax

**Bars.IsFirstBarOfSessionByIndex**(int **index**)

## Warning

{% callout type="warning" %}

This property will always return false on non-intraday bar periods (e.g., Day, Month, etc).

{% /callout %}

## Parameters

{% table %}

---

* **index**
* An int representing an absolute bar index value
{% /table %}

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
    base.OnRender(chartControl, chartScale);
    // loop through only the rendered bars on the chart 
    for(int barIndex = ChartBars.FromIndex; barIndex <= ChartBars.ToIndex; barIndex++)
    {
        // check if the rendered bar is the first bar of the trading session
        if (Bars.IsFirstBarOfSessionByIndex(barIndex))
        {
            DateTime slotTimeAtBarIndex = chartControl.GetTimeBySlotIndex(barIndex);
            Print(string.Format("Bar index {0} was the first bar of the session at slot time {1}.", barIndex, slotTimeAtBarIndex));
        }
    }
}
```
