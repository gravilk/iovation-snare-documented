# Iovation Snare documented & solved
This repository contains files that will make solving Iovation snare.js fraud protection much easier, if not solve it instantly.
This solver worked on **7/3/2023**. It is somewhat likely that something changed in their security since then but updates aren't very common in this script.
This solver can flag if you never change the browser fingerprints that's being sent.

## How snare.js works
Snare.js is a poorly obfuscated/unobfuscated file for fraud protection purposes. Most of the script contains the encoding algorithm for the data that's being sent. There's very little information being sent about the browser. Every part of the JSON is documented in the `main.py` file.
Most of the "protection" here is the obscure encoding algorithm that I just copy-pasted from the original script and modified it slightly to my needs. It's being executed by python using the `pyexecjs` library that you can install via `pip install pyexecjs`.

## Checks
- navigator appName and appVersion
- website URL
- User Agent information split into different parts
- list of all plugin names
- checks for if user agent is Amazon Cloudfront (odd)
- Screen resolution
- Timezone

## How to try this and continue development?
The solver that worked on **7/3/2023** is in the `main.py` file. The current version of the script is in snare.js and has been downloaded from [Poshmark](https://poshmark.com/snare.js).
If you have noticed any changes to it you can make sure by searching for the `toString` function being set in the `_i_cr` object. When you place a breakpoint there and refresh the page you should be able to access the `_i_gi` array which contains all the JSON values. You can also do this to get all the important values for a new fingerprint. If the version is not 3.1.3, it is **very** likely that something has changed.