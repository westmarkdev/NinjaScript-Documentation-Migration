---
title: OnExecutionUpdate()
pathName: onexecutionupdate
parent: strategy
section: references
status: double_check
lg2m: true
---

## Definition

An event driven method which is called on an incoming execution of an order managed by a strategy. An execution is another name for a fill of an order.

* An order can generate multiple executions (partial fills)
* **OnExecutionUpdate** is typically called after [**OnOrderUpdate()**](onorderupdate)
* Only orders which have been submitted and managed by the strategy will call **OnExecutionUpdate()**
* Executions drive the strategy [**Position**](position) object, which is updated when this method is called

{% callout type="note" %}

* Programming in this environment is reserved for the more [advanced user](advanced_order_handling). If you are for example looking to protect a strategy managed position with a basic stop and target, then the [**Set() methods**](managed_approach) would be more convenient.
* When connected to the Playback connection, it is possible for **OnExecutionUpdate()** to trigger in the middle of a call to **OnBarUpdate()**. The Sim101 account adds a simulated random delay for processing execution events, but the Playback connection triggers executions immediately, for the sake of consistency in backtesting. Because of this, **OnExecutionUpdate()** can appear to be triggered earlier than it would in live trading, or when simulation trading on a live connection.
* Please also review [**Multi-Thread Considerations for NinjaScript**](multi_threading_consideration_for_ninjascript).
* Its best practice to only work with the passed by value parameters and not reference parameters. This insures that you process each change of the underlying state.
* Rithmic and Interactive Brokers Users: When using a NinjaScript strategy it is best practice to only work with passed by value data from **OnExecutionUpdate()**. Instances of multiple fills at the same time for the same instrument might result in an incorrect **OnPositionUpdate**, as sequence of events are not guaranteed due to provider API design.
{% /table %}

## Method Return Value

This method does not return a value.

## Syntax

You must override the method in your strategy with the following syntax:

**protected override void OnExecutionUpdate(Execution execution, string executionId, double price, int quantity, MarketPosition marketPosition, string orderId, DateTime time)**

## Parameters

{% table %}

---

* **execution**
* An [**Execution**](execution) object passed by reference representing the execution

---

* **executionId**
* A **string** value representing the execution id

---

* **price**
* A **double** value representing the execution price

---

* **quantity**
* An **int** value representing the execution quantity

---

* **marketPosition**
* A [**MarketPosition**](position_marketposition) object representing the position of the execution. Possible values are:
  * **MarketPosition.Long**
  * **MarketPosition.Short**

---

* **orderId**
* A string representing the order id

---

* **time**
* A [**DateTime**](http://msdn.microsoft.com/en-us/library/system.datetime.aspx) value representing the time of the execution

{% /table %}

## Examples

{% callout type="note" %}

**OnExecutionUpdate** Example (See [**SampleOnOrderUpdate**](using_onorderupdate_and_onexec) for complete example)
{% /callout %}

```csharp
private Order entryOrder = null; // This variable holds an object representing our entry order
private Order stopOrder = null; // This variable holds an object representing our stop loss order
private Order targetOrder = null; // This variable holds an object representing our profit target order
private int sumFilled = 0; // This variable tracks the quantities of each execution making up the entry order

protected override void OnExecutionUpdate(Execution execution, string executionId, double price, int quantity, MarketPosition marketPosition, string orderId, DateTime time)
{
    /* We advise monitoring OnExecutionUpdate() to trigger submission of stop/target orders instead of OnOrderUpdate() since OnExecution() is called after OnOrderUpdate()
    which ensures your strategy has received the execution which is used for internal signal tracking. */
    if (entryOrder != null && entryOrder == execution.Order)
    {
        if (execution.Order.OrderState == OrderState.Filled || execution.Order.OrderState == OrderState.PartFilled || (execution.Order.OrderState == OrderState.Cancelled && execution.Order.Filled > 0))
        {
            // We sum the quantities of each execution making up the entry order
            sumFilled += execution.Quantity;

            // Submit exit orders for partial fills
            if (execution.Order.OrderState == OrderState.PartFilled)
            {
                stopOrder = ExitLongStopMarket(0, true, execution.Order.Filled, execution.Order.AverageFillPrice - 4 * TickSize, "MyStop", "MyEntry");
                targetOrder = ExitLongLimit(0, true, execution.Order.Filled, execution.Order.AverageFillPrice + 8 * TickSize, "MyTarget", "MyEntry");
            }
            // Update our exit order quantities once orderstate turns to filled and we have seen execution quantities match order quantities
            else if (execution.Order.OrderState == OrderState.Filled && sumFilled == execution.Order.Filled)
            {
                // Stop-Loss order for OrderState.Filled
                stopOrder = ExitLongStopMarket(0, true, execution.Order.Filled, execution.Order.AverageFillPrice - 4 * TickSize, "MyStop", "MyEntry");
                targetOrder = ExitLongLimit(0, true, execution.Order.Filled, execution.Order.AverageFillPrice + 8 * TickSize, "MyTarget", "MyEntry");
            }

            // Resets the entryOrder object and the sumFilled counter to null / 0 after the order has been filled
            if (execution.Order.OrderState != OrderState.PartFilled && sumFilled == execution.Order.Filled)
            {
                entryOrder = null;
                sumFilled = 0;
            }
        }
    }

    // Reset our stop order and target orders' Order objects after our position is closed. (1st Entry)
    if ((stopOrder != null && stopOrder == execution.Order) || (targetOrder != null && targetOrder == execution.Order))
    {
        if (execution.Order.OrderState == OrderState.Filled || execution.Order.OrderState == OrderState.PartFilled)
        {
            stopOrder = null;
            targetOrder = null;
        }
    }
}
```

## Additional Reference Samples

Additional reference code samples are available in the NinjaScript Educational Resources section of our support forum.
