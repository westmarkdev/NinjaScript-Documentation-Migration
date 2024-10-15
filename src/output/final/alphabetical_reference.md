---
title: "Alphabetical Reference"
pathName: alphabetical_reference
---

## Definition

The Alphabetical Reference provides a comprehensive list of terms and definitions related to our SDK.

## Content Retrieval

The following script dynamically loads the content from an external HTML file:

```javascript
$(function(){
    $("#includedContent").load("nt8_kwindex.htm");
});
```

## Usage

This script should be included in your web page to access the alphabetical reference efficiently.

{% callout type="note" %}

- Ensure that the external HTML file "nt8_kwindex.htm" is located in the correct directory for the script to function properly.
- This method allows for easy updates to the content without altering the main webpage.
{% /callout %}
