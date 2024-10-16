---
title: "EnterLongStopLimit()"
pathName: /docs/desktop/enterlongstoplimit
---

## Definition

Generates a buy stop limit order to enter a long position.

## Method Return Value

An [Order](/docs/desktop/order) read-only object that represents the order. Reserved for experienced programmers, additional information can be found within the [Advanced Order Handling](/docs/desktop/advanced_order_handling) section.

## Syntax

```csharp
EnterLongStopLimit(double limitPrice, double stopPrice)  
EnterLongStopLimit(double limitPrice, double stopPrice, string signalName)  
EnterLongStopLimit(int quantity, double limitPrice, double stopPrice)  
EnterLongStopLimit(int quantity, double limitPrice, double stopPrice, string signalName)  
EnterLongStopLimit(int barsInProgressIndex, bool isLiveUntilCancelled, int quantity, double limitPrice, double stopPrice, string signalName)
```

{% callout type="note" %}
If using a method signature that does not have the parameter quantity, the order quantity will be taken from the quantity value set in the strategy dialog window when running or backtesting a strategy.
{% /callout %}

## Parameters

|  |  |
| --- | --- |
| signalName | User defined signal name identifying the order generated. Max 50 characters. |
| limitPrice | The limit price of the order. |
| stopPrice | The stop price of the order. |
| quantity | Entry order quantity (if 0 is passed in, will be set to 1, except for stocks 100). |
| isLiveUntilCancelled | The order will NOT expire at the end of a bar, but instead remain live until the [CancelOrder()](/docs/desktop/managed_cancelorder) method is called or its time in force is reached. |
| barsInProgressIndex | The index of the Bars object the order is to be submitted against. Used to determine what instrument the order is submitted for. See the [BarsInProgress](/docs/desktop/barsinprogress) property. |

## Examples

```csharp
protected override void OnBarUpdate()
{
    if (CurrentBar < 20)
        return;

    // Only enter if at least 10 bars have passed since our last entry
    if ((BarsSinceEntryExecution() > 10 || BarsSinceEntryExecution() == -1) && CrossAbove(SMA(10), SMA(20), 1))
        EnterLongStopLimit(High[0] + 2 * TickSize, High[0], "SMA Cross Entry");
}
```
