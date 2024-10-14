










 


Name







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?name.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt;
Name | [Previous page](isvisible.htm)
[Return to chapter overview](common.htm)










Definition
----------


Determines the listed name of the NinjaScript object.


 


Property Value
--------------


A string value.


 


Syntax
------


Name


 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
   
   if (State == State.SetDefaults)
   {
     Name                 = "Examples indicator";
     Description           = @"An example of an indicator used for documentation purposes";      
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
 
 
 



