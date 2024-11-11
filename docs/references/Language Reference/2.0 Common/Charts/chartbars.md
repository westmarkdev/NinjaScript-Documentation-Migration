---
title: ChartBars
pathName: chartbars
parent: charts
section: references
status: check
---

The **ChartBars** class provides GUI access related methods and properties to the primary bars series configured on the Chart through the [Data Series](working_with_price_data) menu. For data access information related to the NinjaScript input's bars series, please use the [Bars Series](bars) object (or the [BarsArray](barsarray) for multi-series input).

{% callout type="note" %}

A ChartBars object will ONLY exist should the hosting NinjaScript type be loaded through a [Chart](chart). For example, a Strategy would have access to a ChartBars property when running on a Chart, but would NOT when loaded through the [Strategies Grid](strategies_tab2) or [Strategy analyzer](strategy_analyzer).

{% /callout %}

![ChartBars](chartbars.png)

{% callout type="warning" %}

It is crucial to check for object references before accessing the ChartBars otherwise possible null reference errors can be expected depending on where the NinjaScript object was started. See example below.

{% /callout %}

## Methods and Properties

{% table %}

* Method/Property
* Description

---

* [Bars](chartbars_bars)
* Data returned from the historical data repository.

---

* [Count](chartbars_count)
* The total number of ChartBars that exist on the chart.

---

* [FromIndex](chartbars_fromindex)
* An index value representing the first bar painted on the chart.

---

* [GetBarIdxByTime()](chartbars_getbaridxbytime)
* An ChartBar index value calculated from a time value on the chart.

---

* [GetBarIdxByX()](chartbars_getbaridxbyx)
* Returns the ChartBar index value at a specified x-coordinate relative to the ChartControl.

---

* [GetTimeByBarIdx()](chartbars_gettimebybaridx)
* The ChartBars time value calculated from a bar index value on the chart.

---

* [Panel](chartbars_panel)
* The Panel index value that the ChartBars reside.

---

* [Properties](chartbars_properties)
* Various ChartBar properties that have been configured from the Chart's [Data Series](working_with_price_data) menu.

---

* [ToChartString()](chartbars_tochartstring)
* A string formatted for the Chart's Data Series Label as well as the period.

---

* [ToIndex](chartbars_toindex)
* An index value representing the last bar painted on the chart.
{% /table %}

## Examples

```csharp
protected override void OnStateChange()
{         
   if (State == State.DataLoaded)
   {
     if(ChartBars != null)
     {
         Print("The starting number of bars on the chart is " + ChartBars.Bars.Count);
     }
     else 
     {
         Print("Strategy was not loaded from a chart, exiting strategy...");
         return;
     }
   }
}
```
