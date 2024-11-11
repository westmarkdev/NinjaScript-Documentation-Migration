---
title: GetSlotIndexByTime()
pathName: getslotindexbytime
parent: chartscale
section: references
status: review
---

## Definition

Returns the slot index relative to the chart control corresponding to a specified time value.

{% callout type="note" %}

Notes:

* A "Slot" is used in Equidistant [bar spacing](barspacingtype) and represents a position on the chart canvas background which may or may not contain a bar. The concept of "Slots" does NOT exist on a TimeBased bar spacing type.  
* If you are looking for information on a bar series, please see [ChartBars.GetBarIdxByTime()](chartbars_getbaridxbytime).
{% /callout %}

## Method Return Value

A double representing a slot index.

## Syntax

**<`chartcontrol>**.GetSlotIndexByTime(**DateTime** time)

{% callout type="warning" %}

Warning: This method CANNOT be called on BarSpacingType.TimeBased charts. You will need to ensure an Equidistant [bar spacing type](barspacingtype) is used, otherwise errors will be thrown.

{% /callout %}

## Method Parameters

{% table %}

* Parameter
* Description

---

* **time**
* A [DateTime](https://msdn.microsoft.com/en-us/library/system.datetime(v=vs.110).aspx) Structure used to determine a slot index
{% /table %}

## Examples

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
