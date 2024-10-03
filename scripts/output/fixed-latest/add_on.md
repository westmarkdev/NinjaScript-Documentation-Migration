










 


Add On







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?add_on.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt;
Add On | [Previous page](triggercustomevent.htm)
[Return to chapter overview](language_reference_wip.htm)










Custom Add Ons can be used to extend NinjaTrader's functionality. The methods and properties covered in this section are unique to custom Add On development.


 


For more information on the Add On development process please see [this](developing_add_ons.htm) article.


 


 




|  |  |
| --- | --- |
| [NinjaTrader Controls](controls.htm) | This section contains controls that are native NinjaTrader controls. |
| [Account](account_class.htm) | The Account class can be used to subscribe to account related events as well as accessing account related information. |
| [BarsRequest](barsrequest.htm) | BarsRequest can be used to request [Bars](bars.htm) data and subscribe to real-time Bars data events. |
| [Connection](connection_class.htm) | The Connection class can be used to monitor connection related events as well as accessing connection related information. |
| [IInstrumentProvider Interface](iinstrumentprovider_interface.htm) | When creating your [NTTabPage](nttabpage_class.htm), if you wish to use the [instrument link](linking_windows.htm), be sure to implement the IInstrumentProvider interface. |
| [IIntervalProvider Interface](iintervalprovider_interface.htm) | When creating your [NTTabPage](nttabpage_class.htm), if you wish to use the [interval link](linking_windows.htm), be sure to implement the IIntervalProvider interface. |
| [INTTabFactory Interface](inttabfactory_class.htm) | If you wish to have tab page functionality like adding, removing, moving, duplicating tabs you must create a class which implements the INTTabFactory interface. |
| [IWorkspacePersistence Interface](iworkspacepersistence_interface.htm) | When creating your [NTWindow](ntwindow.htm), be sure to implement the IWorkspacePersistence interface as well for the ability to save and restore your window with NinjaTrader workspaces. |
| [NTTabPage Class](nttabpage_class.htm) | This is where the actual content for tabs inside the custom add on [NTWindow](ntwindow.htm) can be defined. |
| [Alert and Debug Concepts](alert_and_debug_concepts.htm) | In most scenarios you can use the NinjaScript provided methods for triggering alerts and debugging functionality. However, when building your own custom objects, you may find yourself wanting to use this functionality outside the NinjaScript scope. |
| [AtmStrategy](atmstrategy.htm) | AtmStrategy contains properties and methods used to manage [ATM Strategies](advanced_trade_management_atm.htm). |
| [ControlCenter](controlcenter.htm) | ControlCenter is a XAML-defined class containing the layout and properties of the Control Center window. |
| [FundamentalData](fundamentaldata.htm) | FundamentalData is used to access fundamental snapshot data and for subscribing to fundamental data events.  |
| [MarketData](marketdata.htm) | MarketData can be used to access snapshot market data and for subscribing to market data events. |
| [MarketDepth](marketdepth.htm) | MarketDepth can be used to access snapshot market depth and for subscribing to market depth events. |
| [NewsItems](newsitems.htm) | NewsItems can be used to store news articles. |
| [NewsSubscription](newssubscription.htm) | NewsSubscription can be used for subscribing to News events. |
| [NTMenuItem](ntmenuitem.htm) | NTMenuItem is used to create new menu entries. |
| [NTWindow](ntwindow.htm) | The NTWindow class defines parent windows for custom window creation. Instances of NTWindow act as containers for instances of [NTTabPage](nttabpage_class.htm), in which UI elements and their related logic are contained.  |
| [NumericTextBox](numerictextbox.htm) | NumericTextBox provides functionality for numeric text boxes to capture user input. |
| [OnWindowCreated()](onwindowcreated.htm) | This method is called whenever a new [NTWindow](ntwindow.htm) is created. |
| [OnWindowDestroyed()](onwindowdestroyed.htm) | This method is called whenever a new [NTWindow](ntwindow.htm) is destroyed. |
| [OnWindowRestored()](onwindowrestored.htm) | This method is used to recall any custom XElement data from the workspace by referencing a window. |
| [OnWindowSaved()](onwindowsaved.htm) | This method is used to save any custom XElement data associated with your window. |
| [StartAtmStrategy()](startatmstrategy.htm) | StartAtmStrategy can be used to submit entry orders with ATM strategies. |
| [StrategyBase](strategybase.htm) | StrategyBase contains properties and methods for managing a [Strategy](strategy.htm) object, and is the base class from which [AtmStrategy](atmstrategy.htm) derives. |
| [PropagateInstrumentChange()](propagateinstrumentchange().htm) | In an [NTWindow](ntwindow.htm), PropagateInstrumentChange() sends an Instrument to other windows with the same Instrument Linking color configured. |
| [PropagateIntervalChange()](propagateintervalchange().htm) | In an [NTWindow](ntwindow.htm), PropagateIntervalChange() sends an interval to other windows with the same Interval Linking color configured. |
| [TabControl](tabcontrol.htm) | The TabControl class provides functionality for working with [NTTabPage](nttabpage_class.htm) objects within an [NTWindow](ntwindow.htm). |
| [TabControlManager](tabcontrolmanager.htm) | The TabControlManager class can be used to set or check several properties of a [TabControl](tabcontrol.htm) object. |






 
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
 
 
 



