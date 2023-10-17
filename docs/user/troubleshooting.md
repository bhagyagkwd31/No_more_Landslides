# Application Troubleshooting
Unfortunately, there will always be some cases where the application fails to furnish proper results. In these events, it is helpful to understand the likely failure modes as well as how to troubleshoot the failure.

# Common Failures
## 408
This HTTP status code indicates "Request Timeout".
This indicates the application API endpoint is temporarily offline. We have a high uptime and expect the application to be back online in a short time. Try again after a while and if the issue persists, consider reporting it to us.

## No input page or output
This may also indicate the application being offline and the troubleshooting remains the same as the above.

## Unexpected output
In rare cases, machine learning models can output definitively wrong results.
To ensure as accurate results as possible, provide as many of the input parameters as are available. This ensures that the model works on actual data without making any assumptions of any of the parameters. Our model is deterministic hence garbage output cannot result from valid inputs.
