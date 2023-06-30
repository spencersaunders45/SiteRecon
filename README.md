# SiteRecon

This is an information gathering tool to scan websites for:
- Form locations
- External urls
- emails
- http only urls
- Internal urls

***Please use this tool for good purposes.***

## Dependence's
***
```{python}
pip install rich
pip install requests
pip install beautifulsoup4
```

## How to use this tool

- Navigate to the src directory and use `python3 siterecon.py -h`
### Scan with default settings:
- `python3 siterecon.py [target url]` 

### Change the aggression

Choose how aggressive the scan is. The longer the wait time between requests the less likely you are to be blocked from further requests.

`python3 siterecon.py -ag {A,M,P}`
- A: Aggressive - default is 0 wait time between requests.
- M: Moderate - default is 30 to 45 second wait time between requests.
- P: Passive - default is 45 to 90 second wait time between requests.

You can also use the `-ca` or `--custom-aggression` flag to pass a custom wait time between requests. `python3 siterecon.py -ca 5 90 google.com`. 

### Change the amount of pages scanned

`python3 siterecon.py -c [int]`
- int: The number of pages you want to scan.

### Change the file location of the output file

*Currently only text files are supported for the scan report file.*

`python3 siterecon.py -fp example/file.txt`

### Change defaults 

You also have the ability to change the default values to customize siterecon to your personal preferences. Use `python3 siterecon.py --help` to view all the flags you can use to update the default values.

Use the `-ss` or `--show-settings` flag to view all the default settings. You can all pass `none` in the url parameter to prevent siterecon from attempting to scan.
`python3 siterecon.py -ss none`

## License

MIT