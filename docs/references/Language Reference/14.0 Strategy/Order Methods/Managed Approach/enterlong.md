---
title: EnterLong()
pathName: enterlong
parent: managed_approach
section: references
status: imported
---

## Definition

Generates a buy market order to enter a long position.

## Method Return Value

An **Order** read-only object that represents the order. Reserved for experienced programmers, additional information can be found within the [Advanced Order Handling](advanced_order_handling) section.

## Syntax

**EnterLong()**

**EnterLong(string signalName)**

**EnterLong(int quantity)**

**EnterLong(int quantity, string signalName)**

The following method variation is for experienced programmers who fully understand [Advanced Order Handling](advanced_order_handling) concepts:

**EnterLong(int barsInProgressIndex, int quantity, string signalName)**

{% callout type="note" %}

If using a method signature that does not have the parameter quantity, the order quantity will be taken from the quantity value set in the strategy dialog window when running or backtesting a strategy.

{% /callout %}

## Parameters

{% table %}

* Parameter
* Description

---

* **signalName**
* User defined signal name identifying the order generated. Max 50 characters.

---

* **quantity**
* Entry order quantity (if 0 is passed in, will be set to 1, except for stocks 100)

---

* **barsInProgressIndex**
* The index of the Bars object the order is to be submitted against. Used to determine what instrument the order is submitted for. See the [BarsInProgress](barsinprogress) property.

{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
     if (CurrentBar < 20)
         return;

     // Only enter if at least 10 bars has passed since our last entry
     if ((BarsSinceEntryExecution() > 10 || BarsSinceEntryExecution() == -1) && CrossAbove(SMA(10), SMA(20), 1))
         EnterLong(5, "SMA Cross Entry");
}
```
