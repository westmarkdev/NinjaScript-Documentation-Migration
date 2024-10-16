---
title: "MasterInstrument"
pathName: /docs/desktop/masterinstrument
---

## Definition

An instrument's configuration settings. These are settings and properties which are defined in the [Instrument](/docs/desktop/instruments) window.

{% callout type="warning" %}
The properties in this class should NOT be accessed within the [OnStateChange()](/docs/desktop/onstatechange) method before the State has reached State.DataLoaded.
{% /callout %}

## Methods and Properties

|  |  |
| --- | --- |
| [Compare()](/docs/desktop/compare) | Returns an int value that compares two price values with respect to the Instrument tick size |
| [Currency](/docs/desktop/currency) | The currency that the instrument is traded in |
| [Description](/docs/desktop/masterinstrument_description) | A written representation of a given instrument |
| [Dividends](/docs/desktop/dividends) | A collection of dividends for stock instruments |
| [Exchanges](/docs/desktop/exchanges) | A collection of exchanges configured for an instrument |
| [FormatPrice()](/docs/desktop/formatprice) | Returns a string representing the price formatted to the nearest tick size |
| [InstrumentType](/docs/desktop/instrumenttype) | The type of instrument |
| [MergePolicy](/docs/desktop/mergepolicy) | The Merge Policy that is configured for the current master instrument. |
| [Name](/docs/desktop/masterinstrument_name) | The name of the instrument. |
| [GetNextExpiry()](/docs/desktop/getnextexpiry) | Returns a DateTime structure representing the next futures expiry for a given date |
| [PointValue](/docs/desktop/pointvalue) | Currency value of 1 full point of movement |
| [RolloverCollection](/docs/desktop/rollovercollection) | A collection of expiration dates and offsets for futures instruments |
| [RoundToTickSize()](/docs/desktop/roundtoticksize) | Rounds the value up to the nearest valid value |
| [RoundDownToTickSize()](/docs/desktop/rounddowntoticksize) | Rounds the value down to the nearest valid value |
| [Splits](/docs/desktop/splits) | A collection of splits for stock instruments |
| [TickSize](/docs/desktop/ticksize) | The smallest movement in price configured |
| [Url](/docs/desktop/url) | A web URL where contract details have been collected |
