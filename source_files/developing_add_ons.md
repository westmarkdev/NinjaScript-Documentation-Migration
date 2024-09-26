










 


Developing Add Ons







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?developing_add_ons.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [AddOn Development Overview](addon_development_overview.htm) &gt;
Developing Add Ons | [Previous page](addon_development_overview.htm)
[Return to chapter overview](addon_development_overview.htm)










Add Ons Overview
----------------


Add Ons are incredibly powerful NinjaScript objects that let you create unprecedented tools which are seamlessly integrated (visually and functionally) into NinjaTrader. Experienced programmers can leverage the information available through the framework to create exciting new windows and utilities that can give users an incredible edge over the markets.


 


How to make Add Ons
-------------------


The process to make an Add On is fairly simple once the structure is understood. A few questions should be answered to determine how to build your Add On:


1.Where should the entry point for the Add On be? E.g. Should it be launched from the Control Center menus? Should it be launched from a Chart?

2.Should the Add On leverage the tab functionality available in NinjaTrader?

3.Should the Add On leverage the window linking functionality available in NinjaTrader?

4.Should the Add On be persisted in NinjaTrader workspaces?

 


 


Once the functionality of your Add On is determined you can use the following building blocks to create your Add On:




|  |  |
| --- | --- |
|  [AddOnBase](add_on.htm) | This is where you create the entry point for the Add On. |
| [NTWindow](ntwindow.htm) | This is where you define the parent window container for your Add On. Tabs would reside within this parent window should you choose. This is also where workspace persistence would be created. |
| [NTTabPage](nttabpage_class.htm) | This is where you define the content of each tab that resides inside NTWindow. This is also where you create the window linking functionality. |
| Class implementing the [INTTabFactory](inttabfactory_class.htm) interface | This is necessary to ensure proper tab functionality like adding, removing, moving tabs around in your NTWindow. |



 


The general flow goes from AddOnBase &gt; NTWindow &gt; INTTabFactory &gt; NTTabPage.


AddOnBase determines the user entry point and then creates the event handler to create the NTWindow. NTWindow calls the tab factory which then brings in the NTTabPage content in the form of tabs into NTWindow.





 
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
 
 
 



