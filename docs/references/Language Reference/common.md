---
title: Common
pathName: common
parent: language_reference
order: 2
status: imported
section: references
---

The following section documents methods and properties available to every **NinjaScript** type that access various forms of data including bar data, price data, and statistical forms of data. The Common section is broken into several categories pertaining to distinct **NinjaScript** objects or concepts. An index of topics under the Common section can be found below:

{% table %}

* Category

* Description

---

* [Attributes](attributes)
* Documents both .NET native and NinjaScript custom [attributes](https://msdn.microsoft.com/en-us/library/5x6cd29c(v=vs.110).aspx) which are commonly used to define the behavior of a NinjaScript property or object

---

* [Alert, Debug, Share](alert__debugging_and_sharing)
* Documents methods for triggering alerts, printing debug messages, and using Share Services

---

* [Analytical](analytical)
* Documents methods and properties useful for analyzing and identifying specific conditions within **Series`<t>`** collections

---

* [Bars](bars)
* Represents the data returned from the historical data repository

---

* [Charts](chart)
* Covers information related to accessing chart related data

---

* [Drawing](drawing)
* Documents the drawing of custom shapes, lines, text and colors on your price and indicator panels from both [Indicators](indicator) and [Strategies](strategy)

---

* [Instrument](instrument)
* Represents an instance of a [Master Instrument](masterinstrument)

---

* [ISeries`<t>`](iseriest)
* Documents the interface that is implemented by all NinjaScript classes that manage historical data as an **ISeries`<double>`** used for indicator input, and other object data

---

* [OnBarUpdate()](onbarupdate)
* An event driven method which is called whenever a bar is updated

---

* [OnFundamentalData()](onfundamentaldata)
* An event driven method which is called for every change in fundamental data

---

* [OnMarketDepth()](onmarketdepth)
* An event driven method which is called and guaranteed to be in the correct sequence for every change in level two market data

---

* [OnStateChange()](onstatechange)
* An event driven method which is called whenever the script enters a new **State**

---

* [SessionIterator](sessioniterator)
* An interface which allows you to traverse through various trading hours data elements which apply to a segment of bars

---

* [System Indicator Methods](docs/references/Language%20Reference/2.0%20Common/system_indicator_methods.md)
* Documents syntax and return values for system indicator methods

---

* [TradingHours](tradinghours)
* Represents the Trading Hours information returned from the current bars series

---

* [Name](name)
* Determines the listed name of the NinjaScript object

---

* [IsVisible](isvisible)
* Determines if the current NinjaScript object should be visible on the chart

---

* [DisplayName](indicator_displayname)
* Determines the text display on the chart panel

---

* [Description](description)
* Text which is used on the UI's information box to be display to a user when configuration a NinjaScript object

---

* [Clone()](clone)
* Used to override the default NinjaScript **Clone()** method which is called any time an instance of a NinjaScript object is created

---

* [TriggerCustomEvent()](triggercustomevent.md)
* Provides a way to use your own custom events (such as a Timer object) so that internal NinjaScript indexes and pointers are correctly set prior to processing user code triggered by your custom event

{% /table %}
