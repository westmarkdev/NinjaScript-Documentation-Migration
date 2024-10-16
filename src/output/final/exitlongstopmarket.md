---
title: "ExitLongStopMarket()"
pathName: /docs/desktop/exitlongstopmarket
---

## Definition

Generates a sell stop market order to exit a long position.

## Method Return Value

An [Order](/docs/desktop/order) read-only object that represents the order. Reserved for experienced programmers, additional information can be found within the [Advanced Order Handling](/docs/desktop/advanced_order_handling) section.

## Syntax

```csharp
ExitLongStopMarket(double stopPrice)  
```

```csharp
ExitLongStopMarket(int quantity, double stopPrice)  
```

```csharp
ExitLongStopMarket(double stopPrice, string fromEntrySignal)  
```

```csharp
ExitLongStopMarket(double stopPrice, string signalName, string fromEntrySignal)  
```

```csharp
ExitLongStopMarket(int quantity, double stopPrice, string signalName, string fromEntrySignal)  
```

The following method variation is for experienced programmers who fully understand [Advanced Order Handling](/docs/desktop/advanced_order_handling) concepts:

```csharp
ExitLongStopMarket(int barsInProgressIndex, bool isLiveUntilCancelled, int quantity, double stopPrice, string signalName, string fromEntrySignal)  
```

## Parameters

|  |  |
| --- | --- |
| signalName | User defined signal name identifying the order generated. Max 50 characters. |
| fromEntrySignal | The entry signal name. This ties the exit to the entry and exits the position quantity represented by the actual entry. {% <br> %} **Note:** Using an empty string will attach the exit order to all entries. |
| stopPrice | The stop price of the order. |
| quantity | Entry order quantity. |
| isLiveUntilCancelled | The order will NOT expire at the end of a bar but instead remain live until the CancelOrder() method is called or its time in force is reached. |
| barsInProgressIndex | The index of the Bars object the order is to be submitted against. Used to determine what instrument the order is submitted for. {% <br> %} See the [BarsInProgress](/docs/desktop/barsinprogress) property. |

## Examples

```csharp
private double stopPrice = 0;
protected override void OnBarUpdate()
{
    if (CurrentBar < 20)
        return;

    // Only enter if at least 10 bars has passed since our last entry
    if ((BarsSinceEntryExecution() > 10 || BarsSinceEntryExecution() == -1) && CrossAbove(SMA(10), SMA(20), 1))
    {
        EnterLong("SMA Cross Entry");
        stopPrice = Low[0];
    }

    // Exits position
    ExitLongStopMarket(stopPrice);
}
```

{% callout type="tip" %}
Tips (also see [Overview](/docs/desktop/managed_approach)):

&bull; This method is ignored if a long position does not exist {% <br> %}
&bull; It is helpful to provide a signal name if your strategy has multiple exit points to help identify your exits on a chart {% <br> %}
&bull; You can tie an exit to an entry by providing the entry signal name in the parameter "fromEntrySignal" {% <br> %}
&bull; If you do not specify a quantity the entire position is exited rendering your strategy flat {% <br> %}
&bull; If you do not specify a "fromEntrySignal" parameter the entire position is exited rendering your strategy flat
{% /callout %}
