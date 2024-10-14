










 


Bars Type







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?bars_type.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt;
Bars Type | [Previous page](tabcontrolmanager.htm)
[Return to chapter overview](language_reference_wip.htm)










Creating custom Bars Types allows for incredible flexibility in the way you want to present data in a chart. The methods and properties covered in this section are unique to custom Bars Type development.


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| [AddBar()](addbar.htm) | Adds new data points for the Bars Type. |
| [ApplyDefaultBasePeriodValue](applydefaultbaseperiodvalue.htm) | Sets the default base values used for the [BarsPeriod](barsperiod.htm) selected by the user (e.g., the default PeriodValue, DaysToLoad, etc.) for your custom Bar Type. |
| [ApplyDefaultValue](applydefaultvalue.htm) | Sets the default [BarsPeriod](barsperiod.htm) values used for a custom Bar Type.  |
| [BuiltFrom](builtfrom.htm) | Determines the base dataset used to build the BarsType (i.e., Tick, Minute, Day). |
| [GetInitialLookBackDays()](getinitiallookbackdays.htm) | Determines how many days of data load when a user makes a "bars back" data request. |
| [GetPercentComplete()](getpercentcomplete.htm) | Determines the value your BarsType would return for [Bars.PercentComplete](percentcomplete.htm) |
| [Icon](icon_barstype.htm) | The shape which displays next to the Bars Type menu item.  |
| [IsRemoveLastBarSupported](isremovelastbarsupported.htm) | Determines if the bars type can use the [RemoveLastBar()](removelastbar.htm) method when true, otherwise an exception will be thrown. |
| [IsTimebased](barstype_istimebased.htm) | Used to indicate the BarsType is built from time-based bars (day, minute, second). |
| [OnDataPoint()](ondatapoint.htm) | OnDataPoint() method is where you should adjust data points (bar values) of your series through [AddBar()](addbar.htm) and [UpdateBar()](updatebar.htm). |
| [RemoveLastBar()](removelastbar.htm) | Removes the last data point for the Bars Type. |
| [SessionIterator](barstype_sessioniterator.htm) | Provides trading session information to the bars type. Must be built using the bars object. |
| [UpdateBar()](updatebar.htm) | Updates a data point in our Bars Type. |






 
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
 
 
 



