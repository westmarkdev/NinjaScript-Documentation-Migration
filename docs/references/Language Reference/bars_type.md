---
title: Bars Type
pathName: bars_type
parent: language_reference
status: imported
order: 4
section: references
---

Creating custom Bars Types allows for incredible flexibility in the way you want to present data in a chart. The methods and properties covered in this section are unique to custom Bars Type development.

## Methods and Properties

{% table %}

* Method/Property
* Description

---

* [AddBar()](addbar)
* Adds new data points for the Bars Type.

---

* [ApplyDefaultBasePeriodValue](applydefaultbaseperiodvalue)
* Sets the default base values used for the [BarsPeriod](barsperiod) selected by the user (e.g., the default PeriodValue, DaysToLoad, etc.) for your custom Bar Type.

---

* [ApplyDefaultValue](applydefaultvalue)
* Sets the default [BarsPeriod](barsperiod) values used for a custom Bar Type.

---

* [BuiltFrom](builtfrom)
* Determines the base dataset used to build the BarsType (i.e., Tick, Minute, Day).

---

* [GetInitialLookBackDays()](getinitiallookbackdays)
* Determines how many days of data load when a user makes a "bars back" data request.

---

* [GetPercentComplete()](getpercentcomplete)
* Determines the value your BarsType would return for [Bars.PercentComplete](percentcomplete)

---

* [Icon](icon_barstype)
* The shape which displays next to the Bars Type menu item.

---

* [IsRemoveLastBarSupported](isremovelastbarsupported)
* Determines if the bars type can use the [RemoveLastBar()](removelastbar) method when true, otherwise an exception will be thrown.

---

* [IsTimebased](barstype_istimebased)
* Used to indicate the BarsType is built from time-based bars (day, minute, second).

---

* [OnDataPoint()](ondatapoint)
* OnDataPoint() method is where you should adjust data points (bar values) of your series through [AddBar()](addbar) and [UpdateBar()](updatebar).

---

* [RemoveLastBar()](removelastbar)
* Removes the last data point for the Bars Type.

---

* [SessionIterator](barstype_sessioniterator)
* Provides trading session information to the bars type. Must be built using the bars object.

---

* [UpdateBar()](updatebar)
* Updates a data point in our Bars Type.
{% /table %}
