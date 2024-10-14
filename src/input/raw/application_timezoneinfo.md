


TimeZoneInfo









 


TimeZoneInfo















Definition
----------


Indicates the current time zone that is configured under Tools &gt; Options &gt; General &gt; Preferences &gt; Time zone   

 


Property Value
--------------


A [TimeZoneInfo](https://msdn.microsoft.com/en-us/library/system.timezoneinfo(v=vs.110).aspx) object the represents the current time zone configured for the application


 


Syntax
Core.Globals.GeneralOptions.TimeZoneInfo
-----------------------------------------------


 


Examples
--------




| ns |
| --- |
| Print(String.Format("The application is currently operating in {0}", Core.Globals.GeneralOptions.TimeZoneInfo)); |






 
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
 
 
 



