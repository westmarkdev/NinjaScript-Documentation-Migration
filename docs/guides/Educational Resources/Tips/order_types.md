---
title: Order Types
pathName: order_types
parent: tips
section: guides
status: imported
---

Understanding the different types of entry and exit orders you can place through **NinjaScript** is important. As a trader, it is critical you place the right type of order depending on the current market conditions and your trading style.

[Order Methods](order_methods)

{% table %}

* Method

---

* **EnterLong()**
* **EnterShort()**
* **ExitLong()**
* **ExitShort()**
{% /table %}

These place market orders to either buy or sell. Market orders offer the fastest execution speed and under most conditions, guarantee that your order is filled. Be wary about using them on low volatility securities with large spreads though. You might get filled at a much higher/lower price than you expected.

{% table %}

* Method

---

* **EnterLongStopMarket()**
* **EnterShortStopMarket()**
* **ExitLongStopMarket()**
* **ExitShortStopMarket()**
{% /table %}

These orders wait for the price of the instrument to pass your stop price. Once it passes the stop price the order becomes a market order for execution. Stop orders increase your chances of getting filled at a particular price, but are not guaranteed because they are still ultimately market orders.

{% table %}

* Method

---

* **EnterLongLimit()**
* **EnterShortLimit()**
* **ExitLongLimit()**
* **ExitShortLimit()**
{% /table %}

Limit orders allow you to specify the price you want to be filled at. These orders are useful on low volatility instruments because they ensure you get filled at the price you specified or better. Take note that limit orders are not guaranteed to execute and may cause only partial fills.

{% table %}

* Method

---

* **EnterLongStopLimit()**
* **EnterShortStopLimit()**
* **ExitLongStopLimit()**
* **ExitShortStopLimit()**
{% /table %}

The stop-limit order offers the trader complete control over the order. Like a stop order, the stop-limit order waits until the specified stop price has been reached. Unlike the stop order though, the stop-limit order becomes a limit order instead of a market order when the stop price is reached. The drawback for a stop-limit order is the same as all limit orders; the trader might not be filled if the limit price is never reached.

{% table %}

* Method

---

* **EnterLongMIT()**
* **EnterShortMIT()**
* **ExitLongMIT()**
* **ExitShortMIT()**
{% /table %}

The MIT (Market If Touched) order allows the order to be submitted at Market once the price is touched. This order is similar to a stop order except the buy and sell actions are reversed. For example, a buy MIT order is submitted below market where a buy Stop would be submitted above market.
