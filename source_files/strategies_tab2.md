﻿


Strategies Tab









 


Strategies Tab








[Show/Hide Hidden Text](javascript:HMToggleExpandAll(!HMAnyToggleOpen()) "Click to open/close expanding sections")









The Strategies tab displays running and terminated strategies in a [data grid](data_grids.htm).


 




|  |
| --- |
| Note: The [IncludeTradeHistoryInBacktest](includetradehistoryinbacktest.htm) property is set to false by default when a strategy is applied directly in the Strategies tab. This provides for leaner memory usage, but at the expense of not being able to access Trade objects for historical trades. Thus, fields such as [SystemPerformance.AllTrades.Count](alltrades.htm) that rely on references Trade objects will not have any such references to work with. If you would like to save these objects for reference in your code, you can set IncludeTradeHistoryInBacktest to true in the Configure state. For more information, see the [Working with Historical Trade Data](strategyanalyzer_properties_2.htm) page. |



![tog_minus](tog_minus.gif)        [Understanding the strategies tab](javascript:HMToggle('toggle','UnderstandingTheStrategiesTab','UnderstandingTheStrategiesTab_ICON'))




|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Strategy Display
Active and stopped strategies are listed as a grid and can be started/stopped by left mouse clicking the check box in the Enabled column.
 
ControlCenterStrategiesGrid
 
•Green highlighted "Strategy" name indicates a currently running strategy.•Orange highlighted "Strategy" name indicates the strategy is waiting until it reaches a flat position to be in sync with the account position before fully starting. (Please see the options [Strategies Tab](options_strategies.htm) section for configuration options)•Black highlighted "Strategy" name indicates a disabled strategy. 
Strategies using multiple instruments will be expandable so that each instrument's strategy position can be viewed. In the image above, the second strategy is using ES 06-14 as well as MSFT which is shown below it.
 
Right Click Menu
Right mouse clicking within the strategies grid opens the following menu:
 
ControlCenter_StrategiesContextMenu
 


|  |  |
| --- | --- |
| New Strategy... | [Run a new automated NinjaScript strategy](running_a_ninjascript_strategy.htm) |
| Edit Strategy | Brings up the Edit Strategy window to edit the strategy parameters for the selected strategy. (Only disabled strategies can be edited) |
| Synchronize All Strategies | Will aggregate all strategy positions and syncs aggregate value to the accounts position for the instruments that have running strategies. |
| Enable | Enables the strategy |
| Disable | Disables the strategy |
| Remove | Removes the selected strategy from the grid |
| Strategy Performance | Generates a performance report for the selected strategy (See the "How to view strategy performance" section below) |
| Filter Only Active Strategies | Displays only active strategies |
| Filter By Account | Sets which strategies to display by account |
| Export | Exports the grid contents to "CSV" or "Excel" file format |
| Find... | Search for a term in the grid |
| Print | Select to print either the window or the order grid area. |
| Share | Select to share via your share connections. |
| Properties... | Configure the strategies tab properties |


 |



![tog_minus](tog_minus.gif)        [How to view strategy performance](javascript:HMToggle('toggle','HowToViewStrategyPerformance','HowToViewStrategyPerformance_ICON'))




|  |
| --- |
| Strategy Performance
While the [Account Performance](trade_performance.htm) tab will generate performance report against your account's trade history, the Strategy Performance menu allows you to generate a performance report against the trades generated by the selected strategy.
 
ControlCenter_Strategies_StrategyPerformance
 
•Real-time - Generates performance data for your real-time trades only (since the strategy started running) and will exclude historical trades. If your strategy held a virtual position (calculated against historical data) upon starting, a virtual execution representing the average price of this position will be injected into the real-time results to ensure that a trade pair can be created with the executions resulting from the closing of this position.•Historical &amp; Real-time - Generates performance data for both historical and real-time trade data.•Historical - Generates performance data for historical data only. |



![tog_minus](tog_minus.gif)        [Strategy tab properties](javascript:HMToggle('toggle','StrategyTabProperties','StrategyTabProperties_ICON'))




|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ControlCenter_Strategies_Properties
Strategy Tab Properties


|  |  |
| --- | --- |
| General |  |
| Filter only active strategies | Displays only active strategies |
| Filter by account | Displays only strategies running on the selected account |
| Font | Sets the font for the order grid |
| Tab name | Sets the tab name |
| Columns | Sets that columns are enabled or disabled |



 
How to Save Property Presets
Once you have your properties set to your preference, you can left mouse click on the "preset" text located in the bottom right of the properties dialog. Selecting the option "save" will save these settings as the default settings used every time you open a new window/tab.
 
If you change your settings and later wish to go back to the original settings, you can left mouse click on the preset text and select the option to restore to return to the original settings.
 


|  |
| --- |
| Note: A number of pre-defined variables can be used in the "Tab Name" field. For more information, see the "Tab Name Variables" section of the [Using Tabs](using_tabs.htm) page. |


 |






 
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
 
 
 


HMInitToggle('UnderstandingTheStrategiesTab\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'UnderstandingTheStrategiesTab\',\'UnderstandingTheStrategiesTab\_ICON\')');
HMInitToggle('UnderstandingTheStrategiesTab','hm.type','dropdown','hm.state','0');
HMInitToggle('HowToViewStrategyPerformance\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'HowToViewStrategyPerformance\',\'HowToViewStrategyPerformance\_ICON\')');
HMInitToggle('HowToViewStrategyPerformance','hm.type','dropdown','hm.state','0');
HMInitToggle('StrategyTabProperties\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'StrategyTabProperties\',\'StrategyTabProperties\_ICON\')');
HMInitToggle('StrategyTabProperties','hm.type','dropdown','hm.state','0');



