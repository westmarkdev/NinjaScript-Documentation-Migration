---
title: AccountItem
pathName: accountitem
parent: account
section: references
status: imported
---

# Definition

Represents various account variables used to reflect values the status of the account. Each account connected in NinjaTrader will have it's own unique AccountItem values.

{% callout type="note" %}

For strategies, see also [OnAccountItemUpdate](onaccountitemupdate). For other objects, you can also subscribe to the [AccountItemUpdate](accountitemupdate) stream.
{% /callout %}

## Syntax

**AccountItem**

## Parameters

{% table %}

* AccountItem.BuyingPower
* AccountItem.CashValue
* AccountItem.Commission
* AccountItem.ExcessIntradayMargin
* AccountItem.ExcessInitialMargin
* AccountItem.ExcessMaintenanceMargin
* AccountItem.ExcessPositionMargin
* AccountItem.Fee
* AccountItem.GrossRealizedProfitLoss
* AccountItem.InitialMargin
* AccountItem.IntradayMargin
* AccountItem.LongOptionValue
* AccountItem.LookAheadMaintenanceMargin
* AccountItem.LongStockValue
* AccountItem.MaintenanceMargin
* AccountItem.NetLiquidation
* AccountItem.NetLiquidationByCurrency
* AccountItem.PositionMargin
* AccountItem.RealizedProfitLoss
* AccountItem.ShortOptionValue
* AccountItem.ShortStockValue
* AccountItem.SodCashValue
* AccountItem.SodLiquidatingValue
* AccountItem.UnrealizedProfitLoss
* AccountItem.TotalCashBalance
{% /table %}
