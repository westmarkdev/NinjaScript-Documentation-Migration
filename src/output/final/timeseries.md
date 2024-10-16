---
title: "TimeSeries<datetime>"
pathName: /docs/timeseries
---

## Definition

Represents historical time stamps as an ISeries<datetime> interface which can be used for custom NinjaScript object calculations.

{% callout type="note" %}
In most cases, you will access the historical time series using a core event handler such as OnBarUpdate. For more advanced developers, you may find situations where you wish to access historical time series outside of the core event methods, such as your own custom mouse click. In these advanced scenarios, you may run into situations where the barsAgo pointer is not in sync with the current bar, which may cause errors when trying to obtain this information. In those cases, use the Bars.Get...() methods with the absolute bar index, e.g., [Bars.GetTime()](/docs/desktop/gettime), etc.
{% /callout %}

## Single ISeries<datetime>

|  |  |
| --- | --- |
| Time | A collection of historical bar time stamp values. |

## Multi-Time Frame ISeries<datetime>

|  |  |
| --- | --- |
| Times | Holds an array of ISeries<datetime> objects holding historical bar times. |
