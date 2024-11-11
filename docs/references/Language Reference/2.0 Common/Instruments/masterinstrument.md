---
title: MasterInstrument
pathName: masterinstrument
parent: instruments
order: 5
status: check
section: references
---

## Definition

An instrument's configuration settings. These are settings and properties which are defined in the **Instrument** window.

{% callout type="warning" %}
Warning: The properties in this class should NOT be accessed within the **OnStateChange()** method before the State has reached State.DataLoaded.
{% /callout %}

## Methods and Properties

{% table %}

* Method/Property
* Description

---

* [Compare()](compare)
* Returns An **int** value compares two price values with respect to the Instrument tick size

---

* [Currency](currency)
* The currency that the instrument traded in

---

* [Description](masterinstrument_description)
* A written representation of a given instrument

---

* [Dividends](dividends)
* A collection of dividends for stock instruments

---

* [Exchanges](exchanges)
* A collection of exchanges configured for an instrument

---

* [FormatPrice()](formatprice)
* Returns a string representing the price formatted to the nearest tick size

---

* [InstrumentType](instrumenttype)
* The type of instrument

---

* [MergePolicy](mergepolicy)
* The Merge Policy that is configured for the current master instrument.

---

* [Name](masterinstrument_name)
* The name of the instrument.

---

* [GetNextExpiry()](getnextexpiry)
* Returns a DateTime structure representing the next futures expiry for a given date

---

* [PointValue](pointvalue)
* Currency value of 1 full point of movement

---

* [RolloverCollection](rollovercollection)
* A collection of expiration dates and offsets for futures instruments

---

* [RoundToTickSize()](roundtoticksize)
* Rounds the value up to the nearest valid value

---

* [RoundDownToTickSize()](rounddowntoticksize)
* Rounds the value down to the nearest valid value

---

* [Splits](splits)
* A collection of splits for stock instruments

---

* [TickSize](ticksize)
* The smallest movement in price configured

---

* [Url](url.md)
* A web url where contract details have been collected
{% /table %}
