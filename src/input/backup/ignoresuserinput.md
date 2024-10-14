










 


IgnoresUserInput







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?ignoresuserinput.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
IgnoresUserInput | [Previous page](ignoressnapping.htm)
[Return to chapter overview](drawing_tools.htm)










Definition  

Determines if the drawing tool can be clicked on by the user.


 


Property Value
--------------


A bool value which wen true if the drawing tool cannot not be interacted with by a user; otherwise false.  Default is set to false.


 


Syntax
------


IgnoresUserInput



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
          
   IgnoresUserInput = true; // Set this to true to make the drawing object non-interactive
     }
     else if (State == State.Configure)
     {
 
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
 
 
 



