










 


OnWindowDestroyed()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onwindowdestroyed.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt;
OnWindowDestroyed() | [Previous page](onwindowcreated.htm)
[Return to chapter overview](add_on.htm)










Definition
----------


This method is called whenever a new [NTWindow](ntwindow.htm) is destroyed. It will be called in the thread of that window.  A window is destroyed either by the user closing the window, closing a workspace, or on a shut down of NinjaTrader.


 




|  |
| --- |
| Note:  This method will also be called on a recompile of the NinjaTrader.Custom project (e.g., when you compile an indicator, strategy, or add-on) |





Method Return Value
-------------------


This method does not return a value



Syntax
------


OnWindowDestroyed(Window window)


 


Parameters
----------




|  |  |
| --- | --- |
| window | A Window object which is being removed from the workspace |



 



Examples
--------




| ns |
| --- |
| public class MyWindowAddOn : AddOnBase
{
     private NTMenuItem myMenuItem;
     private NTMenuItem existingMenuItem;
 
     protected override void OnStateChange()
     {
         if (State == State.SetDefaults)
          {
               Description = "Our custom MyWindow add on";
               Name        = "MyWindow";
          }
     }
 
     // Will be called as a new NTWindow is destroyed. It will be called in the thread of that window
     protected override void OnWindowDestroyed(Window window)
     {
          if (myMenuItem != null &amp;&amp; window is ControlCenter)
          {
               if (existingMenuItem != null &amp;&amp; existingMenuItem.Items.Contains(myMenuItem))
                   existingMenuItem.Items.Remove(myMenuItem);
 
               myMenuItem.Click -= OnMenuItemClick;
               myMenuItem = null;
          }
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
 
 
 



