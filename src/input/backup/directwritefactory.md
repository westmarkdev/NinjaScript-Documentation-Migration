










 


DirectWriteFactory







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?directwritefactory.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [Rendering](rendering.htm) &gt;
DirectWriteFactory | [Previous page](d2dfactory.htm)
[Return to chapter overview](rendering.htm)










Definition
----------


Provides an default DirectWrite factory used for creating [SharpDX.DirectWrite](sharpdx_directwrite.htm) components.


 


Property Value
--------------


A read-only SharpDX.DirectWrite.Factory used to create DirectWrite objects compatible with NinjaTrader rendering


 


Syntax
------


NinjaTrader.Core.Globals.DirectWriteFactory


 




| ns |
| --- |
| // create a text format object with default NinjaTrader DirectWrite factory
SharpDX.DirectWrite.TextFormat textFormat = new SharpDX.DirectWrite.TextFormat(NinjaTrader.Core.Globals.DirectWriteFactory, 
   "Arial", 12f);
 
// create a text layout object with default NinjaTrader DirectWrite factory
SharpDX.DirectWrite.TextLayout textLayout = new SharpDX.DirectWrite.TextLayout(NinjaTrader.Core.Globals.DirectWriteFactory, 
   "text to render", textFormat, ChartPanel.W, ChartPanel.H); |






 
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
 
 
 



