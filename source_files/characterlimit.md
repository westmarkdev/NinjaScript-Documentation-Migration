










 


CharacterLimit







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?characterlimit.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Share Service](share_service.htm) &gt;
CharacterLimit | [Previous page](share_service.htm)
[Return to chapter overview](share_service.htm)










Definition
----------


Determines the maximum number of characters the social network allows. Signature, text, and links all contribute to this character count displayed on the share window.


 


A value of int.MaxValue determines no practical limit and will make the character count not appear on the Share window.



Property Value
--------------


A int value that represents the maximum number of characters the social network allows.


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |



 


 


Syntax
------


CharacterLimit


 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{                        
if (State == State.SetDefaults)
{
CharacterLimit        = 280;
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
 
 
 



