---
title: Add On
pathName: add_on
parent: language_reference
order: 3
status: imported
section: references
---

Custom Add Ons can be used to extend NinjaTrader's functionality. The methods and properties covered in this section are unique to custom Add On development.

For more information on the Add On development process please see [this](developing_add_ons) article.

{% table %}

* NinjaTrader Controls
* This section contains controls that are native NinjaTrader controls.

---

* Account
* The Account class can be used to subscribe to account related events as well as accessing account related information.

---

* BarsRequest
* BarsRequest can be used to request [Bars](bars) data and subscribe to real-time Bars data events.

---

* Connection
* The Connection class can be used to monitor connection related events as well as accessing connection related information.

---

* IInstrumentProvider Interface
* When creating your [NTTabPage](nttabpage_class), if you wish to use the [instrument link](linking_windows), be sure to implement the IInstrumentProvider interface.

---

* IIntervalProvider Interface
* When creating your [NTTabPage](nttabpage_class), if you wish to use the [interval link](linking_windows), be sure to implement the IIntervalProvider interface.

---

* INTTabFactory Interface
* If you wish to have tab page functionality like adding, removing, moving, duplicating tabs you must create a class which implements the INTTabFactory interface.

---

* IWorkspacePersistence Interface
* When creating your [NTWindow](ntwindow), be sure to implement the IWorkspacePersistence interface as well for the ability to save and restore your window with NinjaTrader workspaces.

---

* NTTabPage Class
* This is where the actual content for tabs inside the custom add on [NTWindow](ntwindow) can be defined.

---

* Alert and Debug Concepts
* In most scenarios you can use the NinjaScript provided methods for triggering alerts and debugging functionality. However, when building your own custom objects, you may find yourself wanting to use this functionality outside the NinjaScript scope.

---

* AtmStrategy
* AtmStrategy contains properties and methods used to manage [ATM Strategies](advanced_trade_management_atm).

---

* ControlCenter
* ControlCenter is a XAML-defined class containing the layout and properties of the Control Center window.

---

* FundamentalData
* FundamentalData is used to access fundamental snapshot data and for subscribing to fundamental data events.

---

* MarketData
* MarketData can be used to access snapshot market data and for subscribing to market data events.

---

* MarketDepth
* MarketDepth can be used to access snapshot market depth and for subscribing to market depth events.

---

* NewsItems
* NewsItems can be used to store news articles.

---

* NewsSubscription
* NewsSubscription can be used for subscribing to News events.

---

* NTMenuItem
* NTMenuItem is used to create new menu entries.

---

* NTWindow
* The NTWindow class defines parent windows for custom window creation. Instances of NTWindow act as containers for instances of [NTTabPage](nttabpage_class), in which UI elements and their related logic are contained.

---

* NumericTextBox
* NumericTextBox provides functionality for numeric text boxes to capture user input.

---

* OnWindowCreated()
* This method is called whenever a new [NTWindow](ntwindow) is created.

---

* OnWindowDestroyed()
* This method is called whenever a new [NTWindow](ntwindow) is destroyed.

---

* OnWindowRestored()
* This method is used to recall any custom XElement data from the workspace by referencing a window.

---

* OnWindowSaved()
* This method is used to save any custom XElement data associated with your window.

---

* StartAtmStrategy()
* StartAtmStrategy can be used to submit entry orders with ATM strategies.

---

* StrategyBase
* StrategyBase contains properties and methods for managing a [Strategy](strategy) object, and is the base class from which [AtmStrategy](atmstrategy) derives.

---

* PropagateInstrumentChange()
* In an [NTWindow](ntwindow), PropagateInstrumentChange() sends an Instrument to other windows with the same Instrument Linking color configured.

---

* PropagateIntervalChange()
* In an [NTWindow](ntwindow), PropagateIntervalChange() sends an interval to other windows with the same Interval Linking color configured.

---

* TabControl
* The TabControl class provides functionality for working with [NTTabPage](nttabpage_class) objects within an [NTWindow](ntwindow).

---

* TabControlManager
* The TabControlManager class can be used to set or check several properties of a [TabControl](tabcontrol) object.
{% /table %}
