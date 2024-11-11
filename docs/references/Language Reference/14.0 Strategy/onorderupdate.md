---
title: OnOrderUpdate()
pathName: onorderupdate
parent: strategy
section: references
status: added
---

## Definition

An event driven method which is called each time an order managed by a strategy changes state. An order will change state when a change in order quantity, price or state (working to filled) occurs. You can use this method to program your own **order rejection handling**.

{% callout type="note" %}

* Only orders which have been submitted and managed by the strategy will call **OnOrderUpdate()**.
* Programming in this environment is reserved for the more **advanced user**. If you are for example looking to protect a strategy managed position with a basic stop and target, then the **Set() methods** would be more convenient.
* For triggering actions such as the submission of a stop loss order and target order using custom OCO logic when your entry order is filled, we recommend working directly in **OnExecutionUpdate()** instead.
* **OnOrderUpdate()** will run inside of order methods such as **EnterLong()** or **SubmitOrderUnmanaged()**, therefore attempting to assign an order object outside of **OnOrderUpdate()** may not return as soon as expected. If your strategy is dependent on tracking the order object from the very first update, you should try to match your order objects by the order.Name (signal name) from during the **OnOrderUpdate()** as the order is first updated.
* Rithmic and Interactive Brokers Users: When using a NinjaScript strategy it is best practice to only work with passed by value data from **OnExecutionUpdate()**. Instances of multiple fills at the same time for the same instrument might result in an incorrect **OnPositionUpdate**, as sequence of events are not guaranteed due to provider API design. For an example on protecting positions with this approach, see **OnExecutionUpdate()**.
{% /callout %}

{% callout type="critical" %}

* If you want to drive your strategy logic based on order fills you must use **OnExecutionUpdate()** instead of **OnOrderUpdate()**. **OnExecutionUpdate()** is always triggered after **OnOrderUpdate()**. There is internal strategy logic that is triggered after **OnOrderUpdate()** is called but before **OnExecutionUpdate()** that can adversely affect your strategy if you are relying on tracking fills within **OnOrderUpdate()**.

{% /callout %}

## Playback Connection

When connected to the **Playback Connection**, calling market order based methods such as **EnterLong()** and **EnterShort()** will result in order state events being fired prior to the order method return an Order object. This is done to ensure that all events are in sync at high speed playback.

## Method Return Value

This method does not return a value.

## Syntax

You must override the method in your strategy with the following syntax:

**protected override void OnOrderUpdate(Order order, double limitPrice, double stopPrice, int quantity, int filled, double averageFillPrice, OrderState orderState, DateTime time, ErrorCode error, string comment)**

## Method Parameters

{% table %}

---

* order
* An **Order** object passed by reference representing the order object

---

* limitPrice
* A **double** value representing the limit price of the order update

---

* stopPrice
* A **double** value representing the stop price of the order update

---

* quantity
* An **int** value representing the quantity of the order update

---

* filled
* An **int** value representing the filled amount of the order update

---

* averageFillPrice
* A **double** value representing the average fill price of the order update

---

* orderState
* An **OrderState** value representing the state of the order (e.g., filled, canceled, rejected, etc). Note: See order state values table below

---

* time
* A **DateTime** structure representing the last time the order changed state

---

* error
* An **ErrorCode** value which categorizes an error received from the broker. Possible values are: **ErrorCode.LoginExpired**, **ErrorCode.LogOnFailed**, **ErrorCode.NoError**, **ErrorCode.OrderRejected**, **ErrorCode.OrderRejectedByRisk**, **ErrorCode.Panic**, **ErrorCode.UnableToCancelOrder**, **ErrorCode.UnableToChangeOrder**, **ErrorCode.UnableToSubmitOrder**, **ErrorCode.UserAbort**

---

* comment
* A string representing the error message provided directly from the broker
{% /table %}

## OrderState Values

{% table %}

* OrderState
* Description

---

* OrderState.Initialized
* Order is initialized in NinjaTrader

---

* OrderState.Submitted
* Order is submitted to the broker

---

* OrderState.Accepted
* Order is accepted by the broker or exchange

---

* OrderState.TriggerPending
* Order is pending submission

---

* OrderState.Working
* Order is working in the exchange queue

---

* OrderState.ChangePending
* Order change is pending in NinjaTrader

---

* OrderState.ChangeSubmitted
* Order change is submitted to the broker

---

* OrderState.CancelPending
* Order cancellation is pending in NinjaTrader

---

* OrderState.CancelSubmitted
* Order cancellation is submitted to the broker

---

* OrderState.Cancelled
* Order cancellation confirm received from broker

---

* OrderState.Rejected
* Order is rejected

---

* OrderState.PartFilled
* Order is partially filled

---

* OrderState.Filled
* Order is completely filled

---

* OrderState.Unknown
* An unknown order state. Default if broker does not report current order state.
{% /table %}

## Examples

### Understanding the order object parameter vs updating value parameter** ([Multi-Thread Considerations for NinjaScript](multi_threading_consideration_for_ninjascript))

```csharp
protected override void OnOrderUpdate(Cbi.Order order, double limitPrice, double stopPrice,
    int quantity, int filled, double averageFillPrice,
    Cbi.OrderState orderState, DateTime time, Cbi.ErrorCode error, string comment)
{
    Print("The most current order state is: " + order.OrderState);   // OrderState.PartFilled
    Print("This particular order update state is: " + orderState); // OrderState.Working
}
```

### **Properly assigning order object values**

```csharp
private Order entryOrder = null;

protected override void OnBarUpdate()
{
    if (entryOrder == null && Close[0] > Open[0])
        EnterLong("entryOrder");
}

protected override void OnOrderUpdate(Order order, double limitPrice, double stopPrice, int quantity, int filled, double averageFillPrice, OrderState orderState, DateTime time, ErrorCode error, string nativeError)
{
    // check if the current order matches the orderName passed in "EnterLong"()
    // Assign entryOrder in OnOrderUpdate() to ensure the assignment occurs when expected.
    // This is more reliable than assigning Order objects in OnBarUpdate, as the assignment is not guaranteed to be complete if it is referenced immediately after submitting
    if (order.Name == "entryOrder")
        entryOrder = order;

    // if entry order exists
    if (entryOrder != null && entryOrder == order)
    {
        Print(order.ToString());
        if (order.OrderState == OrderState.Cancelled)
        {
            // Do something here
            entryOrder = null;
        }
    }
}
```

Additional reference code samples are available in the NinjaScript Educational Resources section of our support forum.