










 


Dispose()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?dispose.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
Dispose() | [Previous page](displayonchartsmenus.htm)
[Return to chapter overview](drawing_tools.htm)










Definition
----------


Releases any device resources used for the drawing tool.


 


Method Return Value
-------------------


This method does not return a value



Syntax
------


Dispose()



Method Parameters
-----------------


This method does not accept any parameters



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name                 = @"My Drawing Tool";      
   }
 
   else if (State == State.Terminated)
     Dispose();
}
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
 
 
 



