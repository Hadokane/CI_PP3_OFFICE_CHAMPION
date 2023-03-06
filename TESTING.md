![UI](officechampion/static/assets/images/docs/oc_logo.png)

# Testing

The Office Champion app has undergone numerous tests - both automated and manual - along with numerous validation methods in order to ensure it functions as intended and provides a positive user experience throughout.

---

## Contents

---

- [Code Validation](#code-validation)
    - [W3C HTML Validator](#w3c-html-validation) 
    - [W3C CSS Validator](#w3c-css-validation)
    - [JSHint Validator](#jshint-validation)
    - [CI Python Linter](#ci-python-linter)
    - [Wave Validator](#wave-validator)
    - [A11y Contrast Validator](#a11y-contrast-validator)
    - [Lighthouse](#lighthouse)
- [Device Testing](#device-testing)
- [Manual Testing](#manual-testing)
- [Testing User Stories](#testing-user-stories)
    - [First Time User](#first-time-user)
    - [Returning User](#returning-user)
    - [Website Owner](#website-owner)

- [Bugs](#bugs)

Return to [README.md ↑](/README.md#testing)

---

# Code Validation

## W3C HTML Validation

---

-  [W3C HTML Validator](https://validator.w3.org/)

I began my validation by running the website's HTML through W3C's Validation Service.

<details><summary>W3C HTML Validation - Errors</summary><img src="officechampion/static/assets/images/docs/validation/w3c_html1.png" alt="W3C HTML Errors Screen"></details>

I initially encountered the following errors:

- Closing tags were present at the end of ```<img>``` & ```<nav>``` tags throughout the website.
- There were two instances where outer tags had been closed before their inner tags, leading to errors.

After fixing the above issues & resubmitting the website for validation, I received the following passing result and was able to continue onto further validation methods.

<details><summary>W3C HTML Validation - Pass</summary><img src="officechampion/static/assets/images/docs/validation/w3c_html2.png" alt="W3C HTML Pass Screen"></details>

---

## W3C CSS Validation

---

- [W3C CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/)

Next, I carried out validation of the CSS file by running the page through W3C CSS Validation Service - Jigsaw.

<details><summary>W3C CSS Pass</summary><img src="officechampion/static/assets/images/docs/validation/w3c_css.png" alt="W3C CSS Pass Screen"></details>

The results came back successfully.

---

## JSHINT Validation

---

- [JSHint Validator](https://jshint.com/)

I utilised JSHint as a validation tool to help detect if there were any errors or potential problems within my JavaScript code.

<details><summary>JSHint Validation</summary><img src="officechampion/static/assets/images/docs/validation/jshint.png" alt="JSHint Validation"></details>

- The undefined variables were all required by Materialize's inbuilt components to initialise forms and other components.

- The removeNode function is called from within HTML pages whenever an alert is clicked by the user. This allows users to close alert pop-ups.

---

## CI Python Linter

---

- [Code Institute Python Linter - Pep8 Validator](https://pep8ci.herokuapp.com/)

I used Code Institute's Python Linter to check the validity of my code based on Pep 8 styling standards.

I ran each Python page individually through the linter. With each returning a result of: "All clear, no errors found."

<details><summary>Python Lint for - "__init__.py"</summary><img src="officechampion/static/assets/images/docs/validation/ci_init.png" alt="Python Lint Results #1"></details>
<details><summary>Python Lint for - "models.py"</summary><img src="officechampion/static/assets/images/docs/validation/ci_models.png" alt="Python Lint Results #2"></details>
<details><summary>Python Lint for - "routes.py"</summary><img src="officechampion/static/assets/images/docs/validation/ci_routes.png" alt="Python Lint Results #3"></details>
<details><summary>Python Lint for - "run.py"</summary><img src="officechampion/static/assets/images/docs/validation/ci_run.png" alt="Python Lint Results #4"></details>

---

## Wave Validator

---

- [Wave Web Accessibility Evaluation Tool](https://wave.webaim.org/)

This was used to check that the Office Champion website was accessible to as many individuals needs as possible.

On an initial scan I discovered the following accessibility errors:
- The Materialize default of white text on an amber background was actually being flagged as a contrast issue.
- Underlining being used on page headers wasn't best practice. A user could easily mistake this for a hyperlink.
- The home button contained the same link as the adjacent "Office Champions" Hero Image, that was included in the navbar. Repeating adjacent links seemed unnecessary to Wave.

<details><summary>Wave Error #1</summary><img src="officechampion/static/assets/images/docs/validation/wave1.png" alt="Wave Error #1"></details>

<details><summary>Wave Error #2</summary><img src="officechampion/static/assets/images/docs/validation/wave5.png" alt="Wave Error #2"></details>

To fix the above issues:
- I recoloured all menu and navigation text to black. Providing adequate contrast for users.
- I removed all underlining throughout the websites headers.

I also decided to keep the "redundant" additional navigation link of "home". My reasoning being that most users will expect the navbar icon to take them home as this is an extremely common feature across numerous websites. The addition of the written "home" button will provide a means of getting to the home page for users without this expectation without harming the website or other users.

After carrying out the above steps, Office Champion passed Wave validation.

<details><summary>Wave Validation Pass</summary><img src="officechampion/static/assets/images/docs/validation/wave4.png" alt="Wave Validation Screen #4"></details>

---

## A11y Contrast Validator

---

- [A11y Color Contrast Accessibility Validator](https://color.a11y.com/Contrast/)

This was used to ensure the websites colour contrast met WCAG 2.1 Guidelines.

An initial check showed that the burger menu icon on the side-nav bar was a contrast issue. I recoloured this icon from white to black, fixing the issue.

<details><summary>A11y Validation Pass</summary><img src="officechampion/static/assets/images/docs/validation/a11y_val.png" alt="A11y Validation Screen"></details>

---

## Lighthouse

---

- [Google Chrome Lighthouse Validator](https://developer.chrome.com/docs/lighthouse/overview/)

I utilised Lighthouse to run audits to check the performance, accessibility & SEO of my website.

I was reminded to add ```<Meta>``` tags to my base template's head to provide a description of my website, improving it's SEO potential.

After doing the above, Office Champion received very favourable results on both it's Desktop and Mobile audits.

<details><summary>Lighthouse Desktop Pass</summary><img src="officechampion/static/assets/images/docs/validation/lighthouse_desktop.png" alt="Lighthouse Desktop Validation Screen"></details>

<details><summary>Lighthouse Mobile Pass</summary><img src="officechampion/static/assets/images/docs/validation/lighthouse_mobile.png" alt="Lighthouse Mobile Validation Screen"></details>

Return to [Top ↑](/TESTING.md#testing)

---

# Device Testing

The website was tested and functioned as expected on the following devices:

- Novatech LTD. AMD Ryzen 7 3800x, 32GB Desktop
- Lenovo IdeaPad 5 Pro
- Samsung Galaxy S20 & S21
- Samsung Galaxy Tab S7
- MacBook Air with M1 chip
- iPhone 11, 13 & 14
- iPad Air
- Samsung Chrome Book

The website has been tested on up-to-date versions of the following browsers:

- Microsoft Edge
- Google Chrome
- Chrome for android
- Mozilla Firefox
- Opera
- Safari
- Internet Explorer
- Duck Duck Go

The website has also been tested on monitors of 16:9, 16:10 and 21:9 resolutions.

Return to [Top ↑](/TESTING.md#testing)

---

# Manual Testing


sgsdgsgd

Return to [Top ↑](/TESTING.md#testing)

---

# Testing User Stories


Here we will test our previously defined user stories.

---

### First-time User

---

dgdsgdsg

---

### Returning User

---

dgsdgds

---

### Website Owner

---

dgsgds

Return to [Top ↑](/TESTING.md#testing)

---

# Bugs

gdgdsgds


Return to [Top ↑](/TESTING.md#testing)

Return to [README.md ↑](/README.md#testing)