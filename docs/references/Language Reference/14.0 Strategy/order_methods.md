---
title: Order Methods
pathName: order_methods
parent: strategy
section: references
status: review
---

## Order Methods Overview

NinjaScript provides several approaches you can use for order placement within your NinjaScript strategy. The main approaches can be categorized as a Managed approach and an Unmanaged approach.

{% callout type="note" %}

You will not be able to mix and match the two approaches. If you decide to go with the Managed approach you will only be able to use the Managed order methods. If you decide to go with the Unmanaged approach you will only be able to use the Unmanaged order methods.

{% /callout %}

{% table %}

* Managed
* Unmanaged

---

* The Managed approach offers you order methods that are wrapped with an invisible convenience layer that allows you to focus on your system's trading rules leaving the underlying mechanics of order management and the relationships between entry and exit orders and positions to NinjaTrader. The cost for having the convenience layer is that there are **[order handling rules](managed_approach)** that must be followed to prevent order errors.  
  * **[Understanding the Managed approach](managed_approach)**  
  * **[Advanced Order Handling](advanced_order_handling)**  
  * **[CancelOrder()](managed_cancelorder)**  
  * **[EnterLong()](enterlong)**  
  * **[EnterLongLimit()](enterlonglimit)**  
  * **[EnterLongMIT()](enterlongmit)**  
  * **[EnterLongStopMarket()](enterlongstopmarket)**  
  * **[EnterLongStopLimit()](enterlongstoplimit)**  
  * **[EnterShort()](entershort)**  
  * **[EnterShortLimit()](entershortlimit)**  
  * **[EnterShortMIT()](entershortmit)**  
  * **[EnterShortStopMarket()](entershortstopmarket)**  
  * **[EnterShortStopLimit()](entershortstoplimit)**  
  * **[ExitLong()](exitlong)**  
  * **[ExitLongLimit()](exitlonglimit)**  
  * **[ExitLongMIT()](exitlongmit)**  
  * **[ExitLongStopMarket()](exitlongstopmarket)**  
  * **[ExitLongStopLimit()](exitlongstoplimit)**  
  * **[ExitShort()](exitshort)**  
  * **[ExitShortLimit()](exitshortlimit)**  
  * **[ExitShortMIT()](exitshortmit)**  
  * **[ExitShortStopMarket()](exitshortstopmarket)**  
  * **[ExitShortStopLimit()](exitshortstoplimit)**  
  * **[GetRealtimeOrder()](getrealtimeorder)**  
  * **[SetProfitTarget()](setprofittarget)**  
  * **[SetStopLoss()](setstoploss)**  
  * **[SetTrailStop()](settrailstop)**  
  * **[SetParabolicStop()](setparabolicstop)**

---

* The Unmanaged approach offers you more flexible order methods without the convenience layer. This means you are not restricted to any order handling rules besides those imposed by the brokerage/exchange. With such flexibility though, you will have to ensure to program your strategy to handle any and all issues that may arise with placing orders.  
  * **[Understanding the Unmanaged approach](unmanaged_approach)**  
  * **[CancelOrder()](unmanaged_cancelorder)**  
  * **[ChangeOrder()](managed_changeorder)**  
  * **[GetRealtimeOrder()](getrealtimeorder)**  
  * **[IgnoreOverfill](ignoreoverfill)**  
  * **[IsUnmanaged](isunmanaged)**  
  * **[SubmitOrderUnmanaged()](submitorderunmanaged)**
{% /table %}
