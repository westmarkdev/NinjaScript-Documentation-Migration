---
title: Indicator
pathName: indicator
parent: language_reference
order: 8
status: imported
section: references
---

The methods and properties covered in this section are unique to custom indicator development. Indicator configuration properties globally define various behaviors of indicators. All properties have default values and can be overridden by setting them in the **OnStateChange()** method of the indicator.

{% callout type="note" %}

See also the "[Common](common)" section for more method and properties which are shared by NinjaScript types.

{% /callout %}

## Methods and Properties

{% table %}

* Method
* Description

---

* [AddLine()](addline)
* Adds line objects on a chart.

---

* [AddPlot()](addplot)
* Adds plot objects that define how an indicator or strategy data series render on a chart.

---

* [BarsRequiredToPlot](barsrequiredtoplot)
* The number of bars on a chart required before the script plots.

---

* [DisplayInDataBox](displayindatabox)
* Determines if plot(s) display in the chart data box.

---

* [DrawHorizontalGridLines](drawhorizontalgridlines)
* Plots horizontal grid lines on the indicator panel.

---

* [DrawOnPricePanel](drawonpricepanel)
* Determines the chart panel the draw objects renders.

---

* [DrawVerticalGridLines](drawverticalgridlines)
* Plots vertical grid lines on the indicator panel.

---

* [IndicatorBaseConverter](indicatorbaseconverter)
* A custom TypeConverter class handling the designed behavior of an indicator's property descriptor collection.

---

* [IsChartOnly](ischartonly)
* If true, any indicator will be only available for charting usage - indicators with this property enabled would for example not be expected to show if called in a SuperDOM or MarketAnalyzer window.

---

* [IsSuspendedWhileInactive](issuspendedwhileinactive)
* Prevents real-time market data events from being raised while the indicator's hosting feature is in a state that would be considered suspended and not in immediate use by a user.

---

* [PaintPriceMarkers](paintpricemarkers)
* If true, any indicator plot values display price markers in the y-axis.

---

* [ShowTransparentPlotsInDataBox](showtransparentplotsindatabox)
* Determines if plot(s) values which are set to a Transparent brush display in the chart data box.
{% /table %}
