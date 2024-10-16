---
title: "Order Methods"
pathName: /docs/order_methods
---

{% callout type="note" %}
You will not be able to mix and match the two approaches. If you decide to go with the Managed approach you will only be able to use the Managed order methods. If you decide to go with the Unmanaged approach you will only be able to use the Unmanaged order methods.
{% /callout %}

## Order Methods Overview

NinjaScript provides several approaches you can use for order placement within your NinjaScript strategy. The main approaches can be categorized as a Managed approach and an Unmanaged approach.

|  |  |
| --- | --- |
| **Managed** | The Managed approach offers you order methods that are wrapped with an invisible convenience layer that allows you to focus on your system's trading rules leaving the underlying mechanics of order management and the relationships between entry and exit orders and positions to NinjaTrader. The cost for having the convenience layer is that there are [order handling rules](/docs/desktop/managed_approach) that must be followed to prevent order errors.  ›[Understanding the Managed approach](/docs/desktop/managed_approach) ›[Advanced Order Handling](/docs/desktop/advanced_order_handling) ›[CancelOrder()](/docs/desktop/managed_cancelorder) ›[EnterLong()](/docs/desktop/enterlong) ›[EnterLongLimit()](/docs/desktop/enterlonglimit) ›[EnterLongMIT()](/docs/desktop/enterlongmit) ›[EnterLongStopMarket()](/docs/desktop/enterlongstopmarket) ›[EnterLongStopLimit()](/docs/desktop/enterlongstoplimit) ›[EnterShort()](/docs/desktop/entershort) ›[EnterShortLimit()](/docs/desktop/entershortlimit) ›[EnterShortMIT()](/docs/desktop/entershortmit) ›[EnterShortStopMarket()](/docs/desktop/entershortstopmarket) ›[EnterShortStopLimit()](/docs/desktop/entershortstoplimit) ›[ExitLong()](/docs/desktop/exitlong) ›[ExitLongLimit()](/docs/desktop/exitlonglimit) ›[ExitLongMIT()](/docs/desktop/exitlongmit) ›[ExitLongStopMarket()](/docs/desktop/exitlongstopmarket) ›[ExitLongStopLimit()](/docs/desktop/exitlongstoplimit) ›[ExitShort()](/docs/desktop/exitshort) ›[ExitShortLimit()](/docs/desktop/exitshortlimit) ›[ExitShortMIT()](/docs/desktop/exitshortmit) ›[ExitShortStopMarket()](/docs/desktop/exitshortstopmarket) ›[ExitShortStopLimit()](/docs/desktop/exitshortstoplimit) ›[GetRealtimeOrder()](/docs/desktop/getrealtimeorder) ›[SetProfitTarget()](/docs/desktop/setprofittarget) ›[SetStopLoss()](/docs/desktop/setstoploss) ›[SetTrailStop()](/docs/desktop/settrailstop) ›[SetParabolicStop()](/docs/desktop/setparabolicstop) |
| **Unmanaged** | The Unmanaged approach offers you more flexible order methods without the convenience layer. This means you are not restricted to any order handling rules besides those imposed by the brokerage/exchange. With such flexibility though, you will have to ensure to program your strategy to handle any and all issues that may arise with placing orders. ›[Understanding the Unmanaged approach](/docs/desktop/unmanaged_approach) ›[CancelOrder()](/docs/desktop/unmanaged_cancelorder) ›[ChangeOrder()](/docs/desktop/managed_changeorder) ›[GetRealtimeOrder()](/docs/desktop/getrealtimeorder) ›[IgnoreOverfill](/docs/desktop/ignoreoverfill) ›[IsUnmanaged](/docs/desktop/isunmanaged) ›[SubmitOrderUnmanaged()](/docs/desktop/submitorderunmanaged) |

{% callout type="tip" %}
Choose the approach that better fits your strategy needs and ensure that you are familiar with the order methods available within that approach.
{% /callout %}
