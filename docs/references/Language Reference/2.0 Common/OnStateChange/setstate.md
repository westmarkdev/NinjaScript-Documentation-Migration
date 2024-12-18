---
title: SetState()
pathName: setstate
parent: onstatechange
section: references
status: review
---

## Definition

This method is used for changing the **State** of any running NinjaScript object.

{% callout type="note" %}

Notes:

* Attempting to set a State earlier than the current State will be ignored.
* Calling **SetState()** multiple times will be ignored to prevent the object from erroneously setting states unexpectedly.
* Setting State to **State.Terminated** is meant as a way to abort the strategy as it is running. Doing this in a Strategy Analyzer backtest will abort the backtest entirely, and no partial backtest results will be shown.
* After setting **State.Terminated**, you should return from the calling method to help ensure subsequent logic is not processed asynchronously to **OnStateChange()**.
{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

**SetState(State state)**

{% callout type="warning" %}

This method should only be called after the **State** reaches **State.DataLoaded**.

{% /callout %}

## Parameters

{% table %}

* Parameter
* Description

---

* **state**
* The **State** to be set
{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
   // Terminate strategy at 2PM
   if (ToTime(Time[0]) == 140000)
   {
     SetState(State.Terminated);
     return;
   }
}
```
