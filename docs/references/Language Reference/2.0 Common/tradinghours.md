---
status: imported
title: Trading Hours
pathName: tradinghours
parent: common
section: references
---

## Definition

Represents the Trading Hours information returned from the current bars series. The Trading Hours object contains several methods and properties for working with various trading sessions.

{% callout = "warning" }

The properties in this class should NOT be accessed within the [OnStateChange()](onstatechange) method before the State has reached State.DataLoaded

{% /callout }

## Methods and Properties

{% table %}

* Method/Property

* Description

---

* [Get()](tradinghoursget)

* Returns the Trading Hours object for the specified Trading Hours template name

---

* [GetPreviousTradingDayEnd()](getprevioustradingdayend)

* Returns the end date and time of the previous trading session relative to the time passed in the methods parameters.

---

* [Holidays](holidays)

* A collection of full holidays which are configured for a Trading Hours template

---

* [Name](tradinghours_name.md)

* Indicates the name of the trading hours template applied to the Bars series object.

---

* [PartialHolidays](partialholidays)

* A collection of partial holidays which are configured for a Trading Hours template

---

* [Sessions](tradinghours_sessions.md)

* A collection of session definitions of the trading hours template.

---

* [TimeZoneInfo](timezoneinfo)

* Indicates a time zone that is configured by a Trading Hour template

---

{% /table %}
