---
title: "Instrument"
pathName: /docs/instrument
---

## Definition

A tradable symbol. Represents an instance of a [Master Instrument](/docs/desktop/masterinstrument).

{% callout type="warning" %}
The properties in this class should NOT be accessed within the [OnStateChange()](/docs/desktop/onstatechange) method before the State has reached State.DataLoaded.
{% /callout %}

## Methods and Properties

|  |  |
| --- | --- |
| [Exchange](/docs/desktop/exchange) | Exchange of the current instrument |
| [Expiry](/docs/desktop/expiry) | Expiration date of the futures contract |
| [FullName](/docs/desktop/instrument_fullname) | Full name of the instrument |
| [GetInstrument()](/docs/desktop/getinstrument) | Returns an Instrument object by the master instrument name configured in the database. |
| [MasterInstrument](/docs/desktop/masterinstrument) | An instrument's configuration settings. These are settings and properties which are defined in the [Instrument](/docs/desktop/instruments) window. |
| FundamentalData | Instrument thread specific [FundamentalData](/docs/desktop/fundamentaldata) events |
| MarketData | Instrument thread specific [MarketData](/docs/desktop/marketdata) events |
| MarketDepth | Instrument thread specific [MarketDepth](/docs/desktop/marketdepth) events |
| Dispatcher | A Dispatcher used for subscribing to Instrument related events. See [Multi-Threading Considerations](/docs/desktop/multi-threading). |
