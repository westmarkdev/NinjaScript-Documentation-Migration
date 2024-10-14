﻿










 


Protection/DLL Security







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?protection_dll_security.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Distribution](distribution.htm) &gt;
Protection/DLL Security | [Previous page](export_problems.htm)
[Return to chapter overview](distribution.htm)










[![SecureTeam](protection_dll_security_1.gif "SecureTeam")](http://www.secureteam.net/ "SecureTeam")


 


Although .NET DLL files are compiled which prevents users from being able to see your proprietary source code, they are still subject to decompilation and reverse engineering attempts. If you want a higher level of security, you can select the "Protect compiled assemblies" option which adds an additional layer of protection. This additional protection layer is provided by [SecureTeam's Agile.NET](http://www.secureteam.net/ninja-pricing "SecureTeam's Agile.NET") product which has been licensed by NinjaTrader and available at a reduced price to protect NinjaTrader assemblies. This product claims to completely stop MSIL disassembly and decompilation. We use it ourselves and are extremely happy with it.


 


Should you wish to use Agile.NET for protecting your NinjaScript assemblies you will first need to go [here](http://www.secureteam.net/ninja-pricing "CliSecure Download") to download and purchase the product. Once installed, please run the Agile.NET standalone product once to input in the license information you should have received when you downloaded it. After that, when you use NinjaTrader's Export NinjaScript utility and select the "Protect compiled assemblies" option for export, it will automatically protect your NinjaScript assembly with Agile.NET.


 


![Protection_DLL_Security_2](protection_dll_security_2.png)


 


Please note that this version of Agile.NET will only work for protecting NinjaScript assemblies within NinjaTrader. If you would like to protect other files outside of NinjaTrader please consider purchasing the full version of Agile.NET from SecureTeam directly [here](http://www.secureteam.net/ninja-pricing "Agile.NET Purchase") 'Agile.NET 6.0 Code Protection'. NinjaScript assemblies protected with the full version of Agile.NET will also work in NinjaTrader.


 


At this time we recommend using version [6.9.1.2](https://secureteam.net/content/AgileDotNetInstaller6912.exe)


For clients on 8.0.28.0 or older you can continue to use [6.6.0.35](https://secureteam.net/content/AgileDotNetInstaller66035.exe)





 
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
 
 
 


