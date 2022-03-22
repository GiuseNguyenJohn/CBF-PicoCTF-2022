# Redaction gone wrong
Author: John
## Description
Now you DON’T see me.
This report has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?

## Solution

When we open the PDF document, we some data redacted. However, we can drag
our cursor over the text and select the text, when we paste the text somewhere,
we can see the redacted data:
```
Financial Report for ABC Labs, Kigali, Rwanda for the year 2021.
Breakdown - Just painted over in MS word.

Cost Benefit Analysis
Credit Debit
This is not the flag, keep looking
Expenses from the
picoCTF{C4n_Y0u_S33_m3_fully}
Redacted document.
```

**Flag: picoCTF{C4n_Y0u_S33_m3_fully}**