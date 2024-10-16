---
title: "ExitShortLimit()"
pathName: /docs/desktop/exitshortlimit
---

## Definition

Generates a buy to cover limit order to exit a short position.

## Method Return Value

An [Order](/docs/desktop/order) read-only object that represents the order. Reserved for experienced programmers, additional information can be found within the [Advanced Order Handling](/docs/desktop/advanced_order_handling) section.

## Syntax

```csharp
ExitShortLimit(double limitPrice)
```

```csharp
ExitShortLimit(int quantity, double limitPrice)
```

```csharp
ExitShortLimit(double limitPrice, string fromEntrySignal)
```

```csharp
ExitShortLimit(double limitPrice, string signalName, string fromEntrySignal)
```

```csharp
ExitShortLimit(int quantity, double limitPrice, string signalName, string fromEntrySignal)
```

The following method variation is for experienced programmers who fully understand [Advanced Order Handling](/docs/desktop/advanced_order_handling) concepts:

```csharp
ExitShortLimit(int barsInProgressIndex, bool isLiveUntilCancelled, int quantity, double limitPrice, string signalName, string fromEntrySignal)
```

## Parameters

|  |  |
| --- | --- |
| signalName | User defined signal name identifying the order generated. Max 50 characters. |
| fromEntrySignal | The entry signal name. This ties the exit to the entry and exits the position quantity represented by the actual entry. Note:  Using an empty string will attach the exit order to all entries. |
| limitPrice | The limit price of the order. |
| quantity | Entry order quantity. |
| isLiveUntilCancelled | The order will NOT expire at the end of a bar but instead remain live until the CancelOrder() method is called or its time in force is reached. |
| barsInProgressIndex | The index of the Bars object the order is to be submitted against. Used to determine what instrument the order is submitted for. See the [BarsInProgress](/docs/desktop/barsinprogress) property. |

## Examples

```csharp
protected override void OnBarUpdate()
{
    if (CurrentBar < 20)
        return;

    // Only enter if at least 10 bars has passed since our last entry
    if ((BarsSinceEntryExecution() > 10 || BarsSinceEntryExecution() == -1) && CrossBelow(SMA(10), SMA(20), 1))
        EnterShort("SMA Cross Entry");

    // Exits position
    if (CrossAbove(SMA(10), SMA(20), 1))
        ExitShortLimit(GetCurrentAsk());
}
```

{% callout type="tip" %}
Tips (also see [Overview](/docs/desktop/managed_approach)):
  
&bull; This method is ignored if a short position does not exist{% <br> %}
&bull; It is helpful to provide a signal name if your strategy has multiple exit points to help identify your exits on a chart{% <br> %}
&bull; You can tie an exit to an entry by providing the entry signal name in the parameter "fromEntrySignal"{% <br> %}
&bull; If you do not specify a quantity, the entire position is exited rendering your strategy flat{% <br> %}
&bull; If you do not specify a "fromEntrySignal" parameter, the entire position is exited rendering your strategy flat
{% /callout %}