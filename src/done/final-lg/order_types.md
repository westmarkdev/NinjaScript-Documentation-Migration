---
title: "Order Types"
pathName: order_types
---

## Overview

Understanding the different types of entry and exit orders you can place through NinjaScript is important. As a trader, it is critical you place the right type of order depending on the current market conditions and your trading style.

## Order Methods

For general order placement, you can use the following methods:

```csharp
EnterLong();
EnterShort();
ExitLong();
ExitShort();
```

These place market orders to either buy or sell. Market orders offer the fastest execution speed and under most conditions, guarantee that your order is filled. Be wary about using them on low volatility securities with large spreads though. You might get filled at a much higher or lower price than you expected.

## Stop Market Orders

To place orders that wait for the price to pass your specified stop price, you can use the following methods:

```csharp
EnterLongStopMarket();
EnterShortStopMarket();
ExitLongStopMarket();
ExitShortStopMarket();
```

These orders become market orders for execution once the specified stop price is reached. Stop orders increase your chances of getting filled at a particular price, but are not guaranteed because they are still ultimately market orders.

## Limit Orders

For specifying exact prices at which you want to be filled, use the following methods:

```csharp
EnterLongLimit();
EnterShortLimit();
ExitLongLimit();
ExitShortLimit();
```

Limit orders ensure you get filled at the price you specified or better. Note that limit orders are not guaranteed to execute and may result in only partial fills.

## Stop Limit Orders

For complete control over your order, you can use stop-limit orders:

```csharp
EnterLongStopLimit();
EnterShortStopLimit();
ExitLongStopLimit();
ExitShortStopLimit();
```

The stop-limit order waits until the specified stop price is reached, then it becomes a limit order instead of a market order. This order type carries the same drawback as all limit orders: you may not be filled if the limit price is never reached.

## Market If Touched (MIT) Orders

To submit an order at market price once a specific price is touched, you can use the MIT order:

```csharp
EnterLongMIT();
EnterShortMIT();
ExitLongMIT();
ExitShortMIT();
```

The MIT order behaves similarly to a stop order, except that the buy and sell actions are reversed. For example, a buy MIT order is submitted below market, whereas a buy stop order would be submitted above market.

{% callout type="note" %}
Remember to consider market conditions and your trading strategy when choosing the order type to use.
{% /callout %}
