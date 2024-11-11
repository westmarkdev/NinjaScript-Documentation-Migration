---
title: BarsSinceExitExecution()
pathName: barssinceexitexecution
parent: strategy
section: references
status: imported
---

## Definition

Returns the number of bars that have elapsed since the last exit. When a signal name is provided, the number of bars that have elapsed since that last specific exit will be returned.

## Method Return Value

An **int** value that represents a number of bars. A value of -1 will be returned if a previous exit does not exist.

## Syntax

**BarsSinceExitExecution()**

**BarsSinceExitExecution(string signalName)**

The following method signature should be used when working with [multi-time frame and instrument strategies](multi_time_frame_instruments.md):

BarsSinceExitExecution(int barsInProgressIndex, string signalName, int exitExecutionsAgo)

{% callout type="note" %}

When working with a multi-series strategy the BarsSinceExitExecution() will return you the elapsed bars as determined by the first Bars object for the instrument specified in the barsInProgressIndex.

{% /callout %}

## Parameters

{% table %}

* signalName
* The signal name of an exit order specified in an order exit method.

---

* barsInProgressIndex
* The index of the Bars object the entry order was submitted against. See the [BarsInProgress](barsinprogress) property.

---

* exitExecutionsAgo
* Number of exit executions ago. Pass in 0 for the number of bars since the last exit execution.
{% /table %}

{% callout type="note" %}

Please see [SetStopLoss()](setstoploss), [SetProfitTarget()](setprofittarget) or [SetTrailStop()](settrailstop) for their corresponding signal name

{% /callout %}

## Examples

```csharp
protected override void OnBarUpdate()
{ 
   if (CurrentBar < BarsRequiredToTrade) 
       return; 

   // Only enter if at least 10 bars has passed since our last exit or if we have never traded yet
   if ((BarsSinceExitExecution() > 10 || BarsSinceExitExecution() == -1) && CrossAbove(SMA(10), SMA(20), 1))
       EnterLong();
}
```
