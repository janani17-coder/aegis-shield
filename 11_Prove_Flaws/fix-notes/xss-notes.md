# DOM XSS – Initial Investigation

## Application
OWASP Juice Shop – Local Docker Lab

## Test Input
janani-test

## Observation
After submitting the search input, the text appeared
in the browser DOM inside:

<span id="searchValue">janani-test</span>

## Initial Assessment
The input is reflected in the DOM.
This observation alone does not confirm an XSS vulnerability.

## Evidence
The matching HTML element was inspected using
Chrome Developer Tools – Elements tab.

## Next Step
Review the relevant client-side code to determine
whether untrusted input is safely handled.

## Source Code Review

### Vulnerable File
frontend/src/app/search-result/search-result.component.ts

### Vulnerable Code
this.searchValue = this.sanitizer.bypassSecurityTrustHtml(queryParam)

### HTML Rendering
frontend/src/app/search-result/search-result.component.html

<span id="searchValue" [innerHTML]="searchValue"></span>

### Root Cause
The application takes search input from the URL query parameter
and explicitly marks it as trusted HTML. Angular then renders
that content using innerHTML.

This bypasses Angular's normal HTML sanitization.

### Developer Fix
Do not use bypassSecurityTrustHtml() for untrusted search input.
Render the value as ordinary text using Angular interpolation:

<span id="searchValue">{{ searchValue }}</span>

Keep searchValue as a string rather than SafeHtml.

### Regression Test
Submit a harmless HTML-like test string and verify that the
browser displays it as text rather than creating HTML elements.
Also verify that normal search results continue to work.

### Business Impact
In a payroll application, a similar flaw could allow malicious
content to run in an employee's browser and potentially expose
sensitive information or misuse an authenticated session.

## Runtime Evidence

### Test Input
<b>janani-test</b>

### Expected Safe Behaviour
The browser should display the complete input as ordinary text.

### Actual Observation
The browser displayed janani-test in bold.
The HTML formatting was interpreted.

### Result
HTML interpretation confirmed in the local Juice Shop application.

### Evidence Screenshot
evidence/xss/dom-xss-html-rendering.png