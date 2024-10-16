---
title: "BarsSinceEntryExecution()"
pathName: /docs/desktop/barssinceentryexecution
---

## Definition

Returns the number of bars that have elapsed since the last entry. When a signal name is provided, the number of bars that have elapsed since that last specific entry will be returned.

## Method Return Value

An `int` value that represents a number of bars. A value of -1 will be returned if a previous entry does not exist.

### Syntax

```csharp
BarsSinceEntryExecution()
BarsSinceEntryExecution(string signalName)
```

The following method signature should be used when working with [multi-time frame and instrument strategies](/docs/desktop/multi-time_frame__instruments):

```csharp
BarsSinceEntryExecution(int barsInProgressIndex, string signalName, int entryExecutionsAgo)
```

{% callout type="note" %}
When working with a multi-series strategy the BarsSinceEntryExecution() will return you the elapsed bars as determined by the first Bars object for the instrument specified by the barsInProgressIndex.
{% /callout %}

## Parameters

|  |  |
| --- | --- |
| signalName | The signal name of an entry order specified in an order entry method. |
| barsInProgressIndex | The index of the Bars object the entry order was submitted against. {% <br> %} Note: See the [BarsInProgress](/docs/desktop/barsinprogress) property. |
| entryExecutionsAgo | Number of entry executions ago. Pass in 0 for the number of bars since the last entry execution. |

## Examples

```csharp
protected override void OnBarUpdate()
{
    if (CurrentBar < BarsRequiredToTrade)
        return;

    // Only enter if at least 10 bars has passed since our last entry
    if ((BarsSinceEntryExecution() > 10 || BarsSinceEntryExecution() == -1) && CrossAbove(SMA(10), SMA(20), 1))
        EnterLong();
}
```

