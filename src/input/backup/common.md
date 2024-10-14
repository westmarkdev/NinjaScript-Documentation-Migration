










 


Common







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?common.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt;
Common | [Previous page](alphabetical_reference.htm)
[Return to chapter overview](language_reference_wip.htm)










The following section documents methods and properties available to every NinjaScript type that access various forms of data including bar data, price data, and statistical forms of data. The Common section is broken into several categories pertaining to distinct NinjaScript objects or concepts. An index of topics under the Common section can be found below:


 




|  |  |
| --- | --- |
| [Attributes](attributes.htm) | Documents both .NET native and NinjaScript custom [attributes](https://msdn.microsoft.com/en-us/library/5x6cd29c(v=vs.110).aspx) which are commonly used to define the behavior of a NinjaScript property or object |
| [Alert, Debug, Share](alert__debugging_and_sharing.htm) | Documents methods for triggering alerts, printing debug messages, and using Share Services |
| [Analytical](market_data.htm) | Documents methods and properties useful for analyzing and identifying specific conditions within [Series<t>](seriest.htm) collections |
| [Bars](bars.htm) | Represents the data returned from the historical data repository |
| [Charts](chart.htm) | Covers information related to accessing chart related data |
| [Drawing](drawing.htm) | Documents the drawing of custom shapes, lines, text and colors on your price and indicator panels from both [Indicators](indicator.htm) and [Strategies](strategy.htm) |
| [Instrument](instrument.htm) | Represents an instance of a [Master Instrument](masterinstrument.htm) |
| [ISeries<t>](iseriest.htm) | Documents the interface that is implemented by all NinjaScript classes that manage historical data as an ISeries<double> used for indicator input, and other object data |
| [OnBarUpdate()](onbarupdate.htm) | An event driven method which is called whenever a bar is updated |
| [OnFundamentalData()](onfundamentaldata.htm) | An event driven method which is called for every change in fundamental data |
| [OnMarketDepth()](onmarketdepth.htm) | An event driven method which is called and guaranteed to be in the correct sequence for every change in level two market data |
| [OnStateChange()](onstatechange.htm) | An event driven method which is called whenever the script enters a new [State](state.htm) |
| [SessionIterator](sessioniterator.htm) | An interface which allows you to traverse through various trading hours data elements which apply to a segment of bars |
| [System Indicator Methods](indicators.htm) | Documents syntax and return values for system indicator methods |
| [TradingHours](tradinghours.htm) | Represents the Trading Hours information returned from the current bars series |
| [Name](name.htm) | Determines the listed name of the NinjaScript object |
| [IsVisible](isvisible.htm) | Determines if the current NinjaScript object should be visible on the chart |
| [DisplayName](indicator_displayname.htm) | Determines the text display on the chart panel |
| [Description](description.htm) | Text which is used on the UI's information box to be display to a user when configuration a NinjaScript object |
| [Clone()](clone.htm) | Used to override the default NinjaScript Clone() method which is called any time an instance of a NinjaScript object is created |
| [TriggerCustomEvent()](triggercustomevent.htm) | Provides a way to use your own custom events (such as a Timer object) so that internal NinjaScript indexes and pointers are correctly set prior to processing user code triggered by your custom event |






 
 var lastSlashPos = document.URL.lastIndexOf("/") &gt; document.URL.lastIndexOf("\\") ? document.URL.lastIndexOf("/") : document.URL.lastIndexOf("\\");
 if (document.URL.substring(lastSlashPos + 1, lastSlashPos + 4).toLowerCase() != "~hh") {
 if (document.all) setTimeout(function() {
 nsrInit();
 }, 20);
 else nsrInit();
 }
 
 
 $('.sync-toc').show();
 $('p.crumbs').hide();
 }
 
 
 



</double></t></t>