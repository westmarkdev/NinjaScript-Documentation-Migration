---
title: "Removing Draw Objects from the Chart"
pathName: /docs/desktop/removing_draw_objects_from_the
---

Drawing objects can be used for a number of different purposes, like keeping track of where a strategy has its entry point, profit target, and stop loss. If a strategy draws an object(s) for every trade it takes, the chart could quickly become cluttered. This sample will show how to remove the objects that aren't necessary anymore.

{% callout type="note" %}
This is a real-time only strategy. Please view this strategy on a real-time data connection or the Simulated Data Feed.
{% /callout %}

## Key Concepts in This Example

- Drawing lines at the price where the orders are that extend for the duration of the trade
- Removing those lines when the trade is over

## Important Related Documentation

- [Draw](/docs/desktop/drawing)
- [Line()](/docs/desktop/line)
- [RemoveDrawObject()](/docs/desktop/removedrawobject)
- [RemoveDrawObjects()](/docs/desktop/removedrawobjects)
- [CrossAbove()](/docs/desktop/crossabove)
- [CrossBelow()](/docs/desktop/crossbelow)

## Import Instructions

1. Download the file contained in this Help Guide topic to your PC desktop
2. From the Control Center window, select the menu Tools > Import > NinjaScript
3. Select the downloaded file

[SampleRemoveDrawObjects_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleRemoveDrawObjects_NT8.zip)
