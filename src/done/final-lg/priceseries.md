---
title: "PriceSeries<double>"
pathName: priceseries
---

## Definition

Represents historical data as an `ISeries<double>` interface which can be used for custom NinjaScript object calculations.

{% callout type="note" %}
In most cases, you will access the historical price series using a core event handler such as OnBarUpdate. For more advanced developers, you may find situations where you wish to access historical price series outside of the core event methods, such as your own custom mouse click. In these advanced scenarios, you may run into situations where the barsAgo pointer is not in sync with the current bar, which may cause errors when trying to obtain this information. In those cases, please use the Bars.Get...() methods with the absolute bar index, e.g., [Bars.GetClose()](getclose), [Bars.GetOpen()](getopen), etc.
{% /callout %}

## Single `ISeries<double>`

|  |  |
| --- | --- |
| [Close](close) | A collection of historical bar close prices. |
| [High](high) | A collection of historical bar high prices. |
| [Input](input) | A collection of the main historical input values. |
| [Low](low) | A collection of historical bar low prices. |
| [Median](median) | A collection of historical bar median prices. |
| [Open](open) | A collection of historical bar open prices. |
| [Typical](typical) | A collection of historical bar typical prices. |
| [Value](value) | A collection of historical references to the first object (Values[0]) in the indicator. |
| [Weighted](weighted) | A collection of historical bar weighted prices. |

## Multi-Time Frame `ISeries<double>`

|  |  |
| --- | --- |
| [Closes](closes) | Holds an array of `ISeries<double>` objects holding historical bar close prices. |
| [Highs](highs) | Holds an array of `ISeries<double>` objects holding historical bar high prices. |
| [Inputs](inputs) | Holds an array of `ISeries<double>` objects holding main historical input values. |
| [Lows](lows) | Holds an array of `ISeries<double>` objects holding historical bar low prices. |
| [Medians](medians) | Holds an array of `ISeries<double>` objects holding historical bar median prices. |
| [Opens](opens) | Holds an array of `ISeries<double>` objects holding historical bar open prices. |
| [Typicals](typicals) | Holds an array of `ISeries<double>` objects holding historical bar typical prices. |
| [Values](values) | Holds an array of `ISeries<double>` objects holding the indicator's underlying calculated values. |
| [Weighteds](weighteds) | Holds an array of `ISeries<double>` objects holding historical bar weighted prices. |
