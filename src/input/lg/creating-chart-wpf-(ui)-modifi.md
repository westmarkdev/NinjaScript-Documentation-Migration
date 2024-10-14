










 


Creating Chart WPF (UI) Modifications from an Indicator







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?creating-chart-wpf-(ui)-modifi.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Indicator](indicator2.htm) &gt;
Creating Chart WPF (UI) Modifications from an Indicator | [Previous page](using_try-catch_blocks.htm)
[Return to chapter overview](indicator2.htm)










NinjaTrader's extensive C# backend allows for powerful expandability that is unmatched in other trading platforms. Within the context of C# and NinjaScript it is possible to manipulate the window in which the NinjaScript is added. This example demonstrates how chart window modifications can be performed to add your own WPF controls to your chart for custom functionality. These window modifications could be, but are not limited to: adding custom buttons, menus or toolbars.


 


Key concepts in this example
----------------------------


•Adding your own toolbar with WPF Controls to the left/right side of a chart

•Adding your own toolbar with WPF Controls to the top of a chart

•Adding WPF Controls to the MainMenu title bar of a chart window

•Adding custom WPF Controls to Chart Trader

•Modifying existing Chart Trader buttons

 


Important related documentation
-------------------------------


C#


•[Button](https://docs.microsoft.com/en-us/dotnet/api/system.windows.controls.button?view=netframework-4.8)

•[Grid](https://docs.microsoft.com/en-us/dotnet/api/system.windows.controls.grid?view=netframework-4.8)

•[GridSplitter](https://docs.microsoft.com/en-us/dotnet/api/system.windows.controls.gridsplitter?view=netframework-4.8)

•[Menu](https://docs.microsoft.com/en-us/dotnet/api/system.windows.controls.menu?view=netframework-4.8)

•[MenuItem](https://docs.microsoft.com/en-us/dotnet/api/system.windows.controls.menuitem?view=netframework-4.8)

•[StackPanel](https://docs.microsoft.com/en-us/dotnet/api/system.windows.controls.stackpanel?view=netframework-4.8)

NinjaTrader


•[NTMenuItem](ntmenuitem.htm)

•[TabControlManager](tabcontrolmanager.htm)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleWPFModifications.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleWPFModifications.zip)





 
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
 
 
 



