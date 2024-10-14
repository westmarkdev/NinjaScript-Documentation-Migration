










 


IsEditable







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?iseditable.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Market Analyzer Column](market_analyzer_column.htm) &gt;
IsEditable | [Previous page](formatdecimals.htm)
[Return to chapter overview](market_analyzer_column.htm)










Definition
----------


Determines if a Market Analyzer Column is editable.


 


Property Value
--------------


This property returns true if the Market Analyzer Column can be edited; otherwise, false.


 


Syntax
------


IsEditable



Example
-------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
          DataType   = typeof(string);
          IsEditable = true;
     }
} |






 
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
 
 
 



