---
title: "SuperDOM Column"
pathName: /docs/desktop/superdom_column
---

Custom SuperDOM Columns can be used to add additional functionality to the [SuperDOM](/docs/desktop/superdom) window. The methods and properties covered in this section are unique to custom SuperDOM column development.

{% callout type="tip" %}
The system SuperDOM Columns which ship with NinjaTrader are open source and you can review their implementation from the [NinjaScript Editor](/docs/desktop/ns_explorer) SuperDOMColumn folder, or by using the text editor of your choice by reviewing the source code located in Documents\NinjaTrader 8\bin\Custom\SuperDomColumns
{% /callout %}

## In this section

|  |  |
| --- | --- |
| [MarketDepth](/docs/desktop/superdom_marketdepth) | Provides Level 2 information for a SuperDOMColumn. |
| [OnMarketData()](/docs/desktop/superdomcolumn_onmarketdata) | Called and guaranteed to be in the correct sequence for every change in level one market data for the underlying instrument. The OnMarketData() method updates can include but is not limited to the bid, ask, last price and volume. |
| [OnOrderUpdate()](/docs/desktop/superdomcolumn_onorderupdate) | Called every time an [order](/docs/desktop/order) changes state. An order will change state when a change in order quantity, price or state (e.g. working to filled) occurs. |
| [OnPositionUpdate()](/docs/desktop/superdomcolumn_onpositionupdate) | Called every time a [position](/docs/desktop/position) changes state. |
| [OnPropertyChanged()](/docs/desktop/onpropertychanged) | This method should be used any time you wish to repaint the column instead of calling [OnRender()](/docs/desktop/superdomcolumn_onrender) directly. |
| [OnRender()](/docs/desktop/superdomcolumn_onrender) | Used to draw custom content to the SuperDOM Column, such as a Grid. |
| [OnRestoreValues()](/docs/desktop/onrestorevalues) | Called when the column is restored (e.g. from a workspace). |

