---
title: Instrument
pathName: instrument
parent: instruments
section: references
status: review
---

## Definition

A tradable symbol. Represents an instance of a **Master Instrument**.

{% callout type="note" %}

Warning: The properties in this class should NOT be accessed within the **OnStateChange()** method before the State has reached State.DataLoaded.

{% /callout %}

## Methods and Properties

{% table %}

* Method/Property
* Description

---

* [Exchange](exchange)
* Exchange of the current instrument

---

* [Expiry](expiry)
* Expiration date of the futures contract

---

* [FullName](instrument_fullname)
* Full name of the instrument

---

* [GetInstrument()](getinstrument)
* Returns an Instrument object by the master instrument name configured in the database.

---

* [MasterInstrument](masterinstrument)
* An instrument's configuration settings. These are settings and properties which are defined in the **Instrument** window.

---

* FundamentalData
* Instrument thread specific **FundamentalData** events

---

* MarketData
* Instrument thread specific **MarketData** events

---

* MarketDepth
* Instrument thread specific **MarketDepth** events

---

* Dispatcher
* A Dispatcher used for subscribing to Instrument related events. See **Multi-Threading Considerations**.
{% /table %}
