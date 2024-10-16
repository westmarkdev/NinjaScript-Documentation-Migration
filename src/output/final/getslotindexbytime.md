---
title: "GetSlotIndexByTime()"
pathName: /docs/desktop/getslotindexbytime
---

## Definition

Returns the slot index relative to the chart control corresponding to a specified time value.

{% callout type="note" %}
• A "Slot" is used in Equidistant [bar spacing](/docs/desktop/barspacingtype) and represents a position on the chart canvas background which may or may not contain a bar. The concept of "Slots" does NOT exist on a Time-Based bar spacing type.  
• If you are looking for information on a bar series, please see [ChartBars.GetBarIdxByTime()](/docs/desktop/chartbars_getbaridxbytime)
{% /callout %}

## Method Return Value

A double representing a slot index.

### Syntax

```
## <chartcontrol>.GetSlotIndexByTime(DateTime time)
```

{% callout type="warning" %}
This method CANNOT be called on BarSpacingType.TimeBased charts. You will need to ensure an Equidistant [bar spacing type](/docs/desktop/barspacingtype) is used, otherwise errors will be thrown.
{% /callout %}

## Method Parameters

|  |  |
| --- | --- |
| time | A [DateTime](https://msdn.microsoft.com/en-us/library/system.datetime(v=vs.110).aspx) Structure used to determine a slot index |

## Example

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
    // ensure that GetSlotIndexByTime is called on TimeBased charts
    if(chartControl.BarSpacingType != BarSpacingType.TimeBased)
    {
        // get the slot index of the first time painted on the chart
        double slotIndex = chartControl.GetSlotIndexByTime(chartControl.FirstTimePainted);
        Print(slotIndex);
    }
}
```
