---
title: SuperDOM Column
pathName: superdom_column
parent: language_reference
status: imported
order: 15
section: references
---

Custom SuperDOM Columns can be used to add additional functionality to the **SuperDOM** window. The methods and properties covered in this section are unique to custom SuperDOM column development.

{% callout type="note" %}

The system SuperDOM Columns which ship with NinjaTrader are open source and you can review their implementation from the **NinjaScript Editor** SuperDOMColumn folder, or by using the text editor of your choice by reviewing the source code located in Documents\NinjaTrader 8\bin\Custom\SuperDomColumns.

{% /callout %}

## In this section

{% table %}

* Method
* Description

---

* [MarketDepth](superdom_marketdepth)
* Provides Level 2 information for a SuperDOMColumn.

---

* [OnMarketData()](superdomcolumn_onmarketdata)
* Called and guaranteed to be in the correct sequence for every change in level one market data for the underlying instrument. The **OnMarketData()** method updates can include but is not limited to the bid, ask, last price and volume.

---

* [OnOrderUpdate()](superdomcolumn_onorderupdate)
* Called every time an **order** changes state. An order will change state when a change in order quantity, price or state (e.g. working to filled) occurs.

---

* [OnPositionUpdate()](superdomcolumn_onpositionupdate)
* Called every time a **position** changes state.

---

* [OnPropertyChanged()](onpropertychanged)
* This method should be used any time you wish to repaint the column instead of calling **OnRender()** directly.

---

* [OnRender()](superdomcolumn_onrender)
* Used to draw custom content to the SuperDOM Column, such as a Grid.

---

* [OnRestoreValues()](onrestorevalues)
* Called when the column is restored (e.g. from a workspace).
{% /table %}
