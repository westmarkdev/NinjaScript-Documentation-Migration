










 


PriceSeries<double>







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?priceseries.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [ISeries<t>](iseriest.htm) &gt;
PriceSeries<double> | [Previous page](reset.htm)
[Return to chapter overview](iseriest.htm)










Definition
----------


Represents historical data as an ISeries<double> interface which can be used for custom NinjaScript object calculations.


 




|  |
| --- |
| Note:  In most cases, you will access the historical price series using a core event handler such as OnBarUpdate.  For more advance developers, you may find situations where you wish to access historical price series outside of the core event methods, such as your own custom mouse click.  In these advanced scenarios, you may run into situations where the barsAgo pointer is not in sync with the current bar, which may cause errors when trying to obtain this information.  In those cases, please use the Bars.Get...() methods with the absolute bar index, e.g., [Bars.GetClose()](getclose.htm), [Bars.GetOpen()](getopen.htm), etc. |



 


 


Single ISeries<double>
----------------------




|  |  |
| --- | --- |
| [Close](close.htm) | A collection of historical bar close prices. |
| [High](high.htm) | A collection of historical bar high prices. |
| [Input](input.htm) | A collect of the the main historical input values. |
| [Low](low.htm) | A collection of historical bar low prices. |
| [Median](median.htm) | A collection of historical bar median prices. |
| [Open](open.htm) | A collection of historical bar open prices. |
| [Typical](typical.htm) | A collection of historical bar typical prices. |
| [Value](value.htm) | A collection of historical references to the first object (Values[0]) in the indicator |
| [Weighted](weighted.htm) | A collection of historical bar weighted prices. |





Multi-Time Frame ISeries<double>
--------------------------------




|  |  |
| --- | --- |
| [Closes](closes.htm) | Holds an array of ISeries<double> objects holding historical bar close prices. |
| [Highs](highs.htm) | Holds an array of ISeries<double> objects holding historical bar high prices. |
| [Inputs](inputs.htm) | Holds an array of ISeries<double> objects holding main historical input values |
| [Lows](lows.htm) | Holds an array of ISeries<double> objects holding historical bar low prices. |
| [Medians](medians.htm) | Holds an array of ISeries<double>objects holding historical bar median prices. |
| [Opens](opens.htm) | Holds an array of ISeries<double> objects holding historical bar open prices. |
| [Typicals](typicals.htm) | Holds an array of ISeries<double> objects holding historical bar typical prices. |
| [Values](values.htm) | Holds an array of ISeries<double> objects holding hold the indicator's underlying calculated values. |
| [Weighteds](weighteds.htm) | Holds an array of ISeries<double> objects holding historical bar weighted prices. |



 





 
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
 
 
 



</double></double></double></double></double></double></double></double></double></double></double></double></double></t></double></double></t>